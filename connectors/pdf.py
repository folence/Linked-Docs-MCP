"""PDF document connector using pdfplumber."""

import hashlib
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any
import pdfplumber

from schemas.document import Document, DocumentMetadata, AccessLevel
from .base import BaseConnector


class PDFConnector(BaseConnector):
    """Connector for loading PDF documents."""
    
    def _get_source_type(self) -> str:
        """Return the source type identifier."""
        return "pdf"
    
    def load_documents(self, source_path: Path) -> List[Document]:
        """
        Load PDF documents from the specified path.
        
        Args:
            source_path: Path to a PDF file or directory containing PDFs
            
        Returns:
            List of Document objects
        """
        documents = []
        
        if source_path.is_file() and source_path.suffix.lower() == '.pdf':
            doc = self._load_single_pdf(source_path)
            if doc:
                documents.append(doc)
        elif source_path.is_dir():
            for pdf_file in source_path.rglob("*.pdf"):
                doc = self._load_single_pdf(pdf_file)
                if doc:
                    documents.append(doc)
        
        return documents
    
    def _load_single_pdf(self, file_path: Path) -> Document:
        """
        Load a single PDF file.
        
        Args:
            file_path: Path to the PDF file
            
        Returns:
            Document object or None if loading fails
        """
        try:
            with pdfplumber.open(file_path) as pdf:
                # Extract text from all pages
                text_content = []
                for page_num, page in enumerate(pdf.pages, start=1):
                    page_text = page.extract_text()
                    if page_text:
                        text_content.append(page_text)
                
                full_text = "\n\n".join(text_content)
                
                # Generate document ID
                doc_id = self._generate_document_id(file_path)
                
                # Get metadata
                metadata = self.get_metadata(file_path)
                doc_metadata = DocumentMetadata(
                    source_type=self.source_type,
                    access_level=self.access_level,
                    title=metadata.get("title", file_path.stem),
                    author=metadata.get("author"),
                    created_at=metadata.get("created_at"),
                    last_modified=metadata.get("last_modified"),
                    file_path=str(file_path),
                    file_size=metadata.get("file_size"),
                    tags=metadata.get("tags", []),
                    custom_fields={
                        "page_count": len(pdf.pages),
                        "has_images": any(len(page.images) > 0 for page in pdf.pages),
                    }
                )
                
                document = Document(
                    document_id=doc_id,
                    content=full_text,
                    metadata=doc_metadata,
                    chunks=[]
                )
                
                return document
                
        except Exception as e:
            print(f"Error loading PDF {file_path}: {e}")
            return None
    
    def get_metadata(self, file_path: Path) -> Dict[str, Any]:
        """
        Extract metadata from a PDF file.
        
        Args:
            file_path: Path to the PDF file
            
        Returns:
            Dictionary containing metadata fields
        """
        metadata = {}
        
        try:
            # File system metadata
            stat = file_path.stat()
            metadata["file_size"] = stat.st_size
            metadata["last_modified"] = datetime.fromtimestamp(stat.st_mtime)
            metadata["created_at"] = datetime.fromtimestamp(stat.st_ctime)
            
            # PDF-specific metadata
            with pdfplumber.open(file_path) as pdf:
                pdf_metadata = pdf.metadata or {}
                
                metadata["title"] = pdf_metadata.get("Title") or file_path.stem
                metadata["author"] = pdf_metadata.get("Author")
                metadata["subject"] = pdf_metadata.get("Subject")
                metadata["creator"] = pdf_metadata.get("Creator")
                
                # Parse creation/modification dates if available
                if "CreationDate" in pdf_metadata:
                    try:
                        metadata["pdf_created_at"] = pdf_metadata["CreationDate"]
                    except:
                        pass
                
                if "ModDate" in pdf_metadata:
                    try:
                        metadata["pdf_modified_at"] = pdf_metadata["ModDate"]
                    except:
                        pass
            
            # Generate tags based on filename and content
            metadata["tags"] = self._generate_tags(file_path)
            
        except Exception as e:
            print(f"Error extracting metadata from {file_path}: {e}")
        
        return metadata
    
    def _generate_document_id(self, file_path: Path) -> str:
        """
        Generate a unique document ID based on file path.
        
        Args:
            file_path: Path to the document
            
        Returns:
            Unique document ID string
        """
        # Use hash of absolute path for consistency
        path_str = str(file_path.resolve())
        hash_obj = hashlib.md5(path_str.encode())
        return f"{self.source_type}_{hash_obj.hexdigest()[:12]}"
    
    def _generate_tags(self, file_path: Path) -> List[str]:
        """
        Generate tags based on file path and name.
        
        Args:
            file_path: Path to the document
            
        Returns:
            List of tag strings
        """
        tags = []
        
        # Add tags based on directory structure
        parts = file_path.parts
        if len(parts) > 1:
            # Use parent directory names as tags
            tags.extend([p.lower() for p in parts[-3:-1] if p.lower() not in ['data', 'sources']])
        
        # Add tag based on filename patterns
        name_lower = file_path.stem.lower()
        if 'guide' in name_lower:
            tags.append('guide')
        if 'api' in name_lower:
            tags.append('api')
        if 'doc' in name_lower or 'documentation' in name_lower:
            tags.append('documentation')
        if 'tutorial' in name_lower:
            tags.append('tutorial')
        if 'reference' in name_lower:
            tags.append('reference')
        
        return list(set(tags))  # Remove duplicates

