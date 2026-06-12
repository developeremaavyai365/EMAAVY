from pathlib import Path
t = Path("index.html").read_text(encoding="utf-8")
start = t.find('class="hero-showcase hero-command-center"')
end = t.find('</section>', start)
Path("scripts/_showcase_snippet.txt").write_text(t[start:end], encoding="utf-8")
print(len(t[start:end]))
