# Translation pipeline

English is the original. `build/build.py` writes the English pages; `translate/translate_site.py` translates them into
Spanish, German and Romanian with the Claude API and writes them to `/es/`, `/de/`, `/ro/`.

* Needs the GitHub secret `ANTHROPIC_API_KEY`. Without it the step is skipped and the English site is unaffected.
* Only new or changed English strings are sent; everything else comes from `translations/<lang>.json`.
* Every number (phone numbers, percentages) is checked after translation. If a translation changes a number, the English text is kept.
* To fix a translation by hand, edit the value in `translations/<lang>.json`; the cache is never overwritten for existing strings.
* Test without the API: `TRANSLATE_MOCK=1 python translate/translate_site.py` (then delete `es/ de/ ro/`).
