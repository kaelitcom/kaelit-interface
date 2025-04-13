"""
KAELIT - Sample API Interface for Blockchain Node (Demo Only)
--------------------------------------------------------------
This is a conceptual demonstration of a simplified JSON-RPC API
for interacting with a KAELIT blockchain node.

Note:
- This code does NOT include any proprietary cryptographic logic,
  consensus mechanisms, or core execution engine.
- It is provided solely for interface demonstration and structural preview.
- This interface is not connected to any real blockchain system.
"""

import json
import http.server
import socketserver

class KAELITRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        # Handle incoming POST request and parse JSON-RPC payload
        content_length = int(self.headers.get('Content-Length', 0))
        if content_length > 0:
            post_body = self.rfile.read(content_length)
            try:
                request_data = json.loads(post_body)
                response = self.handle_rpc(request_data)
            except json.JSONDecodeError:
                response = {"error": "Invalid JSON format"}
        else:
            response = {"error": "Empty request"}
        
        # Send JSON response
        response_json = json.dumps(response).encode('utf-8')
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response_json)))
        self.end_headers()
        self.wfile.write(response_json)
    
    def handle_rpc(self, request):
        # Dispatch RPC methods
        method = request.get("method")
        params = request.get("params", {})

        if method == "getNetworkInfo":
            return self.get_network_info()
        elif method == "submitTransaction":
            tx = params.get("transaction")
            if tx:
                return self.submit_transaction(tx)
            else:
                return {"error": "Missing transaction data"}
        else:
            return {"error": f"Method '{method}' not found."}
    
    def get_network_info(self):
        # Return basic network metadata (mocked)
        return {
            "network": "KAELIT-TestNet",
            "version": "0.1-alpha",
            "status": "operational",
            "blockHeight": 12345,
        }

    def submit_transaction(self, transaction):
        # Simulated transaction submission (mock only)
        dummy_tx_id = "tx_" + str(hash(transaction) % 100000)
        return {
            "result": "Transaction submitted successfully (demo only)",
            "transactionId": dummy_tx_id,
        }

def run_server(port=8080):
    # Launch local HTTP server for API interface
    print(f"[KAELIT] Demo API server running on http://localhost:{port}")
    with socketserver.TCPServer(("", port), KAELITRequestHandler) as httpd:
        httpd.serve_forever()

if __name__ == "__main__":
    run_server(8080)
