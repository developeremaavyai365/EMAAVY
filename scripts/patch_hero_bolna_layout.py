"""Flatten hero to Bolna-style vertical stack; keep EMAAVY colors."""
from pathlib import Path

HTML_PATH = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"

OLD_INNER = (
    '<div class="hero-center"> <div class="hero-brand"> <div class="hero-brand-stack"> '
    '<span class="hero-brand-letters" aria-hidden="true"> <span class="hero-brand-letter">E</span> '
    '<span class="hero-brand-letter">M</span> <span class="hero-brand-letter">A</span> '
    '<span class="hero-brand-letter">A</span> <span class="hero-brand-letter">V</span> '
    '<span class="hero-brand-letter">Y</span> </span> </div> <p class="hero-tagline">Call Intelligence</p> </div> '
    '<div class="hero-headline"> <p class="hero-headline-kicker"><span class="hero-headline-kicker-line" aria-hidden="true"></span>'
    '<span>Every call. Fully understood.</span><span class="hero-headline-kicker-line" aria-hidden="true"></span></p> '
    '<h1 class="hero-title" aria-label="Decode every call"> <span class="line line-decode"><span class="inner">Decode</span></span> '
    '<span class="line line-every"><span class="inner outline">every</span></span> '
    '<span class="line line-call"><span class="inner glow">call<span class="hero-title-mark" aria-hidden="true">.</span></span></span> '
    '</h1> <p class="hero-pitch">Record, transcribe, and act on every call—<strong>one enterprise platform</strong> '
    'built so your team never misses what matters.</p> </div> <div class="hero-actions"> '
    '<button class="btn-magnetic btn-fill" type="button" data-open-demo>Try EMAAVY</button> </div> </div>'
)

NEW_INNER = (
    '<div class="hero-center"> <p class="hero-badge">'
    '<span class="hero-badge-dot" aria-hidden="true"></span> Every call. Fully understood.</p> '
    '<div class="hero-brand"> <div class="hero-brand-stack"> '
    '<span class="hero-brand-letters" aria-hidden="true"> <span class="hero-brand-letter">E</span> '
    '<span class="hero-brand-letter">M</span> <span class="hero-brand-letter">A</span> '
    '<span class="hero-brand-letter">A</span> <span class="hero-brand-letter">V</span> '
    '<span class="hero-brand-letter">Y</span> </span> </div> <p class="hero-tagline">Call Intelligence</p> </div> '
    '<h1 class="hero-title" aria-label="Decode every call"> <span class="line line-decode"><span class="inner">Decode</span></span> '
    '<span class="line line-every"><span class="inner outline">every</span></span> '
    '<span class="line line-call"><span class="inner glow">call<span class="hero-title-mark" aria-hidden="true">.</span></span></span> '
    '</h1> <p class="hero-pitch">Record, transcribe, and act on every call—<strong>one enterprise platform</strong> '
    'built so your team never misses what matters.</p> '
    '<div class="hero-actions"> <button class="btn-magnetic btn-fill" type="button" data-open-demo>Try EMAAVY</button> </div> </div>'
)

CSS_OLD = """.hero-headline {
  position: relative !important;
  width: 100% !important;
  margin: 0 !important;
  flex: 1 1 auto !important;
  min-height: 0 !important;
  display: flex !important;
  flex-direction: column !important;
  justify-content: center !important;
  padding: clamp(0.65rem, 1.8vh, 1.15rem) clamp(0.85rem, 2.5vw, 1.5rem) clamp(0.75rem, 1.6vh, 1.1rem) !important;
  text-align: center !important;
  border-radius: 20px !important;
  border: 1px solid #e2e8f0 !important;
  background:
    linear-gradient(180deg, #ffffff 0%, #f8fafc 55%, #f1f5f9 100%) !important;
  box-shadow:
    0 1px 2px rgba(15, 23, 42, 0.04),
    0 24px 48px -12px rgba(30, 64, 175, 0.12),
    inset 0 1px 0 rgba(255, 255, 255, 0.9) !important;
  isolation: isolate !important;
}
.hero-headline::before {
  content: '' !important;
  position: absolute !important;
  inset: 12% 8% auto !important;
  height: 58% !important;
  border-radius: 50% !important;
  background: radial-gradient(ellipse at center, rgba(37, 99, 235, 0.14) 0%, transparent 72%) !important;
  pointer-events: none !important;
  z-index: 0 !important;
}
.hero-headline::after {
  content: '' !important;
  position: absolute !important;
  left: 50% !important;
  bottom: 0 !important;
  transform: translateX(-50%) !important;
  width: min(140px, 32%) !important;
  height: 3px !important;
  border-radius: 999px !important;
  background: linear-gradient(90deg, transparent, #2563eb 20%, #3b82f6 50%, #2563eb 80%, transparent) !important;
  opacity: 0.85 !important;
  pointer-events: none !important;
  z-index: 2 !important;
}
.hero-headline-kicker {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 0.85rem !important;
  margin: 0 0 clamp(0.45rem, 1vh, 0.75rem) !important;
  font-size: clamp(0.55rem, 1.2vh, 0.65rem) !important;
  font-weight: 600 !important;
  letter-spacing: 0.2em !important;
  text-transform: uppercase !important;
  color: #475569 !important;
  position: relative !important;
  z-index: 1 !important;
}
.hero-headline-kicker-line {
  display: block !important;
  width: clamp(28px, 8vw, 52px) !important;
  height: 1px !important;
  background: linear-gradient(90deg, transparent, #93c5fd 55%, #2563eb 100%) !important;
}
.hero-headline-kicker-line:last-child {
  background: linear-gradient(90deg, #2563eb, #93c5fd 45%, transparent) !important;
}
"""

CSS_NEW = """/* Bolna-inspired stack: badge → brand → headline → pitch → CTA */
.hero-badge {
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 0.5rem !important;
  margin: 0 !important;
  padding: 0.42rem 0.9rem !important;
  border-radius: 999px !important;
  background: #f8fafc !important;
  border: 1px solid #e2e8f0 !important;
  font-family: 'General Sans', system-ui, sans-serif !important;
  font-size: clamp(0.62rem, 1.25vh, 0.72rem) !important;
  font-weight: 600 !important;
  letter-spacing: 0.12em !important;
  text-transform: uppercase !important;
  color: #475569 !important;
  flex-shrink: 0 !important;
}
.hero-badge-dot {
  width: 6px !important;
  height: 6px !important;
  border-radius: 50% !important;
  background: #2563eb !important;
  flex-shrink: 0 !important;
}
.hero-title,
.hero h1.hero-title {
  flex-shrink: 0 !important;
  margin: 0 !important;
}
"""

CSS_CENTER_PATCH_OLD = """  max-width: 820px !important;
  max-height: calc(100dvh - var(--masthead-h-compact) - 1.5rem) !important;
  margin: 0 auto !important;
  flex: 1 1 auto !important;
  min-height: 0 !important;
  gap: clamp(0.35rem, 1.2vh, 0.75rem) !important;
"""

CSS_CENTER_PATCH_NEW = """  max-width: 640px !important;
  max-height: calc(100dvh - var(--masthead-h-compact) - 1.5rem) !important;
  margin: 0 auto !important;
  flex: 1 1 auto !important;
  min-height: 0 !important;
  gap: clamp(0.5rem, 2vh, 1.25rem) !important;
"""

CSS_PITCH_OLD = """  margin: clamp(0.5rem, 1.2vh, 0.85rem) auto 0 !important;
  padding-top: clamp(0.5rem, 1.1vh, 0.75rem) !important;
  border-top: 1px solid rgba(226, 232, 240, 0.9) !important;
"""

CSS_PITCH_NEW = """  margin: 0 auto !important;
  padding-top: 0 !important;
  border-top: none !important;
  max-width: 32rem !important;
"""

CSS_MEDIA_OLD = """  .hero-headline-kicker {
    margin-bottom: 0.35rem !important;
  }
  .hero-pitch {
    line-height: 1.35 !important;
    margin-top: 0.4rem !important;
    padding-top: 0.4rem !important;
  }
"""

CSS_MEDIA_NEW = """  .hero-pitch {
    line-height: 1.35 !important;
  }
"""

CSS_MEDIA2_OLD = """  .hero-headline {
    border-radius: 14px !important;
  }
  .hero-headline-kicker {
    gap: 0.45rem !important;
    letter-spacing: 0.12em !important;
  }
"""

CSS_MEDIA2_NEW = """  .hero-badge {
    letter-spacing: 0.1em !important;
    padding: 0.38rem 0.75rem !important;
  }
"""


def main():
    text = HTML_PATH.read_text(encoding="utf-8")
    if OLD_INNER not in text:
        # try with corrupted em dash
        alt = OLD_INNER.replace("—", "\u2014").replace("call—", "call")
        if alt not in text:
            # fuzzy: find hero-center start
            start = text.find('<div class="hero-center">')
            end = text.find("</div> </div> <a href=\"#snapshots\"", start)
            if start < 0 or end < 0:
                raise SystemExit("hero-center block not found")
            snippet = text[start:end + len("</div> </div>")]
            print("Found block len", len(snippet))
            text = text[:start] + NEW_INNER + text[end + len("</div> </div>") :]
        else:
            text = text.replace(alt, NEW_INNER, 1)
    else:
        text = text.replace(OLD_INNER, NEW_INNER, 1)

    if CSS_OLD not in text:
        raise SystemExit("CSS headline block not found")
    text = text.replace(CSS_OLD, CSS_NEW, 1)
    text = text.replace(CSS_CENTER_PATCH_OLD, CSS_CENTER_PATCH_NEW, 1)
    text = text.replace(CSS_PITCH_OLD, CSS_PITCH_NEW, 1)
    text = text.replace(CSS_MEDIA_OLD, CSS_MEDIA_NEW, 1)
    text = text.replace(CSS_MEDIA2_OLD, CSS_MEDIA2_NEW, 1)

    # Fix scroll tag duplicate display
    text = text.replace(
        ".hero-scroll-tag {\n  display: none !important;\n  position: absolute !important;",
        ".hero-scroll-tag {\n  display: none !important;\n  position: absolute !important;",
        1,
    )
    block = """.hero-scroll-tag {
  display: none !important;
  position: absolute !important;
  bottom: 1.5rem !important;
  left: 50% !important;
  transform: translateX(-50%) !important;
  display: inline-flex !important;"""
    if block in text:
        text = text.replace(
            block,
            """.hero-scroll-tag {
  display: none !important;
  position: absolute !important;
  bottom: 1.5rem !important;
  left: 50% !important;
  transform: translateX(-50%) !important;""",
            1,
        )

    HTML_PATH.write_text(text, encoding="utf-8")
    print("Hero layout updated:", HTML_PATH.name)


if __name__ == "__main__":
    main()
