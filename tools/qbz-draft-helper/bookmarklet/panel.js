// QBZ Draft Helper - bookmarklet panel (mobile bottom sheet). RECOMMEND ONLY: never clicks or edits ESPN.
(function () {
  if (window.__qbz) { window.__qbz.toggle(); return; }
  const R = self.QBZRules, P = self.QBZParser, LS = "qbzDraftHelper";
  const load = () => { try { return JSON.parse(localStorage.getItem(LS)) || {}; } catch (e) { return {}; } };
  const save = s => { try { localStorage.setItem(LS, JSON.stringify(s)); } catch (e) {} };
  let store = load(); // {slot, overrides:[...], rules:{...}}
  const cfg = () => Object.assign({}, R.DEFAULT_CONFIG, store.rules || {}, { slot: +store.slot || 0, overrides: store.overrides || [] });
  let view = "main", expanded = false, mini = false, lastOn = false, hl = null, lastHtml = "", autoSlot = 0;

  const css = `#qbz{position:fixed;left:0;right:0;bottom:0;z-index:2147483647;background:rgba(15,18,26,.97);color:#eee;font:14px/1.35 -apple-system,system-ui,sans-serif;border-top:3px solid #18c964;border-radius:14px 14px 0 0;padding:8px 12px calc(8px + env(safe-area-inset-bottom));max-height:42vh;overflow:auto;-webkit-overflow-scrolling:touch;box-shadow:0 -4px 18px #000a}
#qbz.x{max-height:82vh}#qbz.m{left:auto;right:10px;bottom:calc(10px + env(safe-area-inset-bottom));border:2px solid #18c964;border-radius:20px;padding:6px 14px;max-height:none}
#qbz.m>*:not(.h){display:none}#qbz.m .h .b{display:none}
#qbz .h{display:flex;justify-content:space-between;align-items:center;gap:6px}
#qbz button{font:inherit;background:#2a3140;color:#cde;border:0;border-radius:8px;padding:6px 10px;min-height:36px;margin-left:4px}
#qbz .s{border-top:1px solid #333;margin-top:6px;padding-top:4px}#qbz .t{font-size:17px;color:#18c964}
#qbz .w{background:#a33;padding:4px 6px;border-radius:6px;margin:4px 0}#qbz .n{color:#fc6}#qbz .r{color:#f66}
#qbz small{color:#aaa}#qbz pre{white-space:pre-wrap;font-size:11px}#qbz textarea,#qbz input{width:100%;box-sizing:border-box;font:12px monospace;background:#000;color:#eee;border:1px solid #444;border-radius:6px}
#qbzf{position:fixed;inset:0;z-index:2147483646;pointer-events:none;background:rgba(24,201,100,.45);animation:qbzf .2s 6 alternate}@keyframes qbzf{to{opacity:0}}`;
  const st = document.createElement("style"); st.textContent = css; document.head.appendChild(st);
  const el = document.createElement("div"); el.id = "qbz"; document.body.appendChild(el);
  const pad = () => { document.body.style.paddingBottom = mini || el.style.display === "none" ? "" : el.offsetHeight + "px"; };

  const esc = s => String(s == null ? "" : s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const pl = p => p ? esc(p.name) + " <small>" + esc(p.pos) + " " + esc(p.team || "") + (p.tag ? " <b class=r>" + esc(p.tag) + "</b>" : "") + "</small>" : "-";

  function flash() {
    const f = document.createElement("div"); f.id = "qbzf"; document.body.appendChild(f); setTimeout(() => f.remove(), 1400);
    try { navigator.vibrate && navigator.vibrate([200, 100, 200]); } catch (e) {}
  }
  function highlight(p) {
    if (hl && hl !== (p && p.el)) hl.style.outline = "";
    if (p && p.el) { p.el.style.outline = "3px solid #18c964"; p.el.style.outlineOffset = "-3px"; hl = p.el; }
  }

  function settingsHtml() {
    const c = cfg(), rest = Object.assign({}, store.rules || {});
    return `<div class=s><b>Settings</b> <small>(saved in this browser for fantasy.espn.com)</small>
<div>Draft slot (0 = auto): <input id=qbzSlot type=number min=0 max=20 value="${esc(c.slot)}" style="width:70px"></div>
<div>News overrides <small>Name | BLOCK or BOOST | note</small><textarea id=qbzOv rows=4>${esc((c.overrides || []).map(o => [o.name, o.action, o.note || ""].join(" | ")).join("\n"))}</textarea></div>
<div>Rule overrides (JSON, only keys you change; defaults below)<textarea id=qbzRules rows=6>${esc(JSON.stringify(rest, null, 1))}</textarea></div>
<details><summary><small>Default rules</small></summary><pre>${esc(JSON.stringify(Object.assign({}, R.DEFAULT_CONFIG, { overrides: undefined }), null, 1))}</pre></details>
<button data-q=save>Save</button><button data-q=reset>Reset all</button><button data-q=main>Back</button> <span id=qbzMsg></span></div>`;
  }

  function tick() {
    if (el.style.display === "none") return;
    if (view === "settings") { if (lastHtml !== "S") { el.innerHTML = head() + settingsHtml(); lastHtml = "S"; pad(); } return; }
    let html;
    try {
      const c = cfg();
      const players = P.readPlayers(document), clk = P.readClock(document, c.teams), roster = P.readRoster(document), auto = P.readAutopick(document);
      if (!c.slot && clk.youOnClock && clk.pick && !autoSlot) {
        const r = Math.ceil(clk.pick / c.teams), w = clk.pick - (r - 1) * c.teams;
        autoSlot = r % 2 ? w : c.teams - w + 1;
      }
      const slot = c.slot || autoSlot, mine = slot ? R.ourPicks(slot, c.teams, c.rounds) : [], cur = clk.pick || 0;
      const onClock = clk.youOnClock || (!!cur && mine.includes(cur));
      const next = mine.find(x => x >= cur) || null, round = next ? mine.indexOf(next) + 1 : (clk.round || 1);
      const until = next != null && cur ? next - cur : null;
      const top = roster.players.find(x => x.pos === "RB");
      const s = { round, pick: next || cur || 1, counts: roster.counts, topRb: top && top.name, topRbTeam: top && top.team,
        haveHandcuff: top && roster.players.some(x => x !== top && x.pos === "RB" && x.team === top.team) };
      const res = R.recommend(players, s, c);
      const pair = next && mine.includes(next + 1) ? R.planPair(players, s, c) : null;
      const replan = !pair && cur && mine.includes(cur) && mine.includes(cur - 1);
      highlight(res.recs[0] && res.recs[0].player);
      if (onClock && !lastOn) flash();
      lastOn = onClock;
      if (mini) { html = head(onClock ? "ON CLOCK: " + (res.recs[0] ? esc(res.recs[0].player.name) : "?") : "QBZ · " + (until == null ? "?" : until) + " to go"); }
      else {
        html = head(onClock ? "<b class=t>ON THE CLOCK " + esc(clk.clock || "") + "</b>" : "<b>" + (until == null ? "?" : until) + "</b> picks to our turn") +
        (auto === "ON" ? "<div class=w>⚠ Autopick looks ON (it takes IR players)</div>" : "") +
        (!slot ? "<div class=w>Slot unknown: set it in ⚙</div>" : "") +
        `<div><small>R${round} · pick ${next || "?"} · slot ${slot || "?"}</small></div>` +
        (res.recs.map((r, i) => `<div class="${i ? "" : "t"}">${i ? "Alt " + i + ": " : "★ "}${pl(r.player)}${r.reach ? " <b class=r>REACH</b>" : ""}${i && !expanded ? "" : "<br><small>" + esc(r.reason) + "</small>"}</div>`).join("") || "<div>No players read. Open ⓘ diagnostics.</div>") +
        (pair ? `<div class=s><b>Turn pair</b> A: ${pl(pair.A && pair.A.player)} → B: ${pl(pair.B && pair.B.player)}</div>` : "") +
        (replan ? `<div class=s><b>Turn pick B (re-planned)</b>: ${pl(res.recs[0] && res.recs[0].player)}</div>` : "") +
        res.notes.map(n => `<div class=n>${esc(n)}</div>`).join("");
        if (expanded) html +=
          `<div class=s><b>Roster vs targets</b><br>${["QB", "RB", "WR", "TE", "DST", "K"].map(k => `${k} ${roster.counts[k] || 0}/${c.targets[k]}${res.deficits[k] ? "<b class=n>+" + res.deficits[k] + "</b>" : ""}`).join(" · ")}${roster.found ? "" : "<br><small>Roster panel not found; counts are 0.</small>"}</div>` +
          `<div class=s><b>Blocked (${res.blocked.length})</b>${res.blocked.slice(0, 10).map(b => `<div><small>${pl(b.player)} - ${esc(b.reason)}</small></div>`).join("")}</div>` +
          `<div class=s><b>Diagnostics</b><pre>${esc(JSON.stringify({ rows: players.length, sample: players[0] ? Object.assign({}, players[0], { el: undefined }) : null, clock: clk, onClock, slot, autopick: auto, rosterFound: roster.found, roster: roster.players.map(x => x.name + " " + x.pos), width: innerWidth }, null, 1))}</pre></div>`;
        html += "<div><small>Recommend only. You make every pick.</small></div>";
      }
    } catch (e) { html = head() + "<div class=w>Parser error: " + esc(e.message) + "</div>"; }
    if (html !== lastHtml) { el.innerHTML = html; lastHtml = html; pad(); }
  }
  function head(label) {
    return `<div class=h><span>${label || "<b>QBZ Draft</b>"}</span><span class=b>${view === "main" ? `<button data-q=exp>${expanded ? "▾" : "▴"}</button><button data-q=set>⚙</button>` : ""}<button data-q=min>${mini ? "▣" : "–"}</button></span>${mini ? "<button data-q=min>▣</button>" : ""}</div>`;
  }

  el.addEventListener("click", e => {
    const b = e.target.closest("[data-q]");
    if (!b) { if (mini) { mini = false; el.classList.remove("m"); lastHtml = ""; tick(); } return; }
    const q = b.getAttribute("data-q");
    if (q === "min") { mini = !mini; el.classList.toggle("m", mini); }
    if (q === "exp") { expanded = !expanded; el.classList.toggle("x", expanded); }
    if (q === "set") view = "settings";
    if (q === "main") view = "main";
    if (q === "save") {
      try {
        store.slot = +document.getElementById("qbzSlot").value || 0;
        store.overrides = document.getElementById("qbzOv").value.split("\n").map(l => l.split("|").map(x => x.trim())).filter(a => a[0])
          .map(([name, action, note]) => ({ name, action: /block/i.test(action) ? "BLOCK" : "BOOST", note: note || "" }));
        const t = document.getElementById("qbzRules").value.trim();
        store.rules = t ? JSON.parse(t) : {};
        save(store); document.getElementById("qbzMsg").textContent = "Saved."; return;
      } catch (err) { document.getElementById("qbzMsg").textContent = "JSON error: " + err.message; return; }
    }
    if (q === "reset") { store = {}; save(store); }
    lastHtml = ""; tick();
  });

  let pending = false;
  const mo = new MutationObserver(m => {
    if (m.every(x => el.contains(x.target))) return;
    if (!pending) { pending = true; setTimeout(() => { pending = false; tick(); }, 50); }
  });
  mo.observe(document.body, { childList: true, subtree: true, characterData: true });
  const iv = setInterval(tick, 300);
  window.__qbz = {
    toggle() { const hide = el.style.display !== "none"; el.style.display = hide ? "none" : ""; if (hide) highlight(null); lastHtml = ""; pad(); tick(); },
    tick, el, stop() { clearInterval(iv); mo.disconnect(); el.remove(); st.remove(); delete window.__qbz; }
  };
  tick();
})();
