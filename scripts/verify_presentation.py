from pathlib import Path
t = Path("index.html").read_text(encoding="utf-8")
checks = [
    "hcc-orbit-layer", "hcc-presentation", "hcc-pres-back", "hcc-pres-nav--prev",
    "data-slide=\"agents\"", "data-slide=\"sales\"", "hcc-slide-headline",
    "hero-command-center-slides.css", "Knowledge Bases", "Sales Operations",
]
for c in checks:
    print(c, c in t)
# balance inside hcc-stage
start = t.find('class="hcc-stage"')
end = t.find('</div></div>', start)  # approximate
block = t[start:start+80000]
print("slides:", block.count('class="hcc-slide'))
