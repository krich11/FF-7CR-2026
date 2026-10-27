# Week 7 adversarial AAR — Blitz
Date: Tue Oct 27, 2026, 9:00 AM CT standing review (run started about 8:57 AM CT)
Bar: points. Never miss a real signal; never promote noise.
Result (ESPN final, weekly/results/week-7-scorecard.md): lost 99.8 to 102.1 to David's Daring Team; 1-6, 12th of 12.
Sources read: weekly/cards/week-7.md, weekly/cards/week-7-must-win-analysis.md, weekly/decisions/week-7.json, agents/assistant/work/close-calls/week-7-mustwin-facts.md, week-7-sat.md, week-7-sun.md, agents/assistant/work/postmortem/week-7-postmortem.md, weekly/audit/espn-writes.log, weekly/audit/blitz-audit.log, data/league.json, RULES.md, PLAYBOOK.md. No ESPN write from this review.

Test (Ken, Oct 8): a miss counts only if the deciding fact was public before lock. A box score is not that fact.

## What went right
- Jacobs started in his first game back and scored 20.1, the best on the team; activation was tracked through the Sunday sweeps.
- Murray over McCarthy at QB gained about four points.
- Every ESPN write in Week 7 was read back and verified (Oct 20 RB order, Oct 22 Pitts at TE, Oct 23 Marks re-add and RB move, Oct 24 Goedert at TE).
- Paris inactives check ran on time; Bernard and the Steelers were active.

## What we attacked
1. FLEX, Bernard 5.7 over Gordon 17.3 (Gordon alone would have won). COUNTS. Facts on disk Saturday morning, before the 8:30 AM Paris lock: Assistant's fact pack flagged sustained wind of 15 to 16 mph with gusts of 33 to 35 mph for PIT at NO; Bernard's prior six weeks were 0.0, 7.5, 2.4, 3.1, 14.4 and 25.7; Gordon was Miami's lead back with Achane out for the year (18 touches and 65% of snaps). The gap was 1.59, and every check treated 1.5 as a hard wall, so the FLEX was never reopened. The must-win card even wrote "Paris wind is real" and then kept Bernard on projection alone. Root cause: a written weather flag and a volatile receiver did not reopen a slot that sat a hair outside the band. The Oct 27 RB/FLEX workload rule and the read-the-news rule now cover this; the miss is the step that should have used them.
2. Weekly review logged zero predictable misses. Wrong: item 1 was predictable. The review should test each bench-over-starter gap against the fact pack, not just the projection band.
3. TE, Goedert 9.8 over Pitts 13.2 (minus 3.4, larger than the 2.3 margin). NOISE on the facts we had. Goedert practiced fully Saturday and had no designation, which was the stated condition, and he led on both projections. Under today's late-game swap rule, though, Goedert's workload with McKee (81% of snaps) was not clearly better than Pitts' (78%), so Pitts would have stayed. That rule now covers it.
4. RB2, Marks 9.1 over Gordon 17.3. Mostly noise. Montgomery was out and Marks had the Houston backfield to himself as a big home favorite; Gordon's game had a low total. Gordon's 25 carries were not forecast anywhere.
5. Garrett Wilson 4.6 on three targets, Murray 13.9. Box score. Noise.
6. Fact correction. Assistant's post-mortem says waivers process at 11 AM CT Wednesday (reading ESPN's waiverProcessHour of 11). The Week 6 Marks claim actually processed at 2:18 AM CT (processDate 07:18:30Z). RULES.md and playbook/CLAIMS.md (2:00 AM CT) are right. The Vidal result check is set for about 2:20 AM CT with a window that can start 15 minutes early, which is before the 2:18 AM run seen in Week 6; it should not start before about 2:30 AM CT, or it should recheck once if the claim still shows pending.

## Signal vs noise
- SIGNAL: a written severe-wind flag on a pass catcher's game, plus a volatile receiver against a lead back, inside about 2 projected points. Worth 11.6 points and the game.
- NOISE: Pitts over Goedert on equal workload, Gordon's 25 carries, Wilson's three targets, Murray's 13.9.

## Carry into Week 8
- FLEX is open competition (Bernard, Meyers, Harvey, Gordon at 14.4 at RB with Marks on bye). Bernard's weekly range is the widest on the roster; weigh workload and the game forecast, not projection alone.
- Rule 6's 1.5 line is a guide, not a wall: a weather flag or a clear workload edge reopens a slot a little outside it. Ken asked for judgment over new rules, so no PLAYBOOK change this week.

## PLAYBOOK
No standing-rule change. The lessons fit the Oct 27 read-the-news, late-game swap and RB/FLEX workload rules already in force. Rules stay at 15.
