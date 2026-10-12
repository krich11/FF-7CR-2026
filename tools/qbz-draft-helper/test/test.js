// Run: node test/test.js   (synthetic data only; not the live ESPN page)
const assert = require("assert");
const R = require("../rules.js"), P = require("../parser.js");
let n = 0; const t = (name, f) => { f(); n++; console.log("ok -", name); };
const C0 = { QB: 0, RB: 0, WR: 0, TE: 0, DST: 0, K: 0 };
const pool = [
  { name: "Josh Allen", pos: "QB", team: "BUF", tag: "", rank: 1, adp: 20 },
  { name: "De'Von Achane", pos: "RB", team: "MIA", tag: "IR", rank: 2, adp: 12 },
  { name: "Trey McBride", pos: "TE", team: "ARI", tag: "", rank: 3, adp: 30 },
  { name: "Puka Nacua", pos: "WR", team: "LAR", tag: "Q", rank: 4, adp: 10 },
  { name: "Derrick Henry", pos: "RB", team: "BAL", tag: "", rank: 5, adp: 11 },
  { name: "Chargers D/ST", pos: "DST", team: "LAC", tag: "", rank: 6, adp: 150 },
  { name: "Late Guy", pos: "WR", team: "NYJ", tag: "", rank: 7, adp: 60 },
  { name: "Justice Hill", pos: "RB", team: "BAL", tag: "", rank: 80, adp: 140 },
];
t("pick numbers snake slot 12", () => assert.deepStrictEqual(R.ourPicks(12, 12, 4), [12, 13, 36, 37]));
t("R1: RB/WR only, IR blocked, Q flagged", () => {
  const r = R.recommend(pool, { round: 1, pick: 12, counts: C0 });
  assert.strictEqual(r.recs[0].player.name, "Puka Nacua");
  assert.match(r.recs[0].reason, /FLAG: tagged Q/);
  const b = Object.fromEntries(r.blocked.map(x => [x.player.name, x.reason]));
  assert.match(b["De'Von Achane"], /IR before R14/);
  assert.match(b["Josh Allen"], /RB\/WR only/);
  assert.match(b["Late Guy"], /reach >10/);
});
t("QB before R7 blocked; elite fallen QB allowed", () => {
  const st = { round: 3, pick: 25, counts: C0 };
  assert.match(R.check(pool[0], st, R.DEFAULT_CONFIG).reason, /QB before R7/);
  assert.ok(R.check(pool[0], { round: 3, pick: 30, counts: C0 }, R.DEFAULT_CONFIG).ok);
  assert.match(R.check(pool[0], { round: 8, pick: 90, counts: Object.assign({}, C0, { QB: 1 }) }, R.DEFAULT_CONFIG).reason, /already have QB/);
});
t("TE only at/after ADP", () => {
  assert.match(R.check(pool[2], { round: 3, pick: 25, counts: C0 }, R.DEFAULT_CONFIG).reason, /TE before ADP/);
  assert.ok(R.check(pool[2], { round: 3, pick: 30, counts: C0 }, R.DEFAULT_CONFIG).ok);
});
t("D/ST only R15+, IR ok from R14", () => {
  assert.match(R.check(pool[5], { round: 10, pick: 120, counts: C0 }, R.DEFAULT_CONFIG).reason, /before R15/);
  assert.ok(R.check(pool[1], { round: 14, pick: 160, counts: { QB: 1, RB: 5, WR: 4, TE: 1 } }, R.DEFAULT_CONFIG).ok);
});
t("reach cap loosens to 20 in R6-11; fallback labelled REACH", () => {
  const p = { name: "X", pos: "WR", team: "SEA", tag: "", rank: 50, adp: 85 };
  assert.ok(R.check(p, { round: 6, pick: 70, counts: C0 }, R.DEFAULT_CONFIG).ok);
  const r = R.recommend([{ ...p, adp: 110 }], { round: 6, pick: 70, counts: C0 });
  assert.ok(r.recs[0].reach); assert.match(r.recs[0].reason, /REACH/);
});
t("fill guarantee forces needed positions", () => {
  const st = { round: 12, pick: 133, counts: { QB: 1, RB: 2, WR: 4, TE: 1, DST: 0, K: 0 } };
  const r = R.recommend(pool, st);
  assert.strictEqual(r.recs[0].player.pos, "RB");
  const st16 = { round: 16, pick: 181, counts: { QB: 1, RB: 6, WR: 5, TE: 2, DST: 1, K: 0 } };
  const r16 = R.recommend(pool.concat([{ name: "Reichard", pos: "K", team: "MIN", tag: "", rank: 200, adp: 170 }]), st16);
  assert.strictEqual(r16.recs[0].player.pos, "K");
});
t("news BLOCK and BOOST overrides", () => {
  const cfg = { overrides: [{ name: "Puka Nacua", action: "BLOCK", note: "ankle news" }, { name: "derrick henry", action: "BOOST" }] };
  const r = R.recommend(pool, { round: 1, pick: 12, counts: C0 }, cfg);
  assert.strictEqual(r.recs[0].player.name, "Derrick Henry");
  assert.ok(r.blocked.some(b => /news block: ankle news/.test(b.reason)));
});
t("handcuff note for top RB", () => {
  const r = R.recommend(pool, { round: 9, pick: 100, counts: { QB: 1, RB: 2, WR: 3, TE: 1 }, topRb: "Derrick Henry", topRbTeam: "BAL" });
  assert.ok(r.notes.some(x => /Justice Hill/.test(x)));
});
t("turn pair re-plans B with A taken", () => {
  const pr = R.planPair(pool, { round: 1, pick: 12, counts: C0 });
  assert.strictEqual(pr.A.player.name, "Puka Nacua");
  assert.strictEqual(pr.B.player.name, "Derrick Henry");
});
t("parser: row text like the Oct 12 mock", () => {
  assert.deepStrictEqual(P.parseRowLines(["12", "De'Von Achane", "IR", "MIA", "RB", "Draft", "45.2"]),
    { name: "De'Von Achane", pos: "RB", team: "MIA", tag: "IR", rank: 12, adp: 45.2 });
  const q = P.parseRowLines(["3", "Puka Nacua", "Q", "LAR, WR", "DRAFT", "8"]);
  assert.strictEqual(q.pos, "WR"); assert.strictEqual(q.team, "LAR"); assert.strictEqual(q.tag, "Q");
  assert.strictEqual(P.parseRowLines(["Header", "Name"]), null);
});
t("parser: clock text", () => {
  const fake = { body: { innerText: "RND 2 OF 16\n00:28\nON THE CLOCK: PICK 13\nRound 2, Pick 1" } };
  const c = P.readClock(fake, 12);
  assert.strictEqual(c.pick, 13); assert.strictEqual(c.round, 2); assert.strictEqual(c.clock, "00:28");
});
console.log(n + " tests passed");
