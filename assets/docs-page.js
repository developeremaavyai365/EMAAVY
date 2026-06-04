/**
 * Documentation page — scroll reveal and card interactions.
 */
(function () {
  document.querySelectorAll('.reveal').forEach((el) => {
    new IntersectionObserver(
      ([e]) => {
        if (e.isIntersecting) el.classList.add('in');
      },
      { threshold: 0.12, rootMargin: '0px 0px -30px 0px' }
    ).observe(el);
  });

  document.querySelectorAll('.click-detail[data-detail^="docs-"]').forEach((el) => {
    const go = () => {
      window.location.href = '../book-demo.html';
    };
    el.addEventListener('click', (e) => {
      if (e.target.closest('button, a')) return;
      go();
    });
    el.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        go();
      }
    });
  });
})();
