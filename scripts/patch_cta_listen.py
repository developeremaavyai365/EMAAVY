"""Replace CTA split section with creative signal chamber design."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "emaavy_white_blue (2).html"
CSS_FILE = ROOT / "assets" / "cta-listen.css"

OLD_CTA = re.compile(
    r'<!-- CTA --> <section class="cta-split reveal" id="cta">.*?</section>',
    re.DOTALL,
)

NEW_CTA = """<!-- CTA --> <section class="cta-listen reveal" id="cta">
  <div class="cta-listen-grid">
    <div class="cta-listen-copy">
      <span class="cta-listen-eyebrow"><span class="cta-live-dot" aria-hidden="true"></span> Live call intelligence</span>
      <h2>Your calls are talking.<br /><span class="cta-gradient-line">Start listening.</span></h2>
      <p class="cta-listen-lead">Every conversation is already full of intent, objections, and revenue signals — EMAAVY captures them in real time, scores them live, and pushes action to your CRM before the line goes cold.</p>
      <div class="cta-trust-row">
        <span class="cta-trust-pill"><strong>Free</strong> tier to start</span>
        <span class="cta-trust-pill"><strong>No</strong> credit card</span>
        <span class="cta-trust-pill"><strong>&lt;48h</strong> go-live</span>
        <span class="cta-trust-pill"><strong>22</strong> languages</span>
      </div>
      <div class="cta-listen-actions">
        <a href="book-demo.html" class="btn-cta-primary" data-magnetic>Get started free →</a>
        <button type="button" class="btn-cta-ghost" data-open-demo>Watch it live</button>
      </div>
    </div>
    <div class="cta-signal-stage" aria-hidden="true">
      <div class="cta-signal-grid-bg"></div>
      <div class="cta-signal-stats">
        <span class="cta-signal-stat"><b>LIVE</b> Transcribing</span>
        <span class="cta-signal-stat"><b>0.4s</b> Latency</span>
      </div>
      <div class="cta-float-card cta-float-card--tl">
        <span class="cta-float-label">Transcript</span>
        <p id="ctaTranscriptLine">"I'd like to book the demo for Thursday…"</p>
        <span class="cta-float-meta">Streaming · EN</span>
      </div>
      <div class="cta-float-card cta-float-card--tr">
        <span class="cta-float-label">Intent</span>
        <p>High buy signal detected</p>
        <div class="cta-intent-bar"><i></i></div>
        <span class="cta-float-meta">+87% score</span>
      </div>
      <div class="cta-float-card cta-float-card--bl">
        <span class="cta-float-label">CRM sync</span>
        <p>HubSpot deal stage → Negotiation</p>
        <span class="cta-float-meta">Webhook fired</span>
      </div>
      <div class="cta-float-card cta-float-card--br">
        <span class="cta-float-label">Sentiment</span>
        <p>Positive arc · last 30s</p>
        <span class="cta-float-meta">Coach alert off</span>
      </div>
      <div class="cta-signal-core">
        <span class="cta-signal-ring"></span>
        <span class="cta-signal-ring"></span>
        <span class="cta-signal-ring"></span>
        <div class="cta-signal-hub">
          <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a3 3 0 0 1 3 3v7a3 3 0 0 1-6 0V5a3 3 0 0 1 3-3z"/><path d="M19 11v1a7 7 0 0 1-14 0v-1"/><path d="M12 19v3"/></svg>
        </div>
      </div>
      <div class="cta-waveform" aria-hidden="true">
        <span></span><span></span><span></span><span></span><span></span><span></span>
        <span></span><span></span><span></span><span></span><span></span><span></span>
      </div>
    </div>
  </div>
</section>"""


def main():
    text = HTML.read_text(encoding="utf-8")
    css = CSS_FILE.read_text(encoding="utf-8")

    if "/* ═══ CTA — Your calls are talking ═══ */" not in text:
        insert_marker = "@media (max-width: 960px) {\n  .faq-promo { grid-template-columns: 1fr !important; }"
        if insert_marker not in text:
            raise SystemExit("insert marker not found")
        text = text.replace(
            insert_marker,
            css.strip() + "\n\n" + insert_marker,
            1,
        )

    if not OLD_CTA.search(text):
        raise SystemExit("old CTA section not found")
    text = OLD_CTA.sub(NEW_CTA, text, count=1)

    if "cta-listen.css" not in text:
        text = text.replace(
            '<link rel="stylesheet" href="assets/nav.css" />',
            '<link rel="stylesheet" href="assets/nav.css" />\n  <link rel="stylesheet" href="assets/cta-listen.css" />',
            1,
        )

    particle_block = re.compile(
        r"/\* CTA particles \*/ const ctaCanvas = document\.getElementById\('ctaParticles'\);.*?drawCta\(\); ",
        re.DOTALL,
    )
    text = particle_block.sub("", text)

    if "cta-listen.js" not in text:
        text = text.replace(
            '<script src="assets/hero-showcase.js" defer></script>',
            '<script src="assets/cta-listen.js" defer></script>\n<script src="assets/hero-showcase.js" defer></script>',
            1,
        )

    HTML.write_text(text, encoding="utf-8")
    print("OK: CTA listen section patched")


if __name__ == "__main__":
    main()
