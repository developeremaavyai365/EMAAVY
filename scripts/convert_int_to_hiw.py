#!/usr/bin/env python3
"""Convert integration cards to hiw-step markup (same as How It Works)."""
from pathlib import Path
import re
from html.parser import HTMLParser

PATH = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"

HIW_HINT = "Tap for details →"


class CardParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_article = False
        self.article_attrs = {}
        self.stack = []
        self.data_detail = ""
        self.logo_img = ""
        self.title = ""
        self.desc = ""
        self.tag = ""
        self.provider = ""
        self.cta = ""
        self._capture = None
        self._buf = []

    def handle_starttag(self, tag, attrs):
        attrs_d = dict(attrs)
        if tag == "article" and not self.in_article:
            cls = attrs_d.get("class", "")
            if "click-detail" in cls or "int-card" in cls:
                self.in_article = True
                self.data_detail = attrs_d.get("data-detail", "")
                self.article_attrs = attrs_d
        if not self.in_article:
            return
        if tag == "img" and "int-card-logo" in " ".join(
            self.stack[-3:] if len(self.stack) >= 3 else self.stack
        ):
            pass
        if tag == "img" and any("int-card-logo" in s for s in self.stack):
            src = attrs_d.get("src", "")
            alt = attrs_d.get("alt", "")
            if src:
                self.logo_img = f'<img src="{src}" alt="{alt}" loading="lazy" decoding="async" />'
        if tag in ("h4", "p", "span", "footer"):
            cls = attrs_d.get("class", "")
            if "llm-card-provider" in cls or "stt-card-provider" in cls:
                self._capture = "provider"
                self._buf = []
            elif tag == "h4":
                self._capture = "title"
                self._buf = []
            elif "llm-card-desc" in cls or "stt-card-desc" in cls or (
                tag == "p" and "tel-card-body" in " ".join(self.stack)
            ):
                self._capture = "desc"
                self._buf = []
            elif "tel-card-tag" in cls or "llm-card-tag" in cls or "stt-card-tag" in cls:
                self._capture = "tag"
                self._buf = []
            elif "tel-card-cta" in cls or "llm-card-cta" in cls or "stt-card-cta" in cls or "int-card-hint" in cls:
                self._capture = "cta"
                self._buf = []
        self.stack.append(tag + (":" + attrs_d.get("class", "") if attrs_d.get("class") else ""))

    def handle_endtag(self, tag):
        if self.stack:
            self.stack.pop()
        if not self.in_article:
            return
        if tag == "article":
            self.in_article = False

    def handle_data(self, data):
        if not self.in_article or not self._capture:
            # fallback: img in logo div
            return
        t = data.strip()
        if not t:
            return
        if self._capture == "provider":
            self.provider = t
        elif self._capture == "title":
            self.title = t
        elif self._capture == "desc":
            self.desc = t
        elif self._capture == "tag":
            self.tag = t
        elif self._capture == "cta":
            self.cta = t
        self._capture = None


def parse_article_html(article_html: str) -> dict:
    """Extract fields from one article element string."""
    detail = ""
    m = re.search(r'data-detail="([^"]*)"', article_html)
    if m:
        detail = m.group(1)

    logo = ""
    m = re.search(
        r'<div class="int-card-logo"[^>]*>(.*?)</div>',
        article_html,
        re.DOTALL | re.I,
    )
    if m:
        inner = m.group(1).strip()
        if "<img" in inner:
            logo = inner
        else:
            bm = re.search(r'<span class="brand-mark"[^>]*>([^<]*)</span>', inner)
            if bm:
                logo = f'<span class="brand-mark">{bm.group(1).strip()}</span>'

    title = ""
    m = re.search(r"<h4[^>]*>([^<]*)</h4>", article_html, re.I)
    if m:
        title = m.group(1).strip()

    desc = ""
    for pat in [
        r'<p class="llm-card-desc"[^>]*>([^<]*)</p>',
        r'<p class="stt-card-desc"[^>]*>([^<]*)</p>',
        r'<div class="tel-card-body"[^>]*>.*?<p[^>]*>([^<]*)</p>',
        r'<p class="[^"]*">([^<]*)</p>',
    ]:
        m = re.search(pat, article_html, re.DOTALL | re.I)
        if m:
            desc = re.sub(r"\s+", " ", m.group(1)).strip()
            if desc and desc != title:
                break

    tag = ""
    for pat in [
        r'<span class="tel-card-tag"[^>]*>([^<]*)</span>',
        r'<span class="llm-card-tag"[^>]*>([^<]*)</span>',
        r'<span class="stt-card-tag"[^>]*>([^<]*)</span>',
        r'<span class="int-card-tag"[^>]*>([^<]*)</span>',
    ]:
        m = re.search(pat, article_html, re.I)
        if m:
            tag = m.group(1).strip()
            break

    provider = ""
    m = re.search(r'<p class="llm-card-provider"[^>]*>([^<]*)</p>', article_html, re.I)
    if m:
        provider = m.group(1).strip()
    if not provider:
        m = re.search(r'<p class="stt-card-provider"[^>]*>([^<]*)</p>', article_html, re.I)
        if m:
            provider = m.group(1).strip()

    if provider and provider != title and not desc.startswith(provider):
        pass  # title stays h4; provider could prefix desc if title empty
    if not title and provider:
        title = provider

    hint = HIW_HINT
    m = re.search(
        r'<span class="(?:tel-card-cta|llm-card-cta|stt-card-cta|int-card-hint)"[^>]*>([^<]*)</span>',
        article_html,
        re.I,
    )
    if m and "tap" in m.group(1).lower():
        hint = m.group(1).strip()

    return {
        "detail": detail,
        "logo": logo,
        "title": title,
        "desc": desc,
        "tag": tag,
        "hint": hint,
    }


def build_hiw_step(data: dict, index: int) -> str:
    detail = data["detail"]
    logo = data["logo"]
    title = data["title"] or "Partner"
    desc = data["desc"] or ""
    tag = data["tag"] or "Integration"
    hint = data["hint"] or HIW_HINT

    num_inner = logo if logo else str(index)
    num = f'<div class="hiw-step-num">{num_inner}</div>'

    parts = [
        f'<article class="hiw-step reveal click-detail" data-detail="{detail}" tabindex="0">',
        num,
        '<span class="hiw-step-icon" aria-hidden="true"></span>',
        f"<h4>{title}</h4>",
        f"<p>{desc}</p>",
        f'<span class="hiw-step-tag">{tag}</span>',
        f'<span class="hiw-step-hint">{hint}</span>',
        "</article>",
    ]
    return "".join(parts)


ARTICLE_RE = re.compile(
    r'<article\b[^>]*class="[^"]*\bint-card\b[^"]*"[^>]*>.*?</article>',
    re.DOTALL | re.I,
)


def convert_section(html: str) -> str:
    marker = "<!-- INTEGRATIONS HUB -->"
    start = html.find(marker)
    if start < 0:
        raise SystemExit("integrations marker not found")
    m = re.search(
        r"<!-- INTEGRATIONS HUB --> <section id=\"integrations\"[^>]*>.*?</section>",
        html[start:],
        re.DOTALL,
    )
    if not m:
        raise SystemExit("integrations section not found")
    sec = m.group(0)
    idx = 1

    def repl_article(match):
        nonlocal idx
        data = parse_article_html(match.group(0))
        out = build_hiw_step(data, idx)
        idx += 1
        return out

    sec = ARTICLE_RE.sub(repl_article, sec)
    sec = sec.replace('class="int-cards-grid"', 'class="hiw-steps"')
    return html[:start] + sec + html[start + len(m.group(0)) :]


CSS_BLOCK = r"""
/* ═══ INTEGRATIONS — HIW card system (exact match) ═══ */
#integrations .hiw-steps {
  position: relative !important;
  z-index: 1 !important;
  display: grid !important;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)) !important;
  gap: 0.75rem !important;
  margin-top: 1rem !important;
}
#integrations .hiw-steps::before {
  display: none !important;
}
#integrations .hiw-step {
  position: relative !important;
  z-index: 1 !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  text-align: center !important;
  padding: 1.35rem 1.1rem 1.15rem !important;
  border-radius: 8px !important;
  background: #ffffff !important;
  border: 1px solid #e2e8f0 !important;
  box-shadow: none !important;
  cursor: pointer !important;
  overflow: visible !important;
  isolation: auto !important;
  transition: border-color 0.2s ease, box-shadow 0.2s ease, opacity 0.65s cubic-bezier(0.16, 1, 0.3, 1), transform 0.65s cubic-bezier(0.16, 1, 0.3, 1) !important;
}
#integrations .hiw-step::before {
  display: none !important;
}
#integrations .hiw-step:hover,
#integrations .hiw-step:focus-visible {
  border-color: #cbd5e1 !important;
  box-shadow: 0 4px 16px rgba(15, 23, 42, 0.06) !important;
  outline: none !important;
  transform: none !important;
}
#integrations .hiw-step-num {
  position: relative !important;
  z-index: 1 !important;
  width: 40px !important;
  height: 40px !important;
  border-radius: 8px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  margin: 0 auto 0.85rem !important;
  font-family: 'Clash Display', sans-serif !important;
  font-weight: 600 !important;
  font-size: 0.72rem !important;
  color: #ffffff !important;
  background: #4A658B !important;
  border: none !important;
  box-shadow: none !important;
  transition: background 0.2s ease !important;
  overflow: hidden !important;
  padding: 0 !important;
}
#integrations .hiw-step-num img {
  width: 22px !important;
  height: 22px !important;
  object-fit: contain !important;
  filter: brightness(0) invert(1) !important;
}
#integrations .hiw-step-num .brand-mark {
  font-size: 0.65rem !important;
  font-weight: 700 !important;
  color: #ffffff !important;
  line-height: 1 !important;
}
#integrations .hiw-step:hover .hiw-step-num,
#integrations .hiw-step:focus-visible .hiw-step-num {
  background: #18345D !important;
}
#integrations .hiw-step-icon {
  display: none !important;
}
#integrations .hiw-step h4 {
  position: relative !important;
  z-index: 1 !important;
  font-family: 'Clash Display', sans-serif !important;
  font-size: 1rem !important;
  font-weight: 600 !important;
  color: #0f172a !important;
  margin-bottom: 0.45rem !important;
  transition: color 0.2s ease !important;
}
#integrations .hiw-step:hover h4,
#integrations .hiw-step:focus-visible h4 {
  color: #4A658B !important;
}
#integrations .hiw-step p {
  position: relative !important;
  z-index: 1 !important;
  font-size: 0.85rem !important;
  color: #64748b !important;
  line-height: 1.6 !important;
  margin: 0 0 0.85rem !important;
}
#integrations .hiw-step-tag {
  position: relative !important;
  z-index: 1 !important;
  margin-top: auto !important;
  font-size: 0.6rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.08em !important;
  text-transform: uppercase !important;
  color: #64748b !important;
  background: #f8fafc !important;
  border: 1px solid #e2e8f0 !important;
  border-radius: 4px !important;
  padding: 0.25rem 0.55rem !important;
  box-shadow: none !important;
  transition: background 0.2s ease, border-color 0.2s ease, color 0.2s ease !important;
}
#integrations .hiw-step:hover .hiw-step-tag,
#integrations .hiw-step:focus-visible .hiw-step-tag {
  background: #f0f4f8 !important;
  border-color: #cbd5e1 !important;
  color: #4A658B !important;
}
#integrations .hiw-step-hint {
  position: relative !important;
  z-index: 1 !important;
  margin-top: 0.55rem !important;
  font-size: 0.6rem !important;
  font-weight: 500 !important;
  letter-spacing: 0.06em !important;
  text-transform: uppercase !important;
  color: #94a3b8 !important;
  opacity: 1 !important;
  transition: color 0.2s ease !important;
}
#integrations .hiw-step:hover .hiw-step-hint,
#integrations .hiw-step:focus-visible .hiw-step-hint {
  color: #64748b !important;
}
#integrations .hiw-step.reveal {
  opacity: 0 !important;
  transform: translateY(24px) !important;
}
#integrations .hiw-step.reveal.in {
  opacity: 1 !important;
  transform: translateY(0) !important;
}
#integrations .hiw-steps .hiw-step.reveal:nth-child(1) { transition-delay: 0.04s !important; }
#integrations .hiw-steps .hiw-step.reveal:nth-child(2) { transition-delay: 0.09s !important; }
#integrations .hiw-steps .hiw-step.reveal:nth-child(3) { transition-delay: 0.14s !important; }
#integrations .hiw-steps .hiw-step.reveal:nth-child(4) { transition-delay: 0.19s !important; }
#integrations .hiw-steps .hiw-step.reveal:nth-child(5) { transition-delay: 0.24s !important; }
#integrations .hiw-steps .hiw-step.reveal:nth-child(6) { transition-delay: 0.29s !important; }
#integrations .hiw-steps .hiw-step.reveal:nth-child(7) { transition-delay: 0.34s !important; }
#integrations .hiw-steps .hiw-step.reveal:nth-child(8) { transition-delay: 0.39s !important; }
#integrations .hiw-steps .hiw-step.reveal:nth-child(n+9) { transition-delay: 0.44s !important; }
#integration-llm .hiw-steps,
#integration-stt .hiw-steps,
#integration-telephony .hiw-steps {
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)) !important;
}
@media (max-width: 900px) {
  #integrations .hiw-steps {
    grid-template-columns: repeat(2, 1fr) !important;
  }
}
@media (max-width: 520px) {
  #integrations .hiw-steps {
    grid-template-columns: 1fr !important;
  }
}
@media (prefers-reduced-motion: reduce) {
  #integrations .hiw-step.reveal {
    opacity: 1 !important;
    transform: none !important;
    transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
  }
}
/* Hide legacy integration card chrome */
#integrations .tel-card-head,
#integrations .tel-card-body,
#integrations .tel-card-foot,
#integrations .llm-card-head,
#integrations .llm-card-body,
#integrations .llm-card-foot,
#integrations .stt-card-head,
#integrations .stt-card-body,
#integrations .stt-card-foot,
#integrations .int-card-logo {
  display: contents !important;
}

"""

CSS_MARKER = "/* ═══ INTEGRATIONS — HIW card system (exact match) ═══ */"
OLD_PREMIUM = "/* ═══ INTEGRATIONS PREMIUM — HIW parity"


def inject_css(html: str) -> str:
    if CSS_MARKER in html:
        i = html.find(CSS_MARKER)
        j = html.find("/* ═══ EMAAVY BRAND PALETTE", i)
        if j < 0:
            j = html.find("</style>", i)
        html = html[:i] + CSS_BLOCK + "\n" + html[j:]
        return html
    # remove old premium block targeting int-card reveals
    if OLD_PREMIUM in html:
        i = html.find(OLD_PREMIUM)
        j = html.find("/* ═══ EMAAVY BRAND PALETTE", i)
        html = html[:i] + CSS_BLOCK + "\n" + html[j:]
    else:
        html = html.replace(
            "/* ═══ EMAAVY BRAND PALETTE — white + secondary navy ═══ */",
            CSS_BLOCK + "\n/* ═══ EMAAVY BRAND PALETTE — white + secondary navy ═══ */",
        )
    return html


def main():
    html = PATH.read_text(encoding="utf-8")
    html = convert_section(html)
    html = inject_css(html)
    PATH.write_text(html, encoding="utf-8")
    # verify
    n = html.count('class="hiw-step reveal click-detail"')
    print(f"Converted {n} hiw-step cards")


if __name__ == "__main__":
    main()
