"""Base connector abstract class for document ingestion."""

from abc import ABC, abstractmethod
from typing import List, Dict, Any
from pathlib import Path
from schemas.document import Document, AccessLevel


class BaseConnector(ABC):
    """
    Abstract base class for document connectors.
    
    Each connector is responsible for:
    - Loading documents from a specific source type
    - Extracting text content and metadata
    - Assigning access levels
    """
    
    def __init__(self, source_id: str, access_level: AccessLevel = AccessLevel.INTERNAL):
        """
        Initialize the connector.
        
        Args:
            source_id: Unique identifier for this connector instance
            access_level: Default access level for documents from this source
        """
        self.source_id = source_id
        self.access_level = access_level
        self.source_type = self._get_source_type()
    
    @abstractmethod
    def _get_source_type(self) -> str:
        """
        Return the source type identifier (e.g., 'pdf', 'markdown', 'html').
        
        Returns:
            Source type string
        """
        pass
    
    @abstractmethod
    def load_documents(self, source_path: Path) -> List[Document]:
        """
        Load documents from the specified path.
        
        Args:
            source_path: Path to document(s) to load
            
        Returns:
            List of Document objects with content and metadata
        """
        pass
    
    @abstractmethod
    def get_metadata(self, file_path: Path) -> Dict[str, Any]:
        """
        Extract metadata from a document file.
        
        Args:
            file_path: Path to the document file
            
        Returns:
            Dictionary containing metadata fields
        """
        pass
    
    def validate_access(self, required_level: AccessLevel) -> bool:
        """
        Check if the required access level is satisfied.
        
        Args:
            required_level: The access level to check against
            
        Returns:
            True if access is granted, False otherwise
        """
        access_hierarchy = {
            AccessLevel.PUBLIC: 0,
            AccessLevel.INTERNAL: 1,
            AccessLevel.RESTRICTED: 2,
            AccessLevel.CONFIDENTIAL: 3,
        }
        return access_hierarchy[self.access_level] <= access_hierarchy[required_level]

