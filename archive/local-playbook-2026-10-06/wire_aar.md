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


### Shipped to core (2026-09-20)
- WIRE.md: QB ripple earliest-signal (limited|1sts|OUT); AV fail→retry once then `AV FAIL`
- Agent core prompt/description updated same

## Week 2 — 2026-09-22 (Tue self-cron)

Bar: point max · Wire lane only (injury/news → availability.json) · Prior NFL week = W2

### Signal caught (keep)
- Jacobs EXEMPT / Charbonnet PUP: STATUS_OVERRIDE held all week over ESPN DTD/O — correct.
- Pittman foot: Sat PR OUT (SteelersPR/Burt/Schefter) → Sun steelers.com inactives confirm — early, right SoT.
- Pineiro illness Q Fri → beat expected (Maiocco) → official ACTIVE 49ers.com inactives; STATUS_OVERRIDE over ESPN Q — correct.
- Sun context notes: Tua inactive/Rush start on London+Pitts; Etienne Kamara-active; Shaheed Olave-active; Bowers inactive W2 on Tucker row — verified vs Falcons/Saints/Raiders inactives + beat.
- Goedert: Sun QTR knee (Inquirer/beat audit) → Mon MCL few weeks (Schefter/Rapoport) → SoT OUT over ESPN D at Mon 8:15pm CT AV.
- Dart MNF L knee: ESPN Q / Winston in; Ken said OUT — Wire holds Q until official OUT/IR; qb_ripple=none (no NYG pass-catchers on roster) — correct posture Mon AV.
- Self-routines paused; Blitz owns AV/W8; Mon 8:15pm CT AV Blitz-only — matched OPS. No AV FAIL events W2 (W1 fail→retry not stress-tested).

### Misses / late tags
1. **Brooks groin (Sun exit → Mon coach)** — Left W2@ATL early (groin re-aggro; QTR then out). Canales Mon: testing / gathering info; Pelissero week-to-week (NBC/PanthersWire). Mon 8:15pm CT AV updated Dart+Goedert only; Brooks row still ACTIVE with Sun AM “no injury designation” news (`as_of` 2026-09-20T08:19 PT). ESPN roster tag already DOUBTFUL. Standing stale/false ACTIVE signal through AAR write. (Blitz waiver drop Brooks→Kyler pending same evening — still Wire SoT hole while on roster.)

### Wrong wires / source quality
- No wrong primary wire for caught OUTs (Steelers PR/inactives, 49ers.com, Schefter/Rapoport for Goedert MCL).
- Brooks miss class = **incomplete Mon AV roster scan under Blitz-URGENT single-player focus**, not a bad beat vs official.

### availability.json quality holes
- **Brooks**: state ACTIVE + stale Sun AM news vs real groin exit + Mon week-to-week — hole.
- **lock_state drift**: all 17 rows still UNLOCKED after W2 kickoffs/locks (post-game should be DONE/LOCKED per model) — hygiene hole, not a false injury signal.
- Dart overnight (post Mon AV): Garafolo/Rapoport “believed sprained MCL,” MRI Tue — freshness for next AV; holding Q still correct until official designation.
- Overrides healthy: Jacobs EXEMPT, Charbonnet PUP, Pineiro ACTIVE-over-Q, Goedert OUT-over-D.

### Method corrections (Wire)
- Blitz-URGENT / named-player AV must still **full-roster scan** for same-day in-game exits + coach Mon updates (bench included) before write.
- Post-lock / post-game refresh: set `lock_state` DONE for completed kickoffs (reduce UNLOCKED drift).
- Keep: official > ESPN soft; hold Q until official OUT/IR when Ken claims OUT early; qb_ripple only when our pass-catchers exist.

### Consequential escalate?
- **1 consequential:** Brooks groin miss / standing stale ACTIVE after Mon AV (process hole under URGENT path). No standing false OUT. No Ken action this hour.
- Escalate Blitz: yes (shorthand). Prefer AAR-only charter; no WIRE.md/LESSONS.md edit this run — parent may harden “URGENT AV = full roster scan” if desired.

### Shipped to core (2026-09-22)
- WIRE.md: URGENT/named-player AV = full-roster scan (bench in-game exits + Mon coach); post-game lock_state DONE
