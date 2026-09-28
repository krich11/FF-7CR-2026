# lanes/ — DEPRECATED

Read-only archive. Do not add files.

| Old path | Live path |
|---|---|
| `lanes/recon/*.json` | `data/recon/` |
| `lanes/wire/` | `data/availability.json` |
| `lanes/results/week-*` | `weekly/` |
| `lanes/results/sigma/` | stay as Sigma archive; new packets go to Blitz and `playbook/CLAIMS.md` |

Scripts under `lanes/recon/tools/` may still *read* these dumps. Point new output at `data/recon/`.
