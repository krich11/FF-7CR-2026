# matchup_adj_resid — methodology stub (paper only)

**Status:** methodology ready · paper track · no live §7 / ESPN  
**Ledger:** `results/sigma/research-ledger.json` → `matchup_adj_resid`  
**Appendix:** `results/sigma/week-{N}-matchup-resid.md`

## Definition
Decompose each rostered skill player's weekly residual (`actual_ppr − adj`) into:
1. **Player component** — residual after removing expected defense-vs-position effect
2. **Matchup component** — how that week's opponent typically allows PPR at the player's position vs league average

Goal: avoid over-punishing form for a tough box or over-crediting a soft-matchup boom.

## Inputs (required — skip track if missing; do not invent)
- Our going-in `adj` and actual PPR (results / box scores)
- Opponent for that game (schedule / ESPN)
- Public defense-vs-position ranks or fantasy points allowed at RB/WR/TE/QB (cite source + as_of)
- Optional: implied team totals (for context only; not a substitute for DVP)

## Computation (v1 stub)
```
raw_resid = actual_ppr - adj
dvp_delta = opponent_fp_allowed_at_pos - league_avg_fp_allowed_at_pos
# scale: shrink dvp_delta into PPR-ish units with a small coefficient (document weekly)
matchup_component = k * dvp_delta   # k chosen + logged; start conservative (e.g. 0.15–0.25)
player_component = raw_resid - matchup_component
matchup_adj_form_add = clamp(0.35 * player_component, ±3.0)  # paper only — does not write live form.json until promoted
```

## How we score Δ vs SPEC
Pre-card (Tue/Fri): build a **paper card** that applies `matchup_adj_form_add` only to FLEX and the marginal RB2/WR2 (same stud-protection as SPEC §7.3 — never sit Achane/London-class on matchup alone).

Monday:
```
delta = actual_ppr(paper_starters) - actual_ppr(SPEC_starters)
```
Only count slots the track was allowed to touch. Cumulate in research-ledger.

## What counts as a flip
A **flip** = paper card differs from SPEC in ≥1 allowed slot (FLEX / marginal RB2/WR2).  
`n_wins` += 1 if `delta > 0` on a flip week. No flip → no win/loss counted (agree with SPEC).

## Packet section (optional)
When data exists: 3–6 lines — top player_components, any paper FLEX flip, Δ last week, cum_delta / flips.
