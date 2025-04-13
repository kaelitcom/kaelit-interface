"""
KAELIT Project - Interface Layer (Demo Only)
---------------------------------------------
This is a simplified demo of the KAELIT JSON-RPC interface.
It does NOT include any core blockchain logic, consensus, or cryptographic implementation.

IPFS Hash: QmXXXX... (KAELIT official publication proof)
For full technical collaboration: https://kaelit.com/partnership
"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class KAELITRequestHandler(BaseHTTPRequestHandler):
    def _set_response(self, content):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        if content_length == 0:
            self._set_response(json.dumps({"error": "Empty request"}).encode())
            return

        try:
            request = json.loads(self.rfile.read(content_length))
            response = self.handle_rpc(request)
        except Exception:
            response = {"error": "Invalid JSON format"}

        self._set_response(json.dumps(response).encode())

    def handle_rpc(self, request):
        method = request.get("method")
        params = request.get("params", {})

        if method == "getNetworkInfo":
            return self.get_network_info()
        elif method == "submitTransaction":
            return self.submit_transaction(params.get("transaction"))
        else:
            return {"error": f"Unknown method: {method}"}

    def get_network_info(self):
        return {
            "network": "KAELIT-TestNet",
            "version": "0.1-demo",
            "status": "operational",
            "latestBlock": 12345
        }

    def submit_transaction(self, tx):
        if not tx:
            return {"error": "Transaction data missing"}
        tx_id = f"tx_{abs(hash(json.dumps(tx))) % 100000}"
        return {
            "result": "Transaction accepted (mock)",
            "transactionId": tx_id
        }

def run_server(port=8080):
    print(f"[KAELIT Demo API] Running on http://localhost:{port}")
    server = HTTPServer(('', port), KAELITRequestHandler)
    server.serve_forever()

if __name__ == "__main__":
    run_server()
