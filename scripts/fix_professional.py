#!/usr/bin/env python3
"""Fix empty logos and remaining professionalization issues."""
import re
from pathlib import Path

HTML = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"

REPLACEMENTS = [
    ('<div class="int-card-logo"><span></span></div><h4>Flash', '<div class="int-card-logo"><img src="https://cdn.simpleicons.org/elevenlabs/0f172a" alt="Flash Bulbul" style="height:24px"/></div><h4>Flash'),
    ('<div class="int-card-logo"><span></span></div><h4>Webhooks', '<div class="int-card-logo"><span class="brand-mark">WH</span></div><h4>Webhooks'),
    ('data-detail="agent-sales"', 'data-detail="agent-sales"'),
    ('<div class="int-card-logo"><span></span></div> <h4>Sales Agent', '<div class="int-card-logo"><span class="brand-mark">SA</span></div> <h4>Sales Agent'),
    ('<div class="int-card-logo"><span></span></div> <h4>Support Agent', '<div class="int-card-logo"><span class="brand-mark">SU</span></div> <h4>Support Agent'),
    ('<div class="int-card-logo"><span></span></div> <h4>Campaign Agent', '<div class="int-card-logo"><span class="brand-mark">CA</span></div> <h4>Campaign Agent'),
    ('<div class="int-card-logo"><span></span></div> <h4>Custom Agent Builder', '<div class="int-card-logo"><span class="brand-mark">CB</span></div> <h4>Custom Agent Builder'),
    ('<div class="int-card-logo"><span></span></div> <span class="int-card-client">Warehouse', '<div class="int-card-logo"><span class="brand-mark">WM</span></div> <span class="int-card-client">Warehouse'),
    ('<div class="int-card-logo"><span></span></div> <span class="int-card-client">NextCall', '<div class="int-card-logo"><span class="brand-mark">NC</span></div> <span class="int-card-client">NextCall'),
    ('<div class="int-card-logo"><span></span></div> <span class="int-card-client">FleetIQ', '<div class="int-card-logo"><span class="brand-mark">FQ</span></div> <span class="int-card-client">FleetIQ'),
    ('<span class="int-card-client">Processed globally</span> <h4>Calls Processed', '<span class="int-card-client">Processed globally</span> <h4>Calls Processed'),
    ('<div class="int-card-logo"><span></span></div> <span class="int-card-client">Processed', '<div class="int-card-logo"><span class="brand-mark">VOL</span></div> <span class="int-card-client">Processed'),
    ('<div class="int-card-logo"><span></span></div> <span class="int-card-client">Live stream', '<div class="int-card-logo"><span class="brand-mark">LIVE</span></div> <span class="int-card-client">Live stream'),
    ('<div class="int-card-logo"><span></span></div> <span class="int-card-client">Intent engine', '<div class="int-card-logo"><span class="brand-mark">INT</span></div> <span class="int-card-client">Intent engine'),
    ('<div class="int-card-logo"><span></span></div> <span class="int-card-client">Operator view', '<div class="int-card-logo"><span class="brand-mark">OPS</span></div> <span class="int-card-client">Operator view'),
    ('<div class="int-card-logo"><span></span></div> <span class="int-card-client">System health', '<div class="int-card-logo"><span class="brand-mark">LAT</span></div> <span class="int-card-client">System health'),
    ('<div class="int-card-logo"><span></span></div> <span class="int-card-client">Compliance', '<div class="int-card-logo"><span class="brand-mark">SEC</span></div> <span class="int-card-client">Compliance'),
    ('<div class="int-card-logo"><span></span></div> <span class="int-card-client">Step 1', '<div class="int-card-logo"><span class="brand-mark">01</span></div> <span class="int-card-client">Step 1'),
    ('<div class="int-card-logo"><span></span></div> <span class="int-card-client">Step 2', '<div class="int-card-logo"><span class="brand-mark">02</span></div> <span class="int-card-client">Step 2'),
    ('<div class="int-card-logo"><span></span></div> <span class="int-card-client">Step 3', '<div class="int-card-logo"><span class="brand-mark">03</span></div> <span class="int-card-client">Step 3'),
    ('<div class="int-card-logo"><span></span></div> <span class="int-card-client">Step 4', '<div class="int-card-logo"><span class="brand-mark">04</span></div> <span class="int-card-client">Step 4'),
    ('<div class="int-card-logo"><span></span></div> <span class="int-card-client">Step 5', '<div class="int-card-logo"><span class="brand-mark">05</span></div> <span class="int-card-client">Step 5'),
    ('<div class="int-card-logo"><span class="brand-mark">GX</span></div><h4>Gladia', '<div class="int-card-logo"><span class="brand-mark">GL</span></div><h4>Gladia'),
    ('<div class="telephony-hero-logo" aria-hidden="true">V</div>', '<div class="telephony-hero-logo" aria-hidden="true"><span class="brand-mark">VZ</span></div>'),
    ('logo: \'<span style="font-weight:800;font-size:1.4rem">V</span>\'', "logo: '<span class=\"detail-brand-mark\">VZ</span>'"),
]

CONTACT_ICONS = {
    'hello@emaavy.ai': '''<div class="contact-card-icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#1e40af" stroke-width="2"><path d="M4 4h16v16H4z"/><path d="m4 7 8 6 8-6"/></svg></div>''',
    'wa.me': '''<div class="contact-card-icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="#25D366"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"/><path d="M12 2C6.477 2 2 6.477 2 12c0 1.89.525 3.66 1.438 5.168L2 22l4.832-1.438A9.955 9.955 0 0 0 12 22c5.523 0 10-4.477 10-10S17.523 2 12 2z"/></svg></div>''',
    'calendly.com': '''<div class="contact-card-icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#1e40af" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg></div>''',
}

JS_OLD = """const ctaCanvas = document.getElementById('ctaParticles');
    const cctx = ctaCanvas.getContext('2d');
    function sizeCta() {
      const parent = ctaCanvas.parentElement;
      ctaCanvas.width = parent.clientWidth;
      ctaCanvas.height = parent.clientHeight;
    }
    sizeCta();
    window.addEventListener('resize', sizeCta);
    const pts = Array.from({ length: 40 }, () => ({
      x: Math.random() * ctaCanvas.width,
      y: Math.random() * ctaCanvas.height,
      vx: (Math.random() - 0.5) * 0.5,
      vy: (Math.random() - 0.5) * 0.5,
      r: Math.random() * 2 + 1
    }));
    function drawCta() {
      cctx.clearRect(0, 0, ctaCanvas.width, ctaCanvas.height);
      pts.forEach((p) => {
        p.x += p.vx;
        p.y += p.vy;
        if (p.x < 0 || p.x > ctaCanvas.width) p.vx *= -1;
        if (p.y < 0 || p.y > ctaCanvas.height) p.vy *= -1;
        cctx.beginPath();
        cctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
        cctx.fillStyle = 'rgba(56, 189, 248, 0.35)';
        cctx.fill();
      });
      requestAnimationFrame(drawCta);
    }
    drawCta();"""

JS_NEW = """const ctaCanvas = document.getElementById('ctaParticles');
    if (ctaCanvas) ctaCanvas.style.display = 'none';"""

TILT_OLD = """document.querySelectorAll('.price-card').forEach((card) => {
      card.addEventListener('mousemove', (e) => {
        if (card.classList.contains('featured')) return;
        const r = card.getBoundingClientRect();
        const x = (e.clientX - r.left) / r.width - 0.5;
        const y = (e.clientY - r.top) / r.height - 0.5;
        card.classList.add('tilt-active');
        card.style.transform = `perspective(800px) rotateY(${x * 10}deg) rotateX(${-y * 10}deg) translateY(-10px)`;
      });
      card.addEventListener('mouseleave', () => {
        card.classList.remove('tilt-active');
        card.style.transform = '';
      });
    });
    const featuredCard = document.querySelector('.price-card.featured');
    if (featuredCard) {
      featuredCard.addEventListener('mouseleave', () => {
        featuredCard.style.transform = 'scale(1.03)';
      });
    }"""

TILT_NEW = "/* price card tilt disabled for professional theme */"

CSS_ADDITIONS = """
    .signal-chip-glow, .hiw-step-glow, .feature-card-glow, .h-card-glow, .workflow-node-glow, .workflow-node-scanline, .workflow-pulse, .platform-hub-glow, .platform-hub-ring, .signal-dot::after, .section-kicker::before { display: none !important; animation: none !important; }
    .signal-band::before, .int-shell::before, #how-it-works::before, #features::before, .template-shell::before, .workflow-shell::before, .platform-shell::before, .nav-dropdown-menu::before, .page-section::before { animation: none !important; }
    .hero-scroll-tag, .hero-actions .btn-fill, .masthead-go, .hero h1 .inner.glow { animation: none !important; }
    .float-card-inner, .fc-1 .float-card-inner, .fc-2 .float-card-inner, .fc-3 .float-card-inner { animation: none !important; }
    .logo-tag::after { display: none; }
    .contact-card-icon { display: flex; align-items: center; justify-content: center; width: 44px; height: 44px; margin: 0 auto 0.75rem; border-radius: 10px; background: #f8fafc; border: 1px solid #e2e8f0; }
    .hiw-step-icon, .feature-icon, .signal-chip-icon-wrap, .workflow-node-icon, .telephony-feature-icon { display: flex !important; align-items: center; justify-content: center; font-family: 'Clash Display', sans-serif; font-weight: 700; font-size: 0.75rem !important; color: #1e40af !important; background: #f8fafc !important; border: 1px solid #e2e8f0 !important; box-shadow: none !important; }
    .signal-band-title { text-shadow: none !important; }
    .signal-live-badge { animation: none !important; box-shadow: none !important; }
    .price-card.featured::after { display: none; }
    .price-card:hover { transform: none !important; }
    .pack-badge.hot { animation: none !important; }
"""


def main():
    text = HTML.read_text(encoding="utf-8")
    for old, new in REPLACEMENTS:
        text = text.replace(old, new)

    # Generic empty int-card logos left
    text = re.sub(
        r'<div class="int-card-logo"><span></span></div>',
        '<div class="int-card-logo"><span class="brand-mark">·</span></div>',
        text,
    )

    for key, icon in CONTACT_ICONS.items():
        text = re.sub(
            rf'(<a class="contact-card[^>]*href="[^"]*{re.escape(key)}[^"]*"[^>]*>)\s*<div class="contact-card-icon">[^<]*</div>',
            rf'\1 {icon}',
            text,
        )
        text = re.sub(
            rf'(<a class="contact-card[^>]*href="[^"]*{re.escape(key)}[^"]*"[^>]*>)\s*<div class="contact-card-icon"></div>',
            rf'\1 {icon}',
            text,
        )

    text = text.replace(JS_OLD, JS_NEW)
    text = text.replace(TILT_OLD, TILT_NEW)
    text = text.replace("/ffffff", "/0f172a")
    text = text.replace("Signal From Every Call", "Enterprise Call Intelligence")
    text = text.replace("Live signal snapshots", "Platform capabilities")
    text = text.replace("Pick your <em>frequency</em>", "Plans for every team")
    text = text.replace('<p class="bento-label" style="margin-bottom:0.75rem">Signal tiers</p>', '<p class="bento-label" style="margin-bottom:0.75rem">Pricing</p>')

    if ".signal-chip-glow, .hiw-step-glow" not in text:
        text = text.replace("</style>", CSS_ADDITIONS + "\n  </style>", 1)

    HTML.write_text(text, encoding="utf-8")
    print("Fixed professional issues in", HTML.name)


if __name__ == "__main__":
    main()
