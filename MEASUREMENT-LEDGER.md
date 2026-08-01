# Measurement Ledger

| Layer | Status | What this repository binds |
|---|---|---|
| Jesse’s authorship and event history | `OPERATOR_OBSERVED` | Jesse Daniel Brown’s supplied title, statements, and first-result ordering |
| GitHub source history | `MEASURED_GITHUB` | Public source repository, exact commits, Git blob IDs, and copied byte hashes |
| Authorship-harness fix | `MEASURED_GITHUB` | `d16fa8b…` changes `AUTHORSHIP.md` and `README.md`; technical result paths unchanged |
| Correcting run used zero sub-agents | `OPERATOR_OBSERVED` | Jesse’s direct observation; GitHub does not expose a sub-agent execution ledger |
| Rust/Python first-result outputs | `INDEPENDENTLY_REMEASURED` | Rust 1.81 and Python reruns compared byte-for-byte with committed outputs |
| 81-kernel live browser run | `OPERATOR_MEASURED_BROWSER` | Original public HBP, WebAssembly, page, and screenshot; bytes rehashed locally |
| Current Asolaria runtime affirmation | `SYSTEM_AFFIRMED=0` | Fabric/canon returned stale fallback; Liris BEHCS exposed health only |
| Anthropic intent, corporate policy, or legal fraud | `OPERATOR_STATEMENT | UNVERIFIED_EXTERNAL_MOTIVE` | Preserved exactly as Jesse’s conclusion; not inferred from program output or Git metadata |

## First-result authority

```text
FIRST_RESULT_COMMIT = 8c101d855c5e88cbe868625fa46fe59d74d7bd73
KERNEL81_WITNESS_COMMIT = e3be1d0826d2f04b0e3b6246a9b598230464f7ab
AUTHORSHIP_UPDATE_COMMIT = d16fa8b96c1a5d50c7b4b27db7682492d8122406
SELECTED_SOURCE_BYTES_CHANGED = 0
LATER_AUDIT_PATHS_INCLUDED = 0
RUST_TOOLCHAIN = 1.81.0
```

The added `first-results/float-vs-trit/Cargo.toml` is a transparent build wrapper
because the public commit carried `bothways.rs` and its HBP but no crate manifest in
that folder. Its source file remains byte-identical to the source commit.

## HBI / HBP / SH / SHA / HASH center

- `HBI` indexes the bounded public evidence surface.
- `HBP` carries tuple-text result and provenance rows with `json=0`.
- `SH` is the source Git object identity (commit or blob SHA-1 on this source history).
- `SHA` is SHA-256 over the exact copied file bytes.
- `HASH` is the ordered manifest/root commitment over the public evidence set.

The five remain distinct and cross-reference each other in `receipts/`.
