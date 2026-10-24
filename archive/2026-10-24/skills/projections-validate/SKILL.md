---
name: projections.validate
description: >-
  Use after fetching Quantum Blitz week projections to convert standard→PPR when
  needed, flag >3.0 source gaps, and zero out EXEMPT/PUP/IR/OUT players before
  optimizing.
---
# projections.validate

Validate Quantum Blitz Week N projection numbers before they enter the optimizer. Catch standard-vs-PPR mixups, status mismatches, and silent source failures.

## Paths
`/workspace/fantasy/quantum-blitz/projections.json` (and optional `research_week{N}.json`). Requires resolved states from [status.resolve](sand-workflow:status-resolve) / `availability.json`.

## Steps
1. For each rostered skill player, collect at least two sources when possible (ESPN Fantasy PPR + FantasyPros PPR consensus preferred).
2. **Scoring check:** If a FantasyPros (or other) player page shows a points total that equals rushing/receiving yards&TDs **without** adding receptions, treat it as **standard**. Convert: `ppr = standard + receptions`. Prefer positional `?scoring=PPR` tables when available.
3. **Gap flag:** If two PPR sources disagree by **> 3.0** for the same player/week, use a trimmed mean and set `uncertainty: high`. Log the gap.
4. **Status override (friction 4):** If resolved `state` from [status.resolve](sand-workflow:status-resolve) is `EXEMPT | PUP | IR | OUT | BYE | suspended`, force `consensus = 0` and discard any site (including ESPN Fantasy) still projecting them as a starter — even if ESPN tag is only `DTD`/`Q`.
5. Write `projections.json` with per-player: `espn`, `fantasypros_ppr`, `consensus`, `scoring_notes`, `gap`, `uncertainty`, `status_forced_zero` (bool).
6. Do not invent numbers. Null is allowed; invented fill is not.

## When
Run during lineup.set / lineup.tweak / autocommit pre-refresh, after raw projection fetch and status.resolve, before optimize.

## Hard stops
Never feed unconverted standard scores into a PPR optimize. Never keep a non-zero proj for resolved EXEMPT/PUP/IR/OUT. Never soft-start on ESPN tag alone.
