from pathlib import Path
t = Path("index.html").read_text(encoding="utf-8")
start = t.find('<section class="hero"')
end = t.find('</section>', start) + len('</section>')
block = t[start:end]
# balance divs
opens = block.count('<div')
closes = block.count('</div>')
print('hero section div balance:', opens, 'open', closes, 'close', 'OK' if opens == closes else 'MISMATCH')
print('has command center:', 'hero-command-center' in block)
print('has old video:', 'heroShowcaseVideo' in block)
print('has old device:', 'hero-showcase-device' in block)
