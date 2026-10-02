> **Update (Oct 2026):** images and fonts are no longer inlined. Images live in `/assets/img/`, fonts in `/assets/fonts/`, and `build_final.py` substitutes file paths. See `CLAUDE.md` at the repo root; the base64 notes below are historical.

# Relevant website — handoff brief for a new Claude Code Cloud task

This package exists because the chat-session cloud sandbox this work was done in cannot
`git push` to GitHub — see "Why this handoff exists" below. Everything needed to pick up
publishing with zero terminal typing by Marcos is in this folder.

## What to do first, in the new task

1. Start a **Claude Code Cloud** session at claude.ai/code (not a regular chat/Cowork
   session) and, at creation time, attach/select the repo **`Relevant-Culture/relevant-website`**.
   This is the step that could not be done retroactively from inside a chat session — Claude
   Code Cloud sessions bind to a chosen repo at creation, which grants git push access for the
   whole session.
2. Upload this handoff folder's contents (or just tell Claude to read them if they're attached
   to the new task/conversation).
3. Have Claude clone the repo, copy `index.html`, `legal.html`, and `404.html` from this
   package into the repo root, commit, and push to `main`. GitHub Pages is already configured
   (Settings → Pages → Deploy from branch → `main` → `/ (root)`), so the push alone makes the
   site live at the org's GitHub Pages URL (custom domain not yet configured, if one is wanted).

## Current repo state (as of this handoff)

- Repo: `https://github.com/Relevant-Culture/relevant-website` (GitHub Organization: `Relevant-Culture`)
- `main` branch currently has only two throwaway test commits (`a900c2e` "test push from device",
  `d315517` "Remove test file") — **no real site content is live yet.**
- A local commit with the real content ("Publish trilingual Relevant site (EN/ES/CA)",
  message includes `index.html`) exists in a clone made during this session, but it was never
  successfully pushed — that's the whole reason this handoff exists.
- GitHub Pages is enabled and configured (branch: `main`, folder: `/root`).

## Files in this package

- **`index.html`** — the finished, ready-to-publish homepage (trilingual EN/ES/CA, single
  self-contained file with images inlined as base64 data URIs). This is the current
  build output — push it as-is unless new edits are needed.
- **`legal.html`** — finished legal/privacy page, ready to publish as-is.
- **`404.html`** — finished custom 404 page, ready to publish as-is.
- **`relevant-prototype.html`** — the *source* template for `index.html`. It's the real
  content/structure file to edit for future copy or layout changes. It contains `{{TOKEN}}`
  placeholders (e.g. `{{IMG_HERO}}`, `{{LIAISON_CCCB}}`) instead of inline images.
- **`build_final.py`** — run this after editing `relevant-prototype.html` to substitute every
  `{{TOKEN}}` placeholder with the matching base64 data URI from
  `relevant-research/img/**/*.dataurl.txt`, producing `relevant-final.html`.
- **`wrap_for_github.py`** — run this after `build_final.py`. It takes `relevant-final.html`,
  wraps it in a full `<!doctype html>` document with `<head>` boilerplate (meta charset,
  viewport, description), and writes `index.html`.
- **`relevant-research/img/`** — every image referenced by `relevant-prototype.html`, pre-encoded
  as base64 data URIs in `.dataurl.txt` files (one file per token). Includes a `liaison/`
  subfolder for the partner/liaison logos. **Do not delete or rename these** — `build_final.py`
  maps tokens to these exact filenames (see the `TOKEN_TO_FILE` dict at the top of the script).

To rebuild `index.html` from a source edit: edit `relevant-prototype.html` → run
`python3 build_final.py` (writes `relevant-final.html`) → run `python3 wrap_for_github.py`
(reads `relevant-final.html`, writes `index.html`) → commit + push `index.html`.

Not included in this package (lower priority, ask if needed): `build_legal.py`, the script
that generates `legal.html` from scratch — it depends on a large third-party webfont package
(`fonts_work/`) that wasn't worth including here. Since `legal.html` is already a finished
static file, just edit it directly with normal HTML edits unless a full regeneration is
truly needed.

## Site architecture notes

- **Trilingual i18n**: EN/ES/CA. Text elements carry `data-i18n="section.key"` attributes;
  a language toggle (`#langToggle` + `button[data-lang="es|ca"]`) swaps the active language
  client-side. All three languages' strings live inside the same HTML file.
- **Single-file, self-contained**: no external image files — every image is a base64
  `data:` URI embedded directly in the HTML. This keeps deployment to "one file, one push"
  but makes the file large (~4.9 MB) and means future edits should go through the
  prototype+build pipeline above, not by hand-editing the giant built `index.html`.
  (A worthwhile future improvement: switch to separate image files instead of inline
  base64, which would make small future edits far cheaper to make/transfer.)
- **Analytics (GA4)**: already fully wired, intentionally left inactive. In the source,
  search for `GA4_ID` — currently `var GA4_ID = "";` (blank on purpose). Analytics is
  gated behind a cookie-consent banner: `getCookieConsent()` / `setCookieConsent()` read/write
  `localStorage` key `relevant_cookie_consent`; `loadGA4()` injects the gtag.js script and
  only fires after the user consents. **To turn analytics on**: get a GA4 Measurement ID
  (starts with `G-`) from Google Analytics and paste it into `GA4_ID`. No other code changes
  needed.

## Why this handoff exists (context on the git-push limitation)

This work was done in a regular Claude chat/Cowork session (cloud sandbox), not a Claude
Code Cloud session. That sandbox enforces a per-session "authorized repository set" — any
`git push` or GitHub API write to a repo not explicitly authorized at session creation
returns a 403 with "access denied by the git proxy: ... not in this session's authorized
repository set." This is a known, currently-unresolved platform limitation (confirmed via
two real public GitHub issues on `anthropics/claude-code`: #96075 and #96609), **not** a
credentials problem — it was independently re-confirmed three times in this session: with a
valid fine-grained PAT alone, with the PAT plus the official "Claude GitHub App"
(github.com/apps/claude) installed on the repo, and on a final clean retest. All three
attempts produced the identical 403.

The only known workaround is starting a **Claude Code Cloud** session (claude.ai/code) with
the target repo attached/selected at creation time — that's a session-creation-time choice
that can't be granted retroactively to an already-running chat session. That's exactly what
this handoff package is for.

## Credentials

A fine-grained GitHub Personal Access Token scoped to `Relevant-Culture/relevant-website`
(Contents: Read and write) was created and tested successfully (a real test commit was
pushed and cleaned up) during this session. **It has been shared in plaintext multiple times
across this conversation and should be treated as compromised — revoke it in GitHub
(Settings → Developer settings → Personal access tokens → Fine-grained tokens) and generate
a fresh one for the new Claude Code Cloud task**, or simply rely on that task's own
repo-attachment authorization instead of a manual PAT.
