# FILESYSTEM.md

This GitHub repo (krich11/FF-7CR-2026, main) is the only operating disk for Blitz and Assistant. If it is not on main, it does not exist. The rulebook is PLAYBOOK.md. Scripts in agents/recon/work/tools/ look for this file to find the repo root, so keep it here.

Cookies and other secrets never go in the repo. They stay in /workspace/fantasy/quantum-blitz/secrets/.

## Live files
- PLAYBOOK.md, RULES.md, STRATEGY.md: rules, league rules, season strategy (Blitz).
- playbook/LESSONS.md, playbook/CLAIMS.md, playbook/SCORECARD.md: lessons, waiver requests, scorecard template (Blitz).
- playbook/CONSULT.md and CONSULTANT.md: Consultant's files. Bots read them and do not edit them.
- trades/: four-sided trade write-ups (Blitz).
- weekly/: cards, decisions, results, votes, and audit logs (Blitz).
- data/availability.json, data/projections/, data/usage/, data/recon/: Assistant's facts.
- data/roster.json and the other data/*.json files: league state from the ESPN client.
- agents/blitz/, agents/assistant/: each bot's charter and work.
- agents/recon/work/tools/: dump scripts Assistant runs.
- code/espn_api/: ESPN client used by the dump scripts.
- FUD/: notes on the other teams.

## Archive
archive/ holds retired files: the old SPEC, LAW, and WAR files, the retired Wire, Sigma, and Recon bots, and the old lanes, ops, rosters, and charters trees. Do not write there.
