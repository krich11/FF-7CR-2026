// QBZ Draft Helper - DOM parser. READ ONLY. Selectors are unverified guesses with text-based fallbacks.
(function (root) {
  const POS_RE = /^(QB|RB|WR|TE|K|D\/ST|DST)$/i;
  const TAG_RE = /^(Q|O|IR|SUSP|PUP|D|DTD|NA|P)$/;
  const NUM_RE = /^\d+(\.\d+)?$/;
  const TEAM_RE = /^[A-Z]{2,3}$/;

  const lines = el => (el.innerText || el.textContent || "").split("\n").map(s => s.trim()).filter(Boolean);

  // Parse one row's text lines into a player, or null.
  function parseRowLines(f) {
    if (!f || f.length < 3) return null;
    let pos = null, tag = "", team = "", name = "";
    const nums = [];
    for (const t of f) {
      if (/^draft$/i.test(t) || /^queue$/i.test(t)) continue;
      // "RB" or "Team, RB" or "SF RB"
      const parts = t.split(/[\s,]+/).filter(Boolean);
      if (!pos && parts.length <= 3 && parts.some(x => POS_RE.test(x))) {
        pos = parts.find(x => POS_RE.test(x)).toUpperCase().replace("D/ST", "DST");
        const tm = parts.find(x => TEAM_RE.test(x) && !POS_RE.test(x) && !TAG_RE.test(x));
        if (tm) team = tm;
        continue;
      }
      if (!tag && TAG_RE.test(t)) { tag = t; continue; }
      if (NUM_RE.test(t)) { nums.push(parseFloat(t)); continue; }
      if (!team && TEAM_RE.test(t)) { team = t; continue; }
      if (!name && /[a-z]/.test(t) && t.length >= 4 && !/draft|queue|bye/i.test(t)) name = t.replace(/\s+(Q|O|IR|SUSP|PUP|DTD)$/, m => { tag = tag || m.trim(); return ""; });
    }
    if (!name || !pos || nums.length === 0) return null;
    return { name, pos, team, tag, rank: nums[0], adp: nums.length > 1 ? nums[nums.length - 1] : null };
  }

  function findRows(doc) {
    let rows = Array.from(doc.querySelectorAll('[role="row"], tr'));
    // Prefer rows that carry their own Draft button (available players).
    const withBtn = rows.filter(r => Array.from(r.querySelectorAll("button, [role=button], a")).some(b => /^\s*draft\s*$/i.test(b.textContent || "")));
    return withBtn.length ? withBtn : rows;
  }

  function readPlayers(doc) {
    const out = [];
    for (const r of findRows(doc)) {
      const p = parseRowLines(lines(r));
      if (p) { p.el = r; out.push(p); }
    }
    return out;
  }

  function readClock(doc, teams) {
    const txt = doc.body ? (doc.body.innerText || "") : "";
    let pick = null, round = null, m;
    if ((m = txt.match(/ON THE CLOCK:?\s*PICK\s*(\d+)/i))) pick = +m[1];
    if ((m = txt.match(/Round\s*(\d+),?\s*Pick\s*(\d+)/i))) {
      round = +m[1];
      const p = +m[2];
      if (!pick) pick = p > teams ? p : (round - 1) * teams + p;
    }
    if (!round && (m = txt.match(/RND\s*(\d+)\s*OF\s*\d+/i))) round = +m[1];
    if (!round && pick) round = Math.ceil(pick / teams);
    const clock = (txt.match(/\b(\d{1,2}:\d{2})\b/) || [])[1] || null;
    const youOnClock = /(you('| a)re on the clock|your pick|it'?s your turn|you are up)/i.test(txt);
    const complete = /draft (is )?complete/i.test(txt);
    return { pick, round, clock, youOnClock, complete };
  }

  // Our roster: look for a "My Team"/"Roster" container and read position-slot lines.
  function readRoster(doc) {
    const counts = { QB: 0, RB: 0, WR: 0, TE: 0, DST: 0, K: 0 };
    const players = [];
    const cands = Array.from(doc.querySelectorAll("section, div, aside")).filter(e => {
      const h = (e.firstElementChild && e.firstElementChild.textContent || "").trim();
      return /^(my team|my roster|roster)\b/i.test(h);
    });
    const box = cands.sort((a, b) => (a.textContent.length - b.textContent.length))[0];
    if (!box) return { counts, players, found: false };
    const f = lines(box);
    for (let i = 0; i < f.length; i++) {
      // Pattern: "RB" slot label followed by "Player Name" then "TEAM RB" or similar.
      const p = parseRowLines(f.slice(i, i + 4).concat(["0"]));
      if (p && !players.find(x => x.name === p.name) && !/empty/i.test(p.name)) { players.push(p); counts[p.pos] = (counts[p.pos] || 0) + 1; i += 2; }
    }
    return { counts, players, found: true };
  }

  function readAutopick(doc) {
    const els = Array.from(doc.querySelectorAll("label, button, div, span")).filter(e => e.children.length < 4 && /auto[\s-]?pick|auto[\s-]?draft/i.test(e.textContent || "") && (e.textContent || "").length < 60);
    for (const e of els) {
      const scope = e.closest("label, div") || e;
      const sw = scope.querySelector('input[type=checkbox], [role=switch], [aria-checked], [aria-pressed]');
      if (sw) {
        const on = sw.checked === true || sw.getAttribute("aria-checked") === "true" || sw.getAttribute("aria-pressed") === "true";
        return on ? "ON" : "OFF";
      }
      if (/autopick\s*(is\s*)?on|autopick enabled/i.test(e.textContent)) return "ON";
    }
    return "unknown";
  }

  const api = { parseRowLines, readPlayers, readClock, readRoster, readAutopick };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else root.QBZParser = api;
})(typeof self !== "undefined" ? self : this);
