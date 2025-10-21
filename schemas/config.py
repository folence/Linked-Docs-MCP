"""Configuration settings for the MCP server."""

from pydantic_settings import BaseSettings
from pathlib import Path

# Get the project root directory (parent of schemas dir) - resolve to absolute path
PROJECT_ROOT = Path(__file__).parent.parent.resolve()

class Settings(BaseSettings):
    """Application configuration settings loaded from environment variables."""

    # Server Settings
    host: str = "127.0.0.1"
    port: int = 8000
    debug: bool = True

    # Embedding Model
    embedding_model: str = "all-MiniLM-L6-v2"
    embedding_device: str = "cpu"

    # Vector Store
    vector_store_type: str = "faiss"
    vector_store_path: Path = Path("./data/vector_store")

    # Metadata Database
    metadata_db_path: Path = Path("./data/metadata.json")

    # Search Settings
    top_k_results: int = 10
    semantic_weight: float = 0.7
    keyword_weight: float = 0.3

    # Chunking
    chunk_size: int = 1280  # Balanced size for context + coverage
    chunk_overlap: int = 128  # 10% overlap for continuity across chunks

    # Audit Logging
    audit_log_path: Path = Path("./data/audit.log")
    enable_audit_logging: bool = True

    # Data Directory
    data_dir: Path = Path("./data")

    class Config:
        env_file = ".env"
        case_sensitive = False
    
    def __init__(self, **data):
        """Initialize and resolve all paths to absolute."""
        super().__init__(**data)
        # Resolve all paths to absolute
        self.data_dir = (PROJECT_ROOT / self.data_dir).resolve()
        self.vector_store_path = (PROJECT_ROOT / self.vector_store_path).resolve()
        self.metadata_db_path = (PROJECT_ROOT / self.metadata_db_path).resolve()
        self.audit_log_path = (PROJECT_ROOT / self.audit_log_path).resolve()


# Global settings instance
settings = Settings()

