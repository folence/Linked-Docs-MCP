"""
Linked Documentation MCP Server - Main Application Entry Point

This is the main entry point for the MCP server that enables AI models to
safely query and reference internal documentation sources.
"""

import time
from pathlib import Path
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from schemas.config import settings
from schemas.document import AccessLevel
from connectors import PDFConnector, MarkdownConnector
from indexing import TextChunker, Embedder, VectorStore, KeywordSearcher
from indexing.hybrid_search import HybridSearchEngine
from core import AccessController, AuditLogger
from routes import router
from routes import mcp_routes


# Global state
document_store = {}  # Stores document metadata
search_engine = None
access_controller = None
audit_logger = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan event handler for startup and shutdown."""
    # Startup
    global search_engine, access_controller, audit_logger, document_store
    
    print("=" * 60)
    print("Linked Documentation MCP Server Starting...")
    print("=" * 60)
    
    # Initialize core components
    print("\n[1/6] Initializing embedder...")
    embedder = Embedder(
        model_name=settings.embedding_model,
        device=settings.embedding_device
    )
    
    print("\n[2/6] Initializing vector store...")
    vector_store = VectorStore(
        embedding_dim=embedder.get_embedding_dimension(),
        store_path=settings.vector_store_path
    )
    
    print("\n[3/6] Initializing keyword searcher...")
    keyword_searcher = KeywordSearcher()
    
    print("\n[4/6] Initializing hybrid search engine...")
    search_engine = HybridSearchEngine(
        vector_store=vector_store,
        keyword_searcher=keyword_searcher,
        embedder=embedder,
        semantic_weight=settings.semantic_weight,
        keyword_weight=settings.keyword_weight
    )
    
    print("\n[5/6] Initializing access control and audit logging...")
    access_controller = AccessController()
    audit_logger = AuditLogger(
        log_path=settings.audit_log_path,
        enabled=settings.enable_audit_logging
    )
    
    # Inject dependencies into routes
    mcp_routes.set_dependencies(
        engine=search_engine,
        controller=access_controller,
        logger=audit_logger,
        doc_store=document_store
    )
    
    print("\n[6/6] Loading and indexing documents...")
    
    # Rebuild document_store from existing chunks in vector store
    if vector_store.chunks:
        print(f"  - Rebuilding document metadata from {len(vector_store.chunks)} existing chunks...")
        for chunk in vector_store.chunks:
            doc_id = chunk.document_id
            if doc_id not in document_store:
                # Reconstruct metadata from chunk
                document_store[doc_id] = {
                    "source_type": chunk.metadata.get("source_type", "unknown"),
                    "access_level": chunk.metadata.get("access_level", "internal"),
                    "title": chunk.metadata.get("title", "Untitled"),
                    "file_path": chunk.metadata.get("file_path", ""),
                    "last_modified": None,  # We don't have this in chunk metadata
                    "last_indexed": None
                }
        print(f"    Reconstructed metadata for {len(document_store)} documents")
    
    await index_documents(
        embedder=embedder,
        vector_store=vector_store,
        keyword_searcher=keyword_searcher
    )
    
    print("\n" + "=" * 60)
    print("Server initialized successfully!")
    print(f"Vector store: {vector_store.get_stats()['total_vectors']} vectors")
    print(f"Keyword index: {keyword_searcher.get_stats()['total_chunks']} chunks")
    print(f"Documents indexed: {len(document_store)}")
    print("=" * 60)
    print(f"\nServer running at: http://{settings.host}:{settings.port}")
    print(f"API docs: http://{settings.host}:{settings.port}/docs")
    print("=" * 60 + "\n")
    
    yield
    
    # Shutdown
    print("\nShutting down server...")
    
    # Save vector store if needed
    if search_engine and hasattr(search_engine, 'vector_store'):
        print("Saving vector store...")
        search_engine.vector_store.save()
    
    print("Shutdown complete.")


# Initialize FastAPI app with lifespan
app = FastAPI(
    title="Linked Documentation MCP Server",
    description="MCP server for querying internal documentation with hybrid search",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(router)


async def startup_event_deprecated():
    """Initialize services on startup."""
    global search_engine, access_controller, audit_logger, document_store
    
    print("=" * 60)
    print("Linked Documentation MCP Server Starting...")
    print("=" * 60)
    
    # Initialize core components
    print("\n[1/6] Initializing embedder...")
    embedder = Embedder(
        model_name=settings.embedding_model,
        device=settings.embedding_device
    )
    
    print("\n[2/6] Initializing vector store...")
    vector_store = VectorStore(
        embedding_dim=embedder.get_embedding_dimension(),
        store_path=settings.vector_store_path
    )
    
    print("\n[3/6] Initializing keyword searcher...")
    keyword_searcher = KeywordSearcher()
    
    print("\n[4/6] Initializing hybrid search engine...")
    search_engine = HybridSearchEngine(
        vector_store=vector_store,
        keyword_searcher=keyword_searcher,
        embedder=embedder,
        semantic_weight=settings.semantic_weight,
        keyword_weight=settings.keyword_weight
    )
    
    print("\n[5/6] Initializing access control and audit logging...")
    access_controller = AccessController()
    audit_logger = AuditLogger(
        log_path=settings.audit_log_path,
        enabled=settings.enable_audit_logging
    )
    
    # Inject dependencies into routes
    mcp_routes.set_dependencies(
        engine=search_engine,
        controller=access_controller,
        logger=audit_logger,
        doc_store=document_store
    )
    
    print("\n[6/6] Loading and indexing documents...")
    await index_documents(
        embedder=embedder,
        vector_store=vector_store,
        keyword_searcher=keyword_searcher
    )
    
    print("\n" + "=" * 60)
    print("Server initialized successfully!")
    print(f"Vector store: {vector_store.get_stats()['total_vectors']} vectors")
    print(f"Keyword index: {keyword_searcher.get_stats()['total_chunks']} chunks")
    print(f"Documents indexed: {len(document_store)}")
    print("=" * 60)
    print(f"\nServer running at: http://{settings.host}:{settings.port}")
    print(f"API docs: http://{settings.host}:{settings.port}/docs")
    print("=" * 60 + "\n")


async def index_documents(embedder, vector_store, keyword_searcher):
    """
    Load and index documents from the data directory.
    Only indexes NEW or CHANGED documents to avoid duplicates.
    
    Args:
        embedder: Text embedder
        vector_store: Vector store for semantic search
        keyword_searcher: Keyword searcher
    """
    global document_store
    
    start_time = time.time()
    sources_dir = settings.data_dir / "sources"
    
    if not sources_dir.exists():
        print(f"Creating sources directory: {sources_dir}")
        sources_dir.mkdir(parents=True, exist_ok=True)
        print("No documents found. Add documents to data/sources/ to index them.")
        return
    
    # Initialize connectors
    pdf_connector = PDFConnector(
        source_id="pdf_connector_001",
        access_level=AccessLevel.INTERNAL
    )
    
    md_connector = MarkdownConnector(
        source_id="markdown_connector_001",
        access_level=AccessLevel.INTERNAL
    )
    
    # Initialize chunker
    chunker = TextChunker(
        chunk_size=settings.chunk_size,
        chunk_overlap=settings.chunk_overlap
    )
    
    all_documents = []
    
    # Load PDF documents
    print(f"  - Loading PDF documents from {sources_dir}...")
    pdf_docs = pdf_connector.load_documents(sources_dir)
    print(f"    Found {len(pdf_docs)} PDF documents")
    all_documents.extend(pdf_docs)
    
    # Load Markdown documents
    print(f"  - Loading Markdown documents from {sources_dir}...")
    md_docs = md_connector.load_documents(sources_dir)
    print(f"    Found {len(md_docs)} Markdown documents")
    all_documents.extend(md_docs)
    
    if not all_documents:
        print("No documents found to index.")
        return
    
    # Filter for NEW or CHANGED documents only
    print(f"  - Checking for new or modified documents...")
    new_documents = []
    skipped_count = 0
    
    for doc in all_documents:
        # Check if document is already indexed
        if doc.document_id in document_store:
            # Document exists - check if it's been modified
            existing = document_store[doc.document_id]
            existing_modified = existing.get("last_modified")
            current_modified = doc.metadata.last_modified.isoformat() if doc.metadata.last_modified else None
            
            # Skip if:
            # 1. We don't have timestamp info (assume already indexed)
            # 2. Timestamps match (definitely not modified)
            if existing_modified is None or existing_modified == current_modified:
                skipped_count += 1
                continue
        
        # New or modified document - needs indexing
        new_documents.append(doc)
    
    print(f"    New/modified: {len(new_documents)}, Already indexed: {skipped_count}")
    
    if not new_documents:
        print("  - No new documents to index. All documents are up to date!")
        return
    
    # Chunk NEW documents only
    print(f"  - Chunking {len(new_documents)} new/modified documents...")
    all_chunks = []
    for doc in new_documents:
        chunks = chunker.chunk_document(doc)
        doc.chunks = chunks
        all_chunks.extend(chunks)
        
        # Store/update document metadata
        document_store[doc.document_id] = {
            "source_type": doc.metadata.source_type,
            "access_level": doc.metadata.access_level.value,
            "title": doc.metadata.title,
            "file_path": doc.metadata.file_path,
            "last_modified": doc.metadata.last_modified.isoformat() if doc.metadata.last_modified else None,
            "last_indexed": time.time()
        }
    
    print(f"    Created {len(all_chunks)} new chunks")
    
    if not all_chunks:
        print("No chunks created from documents.")
        return
    
    # Generate embeddings for NEW chunks only
    print(f"  - Generating embeddings for {len(all_chunks)} new chunks...")
    chunk_texts = [chunk.text for chunk in all_chunks]
    embeddings = embedder.embed_texts(chunk_texts, batch_size=32, show_progress=True)
    
    # Index NEW chunks in vector store
    print(f"  - Indexing in vector store...")
    vector_store.add_chunks(all_chunks, embeddings)
    
    # Index in keyword searcher (NOTE: rebuilds entire index with ALL chunks)
    print(f"  - Rebuilding keyword index with all chunks...")
    all_indexed_chunks = vector_store.chunks  # Get all chunks including old ones
    keyword_searcher.index_chunks(all_indexed_chunks)
    
    # Save vector store
    print(f"  - Saving vector store to {settings.vector_store_path}...")
    vector_store.save()
    
    duration = time.time() - start_time
    print(f"  - Indexing completed in {duration:.2f} seconds")
    print(f"  - Added {len(new_documents)} documents, {len(all_chunks)} chunks")
    
    # Log indexing operation
    if audit_logger:
        audit_logger.log_indexing(
            source_type="mixed",
            document_count=len(all_documents),
            chunk_count=len(all_chunks),
            duration_seconds=duration
        )


async def shutdown_event_deprecated():
    """Cleanup on shutdown - now handled by lifespan."""
    pass


@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "service": "Linked Documentation MCP Server",
        "version": "1.0.0",
        "status": "running",
        "docs": "/docs",
        "endpoints": {
            "health": "/api/v1/health",
            "list_sources": "/api/v1/list_sources",
            "search_docs": "/api/v1/search_docs",
            "get_doc_context": "/api/v1/get_doc_context",
            "stats": "/api/v1/stats"
        }
    }


if __name__ == "__main__":
    # Run the server
    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
        log_level="info"
    )

