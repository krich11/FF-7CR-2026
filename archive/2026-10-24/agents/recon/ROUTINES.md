# Recon: scheduled runs (all times America/Chicago)

Source of truth: `krich11/FF-7CR-2026` `main`. Every run starts with `git pull --rebase` in `/workspace/ff-repo` and ends with a push to `main`.

| Routine | Schedule | What it does | Writes |
|---|---|---|---|
| Recon Monday packet | Tue 7:23 AM CT (`23 7 * * 2`) | Pull main. Refresh league dumps with `agents/recon/work/tools/` (`run_week_scan.py --week N --refresh --diff`; ESPN read-only). Post-week mistakes board for the other 11 teams (graded after MNF is final; unfinished MNF graded as pending). Reset waiver order with RB-need tags per team, claim likelihood, next-opponent starters. Deep-file sections IF WE PASS, TRADE BUTTON, SLATE STACKERS. | `data/recon/` (dumps + `snapshots/<stamp>/`), `agents/recon/work/week-N.md` (+ `week-N/` packets). Sends Blitz the links. |
| Tue adversarial AAR | Tue 9:10 AM CT (`10 9 * * 2`) | Recon-lane after-action review of last week's calls. Short note on quiet weeks. | `agents/recon/work/aar/YYYY-MM-DD-wNN.md`. Sends Blitz the link plus proposed patches (durable rule changes as proposed `RECON.md` patches; Blitz applies). |

## Push rules (both routines)

- Push with `QBZ_GITHUB_TOKEN` only (read from the box secrets store if the env var is empty; never printed, logged, or committed). Never `GITHUB_TOKEN`.
- Commits prefixed `Recon: `. `git pull --rebase` right before push; on rejection rebase and retry. No force-push.
- Cloud agent only if the direct push fails.
- Raw ESPN captures stay local (`/workspace/fantasy/quantum-blitz/recon/raw/`); cookies stay in local `secrets/`.

No other timers. Midweek transaction scans run only when Blitz asks or a material IR/wire event hits.
