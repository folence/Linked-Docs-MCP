"""MCP API routes for documentation search."""

import time
from typing import Optional
from fastapi import APIRouter, HTTPException, Depends
from pathlib import Path

from schemas.search import (
    SearchQuery,
    SearchResponse,
    SearchResult,
    DocumentContextRequest,
    DocumentContextResponse,
    ListSourcesResponse,
    SourceInfo,
)
from schemas.document import AccessLevel

# Router will be created and dependencies injected by main app
router = APIRouter(prefix="/api/v1", tags=["mcp"])

# These will be injected as dependencies
search_engine = None
access_controller = None
audit_logger = None
document_store = None  # Stores document metadata


def set_dependencies(engine, controller, logger, doc_store):
    """
    Set global dependencies for routes.
    
    This is called by the main application to inject dependencies.
    """
    global search_engine, access_controller, audit_logger, document_store
    search_engine = engine
    access_controller = controller
    audit_logger = logger
    document_store = doc_store


@router.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "service": "Linked Documentation MCP Server",
        "version": "1.0.0"
    }


@router.get("/list_sources", response_model=ListSourcesResponse)
async def list_sources():
    """
    List all available documentation sources.
    
    Returns information about indexed sources including document counts.
    """
    if not document_store:
        raise HTTPException(status_code=500, detail="Document store not initialized")
    
    sources_info = []
    total_documents = 0
    
    # Group documents by source type
    source_groups = {}
    for doc_id, doc_meta in document_store.items():
        source_type = doc_meta.get("source_type", "unknown")
        access_level = doc_meta.get("access_level", "internal")
        
        if source_type not in source_groups:
            source_groups[source_type] = {
                "count": 0,
                "access_level": access_level,
                "last_indexed": doc_meta.get("last_indexed")
            }
        
        source_groups[source_type]["count"] += 1
        total_documents += 1
    
    # Create SourceInfo objects
    from datetime import datetime
    for source_type, info in source_groups.items():
        try:
            access_level_enum = AccessLevel(info["access_level"])
        except ValueError:
            access_level_enum = AccessLevel.INTERNAL
        
        # Convert timestamp to ISO format string if present
        last_indexed = info.get("last_indexed")
        if last_indexed and isinstance(last_indexed, (int, float)):
            last_indexed = datetime.fromtimestamp(last_indexed).isoformat()
        
        sources_info.append(
            SourceInfo(
                source_id=f"{source_type}_connector",
                source_type=source_type,
                access_level=access_level_enum,
                document_count=info["count"],
                last_indexed=last_indexed
            )
        )
    
    return ListSourcesResponse(
        sources=sources_info,
        total_sources=len(sources_info),
        total_documents=total_documents
    )


@router.post("/search_docs", response_model=SearchResponse)
async def search_docs(query: SearchQuery):
    """
    Search documentation using hybrid semantic + keyword search.
    
    Returns ranked results with snippets and metadata.
    """
    if not search_engine:
        raise HTTPException(status_code=500, detail="Search engine not initialized")
    
    start_time = time.time()
    
    # Perform hybrid search
    results = search_engine.search(query.query, top_k=query.top_k * 2)  # Get extra for filtering
    
    # Apply access control filters
    if query.access_level and access_controller:
        results = access_controller.filter_chunks(results, max_access_level=query.access_level)
    
    # Filter by source types if specified (ignore empty lists)
    if query.source_types and len(query.source_types) > 0:
        results = [
            (chunk, score) for chunk, score in results
            if chunk.metadata.get("source_type") in query.source_types
        ]
    
    # Filter by tags if specified (ignore empty lists)
    if query.tags and len(query.tags) > 0:
        results = [
            (chunk, score) for chunk, score in results
            if any(tag in chunk.metadata.get("tags", []) for tag in query.tags)
        ]
    
    # Limit to requested top_k
    results = results[:query.top_k]
    
    # Convert to SearchResult objects
    search_results = []
    for chunk, score in results:
        # Extract metadata
        doc_meta = document_store.get(chunk.document_id, {}) if document_store else {}
        
        # Create snippet (truncate if too long)
        snippet = chunk.text[:300] + "..." if len(chunk.text) > 300 else chunk.text
        
        try:
            access_level_enum = AccessLevel(chunk.metadata.get("access_level", "internal"))
        except ValueError:
            access_level_enum = AccessLevel.INTERNAL
        
        search_results.append(
            SearchResult(
                title=chunk.metadata.get("title", "Untitled"),
                uri=chunk.uri,
                snippet=snippet,
                score=score,
                source_type=chunk.metadata.get("source_type", "unknown"),
                access_level=access_level_enum,
                last_modified=doc_meta.get("last_modified"),
                chunk_index=chunk.chunk_index,
                page_number=chunk.page_number,
                section_title=chunk.section_title
            )
        )
    
    search_time_ms = (time.time() - start_time) * 1000
    
    # Log the query
    if audit_logger:
        audit_logger.log_query(
            query=query.query,
            results=results,
            user_id=query.user_id,
            access_level=query.access_level.value if query.access_level else None,
            search_time_ms=search_time_ms
        )
    
    return SearchResponse(
        query=query.query,
        total_results=len(search_results),
        results=search_results,
        search_time_ms=search_time_ms
    )


@router.get("/get_doc_context", response_model=DocumentContextResponse)
async def get_doc_context(uri: str, user_id: Optional[str] = None):
    """
    Retrieve full context for a specific document/chunk by URI.
    
    Args:
        uri: Internal URI (e.g., internal://pdf/doc.pdf#chunk-0)
        user_id: Optional user ID for audit logging
    """
    if not search_engine or not document_store:
        raise HTTPException(status_code=500, detail="Services not initialized")
    
    # Find the chunk by URI
    # Search through the vector store chunks
    matching_chunk = None
    for chunk in search_engine.vector_store.chunks:
        if chunk.uri == uri:
            matching_chunk = chunk
            break
    
    if not matching_chunk:
        raise HTTPException(status_code=404, detail=f"Document not found for URI: {uri}")
    
    # Get document metadata
    doc_meta = document_store.get(matching_chunk.document_id, {})
    
    # Check access control
    try:
        access_level_enum = AccessLevel(matching_chunk.metadata.get("access_level", "internal"))
    except ValueError:
        access_level_enum = AccessLevel.INTERNAL
    
    # Log the access
    if audit_logger:
        audit_logger.log_document_access(
            uri=uri,
            user_id=user_id,
            document_id=matching_chunk.document_id
        )
    
    return DocumentContextResponse(
        uri=uri,
        title=matching_chunk.metadata.get("title", "Untitled"),
        content=matching_chunk.text,
        metadata={
            "document_id": matching_chunk.document_id,
            "chunk_id": matching_chunk.chunk_id,
            "chunk_index": matching_chunk.chunk_index,
            "source_type": matching_chunk.metadata.get("source_type"),
            "page_number": matching_chunk.page_number,
            "section_title": matching_chunk.section_title,
            **doc_meta
        },
        access_level=access_level_enum
    )


@router.get("/stats")
async def get_stats():
    """
    Get statistics about the search engine and indexed documents.
    """
    if not search_engine or not document_store:
        raise HTTPException(status_code=500, detail="Services not initialized")
    
    stats = {
        "total_documents": len(document_store),
        "search_engine": search_engine.get_stats() if hasattr(search_engine, 'get_stats') else {}
    }
    
    return stats

