/**
 * EMAAVY navigation — mobile menu, nav dropdowns, header scroll state
 */
(function () {
  const HOVER_CLOSE_MS = 450;
  const CLOSE_ANIM_MS = 480;

  const DROPDOWN_SPECS = [
    { id: 'integrationsDropdown', menuId: 'integrationsMenu', triggerId: 'integrationsDropdownTrigger', menuWidth: 580 },
    { id: 'agentsDropdown', menuId: 'agentsMenu', triggerId: 'agentsDropdownTrigger', menuWidth: 420 },
    { id: 'lifecycleDropdown', menuId: 'lifecycleMenu', triggerId: 'lifecycleDropdownTrigger', menuWidth: 420 },
    { id: 'faqDropdown', menuId: 'faqMenu', triggerId: 'faqDropdownTrigger', menuWidth: 420 },
  ];

  let dropdownApis = [];
  let mobileCloseBound = false;

  function closeMobileNav() {
    document.getElementById('mobileNavDrawer')?.classList.remove('open');
    document.getElementById('mobileNavBackdrop')?.classList.remove('open');
    document.getElementById('navHamburger')?.classList.remove('open');
    document.body.style.overflow = '';
  }

  function openMobileNav() {
    document.getElementById('mobileNavDrawer')?.classList.add('open');
    document.getElementById('mobileNavBackdrop')?.classList.add('open');
    document.getElementById('navHamburger')?.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  const MASTHEAD_COMPACT_RANGE = 100;
  let mastheadCompactBound = false;

  function initStickyHeader() {
    const header = document.getElementById('siteHeader');
    if (!header) return;
    const onScroll = () => header.classList.toggle('scrolled', window.scrollY > 12);
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  function initMastheadCompact() {
    if (document.body.dataset.page === 'home') return;
    if (mastheadCompactBound) return;
    const masthead = document.getElementById('masthead');
    if (!masthead) return;
    mastheadCompactBound = true;

    masthead.classList.add('compact');
    masthead.style.setProperty('--masthead-progress', window.scrollY > 0 ? '1' : '0.35');

    let ticking = false;

    function refresh() {
      const y = window.scrollY;
      const rect = masthead.getBoundingClientRect();
      const inView = rect.bottom > 0 && rect.top < window.innerHeight;

      if (inView) {
        const progress = Math.min(1, Math.max(0, y / MASTHEAD_COMPACT_RANGE));
        masthead.style.setProperty('--masthead-progress', progress.toFixed(3));
        masthead.classList.toggle('compact', progress > 0.2);
        masthead.classList.toggle('scrolled', y > 6);
      } else {
        masthead.style.setProperty('--masthead-progress', '0');
        masthead.classList.remove('compact', 'scrolled');
      }

      window.EMAAVYComponents?.syncNavOffset?.();
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

  function closeAllDropdowns(except) {
    dropdownApis.forEach((api) => {
      if (api && api !== except) api.close();
    });
  }

  function initNavDropdown(spec) {
    const dropdown = document.getElementById(spec.id);
    const menu = document.getElementById(spec.menuId);
    const trigger = document.getElementById(spec.triggerId);
    const masthead = document.getElementById('masthead') || document.getElementById('siteHeader');

    if (!dropdown || !menu || !trigger) return null;
    if (dropdown.dataset.navInited === '1') return null;
    dropdown.dataset.navInited = '1';

    let closeTimer = null;
    let closeAnimTimer = null;

    function isDesktop() {
      return window.matchMedia('(min-width: 861px)').matches;
    }

    function positionMenu() {
      if (!isDesktop()) {
        menu.classList.remove('is-fixed');
        menu.style.top = '';
        menu.style.left = '';
        menu.style.width = '';
        return;
      }
      const anchor = dropdown.getBoundingClientRect();
      const menuWidth = Math.min(spec.menuWidth || 420, window.innerWidth - 24);
      let left = anchor.left + anchor.width / 2;
      const half = menuWidth / 2;
      left = Math.max(half + 12, Math.min(window.innerWidth - half - 12, left));

      menu.classList.add('is-fixed');
      menu.style.top = `${anchor.bottom + 4}px`;
      menu.style.left = `${left}px`;
      menu.style.width = `${menuWidth}px`;
    }

    function cancelClose() {
      clearTimeout(closeTimer);
      clearTimeout(closeAnimTimer);
      dropdown.classList.remove('is-closing');
    }

    const api = { dropdown, close: closeMenu };

    function openMenu(animate) {
      cancelClose();
      closeAllDropdowns(api);

      const alreadyOpen = dropdown.classList.contains('open') && menu.classList.contains('is-visible');

      dropdown.classList.add('open');
      trigger.setAttribute('aria-expanded', 'true');
      menu.setAttribute('aria-hidden', 'false');
      masthead?.classList.add('nav-dropdown-active');
      positionMenu();

      if (alreadyOpen || animate === false) {
        menu.classList.add('is-visible');
        return;
      }

      menu.classList.remove('is-visible');
      void menu.offsetWidth;
      requestAnimationFrame(() => menu.classList.add('is-visible'));
    }

    function closeMenu() {
      if (!dropdown.classList.contains('open')) return;

      cancelClose();
      menu.classList.remove('is-visible');
      trigger.setAttribute('aria-expanded', 'false');
      menu.setAttribute('aria-hidden', 'true');
      masthead?.classList.remove('nav-dropdown-active');
      dropdown.classList.add('is-closing');

      closeAnimTimer = setTimeout(() => {
        dropdown.classList.remove('open', 'is-closing');
        menu.classList.remove('is-fixed');
        menu.style.top = '';
        menu.style.left = '';
        menu.style.width = '';
      }, CLOSE_ANIM_MS);
    }

    function scheduleClose() {
      clearTimeout(closeTimer);
      closeTimer = setTimeout(closeMenu, HOVER_CLOSE_MS);
    }

    function isMovingWithinDropdown(e) {
      const next = e.relatedTarget;
      return next instanceof Node && dropdown.contains(next);
    }

    function onZoneEnter() {
      if (!isDesktop()) return;
      openMenu(true);
    }

    function onZoneLeave(e) {
      if (!isDesktop()) return;
      if (isMovingWithinDropdown(e)) return;
      scheduleClose();
    }

    function onMenuEnter() {
      if (!isDesktop()) return;
      openMenu(false);
    }

    trigger.setAttribute('aria-haspopup', 'true');
    trigger.setAttribute('aria-expanded', 'false');
    trigger.setAttribute('aria-controls', spec.menuId);
    menu.setAttribute('role', 'menu');
    menu.setAttribute('aria-hidden', 'true');

    trigger.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();
      if (dropdown.classList.contains('open')) closeMenu();
      else openMenu(true);
    });

    dropdown.addEventListener('mouseenter', onZoneEnter);
    dropdown.addEventListener('mouseleave', onZoneLeave);
    menu.addEventListener('mouseenter', onMenuEnter);
    menu.addEventListener('mouseleave', onZoneLeave);

    menu.querySelectorAll('a[href]').forEach((a) => {
      a.setAttribute('role', 'menuitem');
      a.addEventListener('click', () => closeMenu());
    });

    api.open = () => openMenu(true);
    api.toggle = () => (dropdown.classList.contains('open') ? closeMenu() : openMenu(true));

    return api;
  }

  function initDropdowns() {
    dropdownApis = DROPDOWN_SPECS.map(initNavDropdown).filter(Boolean);
  }

  function bindDocumentHandlers() {
    if (bindDocumentHandlers.bound) return;
    bindDocumentHandlers.bound = true;

    document.addEventListener('click', (e) => {
      const inDropdown = dropdownApis.some((api) => api?.dropdown?.contains(e.target));
      if (!inDropdown) closeAllDropdowns();
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        closeMobileNav();
        closeAllDropdowns();
      }
    });

    function repositionOpenMenus() {
      dropdownApis.forEach((entry) => {
        if (!entry?.dropdown?.classList.contains('open')) return;
        const spec = DROPDOWN_SPECS.find((s) => s.id === entry.dropdown.id);
        const menuEl = document.getElementById(spec?.menuId || '');
        if (!menuEl?.classList.contains('is-fixed')) return;
        const anchor = entry.dropdown.getBoundingClientRect();
        const menuWidth = Math.min(spec?.menuWidth || 420, window.innerWidth - 24);
        let left = anchor.left + anchor.width / 2;
        const half = menuWidth / 2;
        left = Math.max(half + 12, Math.min(window.innerWidth - half - 12, left));
        menuEl.style.top = `${anchor.bottom + 4}px`;
        menuEl.style.left = `${left}px`;
        menuEl.style.width = `${menuWidth}px`;
      });
    }

    window.addEventListener('resize', repositionOpenMenus, { passive: true });
    window.addEventListener('scroll', repositionOpenMenus, { passive: true });
  }

  function bindMobileCloseOnce() {
    if (mobileCloseBound) return;
    mobileCloseBound = true;
    document.addEventListener('click', (e) => {
      if (e.target.closest('#mobileNavDrawer a')) closeMobileNav();
    });
  }

  let hamburgerBound = false;

  function initCore() {
    if (!hamburgerBound) {
      hamburgerBound = true;
      document.getElementById('navHamburger')?.addEventListener('click', () => {
        const drawer = document.getElementById('mobileNavDrawer');
        if (drawer?.classList.contains('open')) closeMobileNav();
        else openMobileNav();
      });
      document.getElementById('mobileNavBackdrop')?.addEventListener('click', closeMobileNav);
    }
    bindDocumentHandlers();
    bindMobileCloseOnce();
    initStickyHeader();
    initMastheadCompact();
  }

  function init() {
    initCore();
    initDropdowns();
  }

  function boot() {
    const hasHeader = document.getElementById('masthead') || document.getElementById('siteHeader');
    if (!hasHeader) {
      setTimeout(boot, 50);
      return;
    }
    init();
  }

    window.addEventListener('emaavy:nav-mounted', () => {
      initDropdowns();
      bindMobileCloseOnce();
      if (!mastheadCompactBound) initMastheadCompact();
      if (typeof window.emaavyLandingNav?.syncMastheadHeight === 'function') {
        requestAnimationFrame(() => window.emaavyLandingNav.syncMastheadHeight());
      } else {
        requestAnimationFrame(() => window.EMAAVYComponents?.syncNavOffset?.());
      }
    });

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }

  window.emaavyNav = {
    closeMobileNav,
    openMobileNav,
    closeIntegrationsDropdown: () => {
      const api = dropdownApis.find((a) => a?.dropdown?.id === 'integrationsDropdown');
      api?.close();
    },
    closeAllDropdowns,
  };
})();
