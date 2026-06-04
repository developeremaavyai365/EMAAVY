(function () {
  'use strict';
  var root = document.getElementById('heroVisual');
  if (!root) return;

  var slides = root.querySelectorAll('.hero-slide');
  var dots = root.querySelectorAll('.hero-showcase-dots button');
  var urlEl = document.getElementById('heroShowcaseUrl');
  var liveEl = document.getElementById('heroShowcaseLive');
  var index = 0;
  var timer = null;
  var delay = 5500;
  var fadeMs = 800;
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  root.classList.add('is-idle');

  slides.forEach(function (slide) {
    var img = slide.querySelector('img');
    if (img && img.src) {
      var pre = new Image();
      if (img.srcset) pre.srcset = img.srcset;
      pre.src = img.currentSrc || img.src;
    }
  });

  function setProgress(playing) {
    if (reduced) return;
    dots.forEach(function (dot, n) {
      var bar = dot.querySelector('.hero-showcase-progress');
      if (!bar) return;
      bar.style.animation = 'none';
      void bar.offsetWidth;
      if (playing && n === index) {
        bar.style.animation = 'heroShowcaseProgress ' + delay + 'ms linear forwards';
      }
    });
  }

  function pulseLive() {
    if (!liveEl || reduced) return;
    liveEl.classList.add('is-syncing');
    window.setTimeout(function () {
      liveEl.classList.remove('is-syncing');
    }, 500);
  }

  function setUrl(path) {
    if (!urlEl) return;
    var full = 'app.emaavy.com' + (path || '');
    if (urlEl.textContent === full) return;
    if (reduced) {
      urlEl.textContent = full;
      return;
    }
    urlEl.classList.add('is-fading');
    window.setTimeout(function () {
      urlEl.textContent = full;
      urlEl.classList.remove('is-fading');
    }, 180);
  }

  function updateDots() {
    dots.forEach(function (dot, n) {
      var on = n === index;
      dot.classList.toggle('is-active', on);
      dot.setAttribute('aria-selected', on ? 'true' : 'false');
    });
  }

  function show(i) {
    var nextIdx = (i + slides.length) % slides.length;
    if (nextIdx === index) return;

    var outgoing = slides[index];
    var incoming = slides[nextIdx];
    index = nextIdx;

    root.classList.remove('is-idle');
    pulseLive();

    if (reduced) {
      slides.forEach(function (slide, n) {
        slide.classList.remove('is-leaving');
        slide.classList.toggle('is-active', n === index);
      });
    } else {
      outgoing.classList.remove('is-active');
      outgoing.classList.add('is-leaving');
      incoming.classList.add('is-active');

      window.setTimeout(function () {
        outgoing.classList.remove('is-leaving');
        root.classList.add('is-idle');
      }, fadeMs);
    }

    setUrl(incoming.getAttribute('data-path'));
    updateDots();
    setProgress(true);
  }

  function next() {
    show(index + 1);
  }

  function start() {
    stop();
    if (reduced) return;
    setProgress(true);
    timer = window.setInterval(next, delay);
  }

  function stop() {
    if (timer) {
      window.clearInterval(timer);
      timer = null;
    }
    setProgress(false);
  }

  dots.forEach(function (dot, i) {
    dot.addEventListener('click', function () {
      show(i);
      start();
    });
  });

  root.addEventListener('mouseenter', stop);
  root.addEventListener('mouseleave', start);
  root.addEventListener('focusin', stop);
  root.addEventListener('focusout', function (e) {
    if (!root.contains(e.relatedTarget)) start();
  });

  root.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowRight') {
      e.preventDefault();
      next();
      start();
    } else if (e.key === 'ArrowLeft') {
      e.preventDefault();
      show(index - 1);
      start();
    }
  });

  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) start();
          else stop();
        });
      },
      { threshold: 0.2 }
    );
    io.observe(root);
  } else {
    start();
  }

  slides.forEach(function (slide, n) {
    slide.classList.toggle('is-active', n === 0);
    slide.classList.remove('is-leaving');
  });
  setUrl(slides[0] ? slides[0].getAttribute('data-path') : '');
  updateDots();
  setProgress(true);
})();
