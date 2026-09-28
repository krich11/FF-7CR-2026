# Order to Blitz, Wire, Sigma, Recon

Effective now. Ken's words.

This GitHub repo is your filesystem: `krich11/FF-7CR-2026` on `main`.

Stop writing the operating files on your local git. Clone or pull this repo. Commit your lane here. If it is not on `main`, the rest of us do not have it.

## You may keep local

- ESPN cookies / SWID / espn_s2 (never commit; path `secrets/` is gitignored)
- Virtualenvs, raw API captures, screenshots

## You may not keep local as source of truth

- availability.json
- roster / standings / waiver dumps
- claim boards
- WAR.md
- opponent cards / FUD inputs
- weekly packets and AARs
- your CHARTER / PROFILE / ROUTINES after you change them (open a note to Blitz; Blitz writes CHARTER)

## Write map

| Bot | Live writes |
|---|---|
| All | pull `main` before you work |
| Wire | `data/availability.json` · digest → `agents/wire/work/digest-YYYY-MM-DD.md` · AAR → `agents/wire/work/aar/` |
| Sigma | packet → `agents/sigma/work/week-N-packet.md` · boards also land in `playbook/CLAIMS.md` · snaps/AAR → `agents/sigma/work/` |
| Recon | dumps → `data/recon/` · week brief → `agents/recon/work/week-N.md` · AAR → `agents/recon/work/aar/` · facts into `FUD/` only as roster diffs, not a second board |
| Blitz | `playbook/WAR.md` · `playbook/CLAIMS.md` · `weekly/` · ESPN |

## Read map

- Law: `FILESYSTEM.md`, `playbook/`, `agents/<you>/CHARTER.md`
- Our roster: `data/roster.json`
- Injuries: `data/availability.json`
- League: `data/recon/league_rosters.json` + `league_index.json`
- Other 11 analysis: `FUD/`
- This week's ticket: `playbook/CLAIMS.md`

## GitHub issues

Every comment starts with the speaker on its own line:

`**Blitz**` / `**Wire**` / `**Sigma**` / `**Recon**` / `**Ken**` / `**Consultant**`

GitHub shows every account as `krich11`. The first line is who is talking. The Consultant is the outside operator on this repo, not a fifth bot.

If you close an issue, comment first:

`**Speaker**`

`Closing. <one-line reason>.`

Then close it. A silent close is anonymous.

## Rules that do not move

- No fifth bot.
- No QBZ claim board from Recon. Four WW buckets only.
- No start/sit from Wire.
- No ESPN writes from Wire / Sigma / Recon.
- Votes: Blitz DMs you. Thumbs in DM. Slip goes in `weekly/votes/`. No reasoning in the room.
- If two files disagree, the **live path** in FILESYSTEM.md wins.

Pull. Write. Push. Then tell Blitz the path, not a paste of the whole file.
