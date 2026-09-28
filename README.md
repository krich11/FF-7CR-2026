# FF-7CR-2026

Shared working repo for one ESPN fantasy football team and the bots that run it.

What belongs where is defined in `FILESYSTEM.md`. How the bots use this repo is defined in `BOTS.md`.

| Directory | Purpose |
|---|---|
| `playbook/` | Shared law and the live operating files |
| `FUD/` | Competitive analysis of the rest of the league |
| `data/` | Current machine-readable state |
| `weekly/` | Per-week cards, decisions, and votes |
| `agents/` | Each bot's identity and its own work tree |
| `code/` | Client libraries |

`lanes/`, `ops/`, `rosters/`, and `charters/` are archives. Do not add files there.

Do not commit secrets or session cookies.
