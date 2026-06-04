/**
 * Pricing page — billing toggle, card reveal, optional tilt.
 */
(function () {
  const billingToggle = document.getElementById('billingToggle');
  if (!billingToggle) return;

  const labelMonthly = document.getElementById('labelMonthly');
  const labelYearly = document.getElementById('labelYearly');
  const savePill = document.getElementById('savePill');
  let isYearly = false;

  function updatePrices() {
    document.querySelectorAll('.price-card[data-monthly]').forEach((card) => {
      const amountEl = card.querySelector('.amount');
      const billedEl = card.querySelector('.pack-billed');
      if (!amountEl || !amountEl.dataset.monthly) return;
      const monthly = amountEl.dataset.monthly;
      const yearly = amountEl.dataset.yearly;
      const val = isYearly ? yearly : monthly;
      amountEl.classList.add('flip');
      setTimeout(() => {
        amountEl.textContent = val;
        amountEl.classList.remove('flip');
      }, 180);
      if (billedEl) {
        billedEl.textContent = isYearly ? billedEl.dataset.yearly : billedEl.dataset.monthly;
      }
    });
  }

  billingToggle.addEventListener('click', () => {
    isYearly = !isYearly;
    billingToggle.classList.toggle('yearly', isYearly);
    labelMonthly?.classList.toggle('active', !isYearly);
    labelYearly?.classList.toggle('active', isYearly);
    savePill?.classList.toggle('show', isYearly);
    updatePrices();
  });

  document.querySelectorAll('.price-card.reveal').forEach((card) => {
    new IntersectionObserver(
      ([e]) => {
        if (e.isIntersecting) card.classList.add('in');
      },
      { threshold: 0.2 }
    ).observe(card);
  });

  document.querySelectorAll('.pricing-head.reveal, .pricing-compare.reveal').forEach((el) => {
    new IntersectionObserver(
      ([e]) => {
        if (e.isIntersecting) el.classList.add('in');
      },
      { threshold: 0.12, rootMargin: '0px 0px -30px 0px' }
    ).observe(el);
  });

  document.querySelectorAll('.click-detail[data-detail^="price-"]').forEach((el) => {
    el.addEventListener('click', (e) => {
      if (e.target.closest('button, a')) return;
      window.location.href = '../book-demo.html';
    });
    el.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        window.location.href = '../book-demo.html';
      }
    });
  });

  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!reduceMotion) {
    document.querySelectorAll('.price-card').forEach((card) => {
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
  }
})();
