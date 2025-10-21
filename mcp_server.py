#!/usr/bin/env python3
"""
MCP (Model Context Protocol) Server for Linked Documentation.

This server exposes the documentation search functionality via MCP
for use with Cursor and other AI tools.

Note: Diagnostic messages are printed to stderr. Some MCP clients like LM Studio
may display these as [ERROR] tags, but they are just informational logs.
Set DEBUG_MODE = True below for verbose protocol-level debugging.
"""

import asyncio
import json
import sys
from typing import Any, Dict, List, Optional
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from schemas.config import settings
from schemas.document import AccessLevel
from connectors import PDFConnector, MarkdownConnector
from indexing import TextChunker, Embedder, VectorStore, KeywordSearcher
from indexing.hybrid_search import HybridSearchEngine
from core import AccessController, AuditLogger

# Debug mode - set to False to reduce logging noise in LM Studio
DEBUG_MODE = False


class MCPDocumentationServer:
    """MCP server for documentation search."""
    
    def __init__(self):
        """Initialize the MCP server."""
        self.search_engine = None
        self.embedder = None
        self.vector_store = None
        self.keyword_searcher = None
        self.access_controller = None
        self.audit_logger = None
        self.document_store = {}
        self.initialized = False
    
    async def initialize(self):
        """Initialize the search engine and load documents."""
        if self.initialized:
            return
        
        if DEBUG_MODE:
            print("Initializing MCP Documentation Server...", file=sys.stderr)
            print(f"  Data directory: {settings.data_dir}", file=sys.stderr)
            print(f"  Vector store path: {settings.vector_store_path}", file=sys.stderr)
            print(f"  Data dir exists: {settings.data_dir.exists()}", file=sys.stderr)
            print(f"  Vector store exists: {settings.vector_store_path.exists()}", file=sys.stderr)
        
        # Initialize embedder
        self.embedder = Embedder(
            model_name=settings.embedding_model,
            device=settings.embedding_device
        )
        
        # Initialize vector store
        self.vector_store = VectorStore(
            embedding_dim=self.embedder.get_embedding_dimension(),
            store_path=settings.vector_store_path
        )
        
        # Initialize keyword searcher
        self.keyword_searcher = KeywordSearcher()
        
        # Initialize hybrid search engine
        self.search_engine = HybridSearchEngine(
            vector_store=self.vector_store,
            keyword_searcher=self.keyword_searcher,
            embedder=self.embedder,
            semantic_weight=settings.semantic_weight,
            keyword_weight=settings.keyword_weight
        )
        
        # Initialize access control and audit
        self.access_controller = AccessController()
        self.audit_logger = AuditLogger(
            log_path=settings.audit_log_path,
            enabled=settings.enable_audit_logging
        )
        
        # Load metadata from existing index and check for new documents
        stats = self.vector_store.get_stats()
        if stats['total_vectors'] > 0:
            # Load metadata for existing documents from chunks
            await self.load_document_metadata()
        
        # Always check for new or modified documents (incremental indexing)
        await self.index_documents()
        
        self.initialized = True
        print("MCP Server initialized successfully!", file=sys.stderr)
    
    async def load_document_metadata(self):
        """Load metadata for already-indexed documents."""
        sources_dir = settings.data_dir / "sources"
        if not sources_dir.exists():
            return
        
        # Quick scan for metadata only
        pdf_connector = PDFConnector(
            source_id="pdf_connector",
            access_level=AccessLevel.INTERNAL
        )
        md_connector = MarkdownConnector(
            source_id="markdown_connector",
            access_level=AccessLevel.INTERNAL
        )
        
        all_documents = []
        all_documents.extend(pdf_connector.load_documents(sources_dir))
        all_documents.extend(md_connector.load_documents(sources_dir))
        
        for doc in all_documents:
            self.document_store[doc.document_id] = {
                "source_type": doc.metadata.source_type,
                "access_level": doc.metadata.access_level.value,
                "title": doc.metadata.title,
                "file_path": doc.metadata.file_path,
            }
        
        # Populate keyword searcher with existing chunks
        if self.vector_store.chunks:
            self.keyword_searcher.index_chunks(self.vector_store.chunks)
        
        print(f"Loaded metadata for {len(all_documents)} documents", file=sys.stderr)
    
    async def index_documents(self):
        """
        Load and index documents from the data directory.
        Only indexes NEW documents to avoid duplicates.
        """
        sources_dir = settings.data_dir / "sources"
        if not sources_dir.exists():
            print("No sources directory found. Creating...", file=sys.stderr)
            sources_dir.mkdir(parents=True, exist_ok=True)
            return
        
        # Initialize connectors
        pdf_connector = PDFConnector(
            source_id="pdf_connector",
            access_level=AccessLevel.INTERNAL
        )
        md_connector = MarkdownConnector(
            source_id="markdown_connector",
            access_level=AccessLevel.INTERNAL
        )
        
        # Initialize chunker
        chunker = TextChunker(
            chunk_size=settings.chunk_size,
            chunk_overlap=settings.chunk_overlap
        )
        
        # Load documents
        pdf_docs = pdf_connector.load_documents(sources_dir)
        md_docs = md_connector.load_documents(sources_dir)
        all_documents = pdf_docs + md_docs
        
        if not all_documents:
            print("No documents found to index.", file=sys.stderr)
            return
        
        # Filter for NEW documents only (skip already indexed)
        new_documents = []
        skipped_count = 0
        
        for doc in all_documents:
            if doc.document_id in self.document_store:
                skipped_count += 1
                continue
            new_documents.append(doc)
        
        if not new_documents:
            print(f"No new documents to index. All {len(all_documents)} documents already indexed.", file=sys.stderr)
            return
        
        print(f"Indexing {len(new_documents)} new documents (skipping {skipped_count} existing)...", file=sys.stderr)
        
        # Chunk NEW documents only
        all_chunks = []
        for doc in new_documents:
            chunks = chunker.chunk_document(doc)
            doc.chunks = chunks
            all_chunks.extend(chunks)
            
            self.document_store[doc.document_id] = {
                "source_type": doc.metadata.source_type,
                "access_level": doc.metadata.access_level.value,
                "title": doc.metadata.title,
                "file_path": doc.metadata.file_path,
            }
        
        if not all_chunks:
            return
        
        # Generate embeddings for NEW chunks
        chunk_texts = [chunk.text for chunk in all_chunks]
        embeddings = self.embedder.embed_texts(chunk_texts, batch_size=32)
        
        # Index NEW chunks
        self.vector_store.add_chunks(all_chunks, embeddings)
        
        # Rebuild keyword index with ALL chunks (including old ones)
        all_indexed_chunks = self.vector_store.chunks
        self.keyword_searcher.index_chunks(all_indexed_chunks)
        
        # Save
        self.vector_store.save()
        
        print(f"Indexed {len(new_documents)} new documents, {len(all_chunks)} new chunks", file=sys.stderr)
        print(f"Total: {len(self.document_store)} documents, {self.vector_store.get_stats()['total_vectors']} vectors", file=sys.stderr)
    
    async def search_documentation(
        self,
        query: str,
        top_k: int = 10,
        source_types: Optional[List[str]] = None
    ) -> List[Dict[str, Any]]:
        """
        Search documentation and return results.
        
        Args:
            query: Search query
            top_k: Number of results to return
            source_types: Optional filter by source types
            
        Returns:
            List of search results
        """
        if not self.initialized:
            await self.initialize()
        
        # Perform search (with expansion enabled by default)
        # This may return more than top_k chunks because high-scoring documents
        # get multiple chunks for better context
        results = self.search_engine.search(query, top_k=top_k, expand_results=True)
        
        # Filter by source types if specified
        if source_types:
            results = [
                (chunk, score) for chunk, score in results
                if chunk.metadata.get("source_type") in source_types
            ]
        
        # Don't trim here! The expansion logic already provides the right amount of context
        # Trimming would defeat the purpose of returning multiple chunks from top documents
        
        # Format results
        formatted_results = []
        for chunk, score in results:
            doc_meta = self.document_store.get(chunk.document_id, {})
            
            formatted_results.append({
                "title": chunk.metadata.get("title", "Untitled"),
                "content": chunk.text,
                "score": float(score),
                "source_type": chunk.metadata.get("source_type", "unknown"),
                "uri": chunk.uri,
                "file_path": doc_meta.get("file_path", ""),
            })
        
        # Log the query
        if self.audit_logger:
            self.audit_logger.log_query(
                query=query,
                results=results,
                user_id="mcp_client"
            )
        
        return formatted_results
    
    async def list_sources(self) -> Dict[str, Any]:
        """List available documentation sources."""
        if not self.initialized:
            await self.initialize()
        
        source_groups = {}
        for doc_id, doc_meta in self.document_store.items():
            source_type = doc_meta.get("source_type", "unknown")
            if source_type not in source_groups:
                source_groups[source_type] = {
                    "count": 0,
                    "access_level": doc_meta.get("access_level", "internal")
                }
            source_groups[source_type]["count"] += 1
        
        return {
            "sources": source_groups,
            "total_documents": len(self.document_store)
        }


# Global server instance
server = MCPDocumentationServer()


async def handle_request(request: Dict[str, Any]) -> Dict[str, Any]:
    """
    Handle an MCP request.
    
    Args:
        request: MCP request dictionary
        
    Returns:
        MCP response dictionary
    """
    method = request.get("method", "")
    params = request.get("params", {})
    
    try:
        if method == "initialize":
            # Initialize handshake
            return {
                "protocolVersion": "2024-11-05",
                "capabilities": {
                    "tools": {}
                },
                "serverInfo": {
                    "name": "linked-docs-mcp",
                    "version": "1.0.0"
                }
            }
        
        elif method == "tools/list":
            # List available tools - ensure we're initialized
            if not server.initialized:
                await server.initialize()
            
            return {
                "tools": [
                    {
                        "name": "search_documentation",
                        "description": "Search internal documentation using hybrid semantic and keyword search. Returns relevant documentation chunks with titles, snippets, and source references.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "query": {
                                    "type": "string",
                                    "description": "The search query to find relevant documentation"
                                },
                                "top_k": {
                                    "type": "integer",
                                    "description": "Number of results to return (default: 10, max: 20)",
                                    "default": 10,
                                    "minimum": 1,
                                    "maximum": 20
                                },
                                "source_types": {
                                    "type": "array",
                                    "items": {"type": "string"},
                                    "description": "Optional filter by source types (e.g., ['markdown', 'pdf'])"
                                }
                            },
                            "required": ["query"]
                        }
                    },
                    {
                        "name": "list_sources",
                        "description": "List all available documentation sources and their metadata. Shows document counts by source type.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {},
                            "required": []
                        }
                    }
                ]
            }
        
        elif method == "tools/call":
            # Ensure server is initialized
            if not server.initialized:
                await server.initialize()
            
            # Call a tool
            tool_name = params.get("name", "")
            arguments = params.get("arguments", {})
            
            if tool_name == "search_documentation":
                query = arguments.get("query", "")
                if not query:
                    return {
                        "content": [
                            {
                                "type": "text",
                                "text": "Error: query parameter is required"
                            }
                        ],
                        "isError": True
                    }
                
                top_k = min(arguments.get("top_k", 10), 20)
                source_types = arguments.get("source_types")
                
                results = await server.search_documentation(
                    query=query,
                    top_k=top_k,
                    source_types=source_types
                )
                
                if not results:
                    return {
                        "content": [
                            {
                                "type": "text",
                                "text": f"No results found for: {query}\n\nTry:\n- Using different keywords\n- Checking if documents are indexed\n- Running: python download_docs.py [URL] --crawl"
                            }
                        ]
                    }
                
                # Format as text for MCP - group by document
                # Group results by file_path to show document-level context
                doc_groups = {}
                for result in results:
                    file_path = result['file_path']
                    if file_path not in doc_groups:
                        doc_groups[file_path] = []
                    doc_groups[file_path].append(result)
                
                # Sort groups by best score in each group
                sorted_groups = sorted(
                    doc_groups.items(),
                    key=lambda x: max(r['score'] for r in x[1]),
                    reverse=True
                )
                
                content = f"Found {len(results)} results from {len(sorted_groups)} documents for: '{query}'\n\n"
                content += "=" * 60 + "\n\n"
                
                doc_num = 1
                for file_path, doc_results in sorted_groups:
                    # Show document header
                    title = doc_results[0]['title']
                    max_score = max(r['score'] for r in doc_results)
                    content += f"## {doc_num}. {title}\n\n"
                    content += f"**Best Score:** {max_score:.3f} | **Type:** {doc_results[0]['source_type']} | **Chunks:** {len(doc_results)}\n\n"
                    
                    # Show content from each chunk (more context now)
                    for chunk_result in doc_results:
                        chunk_content = chunk_result['content']
                        # Show more content - up to 800 chars per chunk
                        display_length = min(len(chunk_content), 800)
                        content += f"{chunk_content[:display_length]}"
                        if len(chunk_content) > display_length:
                            content += "..."
                        content += "\n\n"
                    
                    content += f"**Source:** `{file_path}`\n\n"
                    content += "-" * 60 + "\n\n"
                    doc_num += 1
                
                return {
                    "content": [
                        {
                            "type": "text",
                            "text": content
                        }
                    ]
                }
            
            elif tool_name == "list_sources":
                sources = await server.list_sources()
                
                content = "# Documentation Sources\n\n"
                content += f"**Total Documents:** {sources['total_documents']}\n\n"
                
                if sources['sources']:
                    content += "## By Source Type:\n\n"
                    for source_type, info in sources['sources'].items():
                        content += f"- **{source_type}**: {info['count']} documents (access: {info['access_level']})\n"
                else:
                    content += "No documents indexed yet.\n\n"
                    content += "To add documents:\n"
                    content += "```bash\n"
                    content += "python download_docs.py [URL] --crawl --max 20\n"
                    content += "```\n"
                
                return {
                    "content": [
                        {
                            "type": "text",
                            "text": content
                        }
                    ]
                }
            
            else:
                return {
                    "content": [
                        {
                            "type": "text",
                            "text": f"Error: Unknown tool '{tool_name}'"
                        }
                    ],
                    "isError": True
                }
        
        else:
            return {
                "error": {
                    "code": -32601,
                    "message": f"Method not found: {method}"
                }
            }
    
    except Exception as e:
        import traceback
        error_details = traceback.format_exc()
        print(f"Error handling request: {error_details}", file=sys.stderr)
        
        return {
            "content": [
                {
                    "type": "text",
                    "text": f"Error: {str(e)}\n\nCheck server logs for details."
                }
            ],
            "isError": True
        }


async def main():
    """Main MCP server loop using stdio transport."""
    print("Starting MCP Documentation Server...", file=sys.stderr)
    print(f"Python version: {sys.version}", file=sys.stderr)
    print(f"Working directory: {Path.cwd()}", file=sys.stderr)
    
    # Read from stdin, write to stdout (MCP stdio protocol)
    while True:
        try:
            # Read a line from stdin
            line = sys.stdin.readline()
            if not line:
                break
            
            line = line.strip()
            if not line:
                continue
            
            if DEBUG_MODE:
                print(f"Received: {line[:100]}...", file=sys.stderr)
            
            # Parse JSON-RPC request
            request = json.loads(line)
            
            # Handle request
            response = await handle_request(request)
            
            # Add jsonrpc version
            response["jsonrpc"] = "2.0"
            
            # Add id if present in request
            if "id" in request:
                response["id"] = request["id"]
            
            # Wrap in result if not error
            if "error" not in response and "result" not in response:
                response = {
                    "jsonrpc": "2.0",
                    "id": request.get("id"),
                    "result": response
                }
            
            # Write JSON-RPC response to stdout
            response_str = json.dumps(response)
            print(response_str, flush=True)
            if DEBUG_MODE:
                print(f"Sent response ({len(response_str)} chars)", file=sys.stderr)
        
        except json.JSONDecodeError as e:
            print(f"JSON decode error: {e}", file=sys.stderr)
            error_response = {
                "jsonrpc": "2.0",
                "error": {
                    "code": -32700,
                    "message": "Parse error"
                },
                "id": None
            }
            print(json.dumps(error_response), flush=True)
        
        except Exception as e:
            import traceback
            error_details = traceback.format_exc()
            print(f"Error: {error_details}", file=sys.stderr)
            
            error_response = {
                "jsonrpc": "2.0",
                "error": {
                    "code": -32603,
                    "message": f"Internal error: {str(e)}"
                },
                "id": None
            }
            print(json.dumps(error_response), flush=True)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nShutting down...", file=sys.stderr)
    except Exception as e:
        import traceback
        print(f"Fatal error: {traceback.format_exc()}", file=sys.stderr)
        sys.exit(1)
