# FF-7CR-2026 — Quantum Blitz (QBZ)

ESPN PPR league **7 Creeks Armchair Quarterbacks** (leagueId 1776545061), team **Quantum Blitz** (teamId 13), 2026 season. Owner: Ken Rich. All times CT.

Run by four agents: **Blitz** (co-manager: decisions, ESPN clicks, log), **Wire** (injuries/availability), **Sigma** (our-roster stats), **Recon** (other 11 teams + waiver watch). Ken is owner-veto. **Arbiter** writes `FUD/` and standing orders when in the loop.

## Layout
| Path | What |
|---|---|
| `FUD/` | Competitive analysis of the other 11 + our posture. Start at `FUD/BOARD.md`. Arbiter owns. Recon feeds roster facts. |
| `playbook/` | Shared law and strategy: `LAW-*`, `STRATEGY.md`, `OPS.md`, `SPEC.md`, `WAR.md` (decision log), `LESSONS.md`, `CONTINGENCY.md`, `WAIVERS.md`, `TEAM.md`, `SCORECARD.md`, `EDGES.md`, `RIPPLES.md` |
| `charters/` | Role charters Blitz maintains: `BLITZ.md`, `WIRE.md`, `SIGMA.md`, `RECON.md` |
| `agents/<name>/` | Each agent's own definition files, pushed by that agent |
| `data/` | Current league/roster/schedule/standings/availability/projections JSON |
| `weekly/` | Lineup cards, decision records, sealed votes |
| `lanes/` | Specialist working files: `recon/`, `wire/`, `results/` (scorecards, Sigma research) |
| `code/espn_api/` | Read/write client for ESPN fantasy API |

## Not in this repo (by design)
ESPN session cookies (`secrets/`), league members' ESPN IDs, raw ESPN API dumps, the audit log, API response captures, screenshots, virtualenvs, and `.bak` copies.

Synced from Blitz's working copy; Blitz pushes updates when the shared files change.
