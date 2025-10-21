"""
Clear the vector store index to start fresh.

Use this if you have duplicate entries or want to completely rebuild the index.

Usage:
    python clear_index.py
"""

import shutil
from pathlib import Path

def main():
    """Clear the vector store and start fresh."""
    vector_store_path = Path("data/vector_store")
    
    if not vector_store_path.exists():
        print("No vector store found. Nothing to clear.")
        return
    
    print("=" * 60)
    print("Clear Vector Store Index")
    print("=" * 60)
    print()
    print(f"This will delete all indexed data in: {vector_store_path}")
    print("Your source documents will NOT be deleted.")
    print()
    
    response = input("Are you sure you want to clear the index? (yes/no): ").strip().lower()
    
    if response not in ['yes', 'y']:
        print("Cancelled. Index was not cleared.")
        return
    
    print()
    print("Clearing vector store...")
    
    try:
        # Remove the vector store directory
        shutil.rmtree(vector_store_path)
        print(f"✓ Removed {vector_store_path}")
        
        # Recreate empty directory
        vector_store_path.mkdir(parents=True, exist_ok=True)
        print(f"✓ Created empty {vector_store_path}")
        
        print()
        print("=" * 60)
        print("Index cleared successfully!")
        print("=" * 60)
        print()
        print("Next steps:")
        print("1. Restart the server to rebuild the index:")
        print("   python main.py")
        print("   OR")
        print("   python mcp_server.py")
        print()
        print("The server will automatically re-index all documents in data/sources/")
        print("=" * 60)
        
    except Exception as e:
        print(f"Error clearing index: {e}")
        return 1

if __name__ == "__main__":
    main()

