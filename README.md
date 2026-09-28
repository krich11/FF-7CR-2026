# FF-7CR-2026 — Quantum Blitz (QBZ)

ESPN PPR league **7 Creeks Armchair Quarterbacks** (leagueId 1776545061), team **Quantum Blitz** (teamId 13), 2026 season. Owner: Ken Rich. All times CT.

Four bots, one folder each under [`agents/`](agents/README.md): **Blitz**, **Wire**, **Sigma**, **Recon**. Ken is owner-veto. Arbiter writes `FUD/` when in the loop.

## Layout
| Path | What |
|---|---|
| [`agents/`](agents/README.md) | Each bot: CHARTER + profile + routines. Start here. |
| [`FUD/`](FUD/README.md) | Competitive board on the other 11 |
| [`playbook/`](playbook/README.md) | Shared strategy, WAR.md, SPEC, laws |
| [`data/`](data/README.md) | Live JSON (roster, availability, standings) |
| [`weekly/`](weekly/README.md) | Cards, decision JSON, sealed votes |
| [`lanes/`](lanes/README.md) | Work dumps (alias until tools retarget to `agents/<bot>/work/`) |
| [`charters/`](charters/README.md) | Stubs. Real charters are under `agents/` |
| [`rosters/`](rosters/README.md) | Per-club markdown cards |
| [`ops/`](ops/README.md) | Arbiter short-cycle files |
| [`code/espn_api/`](code/espn_api/README.md) | ESPN client |

## Not in this repo
ESPN cookies (`secrets/`), member ESPN IDs, raw API dumps, audit log, screenshots, venvs, `.bak` copies.
