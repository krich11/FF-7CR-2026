# standings_leverage — methodology stub (paper only)

**Status:** methodology ready · **dormant until Week 6** · paper track · FLEX/DST only  
**Ledger:** `results/sigma/research-ledger.json` → `standings_leverage`  
**Appendix:** `results/sigma/week-{N}-standings-lev.md`

## Definition
After Week 6, if Quantum Blitz is in a must-win posture (≥2 games back or SPEC standings mode says must-win), paper-reweight FLEX and DST toward **ceiling** (and slightly away from floor) vs live default 70/20/10. Aligns with SPEC standings-mode intent but isolates FLEX/DST so we can measure regret before touching live weights.

## Inputs
- `standings.json` / ESPN record (via Blitz files)
- Week number ≥ 6
- Candidate FLEX and DST options on roster with floor/ceiling from projections
- Live SPEC card for comparison

## Computation (v1 stub)
If week < 6 or not must-win / ≥2 back: **dormant** (no preds, no flips).

If active:
```
paper_flex_score = 0.55*adj + 0.15*floor + 0.30*ceiling - risk
paper_dst_score  = same weights
```
Pick FLEX/DST maximizing paper score; leave QB/RB/WR/TE/K on SPEC unless separately flipped by another track (this track does not touch those slots).

## How we score Δ vs SPEC
```
delta = actual(FLEX_paper)+actual(DST_paper) - actual(FLEX_SPEC)-actual(DST_SPEC)
```
Only FLEX+DST slots.

## What counts as a flip
Paper FLEX and/or DST ≠ SPEC. Win if combined delta > 0.

## Packet section (optional, Week 6+)
Standings posture, paper weights, FLEX/DST paper picks, Δ + cum ledger. Omit entirely before Week 6.
