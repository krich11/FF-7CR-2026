// QBZ Draft Helper - content script. RECOMMEND ONLY: never clicks, types into, or modifies ESPN controls.
(function () {
  const R = self.QBZRules, P = self.QBZParser;
  let cfg = Object.assign({}, R.DEFAULT_CONFIG);
  let ui = { diag: false, sound: true };
  let lastOnClock = false, lastHighlighted = null, lastHtml = "", autoSlot = 0, pairPlan = null;

  function loadCfg() {
    try {
      chrome.storage.sync.get({ qbzConfig: null, qbzUi: null }, v => {
        if (v.qbzConfig) cfg = Object.assign({}, R.DEFAULT_CONFIG, v.qbzConfig);
        if (v.qbzUi) ui = Object.assign(ui, v.qbzUi);
        tick();
      });
    } catch (e) { /* storage unavailable: defaults */ }
  }
  try { chrome.storage.onChanged.addListener(loadCfg); } catch (e) {}

  const panel = document.createElement("div");
  panel.id = "qbz-panel";
  document.documentElement.appendChild(panel);
  panel.addEventListener("click", e => {
    const t = e.target.closest("[data-qbz]");
    if (!t) return;
    const k = t.getAttribute("data-qbz");
    if (k === "diag") ui.diag = !ui.diag;
    if (k === "sound") ui.sound = !ui.sound;
    if (k === "min") panel.classList.toggle("qbz-min");
    try { chrome.storage.sync.set({ qbzUi: ui }); } catch (e2) {}
    lastHtml = ""; tick();
  });

  const esc = s => String(s == null ? "" : s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const pl = p => p ? esc(p.name) + " <small>" + esc(p.pos) + (p.team ? " " + esc(p.team) : "") + (p.tag ? " <b class='qbz-tag'>" + esc(p.tag) + "</b>" : "") + "</small>" : "-";

  function beep() {
    if (!ui.sound) return;
    try { const a = new AudioContext(), o = a.createOscillator(); o.frequency.value = 880; o.connect(a.destination); o.start(); o.stop(a.currentTime + 0.25); } catch (e) {}
  }

  function highlight(p) {
    if (lastHighlighted && lastHighlighted !== (p && p.el)) { lastHighlighted.style.outline = ""; lastHighlighted.style.outlineOffset = ""; }
    if (p && p.el) { p.el.style.outline = "3px solid #18c964"; p.el.style.outlineOffset = "-3px"; lastHighlighted = p.el; }
  }

  function tick() {
    let html;
    try {
      const players = P.readPlayers(document);
      const clk = P.readClock(document, cfg.teams);
      const roster = P.readRoster(document);
      const auto = P.readAutopick(document);
      // Slot: manual, else infer from the first pick seen while "you're on the clock".
      if (!cfg.slot && clk.youOnClock && clk.pick && clk.pick <= cfg.teams) autoSlot = clk.pick;
      if (!cfg.slot && clk.youOnClock && clk.pick && clk.pick > cfg.teams && !autoSlot) {
        const r = Math.ceil(clk.pick / cfg.teams), w = clk.pick - (r - 1) * cfg.teams;
        autoSlot = r % 2 ? w : cfg.teams - w + 1;
      }
      const slot = cfg.slot || autoSlot;
      const mine = slot ? R.ourPicks(slot, cfg.teams, cfg.rounds) : [];
      const cur = clk.pick || 0;
      const onClock = clk.youOnClock || (!!cur && mine.includes(cur));
      const next = mine.find(x => x >= cur) || null;
      const ourRound = next ? mine.indexOf(next) + 1 : (clk.round || 1);
      const picksUntil = next != null && cur ? next - cur : null;
      const topRb = roster.players.find(x => x.pos === "RB");
      const st = { round: ourRound, pick: next || cur || 1, counts: roster.counts,
        topRb: topRb && topRb.name, topRbTeam: topRb && topRb.team,
        haveHandcuff: topRb && roster.players.some(x => x !== topRb && x.pos === "RB" && x.team === topRb.team) };
      const res = R.recommend(players, st, cfg);
      const backToBack = next && mine.includes(next + 1);
      // Pair: plan when the turn approaches; after A is taken (we're on pick next+1), re-plan B from the live board.
      let pair = null;
      if (backToBack) { pair = R.planPair(players, st, cfg); pairPlan = pair; }
      else if (pairPlan && mine.includes(cur) && mine.includes(cur - 1)) pair = { A: { player: { name: "(taken)" } }, B: res.recs[0], Balts: res.recs.slice(1), replanned: true };
      else pairPlan = null;

      highlight(res.recs[0] && res.recs[0].player);
      if (onClock && !lastOnClock) { beep(); panel.classList.add("qbz-flash"); setTimeout(() => panel.classList.remove("qbz-flash"), 1500); }
      lastOnClock = onClock;

      const counts = ["QB", "RB", "WR", "TE", "DST", "K"].map(k => `<span>${k} ${roster.counts[k] || 0}/${cfg.targets[k]}${res.deficits[k] ? " <b>need " + res.deficits[k] + "</b>" : ""}</span>`).join(" ");
      html = `<div class="qbz-head"><b>QBZ Draft Helper</b> <span class="qbz-btns"><a data-qbz="sound">${ui.sound ? "🔔" : "🔕"}</a> <a data-qbz="diag">diag</a> <a data-qbz="min">_</a></span></div>
      ${auto === "ON" ? `<div class="qbz-warn">⚠ Autopick looks ON - ESPN autopick will take IR players.</div>` : ""}
      ${!slot ? `<div class="qbz-warn">Slot unknown - set it in Options (or wait to go on the clock once).</div>` : ""}
      <div class="${onClock ? "qbz-clock on" : "qbz-clock"}">${onClock ? "ON THE CLOCK" + (clk.clock ? " " + esc(clk.clock) : "") : "Picks until our turn: " + (picksUntil == null ? "?" : picksUntil)}
        <small> R${ourRound} · our pick ${next || "?"} · slot ${slot || "?"}</small></div>
      ${pair ? `<div class="qbz-sec"><b>Turn pair${pair.replanned ? " (re-planned)" : ""}</b><div>A: ${pl(pair.A && pair.A.player)}</div><div>B: ${pl(pair.B && pair.B.player)} <small>${esc(pair.B ? pair.B.reason : "")}</small></div></div>` : ""}
      <div class="qbz-sec"><b>Recommended</b>${res.recs.map((r, i) => `<div class="${i ? "" : "qbz-top"}">${i ? "Alt " + i + ": " : "★ "}${pl(r.player)}${r.reach ? " <b class='qbz-tag'>REACH</b>" : ""}<br><small>${esc(r.reason)}</small></div>`).join("") || "<div>No candidates read (check diagnostics / try a position filter).</div>"}</div>
      ${res.notes.map(n => `<div class="qbz-note">${esc(n)}</div>`).join("")}
      <div class="qbz-sec"><b>Roster vs targets</b><div class="qbz-counts">${counts}</div>${roster.found ? "" : "<small>Roster panel not found - counts are 0.</small>"}</div>
      <div class="qbz-sec"><b>Blocked (${res.blocked.length})</b>${res.blocked.slice(0, 8).map(b => `<div><small>${pl(b.player)} - ${esc(b.reason)}</small></div>`).join("")}</div>
      ${ui.diag ? `<div class="qbz-sec qbz-diag"><b>Diagnostics</b><pre>${esc(JSON.stringify({ rows: players.length, sample: players[0] ? Object.assign({}, players[0], { el: undefined }) : null, clock: clk, onClock, slot, autoSlot, autopick: auto, rosterFound: roster.found, roster: roster.players.map(x => x.name + " " + x.pos) }, null, 1))}</pre></div>` : ""}
      <div class="qbz-foot">Recommend only - you make every pick.</div>`;
    } catch (e) {
      html = `<div class="qbz-head"><b>QBZ Draft Helper</b> <a data-qbz="diag">diag</a></div><div class="qbz-warn">Parser error: ${esc(e.message)}</div>`;
    }
    if (html !== lastHtml) { panel.innerHTML = html; lastHtml = html; }
  }

  let pending = false;
  new MutationObserver(m => {
    if (m.every(x => panel.contains(x.target))) return;
    if (!pending) { pending = true; requestAnimationFrame(() => { pending = false; tick(); }); }
  }).observe(document.body || document.documentElement, { childList: true, subtree: true, characterData: true });
  setInterval(tick, 300);
  loadCfg();
})();
