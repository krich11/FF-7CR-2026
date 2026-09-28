# recon/ — Recon write path

League scout dumps + weekly packets. **Read-only ESPN.** No `availability.json`, no Ken-facing claim boards.

## Layout
| Path | Purpose |
|------|---------|
| `league_index.json` | 12-team summary (waiver rank, record, roster counts) |
| `league_rosters.json` | Full rosters + starters (espn_api) |
| `transactions_recent.json` | Recent FA/waiver/trade/draft activity |
| `last_refresh.json` | Last successful refresh meta |
| `snapshots/` | Pre-refresh dump copies for `material_diff` |
| `weekly/wNN/` | Week packets (`prekick-scan.md`, `waiver-watch.md`, …) |
| `weekly/_TEMPLATE.md` | Brief skeleton for Blitz packets |
| `mistakes/` | Opponent start/sit miss notes (post-week) |
| `tools/` | Local scanners + read-only refresh (no ESPN writes) |

## Tools
```bash
python3 recon/tools/run_week_scan.py --week 1
python3 recon/tools/run_week_scan.py --week 1 --refresh --diff
python3 recon/tools/refresh_dumps.py
python3 recon/tools/waiver_watch.py --week 1
python3 recon/tools/opponent_flags.py --week 1
python3 recon/tools/material_diff.py --week 1
```

`material_diff.ping_blitz == true` → midweek ping Blitz (competition intel only).
Refresh dumps before weekly cards. Never print cookie values.
