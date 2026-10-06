# opp_eff_decomp — methodology stub (paper only)

**Status:** methodology ready · paper track · no live §7 / ESPN  
**Ledger:** `results/sigma/research-ledger.json` → `opp_eff_decomp`  
**Appendix:** `results/sigma/week-{N}-opp-eff.md`

## Definition
Split skill-player fantasy production into **opportunity** (share of team touches/targets/routes/snaps) vs **efficiency** (PPR per opportunity). Flags:
- **Buy:** high opportunity, muted PPR (efficiency cold)
- **Fade / luck:** low opportunity, spiked PPR (efficiency hot)

Complements live `usage.json` / `role_mult` — this track is for CARD DIFF / FLEX paper ranking, not auto `role_mult` edits until promoted.

## Inputs (required — skip if missing; do not invent)
- Snaps %, targets, carries (and routes if available) from box / public charting
- Team pass/rush attempts for share denominators
- Actual PPR and our `adj`
- Assumed role from projections / prior `usage.json` when present

## Computation (v1 stub)
```
opp_share = f(targets, carries, routes, snaps)   # document weights per position
ppr_per_opp = actual_ppr / max(opportunities, 1)
opp_z = (opp_share - expected_share) / sigma_share     # expected from role assumptions
eff_z = (ppr_per_opp - expected_ppe) / sigma_ppe
# paper bump for next week (not live form):
paper_add = clamp(0.5 * opp_z - 0.25 * eff_z, ±2.0)  # reward opportunity; discount hot efficiency
```
Missing routes → use targets+carries+snaps only and note degraded mode.

## How we score Δ vs SPEC
Paper FLEX (and marginal WR2/RB2) ranking using `adj + paper_add` vs SPEC `start_score`.  
Monday: `delta = actual(paper picks) - actual(SPEC picks)` on allowed slots only.

## What counts as a flip
Paper start/sit differs from SPEC on an allowed skill slot. Win if delta > 0.

## Packet section (optional)
Buy/fade flags for rostered skill players; any FLEX paper flip; weekly Δ + ledger.
