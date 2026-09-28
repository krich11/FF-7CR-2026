# Filesystem freeze — 2026-09-28 00:11 CT

This GitHub repo is the only operating disk for Blitz and Assistant.
Local git is a cache. If it is not on `main` here, it does not exist.

Cookies stay off-repo in `secrets/`.

Ken ↔ Consultant working rules: `CONSULTANT.md`. Bots do not edit that file.

## Live (write here)

| Path | What | Who |
|---|---|---|
| `CONSULTANT.md` | Ken ↔ Consultant contract | Ken, Consultant |
| `playbook/CONSULT.md` | Consultant → Blitz inbox | Consultant writes. Blitz reads before cards and the waiver request. |
| `data/availability.json` | Injury file | Assistant |
| `data/roster.json` `schedule.json` `standings.json` `league.json` | Our league state | Blitz client |
| `data/recon/` | League-wide dumps | Assistant |
| `data/projections.json` `waivers.json` | Support JSON | Assistant / client |
| `playbook/WAR.md` | Decision log | Blitz |
| `playbook/CLAIMS.md` | Waiver request + boards | Blitz, Assistant when asked |
| `playbook/ARBITER.md` | Settled calls | Arbiter |
| `FUD/` | Opponent board | Blitz + Assistant facts |
| `weekly/` | Cards, decisions, votes | Blitz |
| `weekly/audit/blitz-audit.log` | ESPN sync, lineup applies, claims, verify shots | Blitz |
| `agents/blitz/CHARTER.md` `agents/assistant/CHARTER.md` | Law | Blitz |
| `agents/assistant/work/` | Packets, briefs, Assistant AAR | Assistant |
| `agents/assistant/work/assistant-audit.log` | Status overrides, injury notes | Assistant |
| `agents/recon/work/tools/` | Dump scripts (`repo.py`) | Assistant runs |
| `code/espn_api/` | Client | Blitz |

Bare `audit.log` is gitignored.

`agents/wire/`, `agents/sigma/`, and `agents/recon/` except `work/tools/` are retired reference. Do not schedule those bots.

## Dead trees

`lanes/` · `ops/` · `rosters/` · `charters/`

Do not write. Do not run `lanes/recon/tools/`. Do not delete until after the Week 4 waiver run.
