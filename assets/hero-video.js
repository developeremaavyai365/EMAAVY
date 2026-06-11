(function () {
  'use strict';

  var root = document.getElementById('heroVisual');
  var video = document.getElementById('heroShowcaseVideo');
  var muteBtn = document.getElementById('heroVideoMute');
  if (!root || !video) return;

  var chapters = root.querySelectorAll('.hero-showcase-chapter');
  var sceneLen = 5;
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function setMuted(muted) {
    video.muted = muted;
    if (muteBtn) {
      muteBtn.setAttribute('aria-pressed', muted ? 'true' : 'false');
      muteBtn.setAttribute('aria-label', muted ? 'Unmute video' : 'Mute video');
      var icon = muteBtn.querySelector('.hero-video-mute-icon');
      var label = muteBtn.querySelector('.hero-video-mute-label');
      if (icon) icon.textContent = muted ? '🔇' : '🔊';
      if (label) label.textContent = muted ? 'Sound off' : 'Sound on';
    }
  }

  if (muteBtn) {
    setMuted(true);
    muteBtn.addEventListener('click', function () {
      setMuted(!video.muted);
      if (!video.muted) {
        video.play().catch(function () {});
      }
    });
  }

  function updateChapters() {
    if (!chapters.length || video.paused) return;
    var idx = Math.floor((video.currentTime % (sceneLen * chapters.length)) / sceneLen);
    chapters.forEach(function (ch, n) {
      ch.classList.toggle('is-active', n === idx);
    });
  }

  video.addEventListener('timeupdate', updateChapters);
  video.addEventListener('loadedmetadata', updateChapters);

  function showVideoFallback() {
    var viewport = root.querySelector('.hero-showcase-viewport');
    if (!viewport || viewport.querySelector('.hero-showcase-video-fallback')) return;
    video.style.display = 'none';
    var img = document.createElement('img');
    img.className = 'hero-showcase-video-fallback';
    img.src = video.getAttribute('poster') || 'assets/hero/dashboard.png';
    img.alt = video.getAttribute('aria-label') || 'EMAAVY platform preview';
    img.decoding = 'async';
    img.loading = 'eager';
    viewport.appendChild(img);
    root.classList.add('hero-showcase--fallback');
    var controls = muteBtn && muteBtn.closest('.hero-showcase-video-controls');
    if (controls) controls.style.display = 'none';
  }

  video.addEventListener('error', showVideoFallback);

  if (!reduced) {
    var playAttempt = function () {
      video.play().catch(function () {
        root.addEventListener('pointerenter', function once() {
          video.play().catch(function () {});
          root.removeEventListener('pointerenter', once);
        });
      });
    };
    if (document.readyState === 'complete') playAttempt();
    else window.addEventListener('load', playAttempt);
  }

  document.addEventListener('visibilitychange', function () {
    if (document.hidden) video.pause();
    else if (!reduced) video.play().catch(function () {});
  });
})();
