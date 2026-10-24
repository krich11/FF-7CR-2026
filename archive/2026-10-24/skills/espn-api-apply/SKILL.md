---
name: espn.api-apply
description: >-
  Use when applying or verifying a Quantum Blitz ESPN lineup via the fantasy API
  (preferred over browser DOM), including post-write verify and Ken alert on
  failure.
---
# espn.api-apply

Preferred ESPN write path for Quantum Blitz: REST lineup transactions + post-read verify. Browser DOM is fallback only.

## Paths
- Client: `/workspace/fantasy/quantum-blitz/espn_api/client.py`
- CLI: `python3 /workspace/fantasy/quantum-blitz/espn_api/cli.py {sync|plan|apply|verify|starters}`
- Auth: `/workspace/fantasy/quantum-blitz/secrets/espn_cookies.json` (`SWID`, `espn_s2`) — never print cookie values in chat
- League defaults in CLI: league `1776545061`, team `13`, season `2026`

## Auth refresh
If read/write returns 401/403:
1. Open ESPN Fantasy in the box browser (existing session).
2. Re-export cookies into `secrets/espn_cookies.json` (chmod 600).
3. Retry once. If still failing, alert Ken and fall back to browser apply + [espn.lineup-shots](sand-workflow:espn-lineup-shots).

## Sync (read)
```
python3 /workspace/fantasy/quantum-blitz/espn_api/cli.py sync
```
Writes `roster.json` with `source: espn_api` and current starters. Prefer this inside [roster.sync](sand-workflow:roster-sync) before opening the team page.

## Plan / apply (write)
Only after `yes, set it` or §7.6 autocommit gates pass.

1. `python3 .../cli.py plan --week N` — show moves vs `decisions/week-N.json`
2. Optional: save browser before shot via [espn.lineup-shots](sand-workflow:espn-lineup-shots) (still useful for Ken)
3. `python3 .../cli.py apply --week N`
4. Read JSON result:
   - `alert: false` and verify ok → success; deliver after shot if using shots skill
   - `noop: true` → already matched
   - `alert: true` → **stop claiming success**; message Ken immediately: `ESPN API VERIFY FAILED` + mismatches / HTTP status; do not leave a half-applied claim; attempt browser apply+shots if Ken wants, or ask

## Verify only
```
python3 /workspace/fantasy/quantum-blitz/espn_api/cli.py verify --week N
```

## Hard stops
- Never print `espn_s2` / `SWID` values
- Never use this for waivers, drops, trades, or IR moves (LINEUP type only)
- Never apply without approval / dead-man gates
- On verify fail: alert Ken in chat; log `ESPN_API_VERIFY_FAIL` in `audit.log`
