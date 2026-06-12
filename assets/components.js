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

  const HOME_SECTION_HREFS = {
    'pages/how-it-works.html': '#how-it-works',
    'pages/integrations/index.html': '#integrations',
    'pages/agents/index.html': '#agents',
    'index.html#campaigns': '#campaigns',
    'pages/features.html': '#features',
    'pages/case-studies.html': '#case-studies',
    'pages/call-lifecycle/index.html': '#journey',
    'pages/faq.html': '#faq',
  };

  function isHomePage() {
    return document.body.dataset.page === 'home';
  }

  function navHref(path) {
    if (isHomePage()) {
      if (HOME_SECTION_HREFS[path]) return HOME_SECTION_HREFS[path];
      if (path && path.includes('#')) {
        const hash = path.split('#').pop();
        if (hash) return '#' + hash;
      }
    }
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
    const mainPath = 'pages/integrations/index.html';
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
    const mainPath = 'pages/agents/index.html';
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
    const mainPath = 'pages/call-lifecycle/index.html';
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
    const mainPath = 'pages/faq.html';
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
        blocks.push(`<a href="${navHref('pages/integrations/index.html')}" data-nav-section="integrations" data-nav-id="integrations">Integrations</a>`);
        blocks.push('<span class="mobile-nav-label">Integration categories</span>');
        blocks.push(`<div class="mobile-sub">${R.integrationHubLayers.map((l) => `<a href="${navHref(l.path)}">${l.label}</a>`).join('')}</div>`);
        return;
      }
      if (item.dropdown === 'agents') {
        blocks.push(`<a href="${navHref('pages/agents/index.html')}" data-nav-section="agents" data-nav-id="agents">Agents</a>`);
        blocks.push('<span class="mobile-nav-label">Agent types</span>');
        blocks.push(`<div class="mobile-sub">${dropdownMenuLinks(R.agents, 'agent')}</div>`);
        return;
      }
      if (item.dropdown === 'lifecycle') {
        blocks.push(`<a href="${navHref('pages/call-lifecycle/index.html')}" data-nav-section="journey" data-nav-id="journey">Call lifecycle</a>`);
        blocks.push('<span class="mobile-nav-label">Lifecycle steps</span>');
        blocks.push(`<div class="mobile-sub">${dropdownMenuLinks(R.callLifecycle, 'lifecycle')}</div>`);
        return;
      }
      if (item.dropdown === 'faq') {
        blocks.push(`<a href="${navHref('pages/faq.html')}" data-nav-section="faq" data-nav-id="faq">FAQ</a>`);
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

  function logoAsset() {
    return R.logo || R.logoMark || 'assets/brand/emaavy-logo.svg';
  }

  function renderLogoImg(variant) {
    const src = navHref(logoAsset());
    const variantCls = variant ? ` emaavy-logo--${variant}` : '';
    const priority = variant === 'nav' || variant === 'hero' ? ' fetchpriority="high"' : '';
    // Intrinsic dimensions preserve aspect ratio; CSS controls display height only.
    return `<img src="${src}" alt="Emaavy" class="emaavy-logo${variantCls} logo-mega-mark" width="648" height="116" decoding="async"${priority} />`;
  }

  function renderMastheadLogo() {
    return `<a href="${R.homeHref(base())}" class="logo-mega logo-mega--wordmark logo-mega--nav-only" id="logoMega" aria-label="Emaavy home">
      ${renderLogoImg('nav')}
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

  function renderFooterCol(title, items) {
    const links = (items || [])
      .map((i) => {
        const href = navHref(i.path);
        return `<li><a href="${href}">${i.label}</a></li>`;
      })
      .join('\n');
    return `
          <div class="footer-premium-col">
            <h3 class="footer-col-title">${title}</h3>
            <ul class="footer-col-links">${links}</ul>
          </div>`;
  }

  function renderFooterSocials() {
    const socials = R.footerNav?.social || [];
    return socials
      .map((s) => {
        let icon = '';
        if (s.id === 'x') {
          icon = '<span aria-hidden="true" style="font-size:0.95rem;font-weight:700;">𝕏</span>';
        } else if (s.id === 'linkedin') {
          icon = '<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>';
        } else if (s.id === 'youtube') {
          icon = '<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>';
        }
        return `<a class="footer-social-link" href="${s.url}" target="_blank" rel="noopener noreferrer" aria-label="${s.label}">${icon}</a>`;
      })
      .join('\n');
  }

  function renderFooter() {
    const fn = R.footerNav || {};
    const legal = (fn.legal || [])
      .map((i) => `<a href="${navHref(i.path)}">${i.label}</a>`)
      .join('\n');

    return `
      <footer class="site-footer site-footer--premium">
        <div class="footer-premium-inner">
          <div class="footer-premium-top">
            <div class="footer-premium-brand">
              <a href="${navHref(R.landingPage || 'index.html')}" class="footer-brand-logo" aria-label="EMAAVY home">
                ${renderLogoImg('footer')}
              </a>
              <p class="footer-brand-tagline">Build, deploy, and manage production-ready LLM-powered voice agents with Twilio, Plivo, RAG knowledgebases, and developer-first APIs.</p>
              <div class="footer-socials" aria-label="Social links">${renderFooterSocials()}</div>
            </div>
            ${renderFooterCol('API Documentation', fn.apiDocs)}
            ${renderFooterCol('Product Features', fn.productFeatures)}
          </div>
          <div class="footer-premium-bar">
            <p class="footer-copy-line">© 2026 EMAAVY Inc. All Rights Reserved.</p>
            <div class="footer-legal-links">${legal}</div>
          </div>
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
    const html = renderMastheadShell();
    const navRoot = document.getElementById('site-nav-root');

    if (navRoot) {
      navRoot.innerHTML = html;
    } else if (existingMasthead) {
      const wrap = document.createElement('div');
      wrap.innerHTML = html.trim();
      const newMasthead = wrap.querySelector('#masthead');
      const newBackdrop = wrap.querySelector('#mobileNavBackdrop');
      const newDrawer = wrap.querySelector('#mobileNavDrawer');
      if (newMasthead && newBackdrop && newDrawer) {
        existingMasthead.replaceWith(newMasthead);
        document.getElementById('mobileNavBackdrop')?.replaceWith(newBackdrop);
        document.getElementById('mobileNavDrawer')?.replaceWith(newDrawer);
      }
    }

    const masthead = document.getElementById('masthead');
    if (masthead && !isHomePage()) {
      masthead.classList.add('compact');
      masthead.style.setProperty('--masthead-progress', '1');
    }

    syncNavOffset();
    window.dispatchEvent(new CustomEvent('emaavy:nav-mounted'));
  }

  function mountFooter() {
    const footerRoot = document.getElementById('site-footer-root');
    if (!footerRoot) return;
    footerRoot.innerHTML = renderFooter();
  }

  function mount() {
    mountMasthead();
    mountFooter();
    window.addEventListener('resize', syncNavOffset, { passive: true });
  }

  window.EMAAVYComponents = {
    mount,
    mountMasthead,
    mountFooter,
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
