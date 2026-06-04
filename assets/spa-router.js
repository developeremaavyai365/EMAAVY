/**
 * SPA hash router for single-file EMAAVY landing page
 */
(function () {
  if (document.body.dataset.spa !== 'true') return;

  const TITLES = {
    home: ['EMAAVY — Signal From Every Call', 'Call intelligence platform — decode every conversation.'],
    'how-it-works': ['How It Works — EMAAVY', 'Four steps from ring to action — connect, transcribe, reason, act.'],
    features: ['Features — EMAAVY', 'Bulk calling, STT, AI agents, call intelligence, and enterprise security.'],
    integrations: ['Integrations — EMAAVY', 'Connect your entire AI stack — LLMs, STT, TTS, CRM, and tools.'],
    agents: ['AI Agents — EMAAVY', 'Deploy sales, support, and outbound AI voice agents at scale.'],
    'case-studies': ['Case Studies — EMAAVY', 'Real client results from EMAAVY campaigns.'],
    pricing: ['Pricing — EMAAVY', 'Starter, Pro, Business, and Enterprise plans.'],
    documentation: ['Documentation — EMAAVY', 'Quickstart, API reference, and agent builder guides.'],
    contact: ['Contact Us — EMAAVY', 'Get in touch with the EMAAVY team.'],
    login: ['Log In — EMAAVY', 'Sign in to your EMAAVY workspace.'],
    'book-demo': ['Book a Demo — EMAAVY', 'Schedule a live EMAAVY product walkthrough.'],
  };

  function viewId(route) {
    if (!route || route === 'home') return 'view-home';
    return 'view-' + route.replace(/\//g, '-');
  }

  function routeFromHash() {
    const hash = window.location.hash.replace(/^#\/?/, '');
    return hash || 'home';
  }

  function routeToDataRoute(route) {
    if (route === 'home') return 'home';
    if (route.startsWith('integrations/')) return 'integration-' + route.split('/')[1];
    if (route.startsWith('agents/')) return 'agent-' + route.split('/')[1];
    return route;
  }

  function setMeta(title, desc) {
    document.title = title;
    let meta = document.querySelector('meta[name="description"]');
    if (!meta) {
      meta = document.createElement('meta');
      meta.name = 'description';
      document.head.appendChild(meta);
    }
    meta.content = desc;
  }

  function navigate(route, push) {
    const id = viewId(route);
    const view = document.getElementById(id);
    if (!view) {
      console.warn('Unknown route:', route);
      return;
    }

    document.querySelectorAll('.spa-view').forEach((v) => v.classList.remove('active'));
    view.classList.add('active');

    const dataRoute = routeToDataRoute(route);
    document.body.dataset.route = dataRoute;

    const t = TITLES[route] || TITLES[route.split('/')[0]];
    if (t) {
      setMeta(t[0], t[1]);
    } else if (route.startsWith('integrations/')) {
      const name = route.split('/')[1].replace(/-/g, ' ').replace(/\b\w/g, (c) => c.toUpperCase());
      setMeta(`${name} Integration — EMAAVY`, `Connect ${name} with EMAAVY call intelligence.`);
    } else if (route.startsWith('agents/')) {
      const name = route.split('/')[1].replace(/-/g, ' ').replace(/\b\w/g, (c) => c.toUpperCase());
      setMeta(`${name} — EMAAVY`, `Deploy the EMAAVY ${name} for your campaigns.`);
    } else {
      setMeta(TITLES.home[0], TITLES.home[1]);
    }

    if (push !== false) {
      const hash = route === 'home' ? '#/' : '#/' + route;
      const url = window.location.pathname + window.location.search + (route === 'home' ? '' : hash);
      if (window.location.hash !== (route === 'home' ? '' : hash) && window.location.href !== url) {
        history.pushState({ route }, '', route === 'home' ? window.location.pathname + window.location.search : hash);
      }
    }

    window.scrollTo(0, 0);
    document.getElementById('integrationsDropdown')?.classList.remove('open');
    document.getElementById('agentsDropdown')?.classList.remove('open');
    window.emaavyNav?.closeMobileNav?.();

    if (window.EMAAVYComponents?.mount) window.EMAAVYComponents.mount();
  }

  function handleLinkClick(e) {
    const a = e.target.closest('a[href^="#/"]');
    if (!a) return;
    e.preventDefault();
    const route = a.getAttribute('href').replace(/^#\/?/, '');
    navigate(route);
  }

  function init() {
    document.addEventListener('click', handleLinkClick);
    window.addEventListener('popstate', () => navigate(routeFromHash(), false));
    window.addEventListener('hashchange', () => navigate(routeFromHash(), false));
    navigate(routeFromHash(), false);
  }

  window.EMAAVYRouter = { navigate, routeFromHash, viewId };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
