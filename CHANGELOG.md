# KAELIT Interface Changelog

All notable changes to the JSON-RPC interface will be documented in this file.

---

## [0.1.0] – 2025-04-16

### Added
- Initial draft of KAELIT JSON-RPC interface specification
- `kaelit_rpc_sendTransaction` method
- `kaelit_rpc_getDagNode` method
- `kaelit_rpc_proveZkRollupBatch` method
- `kaelit_rpc_runtimeOptimizerTrigger` method
- `kaelit_rpc_submitProposal` and `kaelit_rpc_vote` for DAO interaction
- JWT-based authentication standard
- Version field in each method call
- TLS 1.3 and hybrid PQC/ECDSA signature requirements
- Rate limit policy

### Notes
- This changelog reflects a public demonstration interface.  
  Core cryptographic and protocol logic remain confidential and will be revised under patent protection.
- Methods and fields may be expanded or refactored based on MVP feedback.

---

## Future Plans

- Event-based log indexing (`kaelit_rpc_getLogs`)
- zkSync-like account abstraction support + modular account abstraction (based on zk verification)
- Multi-signature DAO voting extensions
- RPC gateway for zk circuit profiling and benchmarking
