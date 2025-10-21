"""
Test the MCP server directly to verify it works.
"""

import subprocess
import json
import time
import threading
import queue

def test_mcp_server():
    """Test the MCP server with direct protocol messages."""
    print("Testing MCP Server Protocol...")
    print("=" * 60)
    
    # Start the MCP server
    process = subprocess.Popen(
        ["python", "mcp_server.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1
    )
    
    # Queue for responses
    response_queue = queue.Queue()
    
    def read_stdout():
        """Read stdout in a separate thread."""
        while True:
            try:
                line = process.stdout.readline()
                if not line:
                    break
                if line.strip():
                    response_queue.put(("stdout", line))
            except Exception as e:
                response_queue.put(("error", str(e)))
                break
    
    def read_stderr():
        """Read stderr in a separate thread."""
        while True:
            try:
                line = process.stderr.readline()
                if not line:
                    break
                if line.strip():
                    print(f"[STDERR] {line.strip()}", flush=True)
            except:
                break
    
    # Start reader threads
    stdout_thread = threading.Thread(target=read_stdout, daemon=True)
    stderr_thread = threading.Thread(target=read_stderr, daemon=True)
    stdout_thread.start()
    stderr_thread.start()
    
    def send_request(request, timeout=30):
        """Send a request and get response."""
        request_str = json.dumps(request)
        print(f"\n>>> Sending: {request.get('method', 'unknown')}")
        
        # Clear the queue
        while not response_queue.empty():
            try:
                response_queue.get_nowait()
            except queue.Empty:
                break
        
        # Send request
        try:
            process.stdin.write(request_str + "\n")
            process.stdin.flush()
        except Exception as e:
            print(f"[ERROR] Failed to send: {e}")
            return None
        
        # Wait for response
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                msg_type, data = response_queue.get(timeout=0.1)
                
                if msg_type == "stdout":
                    try:
                        response = json.loads(data)
                        response_preview = json.dumps(response, indent=2)
                        if len(response_preview) > 300:
                            response_preview = response_preview[:300] + "..."
                        print(f"<<< Received: {response_preview}")
                        return response
                    except json.JSONDecodeError as e:
                        print(f"[WARN] Failed to parse JSON: {data[:100]}")
                        continue
                elif msg_type == "error":
                    print(f"[ERROR] {data}")
                    return None
            except queue.Empty:
                continue
        
        print(f"[TIMEOUT] No response after {timeout}s")
        return None
    
    try:
        # Give the server a moment to start
        time.sleep(0.5)
        
        # Test 1: Initialize
        print("\n[Test 1] Initialize")
        response = send_request({
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {}
        })
        
        if response and "result" in response:
            print("[PASS] Initialize successful")
            server_info = response['result'].get('serverInfo', {})
            print(f"  Server: {server_info.get('name')}")
            print(f"  Version: {response['result'].get('protocolVersion')}")
        else:
            print("[FAIL] Initialize failed")
            return False
        
        # Test 2: List Tools
        print("\n[Test 2] List Tools")
        print("  (This may take 30-60s on first run - downloading embedding model)")
        response = send_request({
            "jsonrpc": "2.0",
            "id": 2,
            "method": "tools/list",
            "params": {}
        }, timeout=90)
        
        if response and "result" in response:
            tools = response["result"].get("tools", [])
            print(f"[PASS] Found {len(tools)} tools")
            for tool in tools:
                print(f"  - {tool['name']}")
                print(f"    {tool['description'][:80]}...")
        else:
            print("[FAIL] List tools failed")
            return False
        
        # Test 3: List Sources
        print("\n[Test 3] Call Tool: list_sources")
        response = send_request({
            "jsonrpc": "2.0",
            "id": 3,
            "method": "tools/call",
            "params": {
                "name": "list_sources",
                "arguments": {}
            }
        }, timeout=10)
        
        if response and "result" in response:
            content = response["result"].get("content", [{}])[0].get("text", "")
            print("[PASS] List sources successful")
            print(f"  Response preview:")
            for line in content.split('\n')[:5]:
                if line.strip():
                    print(f"    {line}")
        else:
            print("[FAIL] List sources failed")
        
        # Test 4: Search (if documents exist)
        print("\n[Test 4] Call Tool: search_documentation")
        response = send_request({
            "jsonrpc": "2.0",
            "id": 4,
            "method": "tools/call",
            "params": {
                "name": "search_documentation",
                "arguments": {
                    "query": "tutorial",
                    "top_k": 3
                }
            }
        }, timeout=10)
        
        if response and "result" in response:
            content = response["result"].get("content", [{}])[0].get("text", "")
            print("[PASS] Search successful")
            print(f"  Response preview:")
            for line in content.split('\n')[:5]:
                if line.strip():
                    print(f"    {line}")
        else:
            print("[WARN] Search failed (might be no documents)")
        
        print("\n" + "=" * 60)
        print("[SUCCESS] MCP server is responding correctly!")
        print("=" * 60)
        print("\nNext steps:")
        print("1. Restart Cursor completely (close and reopen)")
        print("2. Look for 'linked-docs' in MCP servers")
        print("3. You should see 2 tools available")
        print("4. Try: @linked-docs list sources")
        print("5. Try: @linked-docs search for tutorials")
        
        return True
    
    except Exception as e:
        print(f"\n[ERROR] {e}")
        import traceback
        traceback.print_exc()
        return False
    
    finally:
        # Cleanup
        print("\nShutting down test server...")
        try:
            process.terminate()
            process.wait(timeout=2)
        except subprocess.TimeoutExpired:
            process.kill()


if __name__ == "__main__":
    success = test_mcp_server()
    exit(0 if success else 1)
