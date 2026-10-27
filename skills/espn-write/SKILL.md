---
name: espn-write
description: >-
  Use for every Quantum Blitz ESPN write (lineup slot, add, drop, waiver claim,
  trade): apply through ffmcp, then confirm with a get_roster read-back.
---
# espn-write
Blitz has Ken's full authority (Oct 27 2026) for these writes. ESPN decides player status. Never move or drop a player whose game has started.

1. Preview first with the ffmcp tool (apply false) and check the result is what you intend.
2. Lineup: place each chosen player with move_player (QB, RB, WR, TE, FLEX, K, D/ST, BE). Use set_lineup with apply true only when your picks match its preview exactly, because it picks by ESPN projection alone.
3. Adds, drops, claims: add_player with drop, apply true. Trades: propose_trade or respond_to_trade, apply true, and only after both teams' starting lineups improve in analyze_trade.
4. Read back with get_roster (and get_transactions for claims or trades). The move counts only if ESPN shows it.
5. If ffmcp errors, fall back to the old ESPN client in /workspace/fantasy/quantum-blitz/espn_api/client.py (lineups) and read back the same way. A 401, password, 2FA or captcha means stop and tell Ken.
6. Tell Ken in one plain sentence what changed. Write an audit note only if a write fails.
