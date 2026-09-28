"""Shared paths for Recon tools.

Repo (krich11/FF-7CR-2026 main) is the source of truth:
  REPO_ROOT            env REPO_ROOT, default /workspace/ff-repo
  DATA_RECON           $REPO_ROOT/data/recon            (main dumps)
  SNAP                 $REPO_ROOT/data/recon/snapshots  (dated copies)
  WORK                 $REPO_ROOT/agents/recon/work     (week-N/ packets)
Raw ESPN captures are LOCAL ONLY (never inside the repo):
  RAW_ROOT             env RECON_RAW_DIR, default /workspace/fantasy/quantum-blitz/recon/raw
ESPN auth/cookies stay in local secrets (loaded by code/espn_api/client.py; never printed).
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

REPO_ROOT = Path(os.environ.get("REPO_ROOT", "/workspace/ff-repo")).resolve()
DATA = REPO_ROOT / "data"
DATA_RECON = DATA / "recon"
SNAP = DATA_RECON / "snapshots"
WORK = REPO_ROOT / "agents" / "recon" / "work"
RAW_ROOT = Path(os.environ.get("RECON_RAW_DIR", "/workspace/fantasy/quantum-blitz/recon/raw")).resolve()
LOCAL_CLIENT = Path("/workspace/fantasy/quantum-blitz/espn_api")

if RAW_ROOT == REPO_ROOT or REPO_ROOT in RAW_ROOT.parents:
    raise SystemExit(f"RECON_RAW_DIR must be outside the repo ({REPO_ROOT})")


def use_espn_client() -> None:
    """Put the ESPN client on sys.path: repo code/espn_api first, local copy as fallback."""
    for p in (REPO_ROOT / "code" / "espn_api", LOCAL_CLIENT):
        if (p / "client.py").exists():
            sys.path.insert(0, str(p))
            return
    raise SystemExit("ESPN client not found (code/espn_api/client.py)")


def week_dir(week: int) -> Path:
    """Recon week packet dir in the repo: agents/recon/work/week-N/."""
    return WORK / f"week-{week}"


def raw_dir(week: int) -> Path:
    """Local-only raw capture dir: $RECON_RAW_DIR/wNN/."""
    return RAW_ROOT / f"w{week:02d}"


def rel(p: Path) -> str:
    """Repo-relative path string (falls back to absolute if outside repo)."""
    try:
        return str(Path(p).resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(p)
