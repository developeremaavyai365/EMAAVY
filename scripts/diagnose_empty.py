from pathlib import Path
t = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
text = t.read_text(encoding="utf-8")
markers = [
    "class=\"hero\"", "class=\"shell\"", "id=\"top\"", "signal-band",
    "INTEGRATIONS HUB", "detailData", "<script>", "</script>",
]
for m in markers:
    idx = text.find(m)
    print(f"{m!r}: {idx}")

bi = text.find("<body")
ei = text.find("</body>")
body = text[bi:ei]
print(f"body length: {len(body)}")
print(f"hero in body: {'class=\"hero\"' in body}")
print(f"shell in body: {'class=\"shell\"' in body}")

# Check JS syntax with node if available
script_start = text.rfind("<script>")
script_end = text.rfind("</script>")
if script_start >= 0:
    js = text[script_start+8:script_end]
    print(f"script length: {len(js)}")
    # find detailData corruption - img tags with unescaped quotes
    if "logo: '<img src=\"" in js or 'logo: "<img' in js:
        print("WARN: double-quoted img in detailData logo strings")
