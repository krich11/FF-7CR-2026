# data/recon/ — inbox

Recon's real repo is **private local git**. This folder is the only way she exists on GitHub.

Drop, at minimum, after each ESPN pull:

- `league_index.json`
- `league_rosters.json`
- `transactions_recent.json`
- waiver order after reset

If this directory has no fresh `as_of` this week, treat Recon as offline and run FUD off the last known dump in `lanes/recon/` (legacy).

Do not maintain a second Recon workstation under `agents/recon/` or `lanes/recon/`.
