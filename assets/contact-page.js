(function () {
  document.querySelectorAll('.reveal').forEach((el) => {
    new IntersectionObserver(
      ([e]) => {
        if (e.isIntersecting) el.classList.add('in');
      },
      { threshold: 0.08, rootMargin: '0px 0px -20px 0px' }
    ).observe(el);
  });

  const form = document.getElementById('contactForm');
  const toast = document.getElementById('contactToast');

  function showToast(message) {
    if (!toast) return;
    toast.textContent = message;
    toast.classList.add('is-visible');
    setTimeout(() => toast.classList.remove('is-visible'), 4500);
  }

  form?.addEventListener('submit', (e) => {
    e.preventDefault();
    showToast("Message sent — we'll reply within one business day.");
    form.reset();
  });
})();
