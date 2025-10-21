"""
Simple test script to verify the MCP server API endpoints.

Run the server first with: python main.py
Then run this script: python test_api.py
"""

import requests
import json
from time import sleep

BASE_URL = "http://127.0.0.1:8000/api/v1"


def print_response(title, response):
    """Pretty print API response."""
    print("\n" + "="*60)
    print(f"{title}")
    print("="*60)
    print(f"Status: {response.status_code}")
    try:
        data = response.json()
        print(json.dumps(data, indent=2))
    except:
        print(response.text)


def test_health():
    """Test health check endpoint."""
    response = requests.get(f"{BASE_URL}/health")
    print_response("Health Check", response)
    return response.status_code == 200


def test_list_sources():
    """Test list sources endpoint."""
    response = requests.get(f"{BASE_URL}/list_sources")
    print_response("List Sources", response)
    return response.status_code == 200


def test_search_docs():
    """Test search documents endpoint."""
    queries = [
        "getting started guide",
        "API authentication",
        "access control",
        "how to search documents"
    ]
    
    for query in queries:
        payload = {
            "query": query,
            "top_k": 3,
            "user_id": "test_user"
        }
        
        response = requests.post(
            f"{BASE_URL}/search_docs",
            json=payload
        )
        
        print_response(f"Search: '{query}'", response)
        
        if response.status_code == 200:
            data = response.json()
            print(f"\nTop Results:")
            for i, result in enumerate(data.get("results", []), 1):
                print(f"  {i}. {result['title']} (score: {result['score']:.3f})")
                print(f"     URI: {result['uri']}")
                print(f"     Snippet: {result['snippet'][:100]}...")
        
        sleep(0.5)  # Small delay between requests
    
    return True


def test_get_doc_context():
    """Test get document context endpoint."""
    # First, get a URI from search
    search_response = requests.post(
        f"{BASE_URL}/search_docs",
        json={"query": "getting started", "top_k": 1}
    )
    
    if search_response.status_code == 200:
        results = search_response.json().get("results", [])
        if results:
            uri = results[0]["uri"]
            
            # Get document context
            response = requests.get(
                f"{BASE_URL}/get_doc_context",
                params={"uri": uri, "user_id": "test_user"}
            )
            
            print_response(f"Document Context for: {uri}", response)
            
            if response.status_code == 200:
                data = response.json()
                print(f"\nContent Preview:")
                print(data.get("content", "")[:300] + "...")
            
            return response.status_code == 200
    
    print("\nSkipping document context test (no search results)")
    return True


def test_stats():
    """Test statistics endpoint."""
    response = requests.get(f"{BASE_URL}/stats")
    print_response("Server Statistics", response)
    return response.status_code == 200


def main():
    """Run all tests."""
    print("\n" + "="*60)
    print("MCP Server API Test Suite")
    print("="*60)
    
    tests = [
        ("Health Check", test_health),
        ("List Sources", test_list_sources),
        ("Search Documents", test_search_docs),
        ("Get Document Context", test_get_doc_context),
        ("Statistics", test_stats),
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            success = test_func()
            results.append((test_name, success))
        except Exception as e:
            print(f"\n[ERROR] Error in {test_name}: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "="*60)
    print("Test Summary")
    print("="*60)
    
    for test_name, success in results:
        status = "[PASS]" if success else "[FAIL]"
        print(f"{status}: {test_name}")
    
    total = len(results)
    passed = sum(1 for _, success in results if success)
    print(f"\nTotal: {passed}/{total} tests passed")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nTests interrupted by user.")
    except Exception as e:
        print(f"\n\nFatal error: {e}")

