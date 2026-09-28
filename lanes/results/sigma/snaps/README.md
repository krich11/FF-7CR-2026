# Sigma snaps (nflverse / PFR)

**Source:** `https://github.com/nflverse/nflverse-data/releases/download/snap_counts/snap_counts_{season}.csv`  
**Rule:** Never invent snap%. If feed lags or player unmatched → `null` + DATA_QUALITY degraded.

## Files
- `snap_counts_2026_raw.csv` — full season download cache
- `week-{N}.csv` — our-roster rows for that week
- `week-{N}-usage-join.json` — snaps joined to touches/PPR from `results/week-{N}.json`

## Cadence
- W1 backfill: done on greenlight
- Ongoing: refresh raw CSV Mon–Tue after games; rebuild week-N extracts
- FantasyPros key: only if nflverse dies (ask Blitz first)
