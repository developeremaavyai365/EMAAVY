/**
 * Landing page — scroll-spy, smooth anchors (masthead scrolls with page; not fixed).
 */
(function () {
  const SECTION_IDS = [
    'top',
    'how-it-works',
    'integrations',
    'agents',
    'campaigns',
    'features',
    'case-studies',
    'journey',
    'faq',
    'book-demo',
  ];

  const NAV_SECTION_IDS = new Set([
    'how-it-works',
    'integrations',
    'agents',
    'campaigns',
    'features',
    'case-studies',
    'journey',
    'faq',
  ]);

  const ANCHOR_OFFSET = 16;
  const COMPACT_RANGE = 100;

  function isHome() {
    return (
      document.body?.dataset.page === 'home' ||
      (document.getElementById('masthead') && document.querySelector('.rail-dots'))
    );
  }

  function getMasthead() {
    return document.getElementById('masthead');
  }

  function getScrollOffset() {
    const masthead = getMasthead();
    if (!masthead) return ANCHOR_OFFSET;
    const rect = masthead.getBoundingClientRect();
    if (rect.bottom > 0 && rect.top < window.innerHeight) {
      return Math.ceil(rect.height) + ANCHOR_OFFSET;
    }
    return ANCHOR_OFFSET;
  }

  function scrollToId(id, behavior) {
    const el = document.getElementById(id);
    if (!el) return;
    const top = el.getBoundingClientRect().top + window.scrollY - getScrollOffset();
    window.scrollTo({ top: Math.max(0, top), behavior: behavior || 'smooth' });
  }

  function resolveNavSection(sectionId) {
    if (!sectionId || sectionId === 'top' || sectionId === 'book-demo') return null;
    if (sectionId.startsWith('integration-')) return 'integrations';
    return NAV_SECTION_IDS.has(sectionId) ? sectionId : null;
  }

  function computeActiveSection() {
    const line = window.scrollY + ANCHOR_OFFSET + 8;
    let active = 'top';

    for (const id of SECTION_IDS) {
      const el = document.getElementById(id);
      if (!el) continue;
      const top = el.getBoundingClientRect().top + window.scrollY;
      if (top <= line + 2) active = id;
    }

    return active;
  }

  function syncMastheadHeight() {
    const masthead = getMasthead();
    if (!masthead) return;
    const h = Math.ceil(masthead.getBoundingClientRect().height) || 64;
    document.documentElement.style.setProperty('--masthead-h', `${h}px`);
  }

  function updateMastheadState(y) {
    const masthead = getMasthead();
    if (!masthead) return;

    const rect = masthead.getBoundingClientRect();
    const inView = rect.bottom > 0 && rect.top < window.innerHeight;

    if (inView) {
      const progress = Math.min(1, Math.max(0, y / COMPACT_RANGE));
      masthead.style.setProperty('--masthead-progress', progress.toFixed(3));
      masthead.classList.toggle('compact', progress > 0.2);
      masthead.classList.toggle('scrolled', y > 6);
    } else {
      masthead.style.setProperty('--masthead-progress', '0');
      masthead.classList.remove('compact', 'scrolled');
    }

    masthead.classList.remove('masthead--away');
    document.documentElement.style.setProperty('--nav-offset', `${ANCHOR_OFFSET}px`);
    syncMastheadHeight();
  }

  function setActiveUI(sectionId) {
    const navSection = resolveNavSection(sectionId);
    const masthead = getMasthead();
    if (masthead) {
      masthead.classList.toggle('masthead--in-section', sectionId !== 'top');
    }

    document.querySelectorAll('[data-nav-section]').forEach((link) => {
      const key = link.getAttribute('data-nav-section');
      link.classList.toggle('active', !!navSection && key === navSection);
    });

    document.querySelectorAll('.rail-dots a').forEach((dot) => {
      const href = dot.getAttribute('href');
      if (!href || !href.startsWith('#')) return;
      dot.classList.toggle('active', href === `#${sectionId}`);
    });
  }

  function initScrollSpy() {
    let ticking = false;

    function refresh() {
      const y = window.scrollY;
      updateMastheadState(y);
      setActiveUI(computeActiveSection());
      ticking = false;
    }

    function onScrollOrResize() {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(refresh);
    }

    window.addEventListener('scroll', onScrollOrResize, { passive: true });
    window.addEventListener('resize', onScrollOrResize, { passive: true });
    refresh();
  }

  function scrollToHashFromLink(a, e) {
    const href = a.getAttribute('href');
    if (!href || href === '#') return false;

    let id = '';
    try {
      const url = new URL(href, window.location.href);
      if (url.pathname.replace(/\/$/, '') !== location.pathname.replace(/\/$/, '')) return false;
      id = url.hash.slice(1);
    } catch {
      if (!href.startsWith('#')) return false;
      id = href.slice(1);
    }

    if (!id || !document.getElementById(id)) return false;

    e.preventDefault();
    scrollToId(id);
    window.emaavyNav?.closeAllDropdowns?.();
    window.emaavyNav?.closeMobileNav?.();
    return true;
  }

  function initSmoothAnchors() {
    document.querySelector('.rail-dots')?.addEventListener('click', (e) => {
      const a = e.target.closest('a[href]');
      if (a) scrollToHashFromLink(a, e);
    });

    document.querySelector('.masthead-nav')?.addEventListener('click', (e) => {
      if (e.target.closest('.nav-dropdown-caret')) return;
      const a = e.target.closest('a[href]');
      if (!a || a.closest('.nav-dropdown-menu')) return;
      scrollToHashFromLink(a, e);
    });
  }

  function initRailCta() {
    document.querySelector('.rail-cta')?.addEventListener('click', () => {
      const target = document.getElementById('book-demo') || document.getElementById('cta');
      if (target) scrollToId(target.id);
      else window.location.href = 'book-demo.html';
    });
  }

  function initBookDemoSection() {
    const section = document.getElementById('book-demo');
    if (!section) return;

    section.style.scrollMarginTop = `calc(${getScrollOffset()}px + 8px)`;

    const submit = section.querySelector('.demo-submit');
    if (submit && submit.tagName === 'BUTTON') {
      submit.addEventListener('click', () => {
        window.location.href = 'book-demo.html';
      });
    }
  }

  function initLandingScroll() {
    if ('scrollRestoration' in history) {
      history.scrollRestoration = 'manual';
    }

    const rawHash = (location.hash || '').replace(/^#/, '');
    const sectionHash = rawHash && rawHash !== 'top' && rawHash !== '/' ? rawHash : '';

    if (!sectionHash) {
      window.scrollTo(0, 0);
      if (rawHash) {
        history.replaceState(null, '', location.pathname + location.search);
      }
      return;
    }

    const target = document.getElementById(sectionHash);
    if (target) {
      requestAnimationFrame(() => scrollToId(sectionHash, 'instant'));
    } else {
      window.scrollTo(0, 0);
    }
  }

  function boot() {
    if (!isHome()) return;
    initLandingScroll();
    const masthead = getMasthead();
    if (masthead) {
      masthead.classList.add('compact');
      masthead.style.setProperty('--masthead-progress', window.scrollY > 0 ? '1' : '0.35');
    }
    initScrollSpy();
    initSmoothAnchors();
    initRailCta();
    initBookDemoSection();
    requestAnimationFrame(() => {
      updateMastheadState(window.scrollY);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }

  window.emaavyLandingNav = {
    getScrollOffset,
    scrollToId,
    computeActiveSection,
    syncMastheadHeight,
  };
})();
