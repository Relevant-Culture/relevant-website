# Relevant website

Static site for Relevant (relevant.es), served by GitHub Pages from the `main` branch, root folder, at **https://www.relevant.es** (custom domain via the `CNAME` file; DNS at iwantmyname).

## Who you're working with

The site owner is not a developer. Explain things in plain language, avoid jargon, and give click-by-click steps whenever they have to do something themselves (GitHub settings, DNS, Cloudflare). Ask before anything that's hard to undo.

## Publishing

"Publish" / "make it live" means: commit on your working branch, push, open a pull request into `main`, and merge it. The site updates about 1–2 minutes after the merge. The owner has approved this flow for content updates, so you don't need to ask again each time unless the change is risky or unclear. Tell them it's live and what to check.

Never commit secrets or tokens.

## Files

- `index.html` — homepage. **Generated; don't hand-edit it.** Self-contained (~5 MB, images inlined as base64).
- `legal.html` — legal / privacy / cookies page. Hand-edited directly (no build step).
- `404.html` — custom not-found page. Hand-edited directly.
- `CNAME` — custom domain (`www.relevant.es`). Don't remove.
- `_source/` — not published (Jekyll skips `_` folders):
  - `relevant-prototype.html` — **the homepage source; make homepage edits here.** Uses `{{TOKEN}}` placeholders for images.
  - `relevant-research/img/**/*.dataurl.txt` — images as data URIs, one per token. Mapping is `TOKEN_TO_FILE` in `build_final.py`.
  - `build_final.py` → writes `_source/relevant-final.html` (gitignored).
  - `wrap_for_github.py` → wraps that into the full document and writes `../index.html`. Also injects the Cloudflare Web Analytics snippet.
  - `HANDOFF_BRIEF.md` — original handoff notes.

### Rebuilding the homepage

After editing `_source/relevant-prototype.html`:

```
python3 _source/build_final.py
python3 _source/wrap_for_github.py
rm _source/relevant-final.html
```

Commit both the prototype and the regenerated `index.html`.

### Adding or replacing an image

Encode it as a data URI (`data:image/jpeg;base64,...`) in a new `.dataurl.txt` under `_source/relevant-research/img/`, add a token to `TOKEN_TO_FILE` in `build_final.py`, reference `{{TOKEN}}` in the prototype, rebuild. Keep images compressed (aim for under ~300 KB each); the page is already large.

## Three languages: EN / ES / CA

Every visible text change must be made in all three languages.

- **Homepage:** translatable elements carry `data-i18n="section.key"` (e.g. `nav.what`). All three languages' strings live in the JS dictionary in the prototype: the `en: {`, `es: {` and `ca: {` blocks, nested by section (e.g. `nav:{what:"..."}`). Update the matching entry in all three blocks; also update the English fallback text in the HTML element itself. New text needs a new `data-i18n` key plus entries in all three blocks.
- **legal.html:** contains three full copies of the content (EN, then ES, then CA). Edit all three.

If the owner gives text in only one language, translate it, and show them the translations so they can check.

## Analytics and cookies

- Cloudflare Web Analytics (cookieless) is on every page, just before `</body>`. Any new page needs the same snippet; copy it from `404.html`. The homepage gets it from `wrap_for_github.py`.
- Because it's cookieless, the site needs no cookie banner. A GA4 integration with a consent banner is built into the homepage but deliberately off (`var GA4_ID = "";`). Leave it off unless asked.
- The "Cookies" section of `legal.html` describes the Cloudflare analytics in all three languages. Keep it accurate. If you add anything that sets cookies or loads third-party content (embedded video, maps, social widgets, Google Fonts), flag it to the owner first: it may need the consent banner and a legal-page update.

## Before you publish

- Rebuild if you touched the prototype, and check `git diff --stat` only shows what you meant to change.
- Check every `{{TOKEN}}` was substituted (`build_final.py` reports any that weren't).
- Check the text change is in EN, ES and CA.
