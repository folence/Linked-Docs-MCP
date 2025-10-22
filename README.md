# Linked Documentation System

> **A production-ready RAG system with dual interfaces: REST API + MCP Protocol**  
> Enables web applications and AI assistants to intelligently search and reference documentation using hybrid semantic + keyword search.

## 🎯 What Is This?

This is a **complete RAG (Retrieval Augmented Generation) system** that provides two ways to access powerful documentation search:

1. **REST API Server** (`main.py`) - FastAPI-based HTTP server for web applications and integrations
2. **MCP Server** (`mcp_server.py`) - Model Context Protocol server for AI assistants (Cursor, Claude Desktop)

Both servers share the same hybrid search engine, enabling accurate documentation retrieval whether you're building a web app or empowering an AI assistant.

### Key Features

- **Intelligent Hybrid Search**: Combines semantic understanding (FAISS embeddings) with keyword matching (BM25)
- **Smart Ranking**: Title/metadata boosting, multi-chunk document expansion, relevance scoring
- **Multi-Format Support**: PDF, Markdown, and web documentation (via built-in scraper)
- **MCP Native**: Works seamlessly in Cursor, Claude Desktop, and other MCP-compatible tools
- **Enterprise Ready**: Access control, audit logging, local-first architecture
- **Fast**: <200ms search latency, optimized chunking and indexing
- **Zero Cost**: Runs 100% locally, no API keys or cloud dependencies

## 🏗️ How It Works

```
┌─────────────────────────────────────────────────────────┐
│              AI Assistant (Cursor/Claude)               │
└────────────────────┬────────────────────────────────────┘
                     │ MCP Protocol (JSON-RPC over stdio)
                     ▼
┌─────────────────────────────────────────────────────────┐
│                   mcp_server.py                         │
│  ┌─────────────────────────────────────────────────┐   │
│  │  Tools: search_documentation(), list_sources()  │   │
│  └─────────────────────────────────────────────────┘   │
└────────────────────┬────────────────────────────────────┘
                     │
    ┌────────────────┼────────────────┐
    ▼                ▼                ▼
┌─────────┐   ┌──────────┐   ┌──────────────┐
│ Hybrid  │   │ Access   │   │ Audit Logger │
│ Search  │   │ Control  │   │              │
└────┬────┘   └──────────┘   └──────────────┘
     │
     ├─ Semantic Search (FAISS + embeddings)
     │   • Title/metadata boosting
     │   • Multi-chunk document expansion
     │
     └─ Keyword Search (BM25)
         • Exact term matching
         • Traditional ranking
```

### Project Structure

```
LinkedDocsMCP/
├── mcp_server.py          # Main MCP server (stdio interface)
├── main.py                # FastAPI server (for testing/debugging)
├── download_docs.py       # Web documentation scraper CLI
├── connectors/            # Document format handlers
│   ├── pdf.py            # PDF extraction
│   └── markdown.py       # Markdown parsing
├── indexing/             # Search engine core
│   ├── chunker.py        # Semantic text chunking
│   ├── embedder.py       # Sentence transformers
│   ├── vector_store.py   # FAISS vector database
│   ├── keyword_search.py # BM25 implementation
│   └── hybrid_search.py  # Combined search with boosting
├── schemas/              # Data models
│   ├── config.py         # Settings & configuration
│   └── document.py       # Document schemas
├── core/                 # Cross-cutting concerns
│   ├── access_control.py # Permission system
│   └── audit.py          # Query logging
└── data/                 # Local storage
    ├── sources/          # Your documents (PDF, MD)
    └── vector_store/     # Indexed vectors & metadata
```

## 🚀 Quick Start (5 Minutes)

### Prerequisites
- Python 3.10+
- Cursor or Claude Desktop (for MCP integration)

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

**First run**: Downloads ~80MB embedding model (one-time)

### 2. Add Documentation

**Option A: Download from web**
```bash
# Download Factorio wiki (example)
python download_docs.py https://wiki.factorio.com/Tutorials --crawl --max 20
```

**Option B: Add your own files**
```bash
# Copy PDFs or Markdown files
copy your-docs.pdf data/sources/
copy your-guide.md data/sources/
```

### 3. Set Up MCP in Cursor (or other LLM service)

Add to your Cursor MCP config (`~/.cursor/mcp.json` or `C:\Users\<USER>\.cursor\mcp.json`):

```json
{
  "mcpServers": {
    "linked-docs": {
      "command": "python",
      "args": ["C:/full/path/to/LinkedDocsMCP/mcp_server.py"]
    }
  }
}
```

### 4. Restart Cursor & Use!

In Cursor's chat:
```
What are the different enemy types in Factorio?
```

The AI will automatically search your documentation and provide accurate, cited answers! ✨

## Key Features Explained

### Hybrid Search

Combines two complementary approaches:

**Semantic Search (70% weight)**
- Uses `sentence-transformers` (all-MiniLM-L6-v2 model)
- Understands meaning: "authentication setup" matches "configuring auth"
- Converts text to 384-dimensional vectors
- Fast similarity search with FAISS

**Keyword Search (30% weight)**
- Uses BM25 algorithm (same as Elasticsearch)
- Exact term matching: great for technical terms, code, etc.
- Traditional ranking with document length normalization

**Smart Ranking Enhancements:**
- **Title Boosting**: Documents whose titles match the query get 3x boost
- **Multi-Chunk Expansion**: Returns up to 3 sequential chunks from highly relevant documents
- **Document Grouping**: Results grouped by source document for better context

### Semantic Chunking

Unlike naive character-splitting, this uses smart boundaries:

1. **Markdown headers** (`##`, `###`) - keeps sections together
2. **Paragraph breaks** (`\n\n`) - maintains topical coherence  
3. **Sentences** - fallback for unstructured text

**Settings:**
- Chunk size: 2048 characters (whole sections, not fragments)
- Overlap: 200 characters (prevents context loss at boundaries)

### Web Documentation Scraper

Built-in tool to download and convert web docs:

```bash
# Download single page
python download_docs.py https://wiki.example.com/Guide

# Crawl multiple pages (with smart duplicate detection)
python download_docs.py https://wiki.example.com/Main --crawl --max 50

# Force re-download (skip existing detection)
python download_docs.py https://wiki.example.com/Main --crawl --force

# Filter by language
python download_docs.py https://wiki.example.com/Main --crawl --languages en,de
```

**Features:**
- Auto-detects and skips existing pages (saves time & bandwidth)
- Respects same-domain and link patterns
- Polite crawling with configurable delays
- Converts HTML to clean Markdown with metadata
- Preserves document structure (headers, lists, tables)

## 🔒 Security & Access Control

**Built-in features:**
- 4-tier access hierarchy: PUBLIC → INTERNAL → RESTRICTED → CONFIDENTIAL
- Query-time filtering based on user permissions
- Full audit logging (every query tracked)
- Local-only processing (no data leaves your machine)

**Audit logs** (`data/audit.log`):
```json
{
  "timestamp": "2025-10-21T14:30:00Z",
  "event_type": "search",
  "user_id": "mcp_client",
  "query": "enemy types",
  "results_count": 5,
  "search_time_ms": 143
}
```

## ⚙️ Configuration

Edit `schemas/config.py` or set environment variables:

```python
# Search weights
SEMANTIC_WEIGHT = 0.7  # Meaning-based search
KEYWORD_WEIGHT = 0.3   # Exact term matching

# Chunking
CHUNK_SIZE = 1280      # Larger chunks for complete sections
CHUNK_OVERLAP = 128    # Overlap for context continuity

# Model
EMBEDDING_MODEL = "all-MiniLM-L6-v2"  # Fast, accurate, small
```

## 🔧 Advanced Usage

### REST API (for testing/debugging)

```bash
# Start FastAPI server
python main.py

# Search via REST
curl -X POST http://localhost:8000/api/v1/search_docs \
  -H "Content-Type: application/json" \
  -d '{"query": "getting started", "top_k": 5}'

# Interactive API docs
open http://localhost:8000/docs
```

### Programmatic Usage

```python
from indexing.embedder import Embedder
from indexing.vector_store import VectorStore
from indexing.hybrid_search import HybridSearchEngine

# Initialize
embedder = Embedder(model_name="all-MiniLM-L6-v2")
vector_store = VectorStore(embedding_dim=384)
search_engine = HybridSearchEngine(vector_store, keyword_searcher, embedder)

# Search
results = search_engine.search("how to configure auth", top_k=5)
for chunk, score in results:
    print(f"{score:.3f}: {chunk.text[:100]}...")
```

### Technical Highlights

1. **Hybrid search** outperforms pure semantic or keyword alone
2. **Smart chunking** preserves document structure
3. **Title boosting** dramatically improves ranking quality
4. **Multi-chunk expansion** provides complete context
5. **Zero cloud dependencies** - privacy-first architecture
6. **MCP native** - works with any compatible AI assistant

## 🙏 Acknowledgments

Built with:
- **FastAPI** - Modern Python web framework
- **Sentence Transformers** - Semantic embeddings
- **FAISS** - Vector similarity search
- **BM25** (rank-bm25) - Keyword ranking
- **MCP** - Model Context Protocol by Anthropic

---

**Status**: ✅ Demo Ready | **Version**: 1.0.0 | **Updated**: October 2025

