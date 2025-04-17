"""
KAELIT RPC Interface Demo (v0.1.0)

This file is a conceptual demo of KAELIT's planned JSON-RPC interface.
It is NOT connected to any real blockchain logic, consensus engine, cryptographic validation, or signature layer.

For full interface specification, see: interface.md
For changelog, see: CHANGELOG.md
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/rpc', methods=['POST'])
def rpc_endpoint():
    content_length = request.content_length
    if content_length > 0:
        data = request.get_json(force=True)
        method = data.get("method")
        request_id = data.get("id")

        if method == "kaelit_rpc_getNetworkInfo":
            return jsonify({
                "jsonrpc": "2.0",
                "result": {
                    "network": "KAELIT-DevNet",
                    "version": "0.1.0"
                },
                "id": request_id
            })

        elif method == "kaelit_rpc_submitTransaction":
            return jsonify({
                "jsonrpc": "2.0",
                "result": {
                    "txHash": "0xDEMO1234567890"
                },
                "id": request_id
            })

        else:
            return jsonify({
                "jsonrpc": "2.0",
                "error": {
                    "code": -32601,
                    "message": "Method not found"
                },
                "id": request_id
            })
    else:
        return jsonify({
            "jsonrpc": "2.0",
            "error": {
                "code": -32700,
                "message": "Empty request body"
            },
            "id": None
        })

if __name__ == '__main__':
    app.run(debug=True, port=8545)
