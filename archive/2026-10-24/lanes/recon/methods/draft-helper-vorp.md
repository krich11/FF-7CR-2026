# Draft helper — corrected hybrid VORP (fade-only hype tax)

**Lane:** draft-helper methodology only. Does **not** feed WAIVER WATCH, competitor briefs, claim boards, or Ken-facing waiver recs.
**Locked decision (2026-09-05, Ken → Recon → Blitz):** primary pick-sort = corrected hybrid; ESPN PPR ranks stay visible side-by-side as market/hedge disagreement column.
**Author:** Recon (from §5 critique of raw `VORP − 0.35 × max(0, hype_tax)`).

---

## Problems with the prior hybrid

\[
\text{hybrid}_{\text{old}} = \text{VORP} - 0.35 \cdot \max(0,\ \underbrace{r^{\text{our}} - r^{\text{espn}}}_{\Delta r})
\]

- `VORP` is in **season fantasy points**; \(\Delta r\) is in **rank slots** → unit mismatch.
- Flat \(0.35\) is an uncalibrated points-per-rank guess; over-penalizes late rounds, under-penalizes early.
- Overall-rank \(\Delta r\) ignores position cliffs (QB/TE/DST/K).
- Injury-driven ESPN rank drops can **double-count** risk already in `proj`.

---

## §5 preferred formulation (points-mapped, within-position)

Keep **fade-only** (no value boost). Map tax into points via local VORP–rank slope at the player's position.

\[
\begin{aligned}
\text{VORP}_i &= p_i - p^{\text{repl}}_{\pi(i)} \\
\Delta r^{\pi}_i &= \max\bigl(0,\ r^{\text{our}}_{\pi(i)} - r^{\text{espn}}_{\pi(i)}\bigr) \\
\hat s_{\pi}(r) &= \operatorname{median}_{j:\pi(j)=\pi}\bigl(\text{VORP}_{(r)}-\text{VORP}_{(r+1)}\bigr)
\quad\text{(points per rank at position }\pi\text{)} \\
\tau_i &= \Delta r^{\pi}_i \cdot \hat s_{\pi}\!\left(r^{\text{our}}_{\pi(i)}\right) \\
\text{hybrid}_i &= \text{VORP}_i - \alpha \cdot \tau_i
\end{aligned}
\]

**Symbols**
- \(p_i\): season projected fantasy points (league scoring, e.g. PPR)
- \(\pi(i)\): position of player \(i\)
- \(p^{\text{repl}}_{\pi}\): replacement baseline at \(\pi\) (league-specific: roughly `team_count × starters_at_pos` + flex allocation for RB/WR/TE + `team_count` bench layer)
- \(r^{\text{our}}_{\pi}\), \(r^{\text{espn}}_{\pi}\): **within-position** ranks (1 = best)
- \(\alpha \in (0,1]\): fraction of implied reach cost to charge (start **\(\alpha = 0.5\)**)
- Cap: \(\tau_i \le \tau_{\max}\) (suggested **15–25** season points) so late-round rank chaos cannot dominate

**Properties**
- Higher is always better
- Only positive hype (market ahead of us) is penalized
- Negative tax (sleeps) does **not** get a bonus — use a separate value/ADP metric for that
- \(\tau_i\) is in **points**, so subtraction is dimensionally coherent

---

## Alternate (scale-free multiplicative fade)

\[
\text{hybrid}_i = \text{VORP}_i \cdot \exp\!\bigl(-\beta \cdot \max(0,\ z(\Delta r_i))\bigr)
\]

- \(z(\Delta r)\) = z-score of positive rank-tax within the drafted pool (or within position)
- Set \(\beta\) so **+1σ overhype ≈ 5–10% VORP haircut**

Prefer the slope form when within-position VORP curves are stable; use multiplicative when sample sizes are thin.

---

## Operational knobs

| Knob | Guidance |
|------|----------|
| Primary sort | `hybrid` (corrected) |
| Hedge column | ESPN overall (or PPR) rank — disagreement display only |
| K / DST | \(\alpha = 0\) or omit tax (ESPN ranks noisy) |
| QB / TE | shrink \(\alpha\) (e.g. 0.25–0.35); prefer position ranks |
| Injury news | freeze market rank for tax at a pre-news snapshot, or ensure `proj` cut owns the risk |
| Ownership amplifiers | optional; fold into \(g(\Delta r,\%own)\) rather than multiplying raw rank tax |
| Early vs late | optional \(\alpha(r)\) larger early; hard \(\tau_{\max}\) is the minimum late-round guardrail |

---

## What this is not

- Not a Ken-facing claim board
- Not WAIVER WATCH competition intel
- Not a substitute for live ESPN league scout dumps under `recon/`

## Status

Methodology locked 2026-09-05. **Implemented** in `ff-helper` / forks: `draft_metric.annotate_hybrid_scores`, default `player_metric=hybrid`, ESPN ranks remain hedge column.
