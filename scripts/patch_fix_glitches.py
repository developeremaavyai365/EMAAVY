"""Remove visual glitches: scanlines, mesh grids, conflicting CSS, decorative lines."""
from pathlib import Path
import re

HTML = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"

GLITCH_KILL = """
/* ═══ GLITCH-FREE LANDING — hide line artifacts & overlays ═══ */
.scanlines,
.grain,
.ambient,
.masthead-scan,
.hero-glow-layer,
.hero-showcase::before,
.hero-showcase-device::before,
.hero-showcase-header::after,
.hero-showcase-shimmer,
.hero-showcase-vignette,
.hero-showcase-livefx,
#how-it-works .hiw-mesh,
#how-it-works .hiw-mesh-lines,
.int-shell::before,
.telephony-shell::before,
.template-shell::before,
.workflow-shell::before,
.platform-shell::before,
.cap-section::before,
#how-it-works::before,
.template-shell::before,
.nav-dropdown-menu-glow,
.section-kicker::before,
.signal-chip-glow,
.hiw-step-glow,
.feature-card-glow,
.h-card-glow,
.workflow-node-scanline,
.workflow-node-glow,
.workflow-pulse,
.platform-hub-glow,
.platform-hub-ring,
.platform-marquee-pill-glow,
.platform-chip-glow,
.hero-eyebrow::before,
#integrations .telephony-scanline,
#integrations .telephony-hero-scanline,
#integrations .int-scanline,
#integrations .int-card-scanline,
.template-card-scanline {
  display: none !important;
  animation: none !important;
  opacity: 0 !important;
  visibility: hidden !important;
  pointer-events: none !important;
}

/* Kill animated top accent bars (1–4px lines on sections) */
.int-shell::before,
.telephony-shell::before,
.template-shell::before,
.workflow-shell::before,
.platform-shell::before,
.cap-section::before,
#how-it-works::before,
.template-shell::before {
  content: none !important;
  height: 0 !important;
}

/* Legacy base hero grid — overridden by ELEGANT HERO block */
.hero {
  display: flex !important;
  min-height: min(100vh, 100dvh) !important;
  align-items: center !important;
  padding: calc(var(--masthead-h-compact, 72px) + 2rem) clamp(1.25rem, 4vw, 3rem) clamp(2rem, 4vw, 3rem) !important;
}

.shell {
  margin-left: 0 !important;
  position: relative !important;
  z-index: 10 !important;
  max-width: 100% !important;
  overflow-x: hidden !important;
}

body {
  overflow-x: hidden !important;
  background: #ffffff !important;
}

/* Softer hero showcase — no moving lines */
.hero-showcase-device {
  animation: none !important;
}
.hero-showcase.is-idle .hero-slide.is-active .hero-slide-frame img {
  animation: none !important;
}
.hero-showcase-eq i {
  animation: none !important;
}

/* HIW arrows only — no stray borders */
#how-it-works.hiw-stage {
  overflow: visible !important;
  background: #ffffff !important;
}

/* Consistent section spacing */
.cap-section,
#how-it-works.hiw-stage,
#integrations {
  margin-bottom: 4rem !important;
}

/* Remove outline stroke glitches on hero title */
.hero-title .line-every .outline,
.hero h1 .outline {
  -webkit-text-stroke: 0 !important;
  color: #64748b !important;
  -webkit-text-fill-color: #64748b !important;
}

/* Platform stats — no blue glow lines */
.platform-stat,
.cap-section .platform-stat {
  backdrop-filter: none !important;
  box-shadow: none !important;
}
.platform-stat:hover,
.cap-section .platform-stat:hover {
  box-shadow: 0 4px 16px rgba(15, 23, 42, 0.06) !important;
}

@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}

"""

def main():
    text = HTML.read_text(encoding="utf-8")

    # Remove mesh elements from HTML
    text = text.replace(
        ' <div class="hiw-mesh" aria-hidden="true"></div> <div class="hiw-mesh-lines" aria-hidden="true"></div>',
        "",
    )
    text = text.replace('<div class="hiw-mesh" aria-hidden="true"></div>\n  <div class="hiw-mesh-lines" aria-hidden="true"></div>\n', "")

    # Remove duplicate hero rhythm block (merged into glitch kill)
    text = re.sub(
        r"/\* Hero .*? sections rhythm \*/\s*\.hero \{\s*margin-bottom: 0 !important;\s*\}\s*#how-it-works\.hiw-stage \{\s*margin-top: 0 !important;\s*\}\s*",
        "",
        text,
        count=1,
    )

    # Inject glitch-kill before ELEGANT NAVBAR
    nav_marker = "/* ═══ ELEGANT NAVBAR — refined, no glow ═══ */"
    if "GLITCH-FREE LANDING" not in text:
        text = text.replace(nav_marker, GLITCH_KILL + nav_marker, 1)
        print("injected glitch-kill CSS")
    else:
        print("glitch-kill already present")

    # Strengthen existing disable block at top of style (lines 11-12 area)
    old_anim = ".int-shell::before, #how-it-works::before, .cap-section::before"
    if old_anim in text and "hiw-mesh" not in text.split(old_anim)[0][-200:]:
        pass  # glitch kill handles it

    # Hide scanlines in base if still visible — patch base block
    if ".scanlines {" in text and "GLITCH-FREE" in text:
        text = re.sub(
            r"\.scanlines \{[^}]+\}",
            ".scanlines { display: none !important; }",
            text,
            count=1,
        )
        text = re.sub(
            r"\.grain \{[^}]+\}",
            ".grain { display: none !important; }",
            text,
            count=1,
        )
        text = re.sub(
            r"\.ambient \{[^}]+\}",
            ".ambient { display: none !important; }",
            text,
            count=1,
        )
        print("patched base scanlines/grain/ambient")

    # masthead-scan animation off
    if ".masthead-scan {" in text:
        text = re.sub(
            r"\.masthead-scan \{[^}]+\}",
            ".masthead-scan { display: none !important; }",
            text,
            count=1,
        )

    # Fix corrupted shell merge on line 3 if present
    text = text.replace(
        ".masthead-go:hover { box-shadow: 0 0 24px rgba(56, 189, 248, 0.6), 0 0 48px rgba(56, 189, 248, 0.35), inset 0 0 12px rgba(255,255,255,0.15); transform: none; } .shell {\n  display: block !important;\n margin-left: 0; position: relative; z-index: 10; }",
        ".masthead-go:hover { box-shadow: none !important; transform: none; } .shell { margin-left: 0; position: relative; z-index: 10; }",
    )

    # Remove hero asymmetric comment block start if we can neutralize via !important in glitch kill - already done

    # section-kicker ::before can show vertical lines - ensure hidden globally  
    if ".section-kicker::before" not in text.split("GLITCH-FREE")[1][:500]:
        pass
    text = text.replace(
        ".signal-chip-glow, .hiw-step-glow",
        ".section-kicker::before, .signal-chip-glow, .hiw-step-glow",
        1,
    )

    HTML.write_text(text, encoding="utf-8")
    print("done")


if __name__ == "__main__":
    main()
