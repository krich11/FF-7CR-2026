# data/

Current-state JSON for Quantum Blitz and the league. Blitz / the ESPN client refresh these. Specialists read; they do not invent a parallel copy.

| File | Owner-ish | What |
|---|---|---|
| `league.json` | shared | Settings, slots, waiver rules, leagueId |
| `roster.json` | Blitz | Our current roster |
| `schedule.json` | Blitz | Our matchups |
| `standings.json` | Blitz | Our W-L / PF / PA (check `as_of`) |
| `availability.json` | Wire | Injury / tag file |
| `projections.json` | Sigma / client | Point projections |
| `waivers.json` | Recon / client | Wire / FA snapshot |
| `preferences.json` | Blitz | Start/sit preferences |
| `sources.json` | shared | Where numbers came from |

Stale `as_of` is a bug. Say it. Do not paper over Week 2 standings in Week 3.
