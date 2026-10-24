# vorp_lite — methodology stub (paper only)

**Status:** methodology ready · paper track · no live §7 / ESPN  
**Ledger:** `results/sigma/research-ledger.json` → `vorp_lite`  
**Appendix:** `results/sigma/week-{N}-vorp.md`

## Definition
**Intra-roster** replace value only — never league-wide charts. For each started skill/FLEX slot:

```
vorp_lite(player) = start_score(player) - start_score(best_eligible_bench_replacement)
```

Makes CARD DIFF about *our* next-best option, not fantasy Twitter ranks.

## Inputs
- Current `projections.json` start_scores (or adj_form when live form exists)
- Roster eligibility + availability (OUT/PUP/IR/EXEMPT/BYE → 0, ineligible as replacement)
- Locked slots / already-played constraints from SPEC week clock

## Computation (v1 stub)
1. Build legal replacement pool per slot (RB/WR/TE/FLEX rules).
2. Compute vorp_lite for each SPEC starter.
3. Paper alternative: if a bench player’s start_score > starter’s and vorp_lite(starter) < threshold (start **1.5 PPR**), paper-flip that slot.
4. Stud protection: do not paper-sit Achane/London-class solely on vorp_lite < 1.5 unless availability/role broke.

## How we score Δ vs SPEC
```
delta = actual_ppr(vorp_paper_card) - actual_ppr(SPEC_card)
```
FLEX-first; count RB2/WR2 only when flip clears stud gate.

## What counts as a flip
≥1 slot where vorp_lite paper card ≠ SPEC. Win if delta > 0.

## Packet section (optional)
Table: Slot | Starter | Best bench | vorp_lite | Paper flip? — feeds CARD DIFF.
