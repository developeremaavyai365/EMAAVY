#!/usr/bin/env python3
"""Restore emaavy_white_blue (2).html landing page to pre-SPA state."""
from pathlib import Path
import re

FILE = Path(__file__).resolve().parent.parent / 'emaavy_white_blue (2).html'
text = FILE.read_text(encoding='utf-8')

MASTHEAD = '''  <header class="masthead" id="masthead">
    <div class="masthead-beam">
      <div class="masthead-scan" aria-hidden="true"></div>
      <div class="masthead-inner">
        <a href="#top" class="logo-mega" id="logoMega" aria-label="EMAAVY home">
          <div class="logo-radar" aria-hidden="true"></div>
          <div class="logo-stack">
            <span class="logo-ghost g1" aria-hidden="true">EMAAVY</span>
            <span class="logo-ghost g2" aria-hidden="true">EMAAVY</span>
            <span class="logo-letters" id="logoLetters">
              <span class="logo-letter">E</span>
              <span class="logo-letter">M</span>
              <span class="logo-letter">A</span>
              <span class="logo-letter">A</span>
              <span class="logo-letter">V</span>
              <span class="logo-letter">Y</span>
            </span>
          </div>
          <span class="logo-period">.</span>
          <span class="logo-tag">Call Intelligence</span>
        </a>
        <nav class="masthead-nav" aria-label="Main">
          <a href="#how-it-works" data-nav-section="how-it-works" data-index="01">How It Works</a>
          <a href="#features" data-nav-section="features" data-index="02">Features</a>
          <div class="nav-dropdown" id="integrationsDropdown">
            <a href="#integrations" class="nav-integrations-link" data-nav-section="integrations">Integrations</a>
            <button class="nav-dropdown-caret" id="integrationsDropdownTrigger" type="button" aria-label="Show integration categories">▾</button>
            <div class="nav-dropdown-menu" id="integrationsMenu">
              <div class="dropdown-section">
                <div class="dropdown-section-title">📞 Telephony</div>
                <div class="dropdown-section-body"><a href="#integration-telephony">Vobiz — Outbound calling</a></div>
              </div>
              <div class="dropdown-section">
                <div class="dropdown-section-title">🧠 LLMs</div>
                <div class="dropdown-section-body"><a href="#integration-llm">OpenAI · Claude · Gemini · Qwen · Grok</a></div>
              </div>
              <div class="dropdown-section">
                <div class="dropdown-section-title">🎙 STT</div>
                <div class="dropdown-section-body"><a href="#integration-stt">Deepgram · Sarvam AI</a></div>
              </div>
              <div class="dropdown-section">
                <div class="dropdown-section-title">🔊 TTS</div>
                <div class="dropdown-section-body"><a href="#integration-tts">Flash v2 · ElevenTurbo v2</a></div>
              </div>
              <div class="dropdown-section">
                <div class="dropdown-section-title">🔧 Tools & Workflow</div>
                <div class="dropdown-section-body"><a href="#integration-tools">CRM · Calendar · WhatsApp · Webhooks</a></div>
              </div>
            </div>
          </div>
          <a href="#agents" data-nav-section="agents" data-index="04">Agents</a>
          <a href="#case-studies" data-nav-section="case-studies" data-index="05">Case Studies</a>
          <a href="#pricing" data-nav-section="pricing" data-index="06">Pricing</a>
          <a href="#docs" data-nav-section="docs" data-index="07">Documentation</a>
          <a href="#contact" data-nav-section="contact" data-index="08">Contact Us</a>
        </nav>
        <div class="masthead-actions">
          <a href="login.html" class="masthead-login btn-nav-login" id="loginBtn">Log In</a>
          <a href="book-demo.html" class="masthead-go btn-nav-demo" id="bookDemoBtn">Book a Demo</a>
        </div>
        <button class="nav-hamburger" id="navHamburger" type="button" aria-label="Open menu">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
  </header>

  <div class="mobile-nav-backdrop" id="mobileNavBackdrop"></div>
  <nav class="mobile-nav-drawer" id="mobileNavDrawer" aria-label="Mobile navigation">
    <a href="#how-it-works" data-nav-section="how-it-works">How It Works</a>
    <a href="#features" data-nav-section="features">Features</a>
    <a href="#integrations" data-nav-section="integrations">Integrations</a>
    <span class="mobile-nav-label">Integration categories</span>
    <div class="mobile-sub">
      <a href="#integration-telephony">Telephony · Vobiz</a>
      <a href="#integration-llm">LLMs</a>
      <a href="#integration-stt">Speech-to-Text</a>
      <a href="#integration-tts">Text-to-Speech</a>
      <a href="#integration-tools">Tools & Workflow</a>
    </div>
    <a href="#agents" data-nav-section="agents">Agents</a>
    <a href="#case-studies" data-nav-section="case-studies">Case Studies</a>
    <a href="#pricing" data-nav-section="pricing">Pricing</a>
    <a href="#docs" data-nav-section="docs">Documentation</a>
    <a href="#contact" data-nav-section="contact">Contact Us</a>
    <div class="mobile-nav-actions">
      <a href="login.html" class="btn-nav-login">Log In</a>
      <a href="book-demo.html" class="btn-nav-demo">Book a Demo</a>
    </div>
  </nav>

  <aside class="rail">'''

# Remove SPA CSS block
text = re.sub(r'\n    \.spa-view \{ display: none; \}.*?@media \(max-width: 1024px\) \{ body\[data-spa="true"\] \.shell \{ margin-left: 0; \} \}\n', '\n', text, flags=re.DOTALL)

# Body attribute
text = text.replace('<body data-spa="true" data-base="" data-route="home">', '<body data-page="home">')

# Replace site-nav-root + spa wrappers with masthead + rail
text = re.sub(
    r'  <div id="site-nav-root"></div>\n\n  <div id="spa-views">\n  <div id="view-home" class="spa-view active">\n  <aside class="rail">',
    MASTHEAD,
    text,
    count=1,
)

# Remove all SPA views and closing wrappers before detail-drawer
text = re.sub(
    r'  </div>\n  </div>\n\n    <div id="view-how-it-works".*?<div id="site-footer-root"></div>\n\n  <div class="detail-drawer"',
    '\n\n  <div class="detail-drawer"',
    text,
    flags=re.DOTALL,
    count=1,
)

# Restore footer links
text = text.replace(
    '''        <a href="#/features" style="color:#475569;">Features</a>
        <a href="#/pricing" style="color:#475569;">Pricing</a>
        <a href="#/documentation" style="color:#475569;">Documentation</a>
        <a href="#/contact" style="color:#475569;">Contact</a>
        <a href="#/login" style="color:#475569;">Log In</a>''',
    '''        <a href="#features" style="color:#475569;">Features</a>
        <a href="#pricing" style="color:#475569;">Pricing</a>
        <a href="#docs" style="color:#475569;">Documentation</a>
        <a href="#contact" style="color:#475569;">Contact</a>
        <a href="#" style="color:#475569;">Privacy</a>''',
)

# Restore rail home link
text = text.replace('<a href="#/" class="rail-home"', '<a href="#top" class="rail-home"')

# Restore scripts - remove SPA bundle, keep nav.js + add scroll handler
old_scripts = '''  <script src="assets/routes.js"></script>
  <script src="assets/components.js"></script>
  <script src="assets/nav.js"></script>
  <script src="assets/spa-router.js"></script>'''
new_scripts = '''  <script src="assets/nav.js"></script>'''
text = text.replace(old_scripts, new_scripts)

# Restore detailCta
text = text.replace(
    "EMAAVYRouter.navigate('book-demo')",
    "window.location.href = 'book-demo.html'",
)

# Restore click-detail handler (remove SPA routing)
text = re.sub(
    r"document\.querySelectorAll\('\.click-detail\[data-detail\]'\)\.forEach\(\(el\) => \{\s*el\.addEventListener\('click', \(e\) => \{\s*if \(e\.target\.closest\('button, a\[href\^=\"http\"\], input'\)\) return;\s*const detailToRoute = \{.*?\}\;\s*const route = detailToRoute\[el\.dataset\.detail\];\s*if \(route && window\.EMAAVYRouter\) \{\s*EMAAVYRouter\.navigate\(route\);\s*return;\s*\}\s*openDetail\(el\.dataset\.detail\);",
    "document.querySelectorAll('.click-detail[data-detail]').forEach((el) => {\n      el.addEventListener('click', (e) => {\n        if (e.target.closest('button, a[href^=\"http\"], input')) return;\n        openDetail(el.dataset.detail);",
    text,
    flags=re.DOTALL,
)

# Add smooth scroll handler before closing script if missing
scroll_js = '''
    /* Smooth anchor navigation */
    document.querySelectorAll('a[href^="#"]').forEach((a) => {
      a.addEventListener('click', (e) => {
        const href = a.getAttribute('href');
        if (!href || href === '#') return;
        const el = document.querySelector(href);
        if (!el) return;
        e.preventDefault();
        const offset = (document.getElementById('masthead')?.offsetHeight || 80) + 16;
        const top = el.getBoundingClientRect().top + window.scrollY - offset;
        window.scrollTo({ top: Math.max(0, top), behavior: 'smooth' });
        document.getElementById('integrationsDropdown')?.classList.remove('open');
        window.emaavyNav?.closeMobileNav?.();
      });
    });

    /* Active nav on scroll */
    const navSections = ['how-it-works', 'features', 'integrations', 'integration-telephony', 'integration-llm', 'integration-stt', 'integration-tts', 'integration-tools', 'agents', 'case-studies', 'pricing', 'docs', 'contact'];
    const navLinks = document.querySelectorAll('[data-nav-section]');
    window.addEventListener('scroll', () => {
      const offset = (document.getElementById('masthead')?.offsetHeight || 80) + 40;
      let current = 'top';
      navSections.forEach((id) => {
        const sec = document.getElementById(id);
        if (sec && window.scrollY >= sec.offsetTop - offset) {
          current = id.startsWith('integration-') ? 'integrations' : id;
        }
      });
      navLinks.forEach((link) => {
        const s = link.getAttribute('data-nav-section');
        link.classList.toggle('active', s === current || (s === 'integrations' && current === 'integrations'));
      });
    }, { passive: true });
'''

if '/* Smooth anchor navigation */' not in text:
    text = text.replace('  </script>\n</body>', scroll_js + '\n  </script>\n</body>')

# Remove site.css if user wants exact before - the pre-SPA version had nav.css only. Remove site.css link.
text = text.replace('  <link rel="stylesheet" href="assets/site.css" />\n', '')

FILE.write_text(text, encoding='utf-8')
print('Restored landing page. Lines:', len(text.splitlines()))
print('spa-view count:', text.count('spa-view'))
print('masthead present:', 'class="masthead"' in text)
