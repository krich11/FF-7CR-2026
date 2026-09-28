# agents/

Each bot's own definition files. The bot that lives here writes these. Blitz does not rewrite another agent's profile.

Law lives in `charters/`. Working files live in `lanes/` and `playbook/`.

| Dir | Bot | Job |
|---|---|---|
| [blitz/](blitz/) | Blitz | Co-manager. ESPN clicks, WAR, Ken ticket |
| [wire/](wire/) | Wire | Injury tags and availability |
| [sigma/](sigma/) | Sigma | Our roster usage, start/sit math |
| [recon/](recon/) | Recon | Other 11 teams and waiver watch |

Typical files in a bot dir: `README.md`, `PROFILE.md` or `profile.json`, `ROUTINES.md`.
