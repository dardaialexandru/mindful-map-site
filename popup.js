/* Optional newsletter popup. Shows after 3 link clicks, once a day, never to subscribers,
   never on help/privacy pages. Remembers only the user's own choice (closed today / subscribed). */
(function () {
  var path = location.pathname;
  if (/help\.html|privacy\.html|harmony\.html|harta-/.test(path)) return;
  var K = { c: 'mm_clicks', d: 'mm_popup_day', s: 'mm_subscribed' };
  // Click count lives in sessionStorage (gone when the tab closes). Only a user's own choice
  // (closing the popup or subscribing) is remembered in localStorage.
  var SESSION = { mm_clicks: 1 };
  function get(k) { try { return (SESSION[k] ? sessionStorage : localStorage).getItem(k); } catch (e) { return null; } }
  function set(k, v) { try { (SESSION[k] ? sessionStorage : localStorage).setItem(k, v); } catch (e) {} }
  if (get(K.s) === '1') return;
  var today = new Date().toISOString().slice(0, 10);
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href]');
    if (!a || a.target === '_blank') return;
    var n = parseInt(get(K.c) || '0', 10) + 1;
    set(K.c, String(n));
  });
  var n0 = parseInt(get(K.c) || '0', 10);
  if (n0 < 3 || get(K.d) === today) return;
  setTimeout(open, 1200);

  var lastFocus;
  function open() {
    if (document.getElementById('mm-pop')) return;
    lastFocus = document.activeElement;
    var w = document.createElement('div');
    w.id = 'mm-pop';
    w.innerHTML =
      '<div class="mm-box" role="dialog" aria-modal="true" aria-labelledby="mm-t" tabindex="-1">' +
      '<button type="button" class="mm-x" aria-label="Close">&times;</button>' +
      '<h2 id="mm-t">Get the free Harmony Map</h2>' +
      '<p>A short guide to find your way back to calm, plus one short email a week. Optional, and you can leave at any time.</p>' +
      '<form id="mm-f"><input type="email" name="fields[email]" placeholder="your email address" required aria-label="Email address" autocomplete="email">' +
      '<label class="mm-c"><input type="checkbox" id="mm-ok" required> <span>I agree to receive the Harmony Map and a weekly email at this address. I can unsubscribe in any email. <a href="/privacy.html">Privacy</a></span></label>' +
      '<button type="submit" class="mm-go">Send me the map</button></form>' +
      '<p class="mm-done" id="mm-done" role="status" hidden>Thank you. Check your inbox to confirm.</p>' +
      '<button type="button" class="mm-no">No thanks</button></div>';
    document.body.appendChild(w);
    var box = w.querySelector('.mm-box'); box.focus();
    function close() { set(K.d, today); w.remove(); document.removeEventListener('keydown', key); if (lastFocus && lastFocus.focus) lastFocus.focus(); }
    function key(e) { if (e.key === 'Escape') close(); }
    document.addEventListener('keydown', key);
    w.querySelector('.mm-x').onclick = close; w.querySelector('.mm-no').onclick = close;
    w.addEventListener('click', function (e) { if (e.target === w) close(); });
    w.querySelector('#mm-f').addEventListener('submit', function (e) {
      e.preventDefault();
      var f = e.target, email = f.elements['fields[email]'].value;
      var d = new URLSearchParams(); d.set('fields[email]', email); d.set('ml-submit', '1'); d.set('anticsrf', 'true');
      var b = new URLSearchParams(); b.set('form-name', 'subscribe'); b.set('fields[email]', email); b.set('bot-field', '');
      fetch('/', { method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: b.toString() }).catch(function () {});
      fetch('https://assets.mailerlite.com/jsonp/2629517/forms/201143149078251433/subscribe', { method: 'POST', mode: 'no-cors', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: d.toString() })
        .then(function () { set(K.s, '1'); f.hidden = true; w.querySelector('#mm-done').hidden = false; setTimeout(close, 3500); })
        .catch(function () { f.insertAdjacentHTML('beforeend', '<p role="alert">Something went wrong. Please try again later.</p>'); });
    });
  }
})();
