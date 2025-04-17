# KAELIT JSON-RPC Interface Specification

**Version:** 0.1.0

This document outlines the planned JSON-RPC interface for the KAELIT blockchain system.  
It serves as a high-level preview of the system architecture and intended modularity.  
> **Note:** This is an early specification and subject to change.

---

## Overview

KAELIT exposes a modular JSON-RPC interface to allow interaction with:

- Transaction submission and verification  
- DAG-based ledger state traversal  
- zk-SNARK proof requests  
- AI-based optimization triggers  
- DAO governance functions  
- Modular node communication and state sync

All calls require a valid JWT in the `Authorization` header (see **Authentication** below).

---

## Authentication

All methods must include:

```
Authorization: Bearer <your_jwt_token>
```

Invalid or missing tokens will result in an authentication error.

---

## Sample Method Definitions

### `kaelit_rpc_sendTransaction`

Submits a signed transaction to the KAELIT mempool.

```json
{
  "jsonrpc": "2.0",
  "method": "kaelit_rpc_sendTransaction",
  "params": {
    "from": "0x...",
    "to": "0x...",
    "value": "100000",
    "data": "0x...",
    "signature": "0x..."
  },
  "id": 1,
  "version": "0.1.0"
}
```

#### Success Response
```json
{
  "jsonrpc": "2.0",
  "result": { "txHash": "0xabc123..." },
  "id": 1
}
```

#### Error Response
```json
{
  "jsonrpc": "2.0",
  "error": { "code": -32000, "message": "Invalid signature" },
  "id": 1
}
```

---

### `kaelit_rpc_getDagNode`

Retrieves metadata for a specific DAG node.

```json
{
  "jsonrpc": "2.0",
  "method": "kaelit_rpc_getDagNode",
  "params": { "nodeId": "abcd1234" },
  "id": 2,
  "version": "0.1.0"
}
```

---

### `kaelit_rpc_proveZkRollupBatch`

Initiates ZK proof generation for a batch of transactions.

```json
{
  "jsonrpc": "2.0",
  "method": "kaelit_rpc_proveZkRollupBatch",
  "params": {
    "batchId": "batch_01",
    "transactions": [ ... ]
  },
  "id": 3,
  "version": "0.1.0"
}
```

---

### `kaelit_rpc_triggerAiOptimizer`

Triggers the AI model for gas optimization or batch reordering.

```json
{
  "jsonrpc": "2.0",
  "method": "kaelit_rpc_triggerAiOptimizer",
  "params": {
    "scenario": "gas_predict",
    "data": { ... }
  },
  "id": 4,
  "version": "0.1.0"
}
```

---

### `kaelit_rpc_submitProposal`

Submits a new governance proposal to the DAO.

```json
{
  "jsonrpc": "2.0",
  "method": "kaelit_rpc_submitProposal",
  "params": {
    "proposalId": "prop_2025_001",
    "description": "Increase block size",
    "details": "..."
  },
  "id": 5,
  "version": "0.1.0"
}
```

---

### `kaelit_rpc_vote`

Casts a vote on an existing DAO proposal.

```json
{
  "jsonrpc": "2.0",
  "method": "kaelit_rpc_vote",
  "params": {
    "proposalId": "prop_2025_001",
    "vote": "yes"
  },
  "id": 6,
  "version": "0.1.0"
}
```

---

## Versioning & Deprecation

- Each request includes a `"version"` field.  
- Deprecated methods will be marked `"deprecated": true` in future releases.  
- Change log available at: `https://github.com/kaelitcom/kaelit-interface/releases`

---

## Rate Limits

- **100 requests per minute** per API key  
- Payload size limit: **1 MB**  
- Exceeded limits return error code `-32005` ("Rate limit exceeded")

---

## Security & Best Practices

- All endpoints must use **TLS 1.3** or higher  
- Verify request signatures using **hybrid PQC/ECDSA**  
- Validate all inputs against schema definitions

---

> This specification is an early draft.  
> For integration inquiries or to report issues, please open a GitHub Issue or contact the KAELIT.com
