const D = self.QBZRules.DEFAULT_CONFIG;
const $ = id => document.getElementById(id);
function show(c) {
  $("slot").value = c.slot || 0;
  $("ov").value = (c.overrides || []).map(o => [o.name, o.action, o.note || ""].join(" | ")).join("\n");
  const rest = Object.assign({}, c); delete rest.overrides; delete rest.slot;
  $("cfg").value = JSON.stringify(rest, null, 2);
}
chrome.storage.sync.get({ qbzConfig: null }, v => show(Object.assign({}, D, v.qbzConfig || {})));
$("save").onclick = () => {
  try {
    const c = JSON.parse($("cfg").value);
    c.slot = +$("slot").value || 0;
    c.overrides = $("ov").value.split("\n").map(l => l.split("|").map(s => s.trim())).filter(a => a[0])
      .map(([name, action, note]) => ({ name, action: /block/i.test(action) ? "BLOCK" : "BOOST", note: note || "" }));
    chrome.storage.sync.set({ qbzConfig: c }, () => { $("msg").textContent = "Saved."; });
  } catch (e) { $("msg").textContent = "JSON error: " + e.message; }
};
$("reset").onclick = () => chrome.storage.sync.remove("qbzConfig", () => { show(D); $("msg").textContent = "Reset."; });
