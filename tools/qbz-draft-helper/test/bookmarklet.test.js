// Run: NODE_PATH=<dir with jsdom> node test/bookmarklet.test.js  (after node bookmarklet/build.js)
const assert = require("assert"), fs = require("fs"), path = require("path");
const { JSDOM } = require("jsdom");
const txt = fs.readFileSync(path.join(__dirname, "../bookmarklet/bookmarklet.txt"), "utf8");
assert.ok(txt.startsWith("javascript:"));
const code = decodeURI(txt.slice("javascript:".length));
const html = `<body><div>RND 1 OF 16</div><div>00:28</div><div>ON THE CLOCK: PICK 12</div>
<table>${[["1","Puka Nacua","Q","LAR","WR","8"],["2","De'Von Achane","IR","MIA","RB","12"],["3","Derrick Henry","","BAL","RB","11"],["4","Josh Allen","","BUF","QB","20"]]
 .map(r => `<tr>${r.map(c => `<td>${c}</td>`).join("")}<td><button>Draft</button></td></tr>`).join("")}</table></body>`;
const dom = new JSDOM(html, { runScripts: "outside-only", pretendToBeVisual: true, url: "https://fantasy.espn.com/football/draft?leagueId=1" });
const w = dom.window;
// jsdom has no innerText; approximate it with textContent per cell/line.
Object.defineProperty(w.HTMLElement.prototype, "innerText", { get() { return Array.from(this.querySelectorAll("td,div")).length ? Array.from(this.querySelectorAll("td,div")).filter(e => !e.querySelector("td,div")).map(e => e.textContent).join("\n") : this.textContent; } });
w.localStorage.setItem("qbzDraftHelper", JSON.stringify({ slot: 12 }));
const errs = []; w.addEventListener("error", e => errs.push(e.message));
w.eval(code);
assert.deepStrictEqual(errs, []);
const panel = w.document.getElementById("qbz");
assert.ok(panel, "panel built");
const t = panel.textContent;
assert.match(t, /ON THE CLOCK/); assert.match(t, /Puka Nacua/); assert.match(t, /Turn pair/);
assert.match(t, /Derrick Henry/);
// on-the-clock flash
assert.ok(w.document.getElementById("qbzf"), "flash overlay shown");
// recommended row outlined, no clicks on ESPN buttons
let clicked = 0; w.document.querySelectorAll("button").forEach(b => b.addEventListener("click", () => clicked++));
w.__qbz.tick(); assert.strictEqual(clicked, 0);
assert.match(w.document.querySelector("tr").style.outline, /3px/);
// re-tap toggles instead of double-loading
w.eval(code); assert.strictEqual(w.document.querySelectorAll("#qbz").length, 1); assert.strictEqual(panel.style.display, "none");
w.eval(code); assert.strictEqual(panel.style.display, "");
w.__qbz.stop();
console.log("ok - bookmarklet evaluates in jsdom, builds panel, flashes, toggles, never clicks");
