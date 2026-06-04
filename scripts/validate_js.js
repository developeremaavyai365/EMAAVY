const fs = require("fs");
const path = String.raw`c:\Users\DELL\Desktop\New folder (3)\emaavy\index.html`;
const t = fs.readFileSync(path, "utf8");
const navIdx = t.indexOf("assets/nav.js");
const s = t.indexOf("<script>", navIdx);
const e = t.lastIndexOf("</script>");
const js = t.slice(s + 8, e);
try {
  new Function(js);
  console.log("JS parse OK, length", js.length);
} catch (err) {
  console.log("JS ERROR:", err.message);
  const m = /position (\d+)/.exec(err.message);
  if (m) {
    const pos = Number(m[1]);
    console.log("context:", js.slice(Math.max(0, pos - 80), pos + 80));
  }
}
