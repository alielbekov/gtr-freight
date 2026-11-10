(function () {
  'use strict';

  /* Sticky header shadow */
  var header = document.querySelector('.site-header');
  function onScroll() {
    if (!header) return;
    header.classList.toggle('is-scrolled', window.scrollY > 4);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* Mobile menu */
  var toggle = document.querySelector('.nav-toggle');
  var menu = document.querySelector('.nav-menu');
  if (toggle && menu) {
    toggle.addEventListener('click', function () {
      var open = menu.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  /* Dropdowns (click / keyboard on small screens, hover on desktop via CSS) */
  document.querySelectorAll('.dropdown > .nav-link').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      var dd = btn.parentElement;
      var open = dd.classList.toggle('is-open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      document.querySelectorAll('.dropdown.is-open').forEach(function (other) {
        if (other !== dd) {
          other.classList.remove('is-open');
          other.querySelector('.nav-link').setAttribute('aria-expanded', 'false');
        }
      });
    });
  });
  document.addEventListener('click', function (e) {
    if (!e.target.closest('.dropdown')) {
      document.querySelectorAll('.dropdown.is-open').forEach(function (dd) {
        dd.classList.remove('is-open');
        dd.querySelector('.nav-link').setAttribute('aria-expanded', 'false');
      });
    }
  });

  /* Testimonial carousel */
  document.querySelectorAll('.carousel').forEach(function (carousel) {
    var track = carousel.querySelector('.carousel-track');
    var prev = carousel.querySelector('[data-dir="prev"]');
    var next = carousel.querySelector('[data-dir="next"]');
    if (!track) return;
    function step() {
      var card = track.querySelector('.testimonial');
      return card ? card.getBoundingClientRect().width + 24 : 400;
    }
    if (prev) prev.addEventListener('click', function () { track.scrollBy({ left: -step(), behavior: 'smooth' }); });
    if (next) next.addEventListener('click', function () { track.scrollBy({ left: step(), behavior: 'smooth' }); });
    // Start on the middle card so the side cards peek in, like the design.
    function center() {
      var cards = track.querySelectorAll('.testimonial');
      if (cards.length < 2) return;
      var mid = cards[Math.floor(cards.length / 2)];
      track.style.scrollBehavior = 'auto';
      track.scrollLeft = mid.offsetLeft - (track.clientWidth - mid.offsetWidth) / 2;
      track.style.scrollBehavior = '';
    }
    center();
    window.addEventListener('load', center);
  });

  /* Forms: static site, so show a confirmation instead of posting.
     To wire up a backend, set the form's action attribute (e.g. a Formspree
     endpoint) and remove the data-static attribute. */
  document.querySelectorAll('form[data-static]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var card = form.closest('.form-card') || form;
      card.classList.add('is-sent');
      form.reset();
    });
  });
})();
