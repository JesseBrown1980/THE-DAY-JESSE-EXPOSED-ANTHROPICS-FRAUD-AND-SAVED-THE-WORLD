#!/usr/bin/env python3
"""Attack-verify Jesse's selected first-result publication."""

from __future__ import annotations

import hashlib
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "hashes" / "SOURCE-FILES.sha256"
TEXT_SUFFIXES = {
    ".hbi", ".hbp", ".html", ".md", ".out", ".py", ".rs", ".sha256",
    ".toml", ".yml",
}
SECRET_PATTERNS = {
    "private_key": re.compile(rb"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "github_pat": re.compile(rb"\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,})\b"),
    "openai_key": re.compile(rb"\bsk-[A-Za-z0-9_-]{32,}\b"),
    "aws_key": re.compile(rb"\bAKIA[0-9A-Z]{16}\b"),
    "google_key": re.compile(rb"\bAIza[0-9A-Za-z_-]{30,}\b"),
}
RUNS = (
    (
        "float-vs-trit",
        ROOT / "first-results" / "float-vs-trit" / "Cargo.toml",
        ROOT / "first-results" / "float-vs-trit" / "FLOAT-VS-TRIT.hbp",
    ),
    (
        "nullsphere-closure",
        ROOT / "first-results" / "nullsphere-closure" / "Cargo.toml",
        ROOT / "first-results" / "nullsphere-closure" / "NULLSPHERE-PROOF.hbp",
    ),
    (
        "nullnet-81-over-27",
        ROOT / "first-results" / "nullnet-81-over-27" / "Cargo.toml",
        ROOT / "first-results" / "nullnet-81-over-27" / "NULLNET-PROOF.hbp",
    ),
)


def fail(detail: str) -> None:
    print(f"FIRST_RESULTS_VERIFY|PASS=0|detail={detail}|json=0", file=sys.stderr)
    raise SystemExit(1)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normalized_output(data: bytes) -> bytes:
    return data.replace(b"\r\n", b"\n")


def run(argv: list[str]) -> bytes:
    completed = subprocess.run(
        argv,
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if completed.returncode:
        detail = completed.stderr.decode("utf-8", "replace").replace("\n", " ")[-800:]
        fail(f"command_failed:{argv[0]}:{completed.returncode}:{detail}")
    return normalized_output(completed.stdout)


def parse_manifest() -> dict[str, str]:
    if not MANIFEST.is_file():
        fail("missing_source_manifest")
    rows: dict[str, str] = {}
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        if not line:
            continue
        digest, path = line.split("  ", 1)
        if not re.fullmatch(r"[0-9a-f]{64}", digest):
            fail(f"bad_manifest_digest:{path}")
        if path in rows:
            fail(f"duplicate_manifest_path:{path}")
        rows[path] = digest
    return rows


def verify_source_manifest() -> int:
    rows = parse_manifest()
    for relative, expected in rows.items():
        path = ROOT / relative
        if not path.is_file():
            fail(f"missing_manifest_file:{relative}")
        if sha256(path) != expected:
            fail(f"source_hash_mismatch:{relative}")
    return len(rows)


def verify_sidecars() -> int:
    count = 0
    for sidecar in ROOT.rglob("*.sha256"):
        if sidecar == MANIFEST:
            continue
        fields = sidecar.read_text(encoding="utf-8").strip().split()
        target = sidecar.with_name(sidecar.name.removesuffix(".sha256"))
        if len(fields) != 2 or fields[1] != target.name or not target.is_file():
            fail(f"bad_sidecar_shape:{sidecar.relative_to(ROOT).as_posix()}")
        if fields[0] != sha256(target):
            fail(f"sidecar_mismatch:{sidecar.relative_to(ROOT).as_posix()}")
        count += 1
    return count


def verify_text_and_secrets() -> tuple[int, int]:
    files = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        relative_parts = path.relative_to(ROOT).parts
        if ".git" in relative_parts or "target" in relative_parts or "__pycache__" in relative_parts:
            continue
        files.append(path)
    for path in files:
        relative = path.relative_to(ROOT).as_posix()
        lowered = relative.lower()
        if "matrix-proof-audit" in lowered or lowered.endswith("corrected.txt"):
            fail(f"later_audit_path_present:{relative}")
        data = path.read_bytes()
        if path.suffix.lower() in TEXT_SUFFIXES and b"\r\n" in data:
            fail(f"crlf_text:{relative}")
        if len(data) <= 2_000_000:
            for name, pattern in SECRET_PATTERNS.items():
                if pattern.search(data):
                    fail(f"secret_signature:{name}:{relative}")
    return len(files), 0


def verify_hbp_rows() -> int:
    receipts = list(ROOT.rglob("*.hbp")) + list(ROOT.rglob("*.hbi"))
    if not receipts:
        fail("no_hbp_hbi_receipts")
    for receipt in receipts:
        lines = receipt.read_text(encoding="utf-8").splitlines()
        if not lines or any("json=0" not in line for line in lines):
            fail(f"non_tuple_receipt:{receipt.relative_to(ROOT).as_posix()}")
    return len(receipts)


def verify_rust() -> int:
    version = run(["rustc", "+1.81.0", "--version"]).decode().strip()
    if not version.startswith("rustc 1.81.0 "):
        fail(f"wrong_rust:{version}")
    matched = 0
    for name, manifest, expected_path in RUNS:
        run([
            "cargo", "+1.81.0", "clippy", "--quiet", "--locked",
            "--manifest-path", str(manifest), "--", "-D", "warnings",
        ])
        actual = run([
            "cargo", "+1.81.0", "run", "--quiet", "--locked",
            "--manifest-path", str(manifest),
        ])
        expected = expected_path.read_bytes()
        if actual != expected:
            fail(f"stdout_hbp_mismatch:{name}:{hashlib.sha256(actual).hexdigest()}")
        matched += 1
    return matched


def verify_python() -> str:
    script = ROOT / "first-results" / "shared_key_81.py"
    expected = (ROOT / "receipts" / "SHARED-KEY-81-FIRST.out").read_bytes()
    actual = run([sys.executable, str(script)])
    if actual != expected:
        fail(f"shared_key_output_mismatch:{hashlib.sha256(actual).hexdigest()}")
    required = (
        b"drop any ONE seat, recover from the other 80 + banked sum: 81/81",
        b"81 seats outright      = 1,701 bits",
        b"ship 80 + closure      = 1,680 + 21 = 1,701 bits",
    )
    if any(row not in actual for row in required):
        fail("shared_key_required_result_missing")
    return hashlib.sha256(actual).hexdigest()


def verify_kernel_witness() -> str:
    root = ROOT / "browser-evidence" / "kernel81"
    wasm = root / "web" / "kernel81.wasm"
    receipt = (root / "RESULT.hbp").read_text(encoding="utf-8")
    digest = sha256(wasm)
    if digest != "a411d88aa304c58c645ba7f7d0938a6fad4a1457e29b5e695c22ed0977530371":
        fail("kernel81_wasm_hash_mismatch")
    required = (
        "INSTANCES|instantiations=81|distinct_linear_memories=81",
        "ALIVE|reporting=81/81",
        "CLOSURE|cells=27|closed_to_zero=27|global_sum_of_81_arms=0",
    )
    if any(row not in receipt for row in required):
        fail("kernel81_receipt_result_missing")
    return digest


def main() -> None:
    pinned = verify_source_manifest()
    files, secret_findings = verify_text_and_secrets()
    rust_receipts = verify_rust()
    python_digest = verify_python()
    wasm_digest = verify_kernel_witness()
    receipt_count = verify_hbp_rows()
    sidecars = verify_sidecars()
    print(
        "FIRST_RESULTS_VERIFY|PASS=1"
        f"|files={files}|pinned={pinned}|rust_receipts={rust_receipts}"
        f"|python_sha256={python_digest}|wasm_sha256={wasm_digest}"
        f"|receipts={receipt_count}|sidecars={sidecars}"
        f"|secret_findings={secret_findings}|later_audit_paths=0"
        "|rust=1.81.0|json=0"
    )


if __name__ == "__main__":
    main()
