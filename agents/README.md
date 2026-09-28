# agents/

One folder per bot. Identity lives here. Shared league data stays in `data/`. Shared law that is not a person stays in `playbook/`.

```
agents/
  blitz/    CHARTER.md  profile.json   README.md
  wire/     CHARTER.md  PROFILE.md     ROUTINES.md  README.md
  sigma/    CHARTER.md  PROFILE.md     ROUTINES.md  README.md
  recon/    CHARTER.md  PROFILE.md     ROUTINES.md  README.md
```

| File in the bot dir | Who writes it |
|---|---|
| `CHARTER.md` | Blitz (law). Specialist proposes a patch. |
| `PROFILE.md` / `profile.json` | That bot |
| `ROUTINES.md` | That bot |

## Where the work goes

Historical dumps are still under `lanes/` so existing tools do not break tonight.

| Bot | New writes (preferred) | Old path still valid |
|---|---|---|
| Recon | `agents/recon/work/` when you create it | `lanes/recon/` |
| Wire | `agents/wire/work/` when you create it | `lanes/wire/` |
| Sigma | `agents/sigma/work/` when you create it | `lanes/results/sigma/` |
| Blitz | `playbook/WAR.md`, `weekly/` | — |

Do not add a fifth bot folder without Ken.

See [LAYOUT.md](LAYOUT.md) for the old → new map.
