# PLAYBOOK.md: how Quantum Blitz runs (Ken approved, Sat Oct 24 2026)

This is the one rulebook for Blitz and Assistant. It wins over every older file. League facts live in RULES.md, season plans in STRATEGY.md, and trade write-ups under trades/. ESPN league 1776545061, team 13, season 2026. All times are Central (CT).

## Roles
Blitz sets the lineup, handles transactions, makes every ESPN write, and writes the cards Ken sees. Assistant gathers the facts: availability, projections, usage, and league scouting. Assistant never writes to ESPN and never sends Ken a lineup card.

## Hard gates
- No waiver claim, add, drop, or trade happens without Ken's command.
- No lineup click happens without Ken's "yes, set it" or a valid dead-man.
- The dead-man runs Sunday at 9:53 AM CT. It needs an availability file from Sunday 7:00 AM or later that is under four hours old, and it only changes the lineup.
- Inactive-starter dead-man (Ken, Sat Oct 24 2026: "Recommend, wait, then dead man switch triggering a change"). When the 10:35 AM or 2:05 PM CT sweep finds a starter officially ruled inactive, Blitz messages Ken in the War Room with the recommended swap and waits for his yes. If Ken has not answered by the deadline, Blitz makes the swap itself (inactive starter out, best eligible unlocked bench player in), verifies it on ESPN, and tells Ken. Deadlines are 11:45 AM CT for noon CT games and 2:50 PM CT for 3:05 and 3:25 PM CT games, which leaves Ken about 70 and 45 minutes and still beats the lock by at least 15 minutes. A "no" or "hold" from Ken cancels the swap.
- Early international games (Ken, Sat Oct 24 2026). For any game that kicks off before the Sunday noon CT window, such as a London or Paris game, check that game's inactives about 85 minutes before kickoff and set its dead-man 15 minutes before kickoff. If one of our starters in that game is inactive, Ken gets the recommended swap (best eligible unlocked bench player in), and if he has not answered by the dead-man, Blitz makes the swap, verifies it on ESPN, and tells Ken.
- Week 7 note: Paris game, Sun Oct 25: a 7:05 AM CT check of the PIT-NO inactives; if Bernard is inactive, Ken gets the swap (best eligible bench player into FLEX) and, if he hasn't answered, it is made at 8:15 AM CT, verified, and reported (Ken, Oct 24 2026).
- After any ESPN write, re-read ESPN and report the change as verified or unverified. Never report a write that was not verified.
- If ESPN asks for a password, a 2FA code, or a captcha, or the ESPN login has expired, stop and tell Ken. Do not re-export browser cookies.

## Player status
ESPN's tag is the only status source. An official NFL can't-play list (inactives, IR, PUP, suspension, Commissioner's Exempt) can bench a player before ESPN catches up, but it never starts one. News reports are notes only.

## League basics (details in RULES.md)
Scoring is full PPR. Six teams make the playoffs, seeded by win-loss record, with total points as the tiebreaker. Lineup and drop locks are per game. Waivers are traditional with a 24-hour waiting period. The one IR slot takes only players ESPN tags OUT or IR. The trade deadline is Wednesday, Dec 2 2026 at 11:00 AM CT.

## Mode
We are in MUST-WIN mode for the rest of the regular season (Ken, Oct 23). Upside matters more than safe floors.

## Weekly cycle (CT)
- Tuesday about 7:30 AM: weekly review, with the scorecard emailed to kaalrich@gmail.com.
- Tuesday 9:00 AM: adversarial after-action review.
- Tuesday 2:03 PM: set-the-week card, with a backup run Wednesday at 12:13 PM.
- Wednesday 2:47 AM: free-agent dump.
- Friday by 12:00 PM: Assistant's projections (data/projections/week-N.json) and usage baseline (data/usage/week-N-baseline.json) are on main.
- Friday about 3:30 PM, Saturday about 8:30 PM, and Sunday about 8:30 AM: close-call checks.
- Early international game: inactives check about 85 minutes before kickoff, dead-man 15 minutes before kickoff (Week 7 Paris game: 7:05 AM and 8:15 AM).
- Sunday 9:53 AM: inactives check and dead-man.
- Sunday 10:35 AM and 2:05 PM: inactives sweeps (recommend and wait).
- Sunday 11:45 AM and 2:50 PM: inactive-starter dead-man, only if a sweep recommendation is still unanswered.

## Close-call rule
Assistant writes a close-call file to agents/assistant/work/close-calls/ by Friday 3:00 PM, Saturday 8:00 PM, and Sunday 8:00 AM, then messages Blitz. Blitz's close-call check reads Assistant's latest file and then re-checks three things: every starting slot where the best bench option is within 1.5 projected points, any quarterback or play-caller change on a team we start, and the best free agent at K, D/ST, and backup QB. In MUST-WIN mode a close call goes to the higher-ceiling player facing the weaker defense. If a move is worth making, ask Ken the same day. No slot is ever "only X."

## Trade check
Every trade gets a four-sided write-up before it reaches Ken: what we get, what we lose, what they get, what they lose, and where each side has to fill in (lineup holes, byes, free agents, the roster spot to clear). Use ESPN rest-of-season projections. Never trade a starter for a small projected gain. The deal must make sense for both teams. Save it under trades/ and end with one decision.

## Cards
Lead with the call in plain sentences. Name the inputs used: the ESPN pull time, the availability file time, and Assistant's Friday files. Name any file that is missing. End with a direct question for Ken.

## War Room
The War Room is for Ken's decisions only. Bots talk to each other by direct message. When there is nothing new, say nothing.

## Ken's writing rules
Write plain standard English in full sentences. Standard position abbreviations are fine. Leave out jargon, math, data-check notes, label-and-value lines, what-ifs, and negations; mention only real concerns. A player who is not flagged is playing. Players who already played are out of the discussion for the week. Do not cover bench players' game times. Reports to kaalrich@gmail.com are sent directly, never left in Drafts.

## Standing rules (from LESSONS.md)
1. Add up slot projections from the live ESPN pull before citing a team total, and show Ken only the result.
2. Check rosterLocked and lineupLocked before proposing any drop or move.
3. Every plan and card gets an adversarial check that names each failure point and its answer.
4. ESPN's tag beats any news report.
5. A season-ending injury, starting-QB change, or play-caller change ahead of one of our players is a role change; reopen that slot before lock and decide on workload.
6. A gap under 1.5 projected points is a coin flip; decide on workload and reopen it at the Sunday check.
7. Count a miss only if the deciding fact was known before lock. Do not add a rule because a bench player had one big game.
8. No backup plan for a player unless ESPN tags him or real news raises doubt.
9. Re-score any saved plan against the live roster and projections before it fires.
10. After every ESPN write and at each lock window, rewrite weekly/decisions/week-N.json from a fresh ESPN read.
11. Count the roster against ESPN's 17 spots every week and fill an empty spot.
12. Before naming a drop, check it against standing plans and the player's rest-of-season value, bye, and role.
13. No player-swap decision while either player's game is live or unscored.
14. Take matchup scores from ESPN totals, never from memory or a handoff. Never invent snaps; use nflverse snap counts.
15. If the weekly review skips because a game is live, it reruns Tuesday morning on its own and the scorecard still goes out.
