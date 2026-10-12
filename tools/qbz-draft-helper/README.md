# QBZ Draft Helper (Chrome / Edge extension)

A side panel for ESPN fantasy football draft rooms that **recommends** picks using the QBZ draft playbook rules.
It **never clicks Draft or any other ESPN button and never changes anything on ESPN.** You make every pick.
It only runs on `https://fantasy.espn.com/football/draft*`.

> **Honest status:** the rules logic is unit-tested on made-up data, but the extension has **not yet been run
> against the live ESPN draft page**. The page lookups are educated guesses based on the Oct 12, 2026 mock drafts.
> Expect to fix a selector or two in the first mock draft. Diagnostics mode (below) is there to make that quick.

## Install
1. Unzip `qbz-draft-helper.zip` (or download the `tools/qbz-draft-helper/` folder from GitHub).
2. Chrome: open `chrome://extensions`. Edge: open `edge://extensions`.
3. Turn on **Developer mode**.
4. Click **Load unpacked** and pick the unzipped `qbz-draft-helper` folder.
5. Open an ESPN draft room (a mock draft first). The panel appears on the right.

Desktop Chrome/Edge only; it won't work on phones or in the ESPN app.

## What the panel shows
- **On the clock / picks until our turn**, our round, our next overall pick, and our draft slot.
- **★ Recommended pick plus 2 alternates**, each with a reason (rank, ADP, need it fills, news boost, Q-tag flag).
  The recommended row is outlined green on the ESPN page (outline only).
- **Turn pair**: when we pick back to back (slot 1 or 12), it shows pick A and pick B. After A goes in, B is re-planned from the live board.
- **Blocked players** with a reason, such as `IR before R14`, `QB before R7`, `TE before ADP (30)`, `reach >10 (ADP 60)`, `D/ST before R15`, or `news block: ...`.
- **Roster vs targets** (QB 1, RB 6, WR 5, TE 2, D/ST 1, K 1), with what's still needed.
- **Handcuff note** from round 8 on, for our top RB.
- **⚠ Autopick looks ON** warning. ESPN autopick happily drafts IR players, so turn it off.
- A beep and a green flash when we go on the clock. Use 🔔 to turn the sound off, and `_` to minimize the panel.

## The rules (defaults)
- R1–2: best RB or WR only.
- No O / IR / SUSP / PUP before R14. Q is allowed but flagged.
- No QB before R7, unless an elite QB (ADP ≤ 24) has fallen 10+ picks past ADP. Only 1 QB.
- TE only at or past his ADP. Max 2.
- D/ST and K only in R15–16, one each.
- Minimums of 5 RB and 4 WR. When the remaining picks are needed to fill the minimums, only needed positions are recommended, so all 16 spots fill.
- Reach cap: 10 spots past ADP in R1–5 and 20 in R6–11 (the Oct 12 mock lesson), with no cap after that. If nothing legal fits, it recommends the best-ranked player anyway and labels it **REACH**.
- Ranking: ESPN rank, with a news BOOST worth 15 spots.

## Editing the rules
Right-click the extension icon → **Options** (or Details → Extension options):
- **Draft slot**: 0 means auto-detect. Auto-detect works once ESPN shows a "you're on the clock" message, so setting it manually is safer.
- **News overrides**: one per line, `Player Name | BLOCK | note` or `Player Name | BOOST | note`. Use these for the pre-draft news check.
- **Rules JSON**: every number above (`qbFromRound`, `reachCaps`, `targets`, `minimums`, `hardInjuryTags`, and so on).
  Defaults live in `rules.js` → `DEFAULT_CONFIG`.

## Diagnostics
Click **diag** in the panel header. It shows what the parser read: row count, a sample player row, the parsed round, pick, clock,
on-the-clock state, slot, autopick state, and the roster it found. If the row count is 0 or the sample looks wrong, fix
`parser.js` (`findRows` / `parseRowLines`). If the round or pick is wrong, fix `readClock`. If the roster is empty, fix `readRoster`. Then reload the extension.

Known parser limits: ESPN only renders about 33 player rows at a time, so a better legal player further down may be missed.
Use ESPN's position filter tabs before mid-round picks (the panel only sees what's on screen).

## Before the real draft
**Test it in an ESPN mock draft about a week before draft day.** ESPN changes its page layout between seasons, and
any change can break the page lookups. Use diagnostics to confirm rows, round, clock, and roster read correctly, and test from slot 1 or 12 so the turn pair gets exercised.

## Files
- `manifest.json`: Manifest V3, host access limited to the ESPN draft pages.
- `rules.js`: pure rules engine and `DEFAULT_CONFIG` (also used by the tests).
- `parser.js`: read-only DOM parsing with text-based fallbacks.
- `content.js`: the panel, highlighting, MutationObserver plus a 300 ms poll, and the beep.
- `panel.css`, `options.html`, `options.js`.
- `test/test.js`: run `node test/test.js` (synthetic data, 12 tests).
