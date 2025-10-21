"""Document-related data models."""

from datetime import datetime
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field
from enum import Enum


class AccessLevel(str, Enum):
    """Document access levels for permission control."""
    PUBLIC = "public"
    INTERNAL = "internal"
    RESTRICTED = "restricted"
    CONFIDENTIAL = "confidential"


class DocumentMetadata(BaseModel):
    """Metadata associated with a document."""
    
    source_type: str = Field(..., description="Type of source (pdf, markdown, html, etc.)")
    access_level: AccessLevel = Field(default=AccessLevel.INTERNAL, description="Access level for the document")
    title: str = Field(..., description="Document title")
    author: Optional[str] = Field(None, description="Document author")
    created_at: Optional[datetime] = Field(None, description="Document creation timestamp")
    last_modified: Optional[datetime] = Field(None, description="Last modification timestamp")
    file_path: str = Field(..., description="Original file path")
    file_size: Optional[int] = Field(None, description="File size in bytes")
    tags: list[str] = Field(default_factory=list, description="Document tags for categorization")
    custom_fields: Dict[str, Any] = Field(default_factory=dict, description="Additional custom metadata")


class DocumentChunk(BaseModel):
    """A chunk of text from a document with associated metadata."""
    
    chunk_id: str = Field(..., description="Unique identifier for the chunk")
    document_id: str = Field(..., description="Parent document identifier")
    text: str = Field(..., description="Text content of the chunk")
    chunk_index: int = Field(..., description="Sequential index of chunk within document")
    start_char: Optional[int] = Field(None, description="Starting character position in original document")
    end_char: Optional[int] = Field(None, description="Ending character position in original document")
    page_number: Optional[int] = Field(None, description="Page number for PDF documents")
    section_title: Optional[str] = Field(None, description="Section or heading title")
    uri: str = Field(..., description="Internal URI for this chunk (e.g., internal://pdf/doc.pdf#page-1)")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional chunk-specific metadata")


class Document(BaseModel):
    """A complete document with metadata and content."""
    
    document_id: str = Field(..., description="Unique identifier for the document")
    content: str = Field(..., description="Full text content of the document")
    metadata: DocumentMetadata = Field(..., description="Document metadata")
    chunks: list[DocumentChunk] = Field(default_factory=list, description="Document chunks for indexing")
    
    def to_uri(self, locator: Optional[str] = None) -> str:
        """
        Generate an internal URI for this document.
        
        Args:
            locator: Optional locator string (e.g., "page-5", "section-intro")
            
        Returns:
            Internal URI in format: internal://<source_type>/<path>#<locator>
        """
        source = self.metadata.source_type
        path = self.metadata.file_path.replace("\\", "/")
        uri = f"internal://{source}/{path}"
        if locator:
            uri += f"#{locator}"
        return uri

