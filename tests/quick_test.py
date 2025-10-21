"""
Quick interactive test script for the MCP server.

This script provides an interactive way to test the search functionality.
Just run it and type your queries!

Usage:
    python quick_test.py
"""

import requests
import json
import sys

BASE_URL = "http://127.0.0.1:8000/api/v1"


def test_connection():
    """Test if server is running."""
    try:
        response = requests.get(f"{BASE_URL}/health", timeout=2)
        if response.status_code == 200:
            print("[OK] Server is running!")
            return True
        else:
            print(f"[ERROR] Server returned status {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("[ERROR] Cannot connect to server!")
        print("Make sure the server is running: python main.py")
        return False
    except Exception as e:
        print(f"[ERROR] {e}")
        return False


def get_stats():
    """Get server statistics."""
    try:
        response = requests.get(f"{BASE_URL}/stats")
        stats = response.json()
        
        print("\n" + "=" * 60)
        print("Server Statistics")
        print("=" * 60)
        print(f"Total documents:  {stats.get('total_documents', 0)}")
        
        search_engine = stats.get('search_engine', {})
        vector_store = search_engine.get('vector_store', {})
        keyword = search_engine.get('keyword_searcher', {})
        
        print(f"Total chunks:     {vector_store.get('total_chunks', 0)}")
        print(f"Vector dimension: {vector_store.get('embedding_dim', 0)}")
        print(f"Avg tokens/chunk: {keyword.get('avg_tokens_per_chunk', 0):.1f}")
        print("=" * 60)
        
    except Exception as e:
        print(f"[ERROR] Could not get stats: {e}")


def search(query, top_k=5):
    """Perform a search query."""
    try:
        response = requests.post(
            f"{BASE_URL}/search_docs",
            json={"query": query, "top_k": top_k},
            timeout=30
        )
        
        if response.status_code != 200:
            print(f"[ERROR] Search failed with status {response.status_code}")
            print(response.text)
            return
        
        data = response.json()
        
        print("\n" + "=" * 60)
        print(f"Search Results for: '{query}'")
        print("=" * 60)
        print(f"Found {data['total_results']} results in {data['search_time_ms']:.0f}ms")
        print()
        
        if data['total_results'] == 0:
            print("No results found. Try a different query.")
            return
        
        for i, result in enumerate(data['results'], 1):
            print(f"{i}. {result['title']}")
            print(f"   Score: {result['score']:.3f}")
            print(f"   Type:  {result['source_type']}")
            print(f"   {result['snippet'][:150]}...")
            print(f"   URI:   {result['uri']}")
            print()
        
    except requests.exceptions.Timeout:
        print("[ERROR] Search timed out. Server might be slow or stuck.")
    except Exception as e:
        print(f"[ERROR] Search failed: {e}")


def interactive_mode():
    """Run interactive search mode."""
    print("\n" + "=" * 60)
    print("Interactive Search Mode")
    print("=" * 60)
    print("Type your search queries (or 'quit' to exit)")
    print("Commands:")
    print("  stats  - Show server statistics")
    print("  help   - Show this help")
    print("  quit   - Exit")
    print("=" * 60)
    print()
    
    while True:
        try:
            query = input("Search> ").strip()
            
            if not query:
                continue
            
            if query.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break
            
            if query.lower() == 'stats':
                get_stats()
                continue
            
            if query.lower() == 'help':
                print("\nCommands:")
                print("  stats  - Show server statistics")
                print("  help   - Show this help")
                print("  quit   - Exit")
                print("\nOr just type any search query!")
                continue
            
            search(query)
            
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except EOFError:
            print("\n\nGoodbye!")
            break


def main():
    """Main entry point."""
    print("=" * 60)
    print("MCP Server Quick Test")
    print("=" * 60)
    print()
    
    # Test connection
    if not test_connection():
        sys.exit(1)
    
    # Show stats
    get_stats()
    
    # Run some example searches
    print("\n" + "=" * 60)
    print("Running Example Searches")
    print("=" * 60)
    
    example_queries = [
        "factorio tutorials",
        "power production",
        "transport belt"
    ]
    
    for query in example_queries:
        search(query, top_k=3)
        print()
    
    # Interactive mode
    try:
        choice = input("\nEnter interactive mode? (y/n): ").strip().lower()
        if choice in ['y', 'yes']:
            interactive_mode()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")


if __name__ == "__main__":
    main()


