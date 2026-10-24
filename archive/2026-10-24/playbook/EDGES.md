# Shadow edges — Quantum Blitz

**Rule:** SPEC §7 optimizer is live. These three signals are **paper-only** until Ken promotes one midseason.

## Signals

| id | Name | When recorded | What it would change |
|----|------|---------------|----------------------|
| `vegas_flex` | Vegas / implied team total | Card post (Tue/Fri) | FLEX only: slight bump toward higher implied team total / game total |
| `share_trend` | Midweek target/carry share trend | Fri tweak | Skill players: bump if share rising vs season baseline |
| `dst_k_script` | Correlated DST/K environment | When streaming DST/K | Prefer DST/K in games with script/total fit |

## Files

- `edges/shadow/week-{N}-preds.json` — predictions before games (who shadow would start vs SPEC)
- `edges/shadow/week-{N}-score.json` — after Monday: actual PPR if we had followed each signal
- `edges/shadow/ledger.json` — cumulative regret / wins vs SPEC

## Scoring (Monday)

For each signal, only compare slots it was allowed to touch (FLEX for vegas; skill for share; DST/K for script).

```
delta_i = actual_ppr(shadow_pick) - actual_ppr(spec_pick)
```

Cumulative `sum(delta)` and hit rate. Midseason review (~Week 8–9): if one signal is clearly ahead on FLEX/stream decisions **and** sample ≥ 6 decided flips, offer to promote into SPEC. Do not auto-switch.

## Hard stops

- Never change ESPN lineup from shadow alone
- Skip a signal if Vegas/share data missing — do not invent
- Week 1: record preds; form loops empty; score after Mon box scores
