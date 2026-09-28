# data/

Live JSON. Check `as_of`. Stale is a bug.

| File | Who | What |
|---|---|---|
| `league.json` | client | Settings, leagueId |
| `roster.json` | Blitz | Our roster |
| `schedule.json` | Blitz | Our matchups |
| `standings.json` | Blitz | W-L / PF / PA |
| `availability.json` | Wire | **The** injury file |
| `projections.json` | Sigma / client | Projections |
| `waivers.json` | client | FA / WW snapshot |
| `preferences.json` | Blitz | Start/sit prefs |
| `sources.json` | shared | Provenance |
| [recon/](recon/README.md) | Recon export | League dumps from her local git |

Do not create `data/availability2.json`. Do not keep a second roster in `rosters/`.
