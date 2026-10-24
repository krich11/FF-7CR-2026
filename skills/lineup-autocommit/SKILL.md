---
name: lineup.autocommit
description: >-
  Use at the Sunday 9:53 AM CT dead-man to apply the current legal Quantum Blitz
  card to unlocked ESPN lineup slots, only when every gate passes. Re-sync the
  roster and re-check availability first.
---
# lineup.autocommit

The Sunday dead-man for Quantum Blitz. It runs at 9:53 AM CT on Sunday and changes lineup slots only. It never touches waivers, adds, drops, trades, or IR.

## Setup (every run)
1. Pull main in the repo checkout: `cd /workspace/ff-repo && git -c credential.helper= pull -q --rebase https://x-access-token:${QBZ_GITHUB_TOKEN}@github.com/krich11/FF-7CR-2026.git main`. Never echo the token.
2. Read `PLAYBOOK.md` (the rulebook), plus `RULES.md` and `STRATEGY.md` when making a recommendation. All data and rules live in the repo; the old folder `/workspace/fantasy/quantum-blitz/` is used only for the ESPN client (`espn_api/`) and its auth file, which is never printed.
3. After writing, commit and push: `git -c credential.helper= push -q https://x-access-token:${QBZ_GITHUB_TOKEN}@github.com/krich11/FF-7CR-2026.git HEAD:main` (rebase-pull and retry once if rejected).
4. If ESPN auth fails at any point, stop and tell Ken that the ESPN login has expired. Never re-export cookies.

## Gates (all must pass)
1. Fresh availability: `data/availability.json` was written Sunday at 7:00 AM CT or later and is under four hours old. If not, post that the dead-man is blocked for stale availability and leave ESPN alone.
2. Run roster.sync and re-check every starter against ESPN's tag and any official can't-play list. Starters who are OUT, inactive, on bye, or official_block come out.
3. Read Assistant's latest file in `agents/assistant/work/close-calls/` and re-score any slot within 1.5 projected points; in MUST-WIN mode a close call goes to the higher-ceiling player facing the weaker defense.
4. The card in `weekly/cards/week-N.md` and `weekly/decisions/week-N.json` exists and is for this week. Re-score any saved branch against the live roster before it fires.
5. Ken has not said "hold" or "stop" since the card.
6. Only unlocked slots move.

## Steps
1. If the re-check changes the lineup, update the card and decisions file first and post the new card.
2. If any gate fails, post that the dead-man is blocked and why, and leave ESPN alone.
3. Otherwise apply with espn.api-apply and report the result as verified or unverified.

## Output
Plain standard English in full sentences, per Ken's writing rules in PLAYBOOK.md. Name the inputs used (ESPN pull time, availability file time, Assistant's Friday files and latest close-call file where relevant) and name any missing or late file. All times CT.

## Hard stops
Lineup only. A failed verify always goes to Ken immediately.
