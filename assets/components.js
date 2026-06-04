/**
 * Shared navbar & footer — one masthead shell on every page (same as landing).
 */
(function () {
  const R = window.EMAAVY_ROUTES;
  if (!R) return;

  function base() {
    return document.body.dataset.base || '';
  }

  function isActive(navId) {
    const route = document.body.dataset.route || '';
    const parent = R.matchRoute(route);
    if (navId === route) return true;
    if (navId === parent) return true;
    if (navId === 'integrations' && route.startsWith('integration-')) return true;
    if (navId === 'agents' && route.startsWith('agent-')) return true;
    if (navId === 'journey' && route.startsWith('lifecycle-')) return true;
    if (navId === 'faq' && route.startsWith('faq-')) return true;
    if (navId === 'case-studies' && route.startsWith('case-study-')) return true;
    if (navId.startsWith('integration-') && navId === route) return true;
    if (navId.startsWith('agent-') && navId === route) return true;
    return false;
  }

  function activeClass(navId) {
    return isActive(navId) ? ' active' : '';
  }

  function navHref(path) {
    return R.href(path, base());
  }

  const MASTHEAD_SHORT_LABELS = {
    'case-studies': 'Cases',
    documentation: 'Docs',
    journey: 'Lifecycle',
  };

  function navLabel(item, masthead) {
    if (masthead && MASTHEAD_SHORT_LABELS[item.id]) return MASTHEAD_SHORT_LABELS[item.id];
    return item.label;
  }

  function plainLink(item, opts) {
    const { masthead, index } = opts || {};
    const cls = activeClass(item.id).trim();
    const href = navHref(item.path);
    const label = navLabel(item, masthead);
    if (masthead) {
      const idx = index != null ? String(index).padStart(2, '0') : '';
      const indexAttr = idx ? ` data-index="${idx}"` : '';
      return `<a href="${href}" class="${cls}" data-nav-section="${item.id}" data-nav-id="${item.id}"${indexAttr}>${label}</a>`;
    }
    return `<a href="${href}" class="${cls}" data-nav-id="${item.id}">${label}</a>`;
  }

  function dropdownMenuLinks(items, navIdPrefix) {
    return items
      .map((i) => {
        const nid = navIdPrefix ? `${navIdPrefix}-${i.id}` : i.id;
        return `<a href="${navHref(i.path)}" class="${activeClass(nid)}" data-nav-id="${nid}">${i.label}</a>`;
      })
      .join('');
  }

  function renderIntegrationsDropdown(opts) {
    const { masthead } = opts || {};
    const mainPath = masthead
      ? 'index.html#integrations'
      : 'pages/integrations/index.html';
    const mainCls = masthead
      ? `nav-integrations-link${activeClass('integrations')}`
      : activeClass('integrations');
    const sectionAttr = masthead ? ' data-nav-section="integrations"' : ' data-nav-id="integrations"';
    const indexAttr = masthead ? ' data-index="02"' : '';

    let menuBody;
    if (masthead) {
      const links = R.integrationHubLayers
        .map((l) => `<a href="${navHref(l.path)}">${l.label}</a>`)
        .join('');
      menuBody = `
        <div class="nav-dropdown-menu-glow" aria-hidden="true"></div>
        <div class="nav-dropdown-menu-head">
          <span class="nav-dropdown-menu-kicker">Integration hub</span>
          <p>Jump to any category in your AI stack</p>
        </div>
        <div class="nav-dropdown-grid">
          <div class="dropdown-section dropdown-section-wide">
            <div class="dropdown-section-title">EMAAVY integration layers</div>
            <div class="dropdown-link-grid">${links}</div>
          </div>
        </div>`;
    } else {
      const groups = R.integrationGroups
        .map((g) => {
          const items = R.integrations[g.key]
            .map((i) => {
              const nid = `integration-${i.id}`;
              return `<a href="${navHref(i.path)}" class="${activeClass(nid)}" data-nav-id="${nid}">${i.label}</a>`;
            })
            .join('');
          return `<div class="dropdown-section"><div class="dropdown-section-title">${g.title}</div><div class="dropdown-link-grid">${items}</div></div>`;
        })
        .join('');
      menuBody = groups;
    }

    return `
      <div class="nav-dropdown" id="integrationsDropdown">
        <div class="nav-dropdown-split">
          <a href="${navHref(mainPath)}" class="${mainCls}"${sectionAttr}${indexAttr}>Integrations</a>
          <button class="nav-dropdown-caret" id="integrationsDropdownTrigger" type="button" aria-label="Toggle integration categories">▾</button>
        </div>
        <div class="nav-dropdown-menu${masthead ? '' : ' mega'}" id="integrationsMenu" role="menu">${menuBody}</div>
      </div>`;
  }

  function renderAgentsDropdown(opts) {
    const { masthead } = opts || {};
    const mainPath = masthead ? 'index.html#agents' : 'pages/agents/index.html';
    const sectionAttr = masthead ? ' data-nav-section="agents"' : ' data-nav-id="agents"';
    const indexAttr = masthead ? ' data-index="03"' : '';
    const items = dropdownMenuLinks(R.agents, 'agent');

    return `
      <div class="nav-dropdown" id="agentsDropdown">
        <div class="nav-dropdown-split">
          <a href="${navHref(mainPath)}" class="${activeClass('agents')}"${sectionAttr}${indexAttr}>Agents</a>
          <button class="nav-dropdown-caret" id="agentsDropdownTrigger" type="button" aria-label="Agent types">▾</button>
        </div>
        <div class="nav-dropdown-menu mega-agents" id="agentsMenu" role="menu">
          <div class="dropdown-section"><div class="dropdown-link-grid">${items}</div></div>
        </div>
      </div>`;
  }

  function renderLifecycleDropdown(opts) {
    const { masthead } = opts || {};
    const mainPath = masthead ? 'index.html#journey' : 'pages/call-lifecycle/index.html';
    const sectionAttr = masthead ? ' data-nav-section="journey"' : ' data-nav-id="journey"';
    const indexAttr = masthead ? ' data-index="07"' : '';
    const items = dropdownMenuLinks(R.callLifecycle, 'lifecycle');

    return `
      <div class="nav-dropdown" id="lifecycleDropdown">
        <div class="nav-dropdown-split">
          <a href="${navHref(mainPath)}" class="${activeClass('journey')}"${sectionAttr}${indexAttr}>${masthead ? 'Lifecycle' : 'Call lifecycle'}</a>
          <button class="nav-dropdown-caret" id="lifecycleDropdownTrigger" type="button" aria-label="Call lifecycle steps">▾</button>
        </div>
        <div class="nav-dropdown-menu mega-agents" id="lifecycleMenu" role="menu">
          <div class="dropdown-section"><div class="dropdown-link-grid">${items}</div></div>
        </div>
      </div>`;
  }

  function renderFaqDropdown(opts) {
    const { masthead } = opts || {};
    const mainPath = masthead ? 'index.html#faq' : 'pages/faq.html';
    const sectionAttr = masthead ? ' data-nav-section="faq"' : ' data-nav-id="faq"';
    const indexAttr = masthead ? ' data-index="08"' : '';
    const items = dropdownMenuLinks(R.faqTopics, 'faq');

    return `
      <div class="nav-dropdown" id="faqDropdown">
        <div class="nav-dropdown-split">
          <a href="${navHref(mainPath)}" class="${activeClass('faq')}"${sectionAttr}${indexAttr}>FAQ</a>
          <button class="nav-dropdown-caret" id="faqDropdownTrigger" type="button" aria-label="FAQ topics">▾</button>
        </div>
        <div class="nav-dropdown-menu mega-agents" id="faqMenu" role="menu">
          <div class="dropdown-section"><div class="dropdown-link-grid">${items}</div></div>
        </div>
      </div>`;
  }

  function renderDesktopNav(opts) {
    const { masthead } = opts || {};
    let index = 1;
    return R.mainNav
      .map((item) => {
        if (item.dropdown === 'integrations') return renderIntegrationsDropdown(opts);
        if (item.dropdown === 'agents') return renderAgentsDropdown(opts);
        if (item.dropdown === 'lifecycle') return renderLifecycleDropdown(opts);
        if (item.dropdown === 'faq') return renderFaqDropdown(opts);
        const link = plainLink(item, { masthead, index });
        index += 1;
        return link;
      })
      .join('\n');
  }

  function renderAuthActions(opts) {
    const { masthead } = opts || {};
    return R.authNav
      .map((item) => {
        const mastheadCls = masthead ? ' masthead-cta' : '';
        const mastheadVariant =
          masthead && item.id === 'login'
            ? ' masthead-login masthead-cta--login'
            : masthead && item.id === 'book-demo'
              ? ' masthead-go masthead-cta--demo'
              : '';
        const mastheadId =
          masthead && item.id === 'login'
            ? ' id="loginBtn"'
            : masthead && item.id === 'book-demo'
              ? ' id="bookDemoBtn"'
              : '';
        return `<a href="${navHref(item.path)}"${mastheadId} class="${item.className}${mastheadCls}${mastheadVariant}${isActive(item.id) ? ' active' : ''}" data-nav-id="${item.id}">${item.label}</a>`;
      })
      .join('\n');
  }

  function renderMobileNav() {
    const blocks = [];

    R.mainNav.forEach((item) => {
      if (item.dropdown === 'integrations') {
        blocks.push(`<a href="${navHref('index.html#integrations')}" data-nav-section="integrations" data-nav-id="integrations">Integrations</a>`);
        blocks.push('<span class="mobile-nav-label">Integration categories</span>');
        blocks.push(`<div class="mobile-sub">${R.integrationHubLayers.map((l) => `<a href="${navHref(l.path)}">${l.label}</a>`).join('')}</div>`);
        return;
      }
      if (item.dropdown === 'agents') {
        blocks.push(`<a href="${navHref('index.html#agents')}" data-nav-section="agents" data-nav-id="agents">Agents</a>`);
        blocks.push('<span class="mobile-nav-label">Agent types</span>');
        blocks.push(`<div class="mobile-sub">${dropdownMenuLinks(R.agents, 'agent')}</div>`);
        return;
      }
      if (item.dropdown === 'lifecycle') {
        blocks.push(`<a href="${navHref('index.html#journey')}" data-nav-section="journey" data-nav-id="journey">Call lifecycle</a>`);
        blocks.push('<span class="mobile-nav-label">Lifecycle steps</span>');
        blocks.push(`<div class="mobile-sub">${dropdownMenuLinks(R.callLifecycle, 'lifecycle')}</div>`);
        return;
      }
      if (item.dropdown === 'faq') {
        blocks.push(`<a href="${navHref('index.html#faq')}" data-nav-section="faq" data-nav-id="faq">FAQ</a>`);
        blocks.push('<span class="mobile-nav-label">FAQ topics</span>');
        blocks.push(`<div class="mobile-sub">${dropdownMenuLinks(R.faqTopics, 'faq')}</div>`);
        return;
      }
      blocks.push(`<a href="${navHref(item.path)}" data-nav-section="${item.id}" data-nav-id="${item.id}">${item.label}</a>`);
    });

    const auth = R.authNav
      .map((item) => `<a href="${navHref(item.path)}" class="${item.className}">${item.label}</a>`)
      .join('\n');

    return `${blocks.join('\n')}\n<div class="mobile-nav-actions">${auth}</div>`;
  }

  function renderMastheadLogo() {
    const src = navHref(R.logoMark || 'assets/emaavy-mark.png');
    return `<a href="${R.homeHref(base())}" class="logo-mega logo-mega--mark logo-mega--nav-only" id="logoMega" aria-label="EMAAVY home">
      <img src="${src}" alt="EMAAVY" class="logo-mega-mark" width="44" height="44" decoding="async" fetchpriority="high" />
    </a>`;
  }

  function renderMastheadShell() {
    const navOpts = { masthead: true };
    return `
      <header class="masthead" id="masthead">
        <div class="masthead-beam">
          <div class="masthead-inner">
            ${renderMastheadLogo()}
            <nav class="masthead-nav" aria-label="Main">${renderDesktopNav(navOpts)}</nav>
            <div class="masthead-actions">${renderAuthActions(navOpts)}</div>
            <button class="nav-hamburger" id="navHamburger" type="button" aria-label="Open menu">
              <span></span><span></span><span></span>
            </button>
          </div>
        </div>
      </header>
      <div class="mobile-nav-backdrop" id="mobileNavBackdrop"></div>
      <nav class="mobile-nav-drawer" id="mobileNavDrawer" aria-label="Mobile">${renderMobileNav()}</nav>`;
  }

  function renderFooter() {
    const route = document.body.dataset.route || 'home';
    const homeActive = document.getElementById('view-home')?.classList.contains('active');
    if (route === 'home' && homeActive) return '';

    const footerLinks = R.mainNav
      .filter((i) => !['pricing', 'documentation', 'contact'].includes(i.id))
      .slice(0, 6)
      .map((i) => `<a href="${navHref(i.path)}">${i.label}</a>`)
      .join('\n');

    return `
      <footer class="site-footer">
        <div class="footer-inner">
          <div class="footer-brand">
            <b>EMAAVY.</b>
            <p>Enterprise AI for voice, campaigns, and conversation intelligence.</p>
          </div>
          <div class="footer-links">
            ${footerLinks}
            <a href="${navHref('login.html')}">Log In</a>
            <a href="${navHref('book-demo.html')}">Book a Demo</a>
          </div>
          <p class="footer-copy">© <strong>2026 EMAAVY.</strong> All rights reserved.</p>
        </div>
      </footer>`;
  }

  function syncNavOffset() {
    const masthead = document.getElementById('masthead');
    if (!masthead) return;
    const h = Math.ceil(masthead.getBoundingClientRect().height) || 72;
    document.documentElement.style.setProperty('--masthead-h', `${h}px`);
    document.documentElement.style.setProperty('--nav-offset', '16px');
  }

  function mountMasthead() {
    const existingMasthead = document.getElementById('masthead');
    if (document.body.dataset.page === 'home' && existingMasthead) {
      syncNavOffset();
      window.dispatchEvent(new CustomEvent('emaavy:nav-mounted'));
      return;
    }

    const html = renderMastheadShell();
    const wrap = document.createElement('div');
    wrap.innerHTML = html.trim();

    const newMasthead = wrap.querySelector('#masthead');
    const newBackdrop = wrap.querySelector('#mobileNavBackdrop');
    const newDrawer = wrap.querySelector('#mobileNavDrawer');

    const navRoot = document.getElementById('site-nav-root');

    if (navRoot && !existingMasthead) {
      navRoot.innerHTML = html;
    } else if (existingMasthead && newMasthead && newBackdrop && newDrawer) {
      existingMasthead.replaceWith(newMasthead);
      document.getElementById('mobileNavBackdrop')?.replaceWith(newBackdrop);
      document.getElementById('mobileNavDrawer')?.replaceWith(newDrawer);
    } else if (navRoot) {
      navRoot.innerHTML = html;
    }

    const masthead = document.getElementById('masthead');
    if (masthead && document.body.dataset.page !== 'home') {
      masthead.style.setProperty('--masthead-progress', '0');
      masthead.classList.remove('compact', 'scrolled');
    }

    syncNavOffset();
    window.dispatchEvent(new CustomEvent('emaavy:nav-mounted'));
  }

  function mount() {
    mountMasthead();
    const footerRoot = document.getElementById('site-footer-root');
    if (footerRoot) footerRoot.innerHTML = renderFooter();
    window.addEventListener('resize', syncNavOffset, { passive: true });
  }

  window.EMAAVYComponents = {
    mount,
    mountMasthead,
    renderMastheadShell,
    renderFooter,
    renderDesktopNav,
    renderMobileNav,
    syncNavOffset,
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', mount);
  } else {
    mount();
  }
})();
