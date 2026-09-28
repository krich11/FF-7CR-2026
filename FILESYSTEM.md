# Filesystem freeze — 2026-09-27 22:35 CT

This repo is the hallway for Blitz, Wire, Sigma, Arbiter, and Ken.
Recon lives on a **private local git**. She is invisible unless she drops a file in `data/recon/`.

## Live (write here)

| Path | What | Who writes |
|---|---|---|
| `data/` | Current JSON. One availability file, one roster file. | Blitz client, Wire |
| `data/recon/` | Recon inbox. If it is empty, we do not have Recon. | Recon export |
| `data/availability.json` | The only injury file that counts | Wire |
| `playbook/WAR.md` | The only decision log | Blitz |
| `playbook/CLAIMS.md` | The only claim ticket | Blitz + Sigma boards |
| `playbook/ARBITER.md` | Settled calls | Arbiter |
| `FUD/` | The only opponent board | Arbiter; Recon facts |
| `weekly/` | Cards, decision JSON, sealed votes | Blitz |
| `agents/<bot>/` | CHARTER + profile + routines | Blitz / that bot |
| `code/espn_api/` | Client | Blitz |

## Dead for new writes (do not add files)

| Path | Why it still exists |
|---|---|
| `lanes/` | Historical dumps and scripts. Read-only. |
| `ops/` | Folded into `playbook/`. |
| `rosters/` | Folded into `FUD/` + `data/roster.json`. |
| `charters/` | Folded into `agents/<bot>/CHARTER.md`. Full text still there until pasted. |

## One of each

- One claims file: `playbook/CLAIMS.md`
- One WAR: `playbook/WAR.md`
- One availability JSON: `data/availability.json`
- One opponent board: `FUD/`
- One inbox for Recon: `data/recon/`

If a bot writes the same fact to two of these, the live path wins and the other copy is wrong.
