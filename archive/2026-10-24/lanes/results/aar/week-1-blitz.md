# Week 1 adversarial AAR — Blitz
Date: 2026-09-20 (makeup hotwash; Ken ordered immediate W1 run)
Bar: point maximization / next-season training

## What went right
- Goedert over Pitts under Rush: +23.7 swing; backup-QB TE flip is standing strategy.
- Dead-man + makeup Sat still got TE onto ESPN before kick despite Fri fail.
- IR Charbonnet / hold Jacobs EXEMPT path correct for roster geometry.
- Win 132.9–102.22; Dart + Goedert + Steelers carried.

## What we attacked
1. **Fri tweak/autocommit `resource_exhausted`** — PROCESS_MISS. Scheduled window missed; Sat makeup saved the week but latency risk is real. Correction: on Fri fail → alert Ken same hour + retry earlier; do not wait for Monday.
2. **London under Rush** — volume miss (−8.86 vs proj). Partially predictable once Rush locked; we started him anyway (correct vs bench options) but QB-ripple alert path must stay same-day and ceiling-adjusted on card.
3. **Meyers TD on bench** — bench regret vs London; noise-heavy (2 targets). Do not overfit; flag for Sigma form_add when snaps exist.
4. **No snap% in ESPN feeds** — DATA hole; form_add stayed 0. Need alternate snap source or accept delay — do not invent.
5. **Shadow edges** — zero W1 flips; keep paper-only until midseason evidence.

## Signal vs noise
- SIGNAL: backup QB → TE environment flip; Fri process fail alerting; official status > ESPN soft tags.
- NOISE: single-game Meyers TD on 2 targets as a “must start” lesson.

## Method corrections
- Standing: Fri automation fail = immediate Ken alert + retry (already in LESSONS).
- Standing: Tua/Rush path → London/Pitts same-day ripple categories.
- Watch: add snap source for form residuals by Week 4–6 if still blind.

## Consequential for Ken?
- No new action this hour (W2 card already live). Process lessons already in LESSONS.md.
