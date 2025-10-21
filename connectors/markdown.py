"""Markdown document connector."""

import hashlib
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any
import re

from schemas.document import Document, DocumentMetadata, AccessLevel
from .base import BaseConnector


class MarkdownConnector(BaseConnector):
    """Connector for loading Markdown documents."""
    
    def _get_source_type(self) -> str:
        """Return the source type identifier."""
        return "markdown"
    
    def load_documents(self, source_path: Path) -> List[Document]:
        """
        Load Markdown documents from the specified path.
        
        Args:
            source_path: Path to a Markdown file or directory containing Markdown files
            
        Returns:
            List of Document objects
        """
        documents = []
        
        if source_path.is_file() and source_path.suffix.lower() in ['.md', '.markdown']:
            doc = self._load_single_markdown(source_path)
            if doc:
                documents.append(doc)
        elif source_path.is_dir():
            for md_file in source_path.rglob("*.md"):
                doc = self._load_single_markdown(md_file)
                if doc:
                    documents.append(doc)
            for md_file in source_path.rglob("*.markdown"):
                doc = self._load_single_markdown(md_file)
                if doc:
                    documents.append(doc)
        
        return documents
    
    def _load_single_markdown(self, file_path: Path) -> Document:
        """
        Load a single Markdown file.
        
        Args:
            file_path: Path to the Markdown file
            
        Returns:
            Document object or None if loading fails
        """
        try:
            # Read the markdown content
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Generate document ID
            doc_id = self._generate_document_id(file_path)
            
            # Get metadata
            metadata = self.get_metadata(file_path)
            
            # Extract front matter if present
            front_matter = self._extract_front_matter(content)
            if front_matter:
                metadata.update(front_matter)
                # Remove front matter from content
                content = self._remove_front_matter(content)
            
            # Extract title from content if not in metadata
            if "title" not in metadata:
                metadata["title"] = self._extract_title(content) or file_path.stem
            
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
                    "heading_count": self._count_headings(content),
                    "code_blocks": self._count_code_blocks(content),
                }
            )
            
            document = Document(
                document_id=doc_id,
                content=content,
                metadata=doc_metadata,
                chunks=[]
            )
            
            return document
            
        except Exception as e:
            print(f"Error loading Markdown file {file_path}: {e}")
            return None
    
    def get_metadata(self, file_path: Path) -> Dict[str, Any]:
        """
        Extract metadata from a Markdown file.
        
        Args:
            file_path: Path to the Markdown file
            
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
            
            # Generate tags based on filename and content
            metadata["tags"] = self._generate_tags(file_path)
            
        except Exception as e:
            print(f"Error extracting metadata from {file_path}: {e}")
        
        return metadata
    
    def _extract_front_matter(self, content: str) -> Dict[str, Any]:
        """
        Extract YAML front matter from markdown content.
        
        Args:
            content: Markdown content
            
        Returns:
            Dictionary of front matter fields
        """
        front_matter = {}
        
        # Check for YAML front matter (---\n...\n---)
        match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if match:
            yaml_content = match.group(1)
            # Simple parsing (not full YAML parser)
            for line in yaml_content.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    key = key.strip()
                    value = value.strip()
                    
                    # Handle lists
                    if value.startswith('[') and value.endswith(']'):
                        value = [v.strip().strip('"\'') for v in value[1:-1].split(',')]
                    # Remove quotes
                    elif value.startswith('"') and value.endswith('"'):
                        value = value[1:-1]
                    elif value.startswith("'") and value.endswith("'"):
                        value = value[1:-1]
                    
                    front_matter[key] = value
        
        return front_matter
    
    def _remove_front_matter(self, content: str) -> str:
        """Remove YAML front matter from content."""
        return re.sub(r'^---\s*\n.*?\n---\s*\n', '', content, flags=re.DOTALL)
    
    def _extract_title(self, content: str) -> str:
        """
        Extract the first heading as title.
        
        Args:
            content: Markdown content
            
        Returns:
            Title string or empty string
        """
        # Look for first # heading
        match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if match:
            return match.group(1).strip()
        return ""
    
    def _count_headings(self, content: str) -> int:
        """Count the number of headings in the content."""
        return len(re.findall(r'^#+\s+', content, re.MULTILINE))
    
    def _count_code_blocks(self, content: str) -> int:
        """Count the number of code blocks in the content."""
        return len(re.findall(r'```', content)) // 2
    
    def _generate_document_id(self, file_path: Path) -> str:
        """
        Generate a unique document ID based on file path.
        
        Args:
            file_path: Path to the document
            
        Returns:
            Unique document ID string
        """
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
            tags.extend([p.lower() for p in parts[-3:-1] if p.lower() not in ['data', 'sources']])
        
        # Add tag based on filename patterns
        name_lower = file_path.stem.lower()
        if 'readme' in name_lower:
            tags.append('readme')
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
        
        return list(set(tags))

