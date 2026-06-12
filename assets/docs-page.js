/**
 * Documentation page — scroll reveal and card interactions.
 */
(function () {
  var DOC_ROUTES = {
    'docs-quickstart': 'api-docs/using-agents-apis.html',
    'docs-api': 'api-docs/api-authentication.html',
    'docs-agents': 'agents/workforce.html',
  };

  document.querySelectorAll('.reveal').forEach(function (el) {
    new IntersectionObserver(
      function (entries) {
        if (entries[0].isIntersecting) el.classList.add('in');
      },
      { threshold: 0.12, rootMargin: '0px 0px -30px 0px' }
    ).observe(el);
  });

  document.querySelectorAll('.click-detail[data-detail^="docs-"]').forEach(function (el) {
    var detail = el.getAttribute('data-detail');
    var target = DOC_ROUTES[detail] || 'api-docs/api-authentication.html';

    function go() {
      window.location.href = target;
    }

    el.addEventListener('click', function (e) {
      if (e.target.closest('button, a')) return;
      go();
    });
    el.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        go();
      }
    });
  });
})();
