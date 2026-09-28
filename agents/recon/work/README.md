# agents/recon/work/

Recon-only week briefs and after-action files.

Machine dumps belong in `data/recon/`.

## Layout (migrated from local 2026-09-27)

| Path | What |
|---|---|
| `week-N.md` | Week packet index → `week-N/` |
| `week-N/` | Week packets: prekick scan, waiver watch, opponent cards, trade scouts |
| `WEEK_BRIEF_TEMPLATE.md` | Long-form league brief skeleton (`PACKET_TEMPLATE.md` = short form) |
| `aar/` | Recon after-action reviews |
| `mistakes/` | Opponent start/sit miss notes (post-week) |
| `methods/` | Method notes (e.g. draft-helper VORP) |
| `tools/` | Read-only scanners + dump refresh (GET only, no ESPN writes). Paths inside still point at the old local layout; update before running. |

Dumps and dated snapshots: `data/recon/` and `data/recon/snapshots/`.
Local `/workspace/fantasy/quantum-blitz/recon/` is a stale cache.
