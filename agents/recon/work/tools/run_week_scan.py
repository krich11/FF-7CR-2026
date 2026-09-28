#!/usr/bin/env python3
"""Orchestrate dump-based Recon scans for a week (no ESPN writes).

Reads/writes the repo: env REPO_ROOT (default /workspace/ff-repo) -> data/recon/ dumps,
agents/recon/work/week-N/ packets. See _paths.py.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parent


def run(cmd: list[str]) -> None:
    print("+", " ".join(cmd), flush=True)
    subprocess.check_call(cmd)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--week", type=int, default=1)
    ap.add_argument("--refresh", action="store_true", help="ESPN read-only dump refresh first")
    ap.add_argument("--diff", action="store_true", help="diff txs vs latest snapshot")
    args = ap.parse_args()
    py = sys.executable
    if args.refresh:
        run([py, str(TOOLS / "refresh_dumps.py")])
    run([py, str(TOOLS / "waiver_watch.py"), "--week", str(args.week)])
    run([py, str(TOOLS / "opponent_flags.py"), "--week", str(args.week)])
    if args.diff:
        run([py, str(TOOLS / "material_diff.py"), "--week", str(args.week)])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
