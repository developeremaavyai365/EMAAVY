from pathlib import Path
t = Path("index.html").read_text(encoding="utf-8")
print("is-active on agents slide:", 'class="hcc-slide is-active" data-slide="agents"' in t)
print("presentation aria-hidden:", 'hcc-presentation" aria-label="Emaavy capability presentation" aria-hidden="true"' in t)
print("slides without active:", t.count('class="hcc-slide" data-slide='))
start = t.find('class="hcc-stage"')
end = t.find('</section>', t.find('id="top"'))
block = t[start:end]
print("stage div balance", block.count('<div'), block.count('</div>'))
