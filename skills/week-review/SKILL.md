---
name: week.review
description: >-
  Use Tuesday about 7:30 AM CT to review the finished Quantum Blitz week, update
  results and standings, email the Week N scorecard, and record lessons.
---
# week.review

Runs Tuesday about 7:30 AM CT, after Monday night's game is final.

## Setup (every run)
1. Pull main in the repo checkout: `cd /workspace/ff-repo && git -c credential.helper= pull -q --rebase https://x-access-token:${QBZ_GITHUB_TOKEN}@github.com/krich11/FF-7CR-2026.git main`. Never echo the token.
2. Read `PLAYBOOK.md` (the rulebook), plus `RULES.md` and `STRATEGY.md` when making a recommendation. All data and rules live in the repo; the old folder `/workspace/fantasy/quantum-blitz/` is used only for the ESPN client (`espn_api/`) and its auth file, which is never printed.
3. After writing, commit and push: `git -c credential.helper= push -q https://x-access-token:${QBZ_GITHUB_TOKEN}@github.com/krich11/FF-7CR-2026.git HEAD:main` (rebase-pull and retry once if rejected).
4. If ESPN auth fails at any point, stop and tell Ken that the ESPN login has expired. Never re-export cookies.

## Inputs
ESPN results for every rostered player, nflverse snap counts, Assistant's Friday files (`data/projections/week-N.json`, `data/usage/week-N-baseline.json`), and Assistant's Monday packet in `agents/assistant/work/`. Name any that are missing.

## Steps
1. Confirm on ESPN that the matchup is final. If a game is still live, schedule a rerun later Tuesday morning; the scorecard still goes out that day.
2. Write `weekly/results/week-N.json` with each player's points and whether he started.
3. Update `data/standings.json` from ESPN.
4. Find misses where the deciding fact was known before lock. Do not count a bench player's one big game.
5. Run week.scorecard, which emails kaalrich@gmail.com directly.
6. Add up to three lessons to `playbook/LESSONS.md`; if a lesson becomes a standing rule, add it to PLAYBOOK.md.
7. Log the review in `weekly/audit/blitz-audit.log`, commit and push. Chat gets a short summary only.

## Output
Plain standard English in full sentences, per Ken's writing rules in PLAYBOOK.md. Name the inputs used (ESPN pull time, availability file time, Assistant's Friday files and latest close-call file where relevant) and name any missing or late file. All times CT.

## Hard stops
Read-only for ESPN. Never invent stats.
