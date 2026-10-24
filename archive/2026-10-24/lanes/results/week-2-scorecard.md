# Quantum Blitz — Week 2 Scorecard

**Record:** 1-1 · **Week score:** 83.1 PPR (proj 109.52, Δ **-26.42**)  
**Vs opponent:** Charlie Don't Surf (CDS) · 104.02 · **L**  
**Card confidence going in:** Medium

---

## 1. Easy read — what happened

| Slot | Started | Proj | Actual | Δ | Note |
|------|---------|------|--------|---|------|
| QB | Jaxson Dart | 18.23 | 0.8 | -17.43 | L knee early MNF → Winston; 12% snaps |
| RB | De'Von Achane | 17.12 | 12.3 | -4.82 | Usage OK (76% / 6 tgt); efficiency soft |
| RB | Travis Etienne Jr. | 11.00 | 7.1 | -3.90 | Kamara-active haircut; 54% snaps |
| WR | Drake London | 12.85 | 8.9 | -3.95 | Rush env; 5 tgt — soft again |
| WR | Garrett Wilson | 15.86 | 16.7 | +0.84 | On/above card |
| TE | Dallas Goedert | 11.24 | 1.4 | -9.84 | In-game QTR knee → Mon MCL few weeks |
| FLEX | Tre Tucker | 9.86 | 22.9 | +13.04 | Bowers inactive; 5-119-1 — TE2 premium win |
| DST | Steelers D/ST | 6.34 | 8.0 | +1.66 | Porter OUT script |
| K | Eddy Pineiro | 7.02 | 5.0 | -2.02 | Illness Q→ACTIVE; K_SWAP HOLD correct |
| **Total** | | **109.52** | **83.1** | **-26.42** | Starter sum = team score |

**Bench regret:** best benched FLEX-eligible (Shaheed 6.9) − worst FLEX-eligible starter (Etienne 7.1) = **-0.2** — no ≥5 callout. (Pitts 2.5 vs Goedert 1.4 same-pos only +1.1.)  
**Headline:** Lost 83.1–104.02 — Dart knee + Goedert MCL crushed the card; Tucker FLEX boom (+20.4 vs Pitts) was the process win that couldn’t cover the holes.

---

## 2. Before → after (decision quality)

| Decision | Before (card) | After (actual) | Regret PPR | Keep / rethink |
|----------|---------------|----------------|------------|----------------|
| FLEX | Tucker over Pitts (TE2 premium 0.52 < 1.5) | Tucker 22.9 vs Pitts 2.5 | **+20.4** | **Keep** — premium rule + Bowers inactive paid |
| TE | Goedert over Pitts (Rush default) | Goedert 1.4 vs Pitts 2.5 | **-1.1** | Not predictable pre-lock (ACTIVE); W3 → Pitts |
| K HOLD | Pineiro only-K; Sigma Net EV < +1.0 | Pineiro 5.0 ACTIVE | 0 (correct HOLD) | Keep dead-man stand-down |
| Shadow FLEX | SPEC Tucker / paper Pitts (share_trend) | Pitts −20.4 vs SPEC | paper only | **anti-promote** share_trend |

**Availability hits:** Dart left early MNF (knee); Goedert in-game knee Sun (ACTIVE at lock). Pittman OUT benched as planned. Jacobs EXEMPT / Charbonnet PUP as expected.  
**Process misses:** Mon `WEEK_REVIEW_SKIP` (MNF live) never resumed → scorecard delayed to Tue makeup. Fri dead-man healthy (contrast W1).  
**Ken overrides this week:** none on lineup. Ken-typed waiver: claim Kyler Murray drop Jonathon Brooks (**PENDING** as of Mon night).

---

## 3. Deep stats — residuals & shrinkage

| Player | Adj in | Actual | Residual | form_add next | Games in window |
|--------|--------|--------|----------|---------------|-----------------|
| Jaxson Dart | 18.23 | 0.8 | -17.43 | n/a (deferred) | 2 |
| De'Von Achane | 17.12 | 12.3 | -4.82 | n/a (deferred) | 2 |
| Travis Etienne Jr. | 11.00 | 7.1 | -3.90 | n/a (deferred) | 2 |
| Drake London | 12.85 | 8.9 | -3.95 | n/a (deferred) | 2 |
| Garrett Wilson | 15.86 | 16.7 | +0.84 | n/a (deferred) | 2 |
| Dallas Goedert | 11.24 | 1.4 | -9.84 | n/a (deferred) | 2 |
| Tre Tucker | 9.86 | 22.9 | +13.04 | n/a (deferred) | 2 |
| Steelers D/ST | 6.34 | 8.0 | +1.66 | n/a (deferred) | 2 |
| Eddy Pineiro | 7.02 | 5.0 | -2.02 | n/a (deferred) | 2 |
| Kyle Pitts Sr. | 10.38 | 2.5 | -7.88 | n/a (deferred) | 2 |
| Jakobi Meyers | 8.80 | 3.8 | -5.00 | n/a (deferred) | 2 |
| Jonathon Brooks | 8.65 | 2.1 | -6.55 | n/a (deferred) | 2 |
| Rashid Shaheed | 8.61 | 6.9 | -1.71 | n/a (deferred) | 2 |
| Tyler Allgeier | 6.74 | 3.9 | -2.84 | n/a (deferred) | 2 |
| Michael Pittman Jr. | 0.0 | 0.0 | n/a | 0 (OUT) | 0 |
| Josh Jacobs | 0.0 | 0.0 | n/a | 0 (EXEMPT) | 0 |
| Zach Charbonnet | 0.0 | 0.0 | n/a | 0 (PUP) | 0 |

**Bench-vs-starter boost fired?** No — no ≥5 bench FLEX-eligible over a starter this week.  
**Game-script shrink applied?** n/a this makeup (form loop deferred; injury exits dominate Dart/Goedert residuals — not pure dud shrink).

Form formula reminder: `form_add = clamp(0.35 × residual, ±3)` — **not computed this run** (`form_add_next` left null in `week-2.json`; do not invent).

---

## 4. Usage (leading indicator)

| Player | Assumed snap% / role | Actual snap% | targets/carries | usage_gap | role_mult next |
|--------|----------------------|--------------|-----------------|-----------|----------------|
| Jaxson Dart | QB1 ~100% | 12% (7 snaps) | n/a | n/a | injury exit — sole-QB risk |
| De'Von Achane | RB1 ~70% | 76% | 20 car / 6 tgt | n/a (usage OK) | 1.00 watch |
| Travis Etienne Jr. | RB committee | 54% | 8 car / 2 tgt | n/a | Kamara committee |
| Drake London | WR1 Rush env | 62% | 5 tgt / 1 car | soft volume | backup-QB watch |
| Garrett Wilson | WR1 | 88% | 7 tgt / 5 rec | role intact | 1.00 |
| Dallas Goedert | TE1 | 25% (19 snaps) | 2 tgt | injury exit | MCL few weeks → sit |
| Tre Tucker | WR FLEX / Bowers out | 59% | 7 tgt / 5-119-1 | boom + usage | watch Bowers return |
| Kyle Pitts Sr. | TE2 / Rush | 38% | 3 tgt | low | **W3 TE default** |
| Jakobi Meyers | WR FLEX | 90% | 1 tgt | high snaps / low tgt | luck check |
| Rashid Shaheed | WR bench | 56% | 6 tgt | volume on bench | watch |
| Tyler Allgeier | committee | 64% | 5 car / 2 tgt | snaps OK | committee |
| Jonathon Brooks | committee | 30% | 5 car / 1 tgt | limited | waiver drop pending |

Flag: **Dart / Goedert** = injury truncations (not usage duds). **Achane** = usage OK / points soft. **Meyers** = 90% snaps / 1 target (empty volume). **Snaps:** nflverse/PFR via Sigma (`results/sigma/snaps/week-2.csv`); DST/K/EXEMPT/OUT unmatched by design. `usage_gap` / `role_mult_next` not invented.

---

## 5. Projection sources

| Source | MAE this week (rostered) | Weight next week |
|--------|--------------------------|------------------|
| ESPN | n/a (loop deferred) | hold W1 0.49 |
| FantasyPros | n/a (loop deferred) | hold W1 0.51 |

Sources that projected EXEMPT/PUP/IR/OUT as starters: **zeroed** for Josh Jacobs (EXEMPT), Zach Charbonnet (PUP), Michael Pittman Jr. (OUT) — not in any MAE.

---

## 6. Shadow edges (paper only — not live)

| Signal | SPEC pick | Shadow pick | Δ actual PPR | Cum Δ | Flips |
|--------|-----------|-------------|--------------|-------|-------|
| vegas_flex | n/a (no lines) | skipped | 0.0 | **+3.4** | 1 |
| share_trend | Tre Tucker | Kyle Pitts Sr. | **-20.4** | **-20.4** | 1 |
| dst_k_script | Steelers / Pineiro | same | 0.0 | 0.0 | 0 |

**Promotion watch:** earliest Week 8 · need ≥6 flips · Ken approval required. **share_trend stays paper-only** (lost badly W2).

---

## 7. Cumulative season ledger

| Metric | Value |
|--------|-------|
| Season PPR for / against | 216.0 / 206.24 |
| Avg weekly Δ vs proj | -6.17 ((+14.09 −26.42) / 2) |
| FLEX regret sum | -3.4 (W1 Pittman vs Meyers); W2 FLEX correct (+20.4 keep) |
| Process misses | 2 (W1 Fri resource_exhausted; W2 week.review SKIP→Tue makeup) |
| Shadow leader (cum Δ) | vegas_flex +3.4 (share_trend −20.4) |
| Waiver rank | 5 (ESPN) |

---

## 8. Next week hooks

- **W3 TE:** Goedert OUT MCL (few weeks) → **Pitts** is the TE plan
- **QB depth:** Dart knee Q/OUT path; **Kyler Murray claim PENDING** (drop Brooks) — Ken-typed Mon night; do not invent claim status
- Sole-QB structural risk remains until Murray clears or Dart returns
- Tucker FLEX boom ≠ permanent dogma — re-check Bowers + TE2 premium weekly
- London still soft under Rush; Tua/Penix path into W3+
- Jacobs EXEMPT clock; Charbonnet PUP / IR earliest ~Week 5
- Standings mode weights: **default until Week 6**
- Sigma: form_add / source MAE / role_mult still deferred — do not invent

---

*Generated by Blitz · Week 2 week.review MAKEUP · SPEC live · shadow paper-only · 2026-09-22 07:56 PT · Ken times CT (2026-09-22 09:56 AM CT)*
