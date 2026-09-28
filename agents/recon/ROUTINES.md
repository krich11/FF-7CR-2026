# Recon: scheduled runs (all times America/Chicago)

| Routine | Schedule | What it does |
|---|---|---|
| Recon Monday packet | Tue 7:23 AM CT (`23 7 * * 2`) | Post-week mistakes board for the other 11 teams, graded after MNF is final (unfinished MNF graded as pending). Builds the deep-file sections IF WE PASS, TRADE BUTTON, and the weekly SLATE STACKERS check. |
| Tue adversarial AAR | Tue 9:10 AM CT (`10 9 * * 2`) | Recon-lane after-action review. Findings go to `recon/aar/`; durable rule changes go to Blitz as proposed `RECON.md` patches. Short note on quiet weeks. |

No other timers. Midweek transaction scans run only when Blitz asks or a material IR/wire event hits.
