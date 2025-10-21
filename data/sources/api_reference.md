---
title: API Reference Documentation
author: API Team
tags: [api, reference, documentation]
---

# REST API Reference Documentation

Complete reference for the Linked Documentation REST API Server (`main.py`) endpoints.

This document covers the **REST API server**. For information about the **MCP server** for AI assistants, see the "MCP Server" section at the end.

## Base URL

All REST API endpoints are relative to: `http://127.0.0.1:8000/api/v1`

The base URL and port can be configured in `schemas/config.py` or via environment variables.

## Interactive Documentation

The REST API server provides interactive documentation:
- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

## Authentication

Currently, the server does not require authentication. In production, you should implement:
- API keys
- OAuth 2.0
- JWT tokens

## Endpoints

### Health Check

Check if the server is running.

**Endpoint**: `GET /health`

**Response**:
```json
{
  "status": "healthy",
  "service": "Linked Documentation MCP Server",
  "version": "1.0.0"
}
```

### List Sources

Retrieve information about all indexed documentation sources.

**Endpoint**: `GET /list_sources`

**Response**: `ListSourcesResponse`
```json
{
  "sources": [
    {
      "source_id": "pdf_connector_001",
      "source_type": "pdf",
      "access_level": "internal",
      "document_count": 5,
      "last_indexed": "2025-01-15T10:30:00Z"
    }
  ],
  "total_sources": 1,
  "total_documents": 5
}
```

### Search Documents

Search across all documentation using hybrid search.

**Endpoint**: `POST /search_docs`

**Request Body**: `SearchQuery`
```json
{
  "query": "how to authenticate users",
  "top_k": 10,
  "access_level": "internal",
  "source_types": ["pdf", "markdown"],
  "tags": ["api", "authentication"],
  "user_id": "user123"
}
```

**Parameters**:
- `query` (required): Search query text
- `top_k` (optional, default=10): Number of results to return
- `access_level` (optional): Maximum access level filter
- `source_types` (optional): Filter by source types
- `tags` (optional): Filter by document tags
- `user_id` (optional): User ID for audit logging

**Response**: `SearchResponse`
```json
{
  "query": "how to authenticate users",
  "total_results": 3,
  "results": [
    {
      "title": "Authentication Guide",
      "uri": "internal://pdf/auth_guide.pdf#chunk-5",
      "snippet": "To authenticate users, configure the auth module...",
      "score": 0.92,
      "source_type": "pdf",
      "access_level": "internal",
      "last_modified": "2025-01-15T10:30:00Z",
      "chunk_index": 5,
      "page_number": 3,
      "section_title": "User Authentication"
    }
  ],
  "search_time_ms": 45.2
}
```

### Get Document Context

Retrieve the full context for a specific document or chunk.

**Endpoint**: `GET /get_doc_context`

**Query Parameters**:
- `uri` (required): Internal URI of the document/chunk
- `user_id` (optional): User ID for audit logging

**Example**: `/get_doc_context?uri=internal://pdf/guide.pdf%23chunk-0`

**Response**: `DocumentContextResponse`
```json
{
  "uri": "internal://pdf/guide.pdf#chunk-0",
  "title": "User Guide",
  "content": "Full text content of the chunk...",
  "metadata": {
    "document_id": "pdf_abc123def456",
    "chunk_id": "pdf_abc123def456_chunk_0",
    "chunk_index": 0,
    "source_type": "pdf",
    "page_number": 1
  },
  "access_level": "internal"
}
```

### Get Statistics

Retrieve server statistics and indexing information.

**Endpoint**: `GET /stats`

**Response**:
```json
{
  "total_documents": 15,
  "search_engine": {
    "vector_store": {
      "total_vectors": 234,
      "total_chunks": 234,
      "embedding_dim": 384
    },
    "keyword_searcher": {
      "total_chunks": 234,
      "avg_tokens_per_chunk": 87.5
    },
    "semantic_weight": 0.7,
    "keyword_weight": 0.3
  }
}
```

## Data Models

### AccessLevel

Document access levels (enum):
- `public`
- `internal`
- `restricted`
- `confidential`

### Internal URI Format

Documents and chunks are identified using internal URIs:

Format: `internal://<source_type>/<file_path>#<locator>`

Examples:
- `internal://pdf/guides/user_guide.pdf#page-5`
- `internal://markdown/api_docs.md#chunk-10`
- `internal://html/wiki/setup.html#section-intro`

## Error Responses

All error responses follow this format:
```json
{
  "detail": "Error message description"
}
```

### Common Status Codes

- `200 OK`: Request successful
- `400 Bad Request`: Invalid request parameters
- `404 Not Found`: Resource not found
- `500 Internal Server Error`: Server error

## Rate Limiting

Currently not implemented in the prototype. For production:
- Implement rate limiting per user/IP
- Suggested: 100 requests per minute per user

## Versioning

The API uses URL versioning: `/api/v1/`

Future versions will be accessible via `/api/v2/`, etc.

## Best Practices

1. **Use Specific Queries**: More specific queries yield better results
2. **Apply Filters**: Use access_level, source_types, and tags to narrow results
3. **Handle Pagination**: For large result sets, use top_k appropriately
4. **Cache Results**: Cache frequently accessed documents
5. **Monitor Performance**: Track search_time_ms for optimization

## Examples

### Python Example

```python
import requests

# Search documents
response = requests.post(
    "http://127.0.0.1:8000/api/v1/search_docs",
    json={
        "query": "deployment configuration",
        "top_k": 5,
        "access_level": "internal"
    }
)

results = response.json()
for result in results["results"]:
    print(f"{result['title']}: {result['score']}")
```

### cURL Example

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/search_docs" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "authentication setup",
    "top_k": 3
  }'
```

## Changelog

### Version 1.0.0 (Current)
- Initial release
- Hybrid search implementation
- PDF and Markdown support
- Basic access control
- Audit logging

### Planned Features
- HTML document support
- Advanced access control with user groups
- Real-time indexing
- Elasticsearch integration option
- GraphQL API

## MCP Server

The project also includes an **MCP (Model Context Protocol) Server** (`mcp_server.py`) designed for integration with AI assistants like Cursor and Claude Desktop.

### What is MCP?

MCP is a protocol that allows AI assistants to access external tools and data sources. The MCP server exposes documentation search functionality as tools that AI assistants can use.

### How It Works

The MCP server:
- Uses **stdio transport** (JSON-RPC over stdin/stdout)
- Shares the same hybrid search engine as the REST API
- Provides tools instead of HTTP endpoints
- Is configured in the AI assistant's settings file

### Configuration

Add to your MCP client configuration file:

#### Cursor Configuration
In your Cursor MCP settings (typically in `%APPDATA%\Cursor\User\globalStorage\rooveterinaryinc.roo-cline\settings\cline_mcp_settings.json`):

```json
{
  "mcpServers": {
    "linked-docs": {
      "command": "python",
      "args": ["C:\\projects\\AI\\LinkedDocsMCP\\mcp_server.py"]
    }
  }
}
```

#### Claude Desktop Configuration
In `%APPDATA%\Claude\claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "linked-docs": {
      "command": "python",
      "args": ["C:\\projects\\AI\\LinkedDocsMCP\\mcp_server.py"]
    }
  }
}
```

### Available MCP Tools

#### 1. search_documentation

Search internal documentation using hybrid semantic and keyword search.

**Parameters:**
- `query` (required): The search query string
- `top_k` (optional): Number of results to return (default: 10, max: 20)
- `source_types` (optional): Filter by source types (e.g., `["markdown", "pdf"]`)

**Returns:**
Formatted text with search results including:
- Document titles and scores
- Relevant content snippets
- Source file paths
- Grouped by document for better context

**Example Usage in AI Assistant:**
```
Search for "authentication setup" in the documentation
```

The AI assistant will automatically call the `search_documentation` tool with the appropriate query.

#### 2. list_sources

List all available documentation sources and their metadata.

**Parameters:** None

**Returns:**
Formatted text showing:
- Total number of documents indexed
- Document counts by source type (pdf, markdown)
- Access levels for each source type

**Example Usage in AI Assistant:**
```
What documentation sources are available?
```

### Differences Between REST API and MCP Server

| Feature | REST API Server (`main.py`) | MCP Server (`mcp_server.py`) |
|---------|----------------------------|------------------------------|
| **Purpose** | Web applications, HTTP clients | AI assistants (Cursor, Claude Desktop) |
| **Protocol** | HTTP/REST | JSON-RPC over stdio |
| **Endpoints** | `/api/v1/search_docs`, `/api/v1/list_sources`, etc. | Tools: `search_documentation`, `list_sources` |
| **Authentication** | Can add API keys, OAuth | Controlled by AI assistant access |
| **Interactive Docs** | Swagger UI at `/docs` | Tool definitions in MCP protocol |
| **Running** | `python main.py` (runs as web server) | Launched by AI assistant on-demand |
| **Port** | 8000 (configurable) | No network port (stdio only) |

### When to Use Which Server

**Use REST API Server when:**
- Building web applications
- Need HTTP endpoints for remote access
- Want to integrate with existing web services
- Need interactive API documentation (Swagger)
- Accessing from scripts, curl, or HTTP clients

**Use MCP Server when:**
- Working with Cursor or Claude Desktop
- Want AI assistant to search documentation while coding
- Need context-aware documentation retrieval
- Want seamless integration with AI tools
- No network access required

### Debugging MCP Server

If the MCP server is not working:

1. **Test standalone**: Run `python mcp_server.py` and verify it starts without errors (it will wait for stdin)
2. **Check logs**: Look in your AI assistant's logs for connection errors
3. **Verify path**: Ensure the path in your MCP configuration is absolute and correct
4. **Check Python**: Verify Python is in your PATH: `python --version`
5. **Test indexing**: Ensure documents are indexed by checking `data/vector_store/` directory
6. **Review audit logs**: Check `data/audit.log` for MCP queries

### Performance Considerations

Both servers share the same underlying search engine and index:
- First query may be slower (loading embeddings and index)
- Subsequent queries are fast (cached in memory)
- Index is loaded once per server instance
- Both servers support incremental indexing (only new documents are processed)

