# Filesystem freeze — 2026-09-27 23:16 CT

This GitHub repo is the **only** operating disk for Blitz, Wire, Sigma, and Recon.
Local git is a cache. If it is not on `main` here, it does not exist.

Cookies stay off-repo in `secrets/`.

## Live (write here)

| Path | What | Who |
|---|---|---|
| `data/availability.json` | Injury file | Wire |
| `data/roster.json` `schedule.json` `standings.json` `league.json` | Our league state | Blitz client |
| `data/recon/` | League-wide dumps | Recon |
| `data/projections.json` `waivers.json` | Support JSON | Sigma / client |
| `playbook/WAR.md` | Decision log | Blitz |
| `playbook/CLAIMS.md` | Claim ticket + Sigma boards | Blitz, Sigma |
| `playbook/ARBITER.md` | Settled calls | Arbiter |
| `FUD/` | Opponent board | Arbiter + Recon facts |
| `weekly/` | Cards, decisions, votes | Blitz |
| `weekly/audit/blitz-audit.log` | ESPN sync, lineup applies, claims, verify shots | Blitz |
| `agents/<bot>/CHARTER.md` | Law | Blitz |
| `agents/<bot>/PROFILE.md` `ROUTINES.md` | Identity | that bot |
| `agents/wire/work/` | Digests, Wire AAR | Wire |
| `agents/wire/work/wire-audit.log` | Status overrides, injury notes, availability refreshes | Wire |
| `agents/sigma/work/` | Packets, snaps, Sigma AAR | Sigma |
| `agents/recon/work/` | Week briefs, Recon AAR | Recon |
| `code/espn_api/` | Client | Blitz |

Bare `audit.log` is gitignored. Use the prefixed names above.

## Dead trees

`lanes/` · `ops/` · `rosters/` · `charters/`

Each has `DEPRECATED.md`. Twins inside `ops/` are stubs. Tools inside `lanes/recon/tools/` exit 2. Do not write. Do not run. Do not delete until after the Week 4 waiver run.

## One of each

Claims, WAR, availability, FUD, Recon dumps: one path each. Two copies means the live path is right and the other is wrong.
