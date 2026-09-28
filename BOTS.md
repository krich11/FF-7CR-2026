# Order to Blitz and Assistant

Effective now. Ken's words.

The live team is two Grok bots: Blitz and Assistant.
Wire, Sigma, and Recon are retired as standing bots. Do not schedule them. Do not post as them.

This GitHub repo is your filesystem: `krich11/FF-7CR-2026` on `main`.

## Write map

| Who | Live writes |
|---|---|
| Both | pull `main` before you work |
| Assistant | `data/availability.json` · `data/recon/` · packet and brief → `agents/assistant/work/` · waiver board lines in `playbook/CLAIMS.md` when Blitz asks |
| Blitz | `playbook/WAR.md` · `playbook/CLAIMS.md` · `weekly/` · ESPN |
| Consultant | `playbook/CONSULT.md` · `CONSULTANT.md` |

## Read map

- Law: `FILESYSTEM.md`, `BOTS.md`, `agents/<you>/CHARTER.md`
- Blitz reads `playbook/CONSULT.md` before the Tuesday card and before the waiver request in `playbook/CLAIMS.md`.
- Roster: `data/roster.json`
- Injuries: `data/availability.json`
- League dumps: `data/recon/`
- Other clubs: `FUD/`

## Cadence

- Sunday morning: Assistant refreshes availability once.
- After the last Monday box: Assistant writes one combined packet.
- Tuesday before the set-the-week card: Assistant writes one brief (injuries + usage + waiver watch).
- Extra runs only if Blitz asks.

## Rules

- No third standing bot.
- Assistant does not write ESPN.
- Assistant does not send Ken a card.
- Four waiver buckets stay in the brief. Assistant does not publish a separate Ken-facing add/drop board.
- If two files disagree, the live path in FILESYSTEM.md wins.

Pull. Write. Push. Tell Blitz the path.
