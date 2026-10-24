---
name: shadow.edges
description: >-
  Use to record or score Quantum Blitz shadow-edge predictions (Vegas FLEX,
  share trend, DST/K script) without changing the live SPEC optimizer.
---
# shadow.edges

Paper-track three optional Quantum Blitz signals without changing the live SPEC optimizer or ESPN lineup.

## Paths
`/workspace/fantasy/quantum-blitz/` — `EDGES.md`, `edges/shadow/`, `preferences.json` (`shadow_edges`).

## Signals
1. `vegas_flex` — Vegas total / implied team total prior on **FLEX only**
2. `share_trend` — midweek target/carry (or snap) share vs baseline
3. `dst_k_script` — DST/K correlation with game environment when streaming

## When
- **Predict:** at lineup.set / lineup.tweak card post — write `edges/shadow/week-{N}-preds.json` (who shadow would start vs SPEC). Skip a signal if data missing; never invent.
- **Score:** on week.review Monday — write `week-{N}-score.json`, update `ledger.json` (`delta = shadow_actual − spec_actual` on touched slots only).

## Midseason
From Week 8+, if a signal has ≥6 decided flips and clear positive cum_delta, **offer** Ken promotion into SPEC. Never auto-switch.

## Hard stops
Does not write ESPN. Does not change live card assignments. Week 1: `share_trend` is N/A until games exist.
