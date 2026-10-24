# SAMPLE/MOCK — Week 0 Scorecard Deep Fill (§§3–6) — packet v2

> **SAMPLE/MOCK ONLY.** Numbers from `results/sigma/mock-week-0-boxscores.json` only. Not a live Monday scorecard. Blitz owns Ken email.

**DATA_QUALITY:** file team_score **128.4** vs starter-row sum **121.6** (gap **6.8**) — flag, do not invent.

**Context (file-level):** Record 1–0 · team_score 128.4 · proj 119.2 · vs Example FC 121.1 · Δ vs proj +9.2

**Bench regret:** (a) SCORECARD **10.1** Meyers−Pitts · (b) same-pos **8.8** Meyers−Wilson

---

## 3. Deep stats — residuals & shrinkage

| Player | Adj in | Actual | Residual | form_add next | Games in window |
|--------|--------|--------|----------|---------------|-----------------|
| Jaxson Dart | 18.2 | 22.4 | +4.20 | +1.47 | 1 |
| De'Von Achane | 17.5 | 19.1 | +1.60 | +0.56 | 1 |
| Travis Etienne Jr. | 14.3 | 11.2 | −3.10 | −1.08 | 1 |
| Drake London | 15.0 | 16.8 | +1.80 | +0.63 | 1 |
| Garrett Wilson | 13.9 | 9.4 | −4.50 | **−2.32** | 1 |
| Kyle Pitts Sr. | 10.0 | 8.1 | −1.90 | −0.66 | 1 |
| Dallas Goedert | 10.4 | 14.6 | +4.20 | +1.47 | 1 |
| Steelers D/ST | 7.1 | 12.0 | +4.90 | +1.72 | 1 |
| Eddy Pineiro | 7.9 | 8.0 | +0.10 | +0.03 | 1 |
| Jakobi Meyers | 6.2 | 18.2 | +12.00 | **+3.00** | 1 |
| Michael Pittman Jr. | 5.0 | 7.1 | +2.10 | +0.73 | 1 |
| Jonathon Brooks | 6.0 | 6.0 | 0.00 | 0.00 | 1 |
| Tre Tucker | 8.0 | 5.2 | −2.80 | −0.98 | 1 |
| Rashid Shaheed | 8.3 | 4.1 | −4.20 | −1.47 | 1 |
| Josh Jacobs | 0.0 | 0.0 | — | EXEMPT | 0 |
| Zach Charbonnet | 0.0 | 0.0 | — | PUP | 0 |

**Bench-vs-starter boost fired?** Yes — Meyers +1.00 (capped at +3.00), Wilson −0.75 → form_add −2.32.  
**Game-script shrink applied?** No — mock has no script fields; skipped.  
**Form formula:** `form_add = round(clamp(0.35 × residual, ±3), 2)`.

---

## 4. Usage (leading indicator)

| Player | Assumed snap% / role | Actual snap% | targets/carries | usage_gap | role_mult next |
|--------|----------------------|--------------|-----------------|-----------|----------------|
| Jakobi Meyers | 0.55 | 0.88 | 11 / 0 | **+0.33** | **1.15** |
| Michael Pittman Jr. | 0.65 | 0.70 | 6 / 0 | +0.05 | 1.025 |
| Jonathon Brooks | 0.40 | 0.35 | 1 / 8 | −0.05 | 0.975 |
| Tre Tucker | 0.55 | 0.60 | 3 / 0 | +0.05 | 1.025 |
| Rashid Shaheed | 0.50 | 0.45 | 2 / 0 | −0.05 | 0.975 |

**Flag:** Meyers = high points **and** high usage → **buy**, not luck.

---

## 5. Projection sources

| Source | MAE this week (rostered) | Weight next week |
|--------|--------------------------|------------------|
| ESPN | 3.8 | 0.467 |
| FantasyPros | 3.2 | 0.533 |

Jacobs/Charbonnet already zeroed (EXEMPT/PUP).

---

## 6. Shadow edges (paper only — not live)

| Signal | SPEC pick | Shadow pick | Δ actual PPR | Cum Δ | Flips |
|--------|-----------|-------------|--------------|-------|-------|
| vegas_flex | Dallas Goedert | Dallas Goedert | 0.0 | 0.0 | 0 |
| share_trend | — | N/A | — | 0.0 | 0 |
| dst_k_script | Steelers D/ST | Steelers D/ST | 0.0 | 0.0 | 0 |

**This mock: 0 flips.** Promotion watch Week 8 / ≥6 flips / Ken approval.

---

*SAMPLE/MOCK · Sigma packet v2 · 2026-09-05 PT*
