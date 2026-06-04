from pathlib import Path
import re

PATH = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
html = PATH.read_text(encoding="utf-8")
start = html.find("<!-- INTEGRATIONS HUB -->")
end = len(html)
for needle in ['<section id="pricing"', "<footer class=", "</main>"]:
    i = html.find(needle, start + 50)
    if i > start:
        end = min(end, i)
chunk = html[start:end]

def ensure(sub, repl, text):
    if sub in text and repl not in text.replace(sub, repl, 1):
        pass
    return text.replace(sub, repl) if sub in text else text

# Force reveal on all card types (idempotent)
chunk = re.sub(
    r'<article class="int-card (?!reveal )',
    '<article class="int-card reveal ',
    chunk,
)
chunk = chunk.replace(
    '<article class="int-card reveal reveal ',
    '<article class="int-card reveal ',
)
if 'class="call-flow reveal"' not in chunk:
    chunk = chunk.replace('<div class="call-flow" ', '<div class="call-flow reveal" ')

html = html[:start] + chunk + html[end:]
PATH.write_text(html, encoding="utf-8")
print("reveal articles", chunk.count('int-card reveal'))
print("call-flow reveal", chunk.count('call-flow reveal'))
