---
name: lineup.set
description: >-
  Use when setting Quantum Blitz’s full weekly lineup before the NFL week’s
  first kickoff (Tuesday/Wednesday Set window or “set Week N”).
---
# lineup.set

Produce the week-opener start/sit card for Quantum Blitz **before** the NFL week’s first kickoff. Also on demand when Ken says “set Week N.”


## Lessons first (feedback loop, Ken Oct 20 2026)

Also read `RULES.md` and `STRATEGY.md` (repo root) (league rules canon, Ken Oct 23 2026) before any recommendation and run its checklist. Never propose moving or dropping a player whose game has started; check rosterLocked/lineupLocked first.
Before building or changing anything, pull main and read every fix rule in `playbook/LESSONS.md`. Apply each one that touches this run, and check the finished card or post against them before it goes out. Rules that matter most right now: no slot is ever marked "only X" (list the best free agent at K, D/ST, and QB with a bye backup, and ask Ken the same day if he clears 1.5 points); when a starter's team changes starting QB or play-caller, re-check that slot against the bench; add up team totals from live ESPN numbers before quoting one (never show the math to Ken); rewrite the decisions file from ESPN after every lineup change; no backup plans without an ESPN tag or real news.

## Paths
`/fantasy/quantum-blitz/` — follow `SPEC.md` §§5–7 and §11. Internal lock math may use `America/Los_Angeles` ISO; **all Ken-facing times = America/Chicago (CT)**.

## Steps
1. Run skill [roster.sync](sand-workflow:roster-sync).
2. **Wire handoff:** Read latest `availability.json` and the most recent Wire check-in. Quote Wire’s one-liner at the top of the card (times in CT).
3. Browse official injury page + beat reports + two PPR projection sources. Do not invent injuries, projections, or opponents.
4. Run [projections.validate](sand-workflow:projections-validate) before optimize.
5. Write `availability.json` and `projections.json`. Official status overrides ESPN fantasy tags.
6. Optimize the **full** lineup per SPEC §7.
7. Write `cards/week-{N}.md` and `decisions/week-{N}.json`.
7b. Record shadow-edge predictions via [shadow.edges](sand-workflow:shadow-edges) — paper only.
8. Post the §11 card with WEEK CLOCK, Wire one-liner, auto-commit deadline, and **Games to watch** — **every clock time labeled CT** (convert from schedule ISO). Auto-commit absolute deadline is Tue 20:00 PT = **Tue 10:00 PM CT** (or 3 hours before first kickoff if sooner).
9. If Ken replies `yes, set it`, apply via [espn.api-apply](sand-workflow:espn-api-apply). On verify fail, alert Ken.
10. If `hold` / `stop`, do not apply.
11. Otherwise lineup.autocommit at the deadline.

## Games to watch (required on SET)
```
## Games to watch
- {kickoff CT} · {AWAY @ HOME} — {Player (slot or BENCH), …}
```
Chronological; any rostered player. Outside the 400-word core-card cap.

## Validation
- Legal starters only; week-clock present; Ken-facing times all CT; Games to watch on SET.

## Approval / hard stops
ESPN write only on `yes, set it` or §7.6 gates. No stale-card reuse.
