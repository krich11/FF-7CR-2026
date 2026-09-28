#!/usr/bin/env python3
"""Shared paths for Recon tools. One helper. Do not add _paths.py.

Repo (krich11/FF-7CR-2026 main) is the source of truth.
Raw ESPN captures stay LOCAL ONLY via RECON_RAW_DIR (must be outside the repo).
ESPN cookies stay in local secrets. Never print them.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path


def repo_root() -> Path:
    env = os.environ.get("REPO_ROOT")
    if env:
        p = Path(env).resolve()
        if (p / "FILESYSTEM.md").is_file() and (p / "data").is_dir():
            return p
        raise SystemExit(f"REPO_ROOT={p} is not this repo (need FILESYSTEM.md + data/)")
    here = Path(__file__).resolve()
    for p in [here, *here.parents]:
        if (p / "FILESYSTEM.md").is_file() and (p / "data").is_dir():
            return p
    raise SystemExit("repo root not found (need FILESYSTEM.md + data/)")


REPO_ROOT = repo_root()
DATA = REPO_ROOT / "data"
DATA_RECON = DATA / "recon"
SNAP = DATA_RECON / "snapshots"
WORK = REPO_ROOT / "agents" / "recon" / "work"
RAW_ROOT = Path(os.environ.get("RECON_RAW_DIR", "/workspace/fantasy/quantum-blitz/recon/raw")).resolve()

if RAW_ROOT == REPO_ROOT or REPO_ROOT in RAW_ROOT.parents:
    raise SystemExit(f"RECON_RAW_DIR must be outside the repo ({REPO_ROOT})")


def use_espn_client() -> None:
    """Put the ESPN client on sys.path: repo code/espn_api first."""
    client = REPO_ROOT / "code" / "espn_api"
    if (client / "client.py").exists():
        sys.path.insert(0, str(client))
        return
    raise SystemExit("ESPN client not found (code/espn_api/client.py)")


def week_dir(week: int) -> Path:
    return WORK / f"week-{week}"


def raw_dir(week: int) -> Path:
    return RAW_ROOT / f"w{week:02d}"


def rel(p: Path) -> str:
    try:
        return str(Path(p).resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(p)
