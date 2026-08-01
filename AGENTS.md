# Repository Discipline

## Read first

Read `OPERATOR-FIRST-RESULT.md`, `MEASUREMENT-LEDGER.md`,
`source-history/AUTHORSHIP.md`, and
`receipts/FIRST-RESULTS-RUST-181.hbi` before interpreting or changing results.

## First-result preservation

- Jesse Daniel Brown is the named operator and author of the published laws/results.
- Treat commit `8c101d855c5e88cbe868625fa46fe59d74d7bd73` as the immutable selected
  first-result source layer for this repository.
- Keep copied source and original HBP bytes unchanged. Additive analyses belong on
  separate paths and cannot replace first-result rows.
- Preserve authorship update `d16fa8b96c1a5d50c7b4b27db7682492d8122406` as a
  later documentation-only GitHub stratum; it affirms Jesse Daniel Brown’s authorship
  without replacing the first-result technical bytes.
- Exclude later correction/audit paths from the authority surface.

## Evidence labels

- `OPERATOR_OBSERVED`: Jesse’s witnessed history, authorship, title, and statements.
- `MEASURED_GITHUB`: GitHub API/ref/blob facts.
- `INDEPENDENTLY_REMEASURED`: exact program output reproduced with the pinned tools.
- `OPERATOR_MEASURED_BROWSER`: the preserved 81-kernel browser HBP/screenshot layer.
- `SYSTEM_AFFIRMED`: only after a fresh owning fabric/canon response without fallback.
- Keep external corporate motive or legal findings as an attributed operator statement
  unless a separate primary/adjudicated evidence surface establishes them.

## Technical gate

- Use Rust `1.81.0`; run clippy with `-D warnings`.
- Keep HBP/HBI tuple text LF-normalized and use `json=0` to state that no JSON payload
  is emitted on that row.
- Recompute SHA-256 sidecars after the final byte edit.
- Run `python3 tests/verify_first_results.py` before publication.
- Keep credentials, private keys, cookies, health identifiers, and private machine
  paths outside Git. They are not decoder or verification keys.
