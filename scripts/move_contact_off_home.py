"""Remove contact section from home; full contact UI on pages/contact.html."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "emaavy_white_blue (2).html"
CONTACT_PAGE = ROOT / "pages" / "contact.html"
CONTACT_CSS = ROOT / "assets" / "contact-page.css"

CONTACT_INNER = """<section id="contact" class="contact-page-section">
  <div class="contact-page-intro reveal">
    <p class="bento-label">Get In Touch</p>
    <h2>Contact us</h2>
    <p>We'd love to hear from you. Reach out through any of the channels below — or send a message and we'll respond within 24 hours.</p>
  </div>
  <div class="contact-grid">
    <a class="contact-card reveal" href="mailto:hello@emaavy.ai">
      <div class="contact-card-icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#4A658B" stroke-width="2"><path d="M4 4h16v16H4z"/><path d="m4 7 8 6 8-6"/></svg></div>
      <h4>Email us</h4>
      <p>hello@emaavy.ai</p>
    </a>
    <a class="contact-card reveal" href="https://wa.me/919999999999" target="_blank" rel="noopener">
      <div class="contact-card-icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="#25D366"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"/><path d="M12 2C6.477 2 2 6.477 2 12c0 1.89.525 3.66 1.438 5.168L2 22l4.832-1.438A9.955 9.955 0 0 0 12 22c5.523 0 10-4.477 10-10S17.523 2 12 2z"/></svg></div>
      <h4>WhatsApp</h4>
      <p>Chat with our team directly</p>
    </a>
    <a class="contact-card reveal" href="https://calendly.com/emaavy" target="_blank" rel="noopener">
      <div class="contact-card-icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#4A658B" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg></div>
      <h4>Schedule a call</h4>
      <p>Book a 30-min intro call</p>
    </a>
  </div>
</section>"""

CONTACT_PAGE_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Contact Us — EMAAVY</title>
  <meta name="description" content="Contact EMAAVY — email, WhatsApp, schedule a call, or send a message. Our team responds within 24 hours." />
  <meta name="robots" content="index, follow" />
  <meta property="og:title" content="Contact Us — EMAAVY" />
  <meta property="og:description" content="Contact EMAAVY — sales, support, and partnership inquiries." />
  <meta property="og:type" content="website" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://api.fontshare.com/v2/css?f[]=clash-display@400,500,600,700&f[]=general-sans@300,400,500,600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../assets/nav.css" />
  <link rel="stylesheet" href="../assets/site.css" />
  <link rel="stylesheet" href="../assets/contact-page.css" />
  <style>
    .reveal {{ opacity: 0; transform: translateY(20px); transition: opacity 0.6s ease, transform 0.6s ease; }}
    .reveal.in {{ opacity: 1; transform: none; }}
  </style>
</head>
<body data-base="../" data-route="contact">
  <div id="site-nav-root"></div>
  <main class="page-main contact-page-main">
    <section class="page-hero compact">
      <div class="container">
        <span class="page-kicker">Contact</span>
        <h1>Get in touch</h1>
        <p>Questions about EMAAVY? Sales, support, and partnerships — we respond within 24 hours.</p>
      </div>
    </section>
    <section class="page-section">
      <div class="container contact-page-container">
{contact_inner}
        <div class="contact-form-wrap">
          <h3>Send a message</h3>
          <p>Prefer a written note? We'll route it to the right team.</p>
          <form class="contact-form glow-card">
            <input class="demo-input" type="text" placeholder="Your name" required />
            <input class="demo-input" type="email" placeholder="Work email" required />
            <textarea placeholder="How can we help?" rows="4"></textarea>
            <button type="submit" class="btn-primary">Send message →</button>
          </form>
        </div>
        <div class="cta-row" style="margin-top:2rem">
          <a href="../book-demo.html" class="btn-outline">Book a demo</a>
        </div>
      </div>
    </section>
  </main>
  <div id="site-footer-root"></div>
  <script src="../assets/routes.js"></script>
  <script src="../assets/components.js"></script>
  <script src="../assets/nav.js"></script>
  <script src="../assets/contact-page.js"></script>
</body>
</html>
"""

PREFIXES = (".contact-grid", ".contact-card", "#contact", ".contact-page")


def extract_css():
    text = HTML.read_text(encoding="utf-8")
    m = re.search(r"<style>(.*?)</style>", text, re.DOTALL)
    if not m:
        return ""
    rules = []
    for chunk in m.group(1).split("}"):
        if "{" not in chunk:
            continue
        sel = chunk.split("{")[0]
        if any(p in sel for p in PREFIXES) or "contact-grid" in chunk or "contact-card" in chunk:
            rules.append(chunk.strip() + "}")
    header = """/* Contact page */
.contact-page-main { padding-bottom: 4rem; }
.contact-page-container { max-width: 960px; }
.contact-page-intro { text-align: center; margin-bottom: 2.5rem; }
.contact-page-intro h2 {
  font-family: 'Clash Display', sans-serif;
  font-size: clamp(2rem, 4vw, 2.75rem);
  color: #0f172a;
  letter-spacing: -0.03em;
  margin: 0.5rem 0;
}
.contact-page-intro p { color: #475569; max-width: 52ch; margin: 0 auto; }
.contact-form-wrap { margin-top: 3rem; max-width: 480px; margin-left: auto; margin-right: auto; }
.contact-form-wrap h3 { font-family: 'Clash Display', sans-serif; font-size: 1.35rem; color: #0f172a; margin-bottom: 0.35rem; }
.contact-form-wrap > p { color: #64748b; font-size: 0.9rem; margin-bottom: 1rem; }
.contact-form { padding: 1.75rem; display: grid; gap: 0.75rem; }
.contact-form .demo-input,
.contact-form textarea {
  width: 100%;
  padding: 0.85rem 1rem;
  border: 1px solid #e2e8f0;
  border-radius: 10px;
  font-family: inherit;
  font-size: 0.9rem;
}
.contact-form textarea { resize: vertical; min-height: 100px; }
.contact-form .btn-primary { width: 100%; justify-content: center; border: none; cursor: pointer; }
"""
    return header + "\n".join(rules)


def main():
    text = HTML.read_text(encoding="utf-8")

    pattern = re.compile(r"<!-- CONTACT US -->.*?</section>\s*<footer>", re.DOTALL)
    if not pattern.search(text):
        raise SystemExit("contact section not found")
    text = pattern.sub("<footer>", text, count=1)

    replacements = [
        (
            'href="#contact" data-nav-section="contact"',
            'href="pages/contact.html" data-nav-id="contact"',
        ),
        ('href="#contact" data-index="', 'href="pages/contact.html" data-index="'),
        ('href="#contact" data-label="', 'href="pages/contact.html" data-label="'),
        (
            '<a href="#contact" style="color:#475569;">Contact</a>',
            '<a href="pages/contact.html" style="color:#475569;">Contact</a>',
        ),
    ]
    for old, new in replacements:
        text = text.replace(old, new)

    text = re.sub(r"'contact',\s*", "", text)
    text = re.sub(r",\s*'contact'", "", text)

    HTML.write_text(text, encoding="utf-8")

    CONTACT_CSS.write_text(extract_css(), encoding="utf-8")
    CONTACT_PAGE.write_text(
        CONTACT_PAGE_HTML.format(contact_inner=CONTACT_INNER),
        encoding="utf-8",
    )
    print("OK: contact removed from home; pages/contact.html updated")


if __name__ == "__main__":
    main()
