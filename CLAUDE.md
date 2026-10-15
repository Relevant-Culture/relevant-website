# Relevant website

Static site for Relevant (relevant.es), served by GitHub Pages from the `main` branch, root folder, at **https://www.relevant.es** (custom domain via the `CNAME` file; DNS at iwantmyname).

## Who you're working with

The site owner is not a developer. Explain things in plain language, avoid jargon, and give click-by-click steps whenever they have to do something themselves (GitHub settings, DNS, Cloudflare). Ask before anything that's hard to undo.

## Publishing

"Publish" / "make it live" means: commit on your working branch, push, open a pull request into `main`, and merge it. The site updates about 1–2 minutes after the merge. The owner has approved this flow for content updates, so you don't need to ask again each time unless the change is risky or unclear. Tell them it's live and what to check.

Never commit secrets or tokens.

## Files

- `index.html` — homepage. **Edit it directly.** Images are separate files in `img/` (WebP), referenced as `img/<name>.webp`.
- `img/` — homepage images. Keep new ones compressed WebP (aim for under ~300 KB each).
- `legal.html` — legal / privacy / cookies page. Hand-edited directly.
- `404.html` — custom not-found page. Hand-edited directly.
- `CNAME` — custom domain (`www.relevant.es`). Don't remove.
- `_source/` — **outdated; don't use it to rebuild.** It's the original build pipeline from before the images moved to `img/` (prototype with `{{TOKEN}}` placeholders, base64 images, `build_final.py`, `wrap_for_github.py`). Running it would overwrite `index.html` and undo the `img/` change. Kept for reference only; Jekyll doesn't publish `_` folders.

### Email address

The contact address (info@relevant.es) is deliberately **not** written in the page source, to keep it away from spam harvesters. A small script after the Contact section assembles it in the browser and fills in every link with class `js-mail` (and the visible text of `js-mail-text`). Don't add plain `mailto:` links or plain-text email addresses anywhere on the site; reuse the `js-mail` classes instead.

## Three languages: EN / ES / CA

Every visible text change must be made in all three languages.

- **Homepage:** translatable elements carry `data-i18n="section.key"` (e.g. `nav.what`). All three languages' strings live in the JS dictionary near the end of `index.html`: the `en: {`, `es: {` and `ca: {` blocks, nested by section (e.g. `nav:{what:"..."}`). Update the matching entry in all three blocks; also update the English fallback text in the HTML element itself. New text needs a new `data-i18n` key plus entries in all three blocks.
- **legal.html:** contains three full copies of the content (EN, then ES, then CA). Edit all three.

If the owner gives text in only one language, translate it, and show them the translations so they can check.

## Analytics and cookies

- Cloudflare Web Analytics (cookieless) is on every page, just before `</body>`. Any new page needs the same snippet; copy it from `404.html`.
- Because it's cookieless, the site needs no cookie banner. A GA4 integration with a consent banner is built into the homepage but deliberately off (`var GA4_ID = "";`). Leave it off unless asked.
- The "Cookies" section of `legal.html` describes the Cloudflare analytics in all three languages. Keep it accurate. If you add anything that sets cookies or loads third-party content (embedded video, maps, social widgets, Google Fonts), flag it to the owner first: it may need the consent banner and a legal-page update.

## Before you publish

- Check `git diff --stat` only shows what you meant to change.
- Open the changed pages in the headless browser and check them at desktop and phone widths.
- Check the text change is in EN, ES and CA.
