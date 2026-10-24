---
name: espn.lineup-shots
description: >-
  Use whenever applying a Quantum Blitz ESPN lineup (yes set it or autocommit)
  to capture labeled before/after starter-table screenshots with distinct
  hashes.
---
# espn.lineup-shots

Capture and deliver labeled ESPN lineup before/after screenshots for Quantum Blitz. Use on every `yes, set it` apply and every autocommit apply (including no-ops: still save a current-state after shot).

## Paths
`/workspace/fantasy/quantum-blitz/cards/` — write `before.png` and `after.png`. Log hashes to `audit.log`.

## Steps
1. Open the team lineup page (Week N). Confirm NFL week tab matches the card.
2. **Scroll the full STARTERS table into view** (QB through K visible). Header-only shots are invalid — discard and reshoot.
3. Capture `before.png`. Compute SHA-256 (or file size + short hash). Record in audit: `SHOT_BEFORE week=N hash=...`.
4. Perform the ESPN moves (or confirm no-op). Submit if required.
5. Scroll STARTERS into view again (FLEX and bench top rows visible when a FLEX swap happened). Capture `after.png`.
6. **Verify before ≠ after hashes** when a real move happened. If hashes match after a claimed swap, reshoot after and re-check DOM text for the expected starter names.
7. Deliver to Ken as **two separate messages**:
   - First: `**Before**` + attach `before.png`
   - Second: `**After**` + attach `after.png`
   Never attach only one when both exist. Never reuse a prior week's file without overwriting.

## Validation
- Starters table is readable in both images (not just team header/ads).
- After-shot player names match the apply-target card for changed slots.
- Files under `cards/before.png` and `cards/after.png` are distinct bytes when a move occurred.

## Hard stops
Do not tell Ken “applied” until both shots are saved (no-op may use the same visual for before/after but still send two labeled attachments or one labeled `After (no-op — already matched)` with the current table).
