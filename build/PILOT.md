# Illustrated pages (pilot design)

`index.html`, `help.html`, `privacy.html`, `soul.html`, `feel/*.html` and `need/*.html` are the illustrated version of
the site (tree, illustrations, voiced explainer videos in `media/`). They are NOT written by `build.py`: `write()` skips
them, so the build and the translation workflow cannot overwrite them. Edit those files directly, or regenerate them
from the pilot generator and copy them in. The pages `needs.html`, `doors.html`, `door/*`, `life.html`, `map.html`,
`background.html`, `connections.html`, `how-we-know.html` still come from `build.py`.

Email collection is unchanged: the popup posts to the Netlify form `subscribe` (declared in `harmony.html`) and to the
MailerLite form endpoint, exactly as `popup.js` does.

## Translations

The translation workflow no longer runs automatically on pushes. The illustrated pages are English only for now; if the
workflow ran, language redirects (`lang.js`) could send visitors to pages that do not exist. Switch translations on again
only after the illustrated pages are covered (add them to the translator and test `/es/`, `/de/`, `/ro/`).
