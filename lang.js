/* Suggest the visitor's language once per visit, on the home page only. No cookies, no storage that outlives the tab. */
(function () {
  try {
    document.addEventListener('click', function (e) {
      var a = e.target.closest && e.target.closest('nav.langs a');
      if (a) sessionStorage.setItem('mm_lang_set', '1');
    });
    if (location.pathname !== '/' || sessionStorage.getItem('mm_lang_set')) return;
    var l = (navigator.language || '').slice(0, 2).toLowerCase();
    if (['es', 'de', 'ro'].indexOf(l) > -1) { sessionStorage.setItem('mm_lang_set', '1'); location.replace('/' + l + '/'); }
  } catch (e) {}
})();
