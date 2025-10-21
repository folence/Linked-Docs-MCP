"""Access control for document filtering."""

from typing import List, Optional
from schemas.document import AccessLevel, DocumentChunk


class AccessController:
    """
    Manages access control for documents and search results.
    """
    
    # Define access hierarchy (lower number = less restrictive)
    ACCESS_HIERARCHY = {
        AccessLevel.PUBLIC: 0,
        AccessLevel.INTERNAL: 1,
        AccessLevel.RESTRICTED: 2,
        AccessLevel.CONFIDENTIAL: 3,
    }
    
    def __init__(self):
        """Initialize the access controller."""
        pass
    
    def filter_chunks(
        self,
        chunks: List[tuple],  # List of (chunk, score) tuples
        max_access_level: Optional[AccessLevel] = None,
        user_access_level: Optional[AccessLevel] = None
    ) -> List[tuple]:
        """
        Filter chunks based on access level.
        
        Args:
            chunks: List of (chunk, score) tuples
            max_access_level: Maximum access level to include
            user_access_level: User's access level (if None, uses max_access_level)
            
        Returns:
            Filtered list of (chunk, score) tuples
        """
        if not max_access_level and not user_access_level:
            # No filtering needed
            return chunks
        
        # Use user access level if provided, otherwise use max_access_level
        allowed_level = user_access_level or max_access_level
        
        filtered = []
        for chunk, score in chunks:
            chunk_access_level = self._get_chunk_access_level(chunk)
            if self.can_access(allowed_level, chunk_access_level):
                filtered.append((chunk, score))
        
        return filtered
    
    def can_access(
        self,
        user_level: AccessLevel,
        document_level: AccessLevel
    ) -> bool:
        """
        Check if a user with given access level can access a document.
        
        Args:
            user_level: User's access level
            document_level: Document's access level
            
        Returns:
            True if access is allowed, False otherwise
        """
        user_rank = self.ACCESS_HIERARCHY.get(user_level, 0)
        doc_rank = self.ACCESS_HIERARCHY.get(document_level, 0)
        
        # User can access if their level rank is >= document level rank
        return user_rank >= doc_rank
    
    def _get_chunk_access_level(self, chunk: DocumentChunk) -> AccessLevel:
        """
        Extract access level from chunk metadata.
        
        Args:
            chunk: Document chunk
            
        Returns:
            AccessLevel of the chunk
        """
        # Try to get from metadata
        if "access_level" in chunk.metadata:
            access_level_str = chunk.metadata["access_level"]
            try:
                return AccessLevel(access_level_str)
            except ValueError:
                pass
        
        # Default to INTERNAL if not specified
        return AccessLevel.INTERNAL
    
    def get_allowed_access_levels(self, user_level: AccessLevel) -> List[AccessLevel]:
        """
        Get all access levels that a user can access.
        
        Args:
            user_level: User's access level
            
        Returns:
            List of allowed AccessLevel values
        """
        user_rank = self.ACCESS_HIERARCHY.get(user_level, 0)
        allowed = []
        
        for level, rank in self.ACCESS_HIERARCHY.items():
            if user_rank >= rank:
                allowed.append(level)
        
        return allowed

