---
name: roster-moves
description: >-
  Use for Quantum Blitz waiver claims, free-agent adds and drops, and trade
  offers or replies.
---
# roster-moves
1. Pull get_waiver_targets, get_available_players and get_roster from ffmcp; get_transactions for claim results and get_pending_trades for offers.
2. Read the news on the player you would add and the one you would drop.
3. Make a move when it adds points this week or the next few weeks without leaving a slot unfillable (byes, injuries). Drop only unlocked players, weakest first. Waivers process about 2:00 AM CT Wednesday; after that, free agents add immediately.
4. Trades: run analyze_trade or find_trade_partners. Offer or accept only if our starting lineup improves and the deal makes sense for the other team too.
5. Make it with espn-write and confirm on ESPN.
6. Tell Ken in one plain sentence what changed. If nothing changed, say nothing.
