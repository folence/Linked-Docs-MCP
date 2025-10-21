---
title: Getting Started Guide
author: Documentation Team
tags: [guide, tutorial, getting-started]
---

# Getting Started Guide

Welcome to the Linked Documentation System! This guide will help you get started with using the system.

## Overview

The system provides two servers for searching and retrieving documentation using hybrid semantic and keyword search:

1. **REST API Server** (`main.py`) - FastAPI-based HTTP server for web applications
2. **MCP Server** (`mcp_server.py`) - Model Context Protocol server for AI assistants (Cursor, Claude Desktop, etc.)

Both servers use the same hybrid search engine that combines:

- **Semantic Search**: Understands the meaning of your queries using AI embeddings
- **Keyword Search**: Fast traditional search using BM25 algorithm
- **Hybrid Approach**: Combines both methods for optimal results

## Key Features

### 1. Multi-Format Support

The server supports various documentation formats:
- PDF documents
- Markdown files (.md)
- HTML pages (coming soon)

### 2. Access Control

Documents are tagged with access levels to ensure secure access:
- **Public**: Freely accessible to all users
- **Internal**: Available to internal team members
- **Restricted**: Limited to specific groups
- **Confidential**: Highly restricted access

### 3. Audit Logging

All queries and document accesses are logged for compliance and security auditing.

## Quick Start

### Installation

1. Install Python 3.10 or higher
2. Clone the repository
3. Install dependencies: `pip install -r requirements.txt`
4. Configure environment variables in `.env`

### Running the REST API Server

Start the REST API server with:
```bash
python main.py
```

The server will be available at `http://127.0.0.1:8000` with interactive API docs at `/docs`.

#### REST API Usage

Search documents:
```bash
curl -X POST "http://127.0.0.1:8000/api/v1/search_docs" \
  -H "Content-Type: application/json" \
  -d '{"query": "how to configure authentication", "top_k": 5}'
```

List sources:
```bash
curl "http://127.0.0.1:8000/api/v1/list_sources"
```

Get statistics:
```bash
curl "http://127.0.0.1:8000/api/v1/stats"
```

### Running the MCP Server

The MCP server is designed to be used with AI assistants like Cursor or Claude Desktop. It uses stdio transport (JSON-RPC over stdin/stdout).

Configure in your MCP client's configuration file (e.g., Cursor's MCP settings):
```json
{
  "mcpServers": {
    "linked-docs": {
      "command": "python",
      "args": ["C:\\path\\to\\LinkedDocsMCP\\mcp_server.py"]
    }
  }
}
```

The MCP server provides tools:
- `search_documentation` - Search internal documentation
- `list_sources` - List available documentation sources

These tools will appear in your AI assistant's tool palette.

## Architecture

The system uses a modular architecture with the following components:

- **Connectors**: Load documents from various sources (PDF, Markdown)
- **Indexing**: Create searchable indices using FAISS (vector) and BM25 (keyword)
- **Search Engine**: Hybrid search combining semantic and keyword methods
- **Servers**:
  - **REST API Server** (`main.py`): FastAPI HTTP server with endpoints at `/api/v1/*`
  - **MCP Server** (`mcp_server.py`): JSON-RPC stdio server for AI assistants
- **Access Control**: Permission management and document access levels
- **Audit Logging**: Query and access tracking

## Best Practices

1. **Organize Documents**: Keep your documentation well-organized in the `data/sources` directory
2. **Use Descriptive Titles**: Ensure documents have clear titles for better searchability
3. **Tag Appropriately**: Add relevant tags to help with filtering
4. **Regular Updates**: Re-index documents when they change

## Troubleshooting

### REST API Server Won't Start

- Check that all dependencies are installed: `pip install -r requirements.txt`
- Verify Python version is 3.10+
- Ensure the `data` directory exists
- Check port 8000 is not already in use
- Review console output for error messages

### MCP Server Not Connecting

- Verify the path in your MCP client configuration is correct
- Check that Python is in your PATH
- Look for error messages in your AI assistant's logs
- Test the server standalone: `python mcp_server.py` (it will wait for stdin input)

### Search Returns No Results

- Verify documents are in the `data/sources` directory
- Check that indexing completed successfully (look for vector store files in `data/vector_store/`)
- Add documents by placing PDF or Markdown files in `data/sources/`
- Restart the server to trigger re-indexing

### Poor Search Quality

- Try adjusting semantic vs keyword weights in `schemas/config.py`
- Consider the chunk size settings (default: 512 tokens)
- Review document quality and formatting
- Ensure documents have proper titles and structure

## Support

For additional help and support, please refer to:
- **REST API Documentation**: `http://127.0.0.1:8000/docs` (interactive Swagger UI)
- **API Reference**: See `api_reference.md` for detailed endpoint documentation
- **GitHub Issues**: Report bugs and feature requests
- **Audit Logs**: Check `data/audit.log` for query history and debugging

## Next Steps

Now that you understand the basics, explore:
- **For Web Integration**: Use the REST API server with your web applications
- **For AI Assistants**: Configure the MCP server in Cursor or Claude Desktop
- **Advanced Features**: Explore access control, custom connectors, and performance tuning
- **Adding Documents**: Place your internal docs in `data/sources/` and restart the server

