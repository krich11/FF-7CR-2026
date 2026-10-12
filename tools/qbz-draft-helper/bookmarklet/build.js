// Build: node bookmarklet/build.js  (needs terser: npm i terser, or NODE_PATH pointing to it)
const fs = require("fs"), path = require("path"), { minify } = require("terser");
const d = path.join(__dirname, "..");
const src = ["rules.js", "parser.js", "bookmarklet/panel.js"].map(f => fs.readFileSync(path.join(d, f), "utf8")).join("\n;\n");
(async () => {
  const out = await minify("(function(){var module;" + src + "})();", { compress: { passes: 2 }, mangle: true, format: { comments: false } });
  fs.writeFileSync(path.join(__dirname, "qbz-bookmarklet.min.js"), out.code);
  const url = "javascript:" + encodeURI(out.code);
  fs.writeFileSync(path.join(__dirname, "bookmarklet.txt"), url);
  console.log("minified", out.code.length, "chars; bookmarklet", url.length, "chars");
})();
