"""Text chunking utilities for document processing."""

from typing import List
from schemas.document import Document, DocumentChunk


class TextChunker:
    """
    Splits document text into smaller chunks for indexing.
    
    Uses sliding window approach with overlap to maintain context.
    """
    
    def __init__(self, chunk_size: int = 1280, chunk_overlap: int = 128):
        """
        Initialize the chunker.
        
        Args:
            chunk_size: Target size of each chunk in characters
            chunk_overlap: Number of characters to overlap between chunks
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
    
    def chunk_document(self, document: Document) -> List[DocumentChunk]:
        """
        Split a document into chunks using semantic boundaries.
        
        Prioritizes splitting at:
        1. Section headers (##, ###, etc.)
        2. Paragraph boundaries
        3. Sentence boundaries
        
        Args:
            document: Document to chunk
            
        Returns:
            List of DocumentChunk objects
        """
        chunks = []
        text = document.content
        
        # Handle empty documents
        if not text or not text.strip():
            return chunks
        
        # Try semantic chunking first (split on headers/sections)
        sections = self._split_into_sections(text)
        
        current_chunk = ""
        current_start = 0
        chunk_index = 0
        
        for section in sections:
            # If adding this section exceeds chunk size and we have content
            if len(current_chunk) + len(section) > self.chunk_size and current_chunk:
                # Save current chunk
                chunk = self._create_chunk(
                    document=document,
                    text=current_chunk.strip(),
                    chunk_index=chunk_index,
                    start_char=current_start,
                    end_char=current_start + len(current_chunk)
                )
                chunks.append(chunk)
                
                # Calculate overlap for next chunk
                overlap_text = self._get_overlap_text(current_chunk, self.chunk_overlap)
                current_chunk = overlap_text + section
                current_start = current_start + len(current_chunk) - len(overlap_text) - len(section)
                chunk_index += 1
            else:
                current_chunk += section
        
        # Add the last chunk if there's remaining text
        if current_chunk.strip():
            chunk = self._create_chunk(
                document=document,
                text=current_chunk.strip(),
                chunk_index=chunk_index,
                start_char=current_start,
                end_char=current_start + len(current_chunk)
            )
            chunks.append(chunk)
        
        return chunks
    
    def _split_into_sections(self, text: str) -> List[str]:
        """
        Split text into semantic sections.
        
        Prioritizes splitting at:
        1. Markdown headers (##, ###)
        2. Double newlines (paragraphs)
        3. Single newlines
        
        Args:
            text: Text to split
            
        Returns:
            List of text sections
        """
        import re
        
        # Split on markdown headers but keep the header with the section
        # This regex matches lines starting with # (headers)
        header_pattern = r'(^|\n)(#{1,6}\s+.+)'
        
        # First, try to split on headers
        parts = re.split(header_pattern, text, flags=re.MULTILINE)
        
        # Reconstruct sections, keeping headers with their content
        sections = []
        current_section = ""
        
        for part in parts:
            if not part or part == '\n':
                continue
            
            # If it's a header, start a new section
            if re.match(r'^#{1,6}\s+', part.strip()):
                if current_section:
                    sections.append(current_section)
                current_section = part
            else:
                current_section += part
        
        if current_section:
            sections.append(current_section)
        
        # If no headers found, split on paragraph boundaries
        if len(sections) <= 1:
            sections = re.split(r'\n\s*\n', text)
        
        # If still too few sections, fall back to sentence splitting
        if len(sections) <= 1:
            sections = self._split_into_sentences(text)
        
        return sections
    
    def _split_into_sentences(self, text: str) -> List[str]:
        """
        Split text into sentences.
        
        Args:
            text: Text to split
            
        Returns:
            List of sentences
        """
        import re
        
        # Simple sentence splitting on common terminators
        # This is a basic implementation; could be improved with more sophisticated NLP
        sentences = re.split(r'(?<=[.!?])\s+', text)
        return sentences
    
    def _get_overlap_text(self, text: str, overlap_size: int) -> str:
        """
        Get the last N characters of text for overlap.
        
        Args:
            text: Text to get overlap from
            overlap_size: Number of characters to overlap
            
        Returns:
            Overlap text
        """
        if len(text) <= overlap_size:
            return text
        
        # Try to find a good breaking point (space) near the overlap boundary
        overlap_text = text[-overlap_size:]
        space_idx = overlap_text.find(' ')
        if space_idx > 0:
            return overlap_text[space_idx + 1:]
        return overlap_text
    
    def _create_chunk(
        self,
        document: Document,
        text: str,
        chunk_index: int,
        start_char: int,
        end_char: int
    ) -> DocumentChunk:
        """
        Create a DocumentChunk object.
        
        Args:
            document: Parent document
            text: Chunk text
            chunk_index: Index of this chunk
            start_char: Starting character position
            end_char: Ending character position
            
        Returns:
            DocumentChunk object
        """
        chunk_id = f"{document.document_id}_chunk_{chunk_index}"
        
        # Create URI with chunk locator
        uri = document.to_uri(f"chunk-{chunk_index}")
        
        return DocumentChunk(
            chunk_id=chunk_id,
            document_id=document.document_id,
            text=text,
            chunk_index=chunk_index,
            start_char=start_char,
            end_char=end_char,
            uri=uri,
            metadata={
                "source_type": document.metadata.source_type,
                "access_level": document.metadata.access_level.value,
                "title": document.metadata.title,
            }
        )

