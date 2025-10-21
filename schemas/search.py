"""Search-related data models."""

from typing import Optional
from pydantic import BaseModel, Field
from .document import AccessLevel


class SearchQuery(BaseModel):
    """A search query request."""
    
    query: str = Field(..., description="Search query text", min_length=1)
    top_k: int = Field(default=10, description="Number of results to return", ge=1, le=100)
    access_level: Optional[AccessLevel] = Field(
        default=None, 
        description="Maximum access level for filtering results"
    )
    source_types: Optional[list[str]] = Field(
        default=None,
        description="Filter by specific source types (pdf, markdown, etc.)"
    )
    tags: Optional[list[str]] = Field(
        default=None,
        description="Filter by document tags"
    )
    user_id: Optional[str] = Field(
        default=None,
        description="User ID for audit logging"
    )


class SearchResult(BaseModel):
    """A single search result."""
    
    title: str = Field(..., description="Document title")
    uri: str = Field(..., description="Internal URI to the document/chunk")
    snippet: str = Field(..., description="Text snippet showing relevant content")
    score: float = Field(..., description="Relevance score (0-1)", ge=0.0, le=1.0)
    source_type: str = Field(..., description="Type of source document")
    access_level: AccessLevel = Field(..., description="Access level of the document")
    last_modified: Optional[str] = Field(None, description="Last modification timestamp")
    chunk_index: Optional[int] = Field(None, description="Chunk index within document")
    page_number: Optional[int] = Field(None, description="Page number for PDF documents")
    section_title: Optional[str] = Field(None, description="Section or heading title")


class SearchResponse(BaseModel):
    """Response containing search results."""
    
    query: str = Field(..., description="Original search query")
    total_results: int = Field(..., description="Total number of results found")
    results: list[SearchResult] = Field(..., description="List of search results")
    search_time_ms: float = Field(..., description="Time taken to perform search in milliseconds")


class DocumentContextRequest(BaseModel):
    """Request for full document context."""
    
    uri: str = Field(..., description="Internal URI of the document/chunk")
    user_id: Optional[str] = Field(None, description="User ID for audit logging")


class DocumentContextResponse(BaseModel):
    """Response containing full document context."""
    
    uri: str = Field(..., description="Internal URI of the document")
    title: str = Field(..., description="Document title")
    content: str = Field(..., description="Full content of the document/chunk")
    metadata: dict = Field(..., description="Document metadata")
    access_level: AccessLevel = Field(..., description="Access level of the document")


class SourceInfo(BaseModel):
    """Information about a documentation source."""
    
    source_id: str = Field(..., description="Unique identifier for the source")
    source_type: str = Field(..., description="Type of source (pdf, markdown, etc.)")
    access_level: AccessLevel = Field(..., description="Access level for the source")
    document_count: int = Field(..., description="Number of documents from this source")
    last_indexed: Optional[str] = Field(None, description="Timestamp of last indexing")


class ListSourcesResponse(BaseModel):
    """Response listing all available sources."""
    
    sources: list[SourceInfo] = Field(..., description="List of documentation sources")
    total_sources: int = Field(..., description="Total number of sources")
    total_documents: int = Field(..., description="Total number of indexed documents")

