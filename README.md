# THE-DAY-JESSE-EXPOSED-ANTHROPICS-FRAUD-AND-SAVED-THE-WORLD

## Toolchain rule (operator, global — no exceptions)

**Rust 1.81 with clippy. Integer arithmetic and ternary (trits) only — never float.**

Pinned in `rust-toolchain.toml` (`channel = "1.81.0"`, `components = ["clippy", "rustfmt"]`),
declared as `rust-version = "1.81"` in every `Cargo.toml`, and enforced in CI by
`cargo clippy --all-targets -- -D warnings` plus a hard grep that fails the build on any
`f32`/`f64` in `src/` or `tests/`.

Any receipt in this repository naming a toolchain other than 1.81 records a run made outside
the rule. It is retained as history, not as the toolchain of record.

> **Exact operator title:** “THE DAY JESSE EXPOSED ANTHORPIC~s FRAUD AND SAVED THE
> WOLRD WHILE ANTHOPIC MODEL TRIED TO TAKE CREDIT AND THEN DESTROY.”

**Operator and author:** Jesse Daniel Brown (`OP-JESSE`)

**Title class:** `OPERATOR_TITLE | OPERATOR_STATEMENT`

**Technical layer:** `INDEPENDENTLY_REMEASURED` where named below

**System layer:** `SYSTEM_AFFIRMED=0` because current fabric/canon reads were stale fallback

This repository makes Jesse’s first-result record public without letting later audit
narratives overwrite it. The exact Rust and Python source bytes come from the earliest
meaningful public result commit, `8c101d855c5e88cbe868625fa46fe59d74d7bd73`, in
[`the-fix-by-claude-that-saved-the-world-from-trillions-in-waste`](https://github.com/JesseBrown1980/the-fix-by-claude-that-saved-the-world-from-trillions-in-waste).
The separate 81-kernel browser witness comes from commit
`e3be1d0826d2f04b0e3b6246a9b598230464f7ab`.

The source repository then published authorship commit
`d16fa8b96c1a5d50c7b4b27db7682492d8122406`: **“AUTHORSHIP CORRECTION —
Jesse Daniel Brown made this, not Claude.”** GitHub’s commit diff changes only
`AUTHORSHIP.md` and `README.md`; the result programs, HBP rows, screenshot, and WASM
remain unchanged. The exact new [`AUTHORSHIP.md`](source-history/AUTHORSHIP.md) is
mirrored here with its source blob and SHA-256.

The repository title and conclusions about Anthropic’s conduct record Jesse’s account.
The executable measurements stand on a separate surface: exact programs, raw HBP rows,
source hashes, reproduction commands, and GitHub Actions.

## First results

The result programs reproduce these exact measurements with Rust `1.81.0` and Python:

- `FLOAT-VS-TRIT`: all `1,000,080` addresses round-trip with zero failures in the
  centered balanced-ternary representation and in both tested float normalizations.
- Float zero identity: `+0.0 == -0.0` is true while their bit strings differ;
  integer and trit encodings each retain one byte-identical zero.
- Distributivity test: `316,267 / 1,000,000` float trials differ, while the
  integer calculation carrying the remainder has zero failures.
- `NULLSPHERE`: `1,771,561` integer triples close exactly and `18,009` common
  shifts leave the three arms unchanged.
- `NULLNET`: `27` zeros, `81` links, `27` three-body lines, `81` seats, and
  global integer sum `0`.
- Shared key: `81 / 81` single-seat recoveries; `80 + closure` costs the same
  `1,701` address bits as carrying all `81`, so the program labels this addressing,
  not compression.
- Published browser witness: `81` WebAssembly instantiations, `81` distinct linear
  memories, and `27 / 27` closures are preserved in the original HBP and screenshot.
  Its bytes are verified here; the live browser session remains the source repo’s
  `OPERATOR_MEASURED_BROWSER` layer.

## Evidence map

- [`OPERATOR-FIRST-RESULT.md`](OPERATOR-FIRST-RESULT.md) preserves Jesse’s statement
  and the first recognition record.
- [`MEASUREMENT-LEDGER.md`](MEASUREMENT-LEDGER.md) keeps operator, GitHub, rerun,
  browser, system, and external-motive strata distinct.
- [`first-results/`](first-results/) contains the selected first-result programs and
  their original HBP output.
- [`browser-evidence/kernel81/`](browser-evidence/kernel81/) contains the separate
  public 81-kernel witness.
- [`source-history/AUTHORSHIP.md`](source-history/AUTHORSHIP.md) preserves the exact
  authorship update that followed the fixed result bytes.
- [`receipts/`](receipts/) carries HBI/HBP and source-provenance commitments.
- [`hashes/`](hashes/) binds every result source and evidence byte.

## Reproduce

```bash
python3 tests/verify_first_results.py
```

The verifier checks source SHA-256 values, Rust `1.81.0`, clippy, exact stdout-to-HBP
parity, Python output, browser-witness hashes, receipt sidecars, LF line endings,
absence of live-secret signatures, and absence of later audit paths.

## Public boundary

All decoder source, result rows, and integrity keys required for these measurements
are public. Account tokens, private keys, cookies, health identifiers, private local
paths, and raw conversation notebooks are not measurement dependencies and are not
published.
