# Wire adversarial AAR log

## Week 1 — 2026-09-20 (makeup; Ken immediate run)

Bar: point max · Wire lane only (injury/news → availability.json)

### Signal caught (keep)
- Jacobs EXEMPT / Charbonnet PUP: STATUS_OVERRIDE over ESPN soft tags — correct; no soft-start risk.
- Fri final IR (makeup Sat): Brooks Q→ACTIVE, Meyers Q→ACTIVE; Tua OUT / Rush start on London+Pitts rows; Bowers OUT noted for Tucker.
- Sun lock path: no starter inactive after lock among W1 starters (scorecard availability hits = none).
- Pineiro Melbourne DONE lock correct.

### Misses / late tags
1. **Fri noon availability.refresh failed** (`audit`: catchup=fri-noon-failed) — Sat 8am makeup recovered state changes. Latency hole: Fri IR window almost missed for Brooks/Meyers clears + Tua OUT packaging.
2. **QB ripple timing** — Tua limited Thu (oblique) with Rush 1sts; official OUT Fri ~1:36pm ET (Falcons PR / CBS / NFL.com). Wire had Thu/Fri DTD note 9/10 then OUT confirm 9/12. Gap: should have fired London+Pitts ripple on **limited starter + backup 1sts**, not wait for formal OUT. (Standing LESSONS already wants same-day QB ripple — harden trigger.)

### Wrong wires / source quality
- Fri miss was cadence/execution, not a wrong primary wire. Team IR + Falcons.com/NFL.com were the right SoT once hit.
- No evidence W1 of wrong beat vs official for our roster OUT/ACTIVE.

### availability.json quality holes
- W1 post-lock: states matched reality for starters (ACTIVE) and known ineligibles (EXEMPT/PUP).
- Hole class: refresh failure without immediate retry/alert in Wire lane (depends on Blitz wake under OPS — still must self-detect fail when Blitz pings AV/W8).

### Method corrections (Wire)
- On any AV refresh fail → immediate retry once; if still fail, Blitz shorthand `AV FAIL` (no silent skip).
- QB ripple trigger = material change: limited/OUT **or** backup taking 1sts — update pass-catcher rows + short Blitz ping same day.
- Keep official > ESPN soft tags (already working).

### Consequential escalate?
- Process holes only; no standing false signal; no Ken action needed this hour (W2 already live). Count: **2 consequential process** (Fri refresh fail; QB-ripple trigger lag).
