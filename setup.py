"""
Setup script for the Linked Documentation MCP Server.

This script helps with initial setup and verification.
"""

import sys
from pathlib import Path


def check_python_version():
    """Check if Python version is 3.10+."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 10):
        print(f"[FAIL] Python 3.10+ required. Current version: {version.major}.{version.minor}")
        return False
    print(f"[OK] Python version: {version.major}.{version.minor}.{version.micro}")
    return True


def check_dependencies():
    """Check if key dependencies are installed."""
    # Map of package names to their import names
    required_packages = {
        "fastapi": "fastapi",
        "uvicorn": "uvicorn",
        "pydantic": "pydantic",
        "faiss-cpu": "faiss",
        "sentence-transformers": "sentence_transformers",
        "rank-bm25": "rank_bm25",
        "pdfplumber": "pdfplumber",
        "beautifulsoup4": "bs4",
        "python-dotenv": "dotenv",
    }
    
    missing = []
    for package_name, import_name in required_packages.items():
        try:
            __import__(import_name)
            print(f"[OK] {package_name} installed")
        except ImportError:
            print(f"[FAIL] {package_name} not installed")
            missing.append(package_name)
    
    if missing:
        print(f"\nMissing packages: {', '.join(missing)}")
        print("Install with: pip install -r requirements.txt")
        return False
    return True


def setup_directories():
    """Create necessary directories."""
    directories = [
        "data",
        "data/sources",
        "data/vector_store",
    ]
    
    for dir_path in directories:
        path = Path(dir_path)
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
            print(f"[OK] Created directory: {dir_path}")
        else:
            print(f"[OK] Directory exists: {dir_path}")
    
    return True


def check_env_file():
    """Check if .env file exists."""
    env_path = Path(".env")
    if not env_path.exists():
        print("[WARN] .env file not found")
        print("Creating default .env file...")
        
        # Default configuration
        default_env = """# Linked Documentation MCP Server Configuration

# Server Settings
HOST=127.0.0.1
PORT=8000
DEBUG=true

# Embedding Model
EMBEDDING_MODEL=all-MiniLM-L6-v2
EMBEDDING_DEVICE=cpu

# Vector Store
VECTOR_STORE_TYPE=faiss
VECTOR_STORE_PATH=./data/vector_store

# Metadata Database
METADATA_DB_PATH=./data/metadata.json

# Search Settings
TOP_K_RESULTS=10
SEMANTIC_WEIGHT=0.7
KEYWORD_WEIGHT=0.3

# Chunking
CHUNK_SIZE=512
CHUNK_OVERLAP=50

# Audit Logging
AUDIT_LOG_PATH=./data/audit.log
ENABLE_AUDIT_LOGGING=true

# Data Directory
DATA_DIR=./data
"""
        try:
            with open(env_path, 'w') as f:
                f.write(default_env)
            print("[OK] Created .env file with default configuration")
        except Exception as e:
            print(f"[FAIL] Error creating .env file: {e}")
            return False
    else:
        print("[OK] .env file exists")
    
    return True


def main():
    """Run setup checks."""
    print("=" * 60)
    print("Linked Documentation MCP Server - Setup")
    print("=" * 60)
    print()
    
    checks = [
        ("Python Version", check_python_version),
        ("Dependencies", check_dependencies),
        ("Directories", setup_directories),
        ("Environment File", check_env_file),
    ]
    
    results = []
    for name, check_func in checks:
        print(f"\n[{name}]")
        try:
            success = check_func()
            results.append((name, success))
        except Exception as e:
            print(f"[ERROR] Error: {e}")
            results.append((name, False))
    
    # Summary
    print("\n" + "=" * 60)
    print("Setup Summary")
    print("=" * 60)
    
    all_passed = True
    for name, success in results:
        status = "[PASS]" if success else "[FAIL]"
        print(f"{status}: {name}")
        if not success:
            all_passed = False
    
    if all_passed:
        print("\n[SUCCESS] All checks passed! You can now run the server with:")
        print("   python main.py")
    else:
        print("\n[ERROR] Some checks failed. Please fix the issues above.")
        print("   Install dependencies: pip install -r requirements.txt")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()

