// QBZ Draft Helper - rules engine (pure logic, no DOM). Also loaded by Node tests.
(function (root) {
  const DEFAULT_CONFIG = {
    teams: 12,
    rounds: 16,
    slot: 0,                 // 0 = auto-detect; otherwise 1..12
    earlyRounds: 2,          // R1..earlyRounds: RB/WR only
    hardInjuryTags: ["O", "IR", "SUSP", "PUP"],
    injuryOkFromRound: 14,   // hard tags allowed from this round on
    flagTags: ["Q", "D", "DTD"],
    qbFromRound: 7,
    eliteQbAdp: 24,          // elite QB exception: ADP <= this...
    eliteQbFall: 10,         // ...and fallen this many picks past ADP
    dstKFromRound: 15,
    targets: { QB: 1, RB: 6, WR: 5, TE: 2, DST: 1, K: 1 },
    minimums: { QB: 1, RB: 5, WR: 4, TE: 1, DST: 1, K: 1 },
    reachCaps: [ { upToRound: 5, cap: 10 }, { upToRound: 11, cap: 20 } ], // later rounds: no cap
    handcuffFromRound: 8,
    boostSpots: 15,          // a news BOOST counts as this many rank spots better
    overrides: []            // [{name, action: "BLOCK"|"BOOST", note}]
  };

  const norm = s => String(s || "").toLowerCase().replace(/[^a-z]/g, "");

  function pickNumber(round, slot, teams) {
    return round % 2 === 1 ? (round - 1) * teams + slot : round * teams - slot + 1;
  }
  function ourPicks(slot, teams, rounds) {
    const out = [];
    for (let r = 1; r <= rounds; r++) out.push(pickNumber(r, slot, teams));
    return out;
  }
  function roundOfPick(pick, teams) { return Math.ceil(pick / teams); }
  function reachCap(round, cfg) {
    for (const c of cfg.reachCaps) if (round <= c.upToRound) return c.cap;
    return Infinity;
  }
  function override(p, cfg) {
    return (cfg.overrides || []).find(o => o && norm(o.name) && norm(o.name) === norm(p.name));
  }

  // Positions we must still fill, given counts and minimums.
  function deficits(counts, cfg) {
    const d = {};
    for (const k of Object.keys(cfg.minimums)) d[k] = Math.max(0, cfg.minimums[k] - (counts[k] || 0));
    return d;
  }

  // Hard check of one player. Returns {ok, reason, soft} (soft = only a reach).
  function check(p, st, cfg) {
    const P = p.pos, c = st.counts, r = st.round;
    const ov = override(p, cfg);
    if (ov && /block/i.test(ov.action)) return { ok: false, reason: "news block" + (ov.note ? ": " + ov.note : "") };
    if (cfg.hardInjuryTags.includes(p.tag) && r < cfg.injuryOkFromRound) return { ok: false, reason: p.tag + " before R" + cfg.injuryOkFromRound };
    if (P === "DST" || P === "K") {
      if (r < cfg.dstKFromRound) return { ok: false, reason: (P === "DST" ? "D/ST" : "K") + " before R" + cfg.dstKFromRound };
      if ((c[P] || 0) >= cfg.targets[P]) return { ok: false, reason: "already have " + P };
      return { ok: true };
    }
    if (r <= cfg.earlyRounds && P !== "RB" && P !== "WR") return { ok: false, reason: "R1-" + cfg.earlyRounds + " RB/WR only" };
    if (P === "QB") {
      if ((c.QB || 0) >= cfg.targets.QB) return { ok: false, reason: "already have QB" };
      const elite = p.adp != null && p.adp <= cfg.eliteQbAdp && st.pick >= p.adp + cfg.eliteQbFall;
      if (r < cfg.qbFromRound && !elite) return { ok: false, reason: "QB before R" + cfg.qbFromRound };
    }
    if (P === "TE") {
      if ((c.TE || 0) >= cfg.targets.TE) return { ok: false, reason: "TE target met" };
      if (p.adp != null && st.pick < p.adp) return { ok: false, reason: "TE before ADP (" + p.adp + ")" };
    }
    if ((P === "RB" || P === "WR") && (c[P] || 0) >= cfg.targets[P]) return { ok: false, reason: P + " target met" };
    if (!cfg.targets.hasOwnProperty(P)) return { ok: false, reason: "unknown position " + P };
    // Fill guarantee: keep R15-16 for D/ST+K; before that, if core needs >= core picks left, only needed positions.
    const d = deficits(c, cfg);
    if (r < cfg.dstKFromRound) {
      const coreLeft = cfg.dstKFromRound - r; // rounds r..dstKFromRound-1
      const coreNeed = d.QB + d.RB + d.WR + d.TE;
      if (coreNeed >= coreLeft && !d[P]) return { ok: false, reason: "need " + Object.keys(d).filter(k => d[k] && k !== "DST" && k !== "K").join("/") + " to fill roster" };
    } else if (P !== "DST" && P !== "K") {
      const slotsLeft = cfg.rounds - r + 1;
      if (d.DST + d.K >= slotsLeft) return { ok: false, reason: "R" + r + " reserved for D/ST/K" };
    }
    const cap = reachCap(r, cfg);
    if (p.adp != null && p.adp - st.pick > cap) return { ok: false, soft: true, reason: "reach >" + cap + " (ADP " + p.adp + ")" };
    return { ok: true };
  }

  function score(p, cfg, st) {
    let s = p.rank != null ? p.rank : (p.adp != null ? p.adp : 999);
    const ov = override(p, cfg);
    if (ov && /boost/i.test(ov.action)) s -= cfg.boostSpots;
    if (st.handcuffTeam && p.pos === "RB" && p.team === st.handcuffTeam && st.round >= cfg.handcuffFromRound) s -= 5;
    return s;
  }

  function why(p, st, cfg, extra) {
    const bits = [];
    bits.push("#" + (p.rank != null ? p.rank : "?") + " rank, ADP " + (p.adp != null ? p.adp : "?"));
    const d = deficits(st.counts, cfg);
    if (d[p.pos]) bits.push("fills " + p.pos + " need");
    const ov = override(p, cfg);
    if (ov && /boost/i.test(ov.action)) bits.push("news boost" + (ov.note ? ": " + ov.note : ""));
    if (cfg.flagTags.includes(p.tag)) bits.push("FLAG: tagged " + p.tag);
    if (st.handcuffTeam && p.pos === "RB" && p.team === st.handcuffTeam) bits.push("handcuff for " + st.topRb);
    if (extra) bits.push(extra);
    return bits.join("; ");
  }

  // players: [{name,pos,team,tag,rank,adp}] (available only). st: {round, pick, counts, topRb?, topRbTeam?}
  function recommend(players, st, cfg) {
    cfg = Object.assign({}, DEFAULT_CONFIG, cfg || {});
    st = Object.assign({ counts: {} }, st);
    st.handcuffTeam = st.topRbTeam || null;
    const legal = [], blocked = [], reaches = [];
    for (const p of players) {
      const c = check(p, st, cfg);
      if (c.ok) legal.push(p);
      else if (c.soft) { reaches.push(p); blocked.push({ player: p, reason: c.reason }); }
      else blocked.push({ player: p, reason: c.reason });
    }
    const by = (a, b) => score(a, cfg, st) - score(b, cfg, st);
    legal.sort(by); reaches.sort(by);
    let recs = legal.slice(0, 3).map(p => ({ player: p, reason: why(p, st, cfg) }));
    if (recs.length < 3) {
      for (const p of reaches) {
        if (recs.length >= 3) break;
        recs.push({ player: p, reach: true, reason: why(p, st, cfg, "REACH: nothing legal within cap (" + (p.adp - st.pick) + " spots early)") });
      }
    }
    const notes = [];
    if (st.topRb && st.round >= cfg.handcuffFromRound && !st.haveHandcuff) {
      const hc = players.find(p => p.pos === "RB" && p.team === st.topRbTeam && p.name !== st.topRb);
      notes.push(hc ? "Handcuff available for " + st.topRb + ": " + hc.name : "No handcuff for " + st.topRb + " in visible rows (try RB filter)");
    }
    return { recs, blocked, deficits: deficits(st.counts, cfg), notes };
  }

  // Back-to-back pair: plan A, then re-plan B with A taken.
  function planPair(players, st, cfg) {
    const a = recommend(players, st, cfg);
    const A = a.recs[0];
    if (!A) return { A: null, B: null };
    const counts = Object.assign({}, st.counts);
    counts[A.player.pos] = (counts[A.player.pos] || 0) + 1;
    const rest = players.filter(p => p !== A.player);
    const b = recommend(rest, Object.assign({}, st, { counts, round: st.round + 1, pick: st.pick + 1 }), cfg);
    return { A, B: b.recs[0] || null, Balts: b.recs.slice(1) };
  }

  const api = { DEFAULT_CONFIG, pickNumber, ourPicks, roundOfPick, reachCap, check, recommend, planPair, deficits };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else root.QBZRules = api;
})(typeof self !== "undefined" ? self : this);
