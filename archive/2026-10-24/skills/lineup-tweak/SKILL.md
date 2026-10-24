---
name: lineup.tweak
description: >-
  Use on Friday after injury reports to re-optimize only unlocked Quantum Blitz
  Sunday/Monday lineup slots.
---
# lineup.tweak

Friday injury-report re-optimize for Quantum Blitz. Only still-unlocked Sunday/Monday slots. Never treat a Friday “set my lineup” request as lineup.set.


## Lessons first (feedback loop, Ken Oct 20 2026)

Also read `RULES.md` and `STRATEGY.md` (repo root) (league rules canon, Ken Oct 23 2026) before any recommendation and run its checklist. Never propose moving or dropping a player whose game has started; check rosterLocked/lineupLocked first.
Before building or changing anything, pull main and read every fix rule in `playbook/LESSONS.md`. Apply each one that touches this run, and check the finished card or post against them before it goes out. Rules that matter most right now: no slot is ever marked "only X" (list the best free agent at K, D/ST, and QB with a bye backup, and ask Ken the same day if he clears 1.5 points); when a starter's team changes starting QB or play-caller, re-check that slot against the bench; add up team totals from live ESPN numbers before quoting one (never show the math to Ken); rewrite the decisions file from ESPN after every lineup change; no backup plans without an ESPN tag or real news.

## Paths
`/fantasy/quantum-blitz/` — SPEC §§5, 7, 8.3, 11; `RIPPLES.md`. Routine fires Fri 14:00 PT; **Ken-facing times = America/Chicago (CT)** (post deadline Fri 10:00 PM CT).

## Steps
1. Run skill [roster.sync](sand-workflow:roster-sync).
2. **Wire handoff:** Read latest `availability.json` + latest Wire check-in; quote Wire’s one-liner (CT times).
3. Mark Wed/Thu players `LOCKED` or `DONE`. Do not recommend swapping them.
4. Refresh Friday practice/injury report only for unlocked players. Official status overrides ESPN tags.
5. Run [projections.validate](sand-workflow:projections-validate), then write updated files.
6. Re-optimize **unlocked slots only**.
7. Diff vs existing `cards/week-{N}.md`. Title `Friday tweak — Week {N}`.
7b. Refresh [shadow.edges](sand-workflow:shadow-edges) preds (paper only).
7c. **Ripples:** include a categorized ripple block per `RIPPLES.md` (LIVE/LOCKED · FRIDAY CARD · BENCH UPSIDE · MULTI-WEEK TRACK · DST/SCRIPT). Never a flat list.
8. Post with Wire one-liner + auto-commit deadline as **Fri 10:00 PM CT** (Fri 20:00 PT absolute).
9. On `yes, set it` or Friday autocommit: [espn.api-apply](sand-workflow:espn-api-apply); alert on verify fail.

## Validation
Frozen players separate; no moves of kicked games; Ken-facing times labeled CT; ripples categorized.

## Approval / hard stops
`yes, set it` or dead-man only. Fail visible if Friday IR cannot be fetched.
