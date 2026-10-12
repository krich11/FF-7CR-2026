# QBZ Draft Helper: iPhone Safari bookmarklet

It's one bookmark, with no app and no hosting. The whole helper (rules, page reader and panel) is inside the bookmark itself.
It never downloads code from anywhere. It is **recommend-only**: it never taps Draft or anything else on ESPN.

> **Honest status:** it is tested only in a simulated page on a computer. It has **not** been run on the live ESPN draft
> page or on an iPhone. ESPN's mobile draft layout may differ from the desktop one the page reader was built from.
> **Test it in a mock draft first with the panel expanded (▴) so the Diagnostics section is visible.**

## One-time setup on iPhone
1. **Get the text.** On the phone, open the GitHub file `tools/qbz-draft-helper/bookmarklet/bookmarklet.txt` in repo
   krich11/FF-7CR-2026 and tap **Raw**. Select all and copy it. It's about 19,000 characters and starts with `javascript:`.
   (Alternatively, paste it into a Notes note from a computer and copy it from Notes on the phone.)
2. In Safari, **bookmark any page**: tap Share, then **Add Bookmark**, then Save.
3. Open Bookmarks (the book icon), tap **Edit**, and tap the new bookmark.
4. Rename it **QBZ Draft**. Clear the address field, **paste** the copied text, and tap Done.

## Using it
1. Open the ESPN draft room **in Safari, not the ESPN app**. If Safari bounces you to the app, long-press the link and choose Open in Safari,
   or type the `fantasy.espn.com` address directly.
2. Tap the address bar, type **QBZ**, and tap the **QBZ Draft** bookmark in the suggestions. You can also open it from Bookmarks.
3. A sheet appears at the bottom of the screen. **If the page reloads, tap the bookmark again.** Tapping it while the sheet is showing hides it, and tapping it again brings it back.

## The sheet
- **Collapsed view:** the top pick (★) with its reason, 2 alternates, picks until our turn, and at the turn the planned **pair A → B** (B is re-planned after A goes in).
  The recommended row on ESPN's page gets a green outline.
- **▴ expands it** to show roster counts against targets, blocked players with reasons (such as `IR before R14`, `QB before R7`, or `reach >10`) and diagnostics.
- **– shrinks it to a small pill** in the bottom-right corner, which still shows "ON CLOCK: <pick>". Tap the pill to bring the sheet back.
  The page also gets matching bottom padding so you can scroll ESPN's list and Draft buttons out from under the sheet.
- **On our turn the whole screen flashes green.** Beeps are unreliable on iPhone, so it doesn't use them.
- **⚠ banners:** Autopick looks ON, or the draft slot is unknown.

## Settings (⚙)
Settings are saved in Safari's storage for fantasy.espn.com on this phone only:
- **Draft slot.** 0 means auto-detect, which only works once you've been on the clock. Setting it by hand is safer.
- **News overrides.** One per line: `Player Name | BLOCK | note` or `Player Name | BOOST | note`.
- **Rule overrides (JSON).** Only the keys you want to change, e.g. `{"qbFromRound": 8}`. Tap "Default rules" to see every key.
  **Reset all** clears the slot, the overrides and the rules.

## If it doesn't work
- **Nothing happens when you tap the bookmark.** Make sure the address starts with `javascript:`. Safari sometimes drops a long paste, so re-copy from Raw.
- **The sheet says no players were read, or the rows count is 0.** ESPN's mobile layout differs. Send a screenshot of the Diagnostics section so the page reader can be fixed.
- **The round or pick looks wrong.** Set the slot by hand in ⚙ and check the "clock" line in Diagnostics.

## Rebuilding (for maintainers)
`npm i terser jsdom`, then `node bookmarklet/build.js`. That writes `bookmarklet.txt` and `qbz-bookmarklet.min.js` from `rules.js`, `parser.js` and `bookmarklet/panel.js`.
Tests: `node test/test.js` and `node test/bookmarklet.test.js`.
