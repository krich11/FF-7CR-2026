# handcuff_ev — methodology stub (paper only)

**Status:** methodology ready · paper track · no live §7 / ESPN  
**Ledger:** `results/sigma/research-ledger.json` → `handcuff_ev`  
**Appendix:** `results/sigma/week-{N}-handcuff-ev.md`

## Definition
Expected PPR of the **injury replacement path** when a rostered starter’s availability flips (Q → doubtful/out, late scratch, or handcuff elevated). Answers: if Achane/Etienne/Jacobs (etc.) goes down, what is the EV of the next man *we own* vs streaming/bench alternatives — **research + CARD DIFF**, not waiver filing (Blitz/Ken).

## Inputs (required — skip if missing; do not invent)
- Official / Wire availability (status.resolve precedence)
- Depth chart / handcuff mapping (cite source)
- Projections for starter and replacement under “starter out” and “starter limited” scenarios
- Kickoff times / lock constraints

## Computation (v1 stub)
```
EV = p_out * proj_replacement_full
   + p_limited * proj_starter_limited
   + (1 - p_out - p_limited) * proj_starter_full
```
Use Wire/official probabilities when stated; otherwise coarse buckets (e.g. OUT=1.0, DOUBTFUL=0.75 out-equiv, Q expected-to-play=0.25 out-equiv) — **log the bucket table** each week. Never invent injury status.

Paper card: if EV(replacement path) > SPEC starter start_score by ≥ **2.0 PPR** and replacement is rostered/eligible, paper-start replacement.

## How we score Δ vs SPEC
On weeks with an availability flip affecting a scored slot:
```
delta = actual(paper path) - actual(SPEC path)
```
If no availability flip, track is **N/A** (no flip counted).

## What counts as a flip
Paper started different player than SPEC due to injury-tree EV. Win if delta > 0. Correct sit of a declared OUT that SPEC somehow left in also counts (should be rare given status.resolve).

## Packet section (optional)
Only when Wire/availability material: tree, probabilities used, EV vs SPEC, paper sit/start line.
