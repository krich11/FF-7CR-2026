#!/usr/bin/env python3
"""Locate the FF-7CR-2026 repo root from any tool in this tree."""
from __future__ import annotations

from pathlib import Path


def repo_root() -> Path:
    here = Path(__file__).resolve()
    for p in [here, *here.parents]:
        if (p / "FILESYSTEM.md").is_file() and (p / "data").is_dir():
            return p
    raise SystemExit("repo root not found (need FILESYSTEM.md + data/)")
