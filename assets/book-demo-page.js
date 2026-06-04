(function () {
  const form = document.getElementById('demoForm');
  const toast = document.getElementById('demoToast');

  function showToast(message) {
    if (!toast) return;
    toast.textContent = message;
    toast.classList.add('is-visible');
    setTimeout(() => toast.classList.remove('is-visible'), 5000);
  }

  form?.addEventListener('submit', (e) => {
    e.preventDefault();
    const slot = form.querySelector('input[name="slot"]:checked');
    if (!slot) {
      showToast('Please pick a preferred time slot for your walkthrough.');
      return;
    }
    const email = form.querySelector('[name="email"]');
    if (email && !email.value.includes('@')) {
      showToast('Enter a valid work email so we can send your calendar invite.');
      return;
    }
    showToast(
      "You're booked! Our team will confirm your demo within 24 hours — check your inbox."
    );
    form.reset();
  });
})();
