"""Audit logging for query tracking."""

import json
from datetime import datetime
from pathlib import Path
from typing import List, Optional
from schemas.document import DocumentChunk


class AuditLogger:
    """
    Logs queries and accessed documents for audit trail.
    """
    
    def __init__(self, log_path: Path, enabled: bool = True):
        """
        Initialize the audit logger.
        
        Args:
            log_path: Path to the audit log file
            enabled: Whether audit logging is enabled
        """
        self.log_path = log_path
        self.enabled = enabled
        
        if self.enabled:
            # Ensure log directory exists
            self.log_path.parent.mkdir(parents=True, exist_ok=True)
    
    def log_query(
        self,
        query: str,
        results: List[tuple],  # List of (chunk, score) tuples
        user_id: Optional[str] = None,
        access_level: Optional[str] = None,
        search_time_ms: Optional[float] = None
    ):
        """
        Log a search query and its results.
        
        Args:
            query: The search query
            results: Search results (chunk, score tuples)
            user_id: Optional user identifier
            access_level: Optional access level filter used
            search_time_ms: Time taken for search in milliseconds
        """
        if not self.enabled:
            return
        
        # Build log entry
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "event_type": "search_query",
            "query": query,
            "user_id": user_id or "anonymous",
            "access_level": access_level,
            "result_count": len(results),
            "search_time_ms": search_time_ms,
            "returned_documents": [
                {
                    "document_id": chunk.document_id,
                    "chunk_id": chunk.chunk_id,
                    "uri": chunk.uri,
                    "score": float(score),
                    "source_type": chunk.metadata.get("source_type"),
                }
                for chunk, score in results
            ]
        }
        
        # Write to log file
        self._write_log(log_entry)
    
    def log_document_access(
        self,
        uri: str,
        user_id: Optional[str] = None,
        document_id: Optional[str] = None
    ):
        """
        Log access to a specific document.
        
        Args:
            uri: Document URI
            user_id: Optional user identifier
            document_id: Optional document identifier
        """
        if not self.enabled:
            return
        
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "event_type": "document_access",
            "uri": uri,
            "document_id": document_id,
            "user_id": user_id or "anonymous",
        }
        
        self._write_log(log_entry)
    
    def log_indexing(
        self,
        source_type: str,
        document_count: int,
        chunk_count: int,
        duration_seconds: Optional[float] = None
    ):
        """
        Log document indexing operation.
        
        Args:
            source_type: Type of source indexed
            document_count: Number of documents indexed
            chunk_count: Number of chunks created
            duration_seconds: Time taken for indexing
        """
        if not self.enabled:
            return
        
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "event_type": "indexing",
            "source_type": source_type,
            "document_count": document_count,
            "chunk_count": chunk_count,
            "duration_seconds": duration_seconds,
        }
        
        self._write_log(log_entry)
    
    def _write_log(self, log_entry: dict):
        """
        Write a log entry to the audit log file.
        
        Args:
            log_entry: Dictionary containing log data
        """
        try:
            with open(self.log_path, 'a', encoding='utf-8') as f:
                f.write(json.dumps(log_entry) + '\n')
        except Exception as e:
            print(f"Error writing to audit log: {e}")
    
    def get_recent_logs(self, count: int = 100) -> List[dict]:
        """
        Retrieve recent log entries.
        
        Args:
            count: Number of recent entries to retrieve
            
        Returns:
            List of log entry dictionaries
        """
        if not self.log_path.exists():
            return []
        
        logs = []
        try:
            with open(self.log_path, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip():
                        logs.append(json.loads(line))
        except Exception as e:
            print(f"Error reading audit log: {e}")
        
        # Return most recent entries
        return logs[-count:]

