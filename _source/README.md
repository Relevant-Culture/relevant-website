# Site source

`_source/` is ignored by GitHub Pages (Jekyll skips folders starting with `_`), so nothing here is published.

To rebuild the homepage after editing `relevant-prototype.html`:

```
python3 _source/build_final.py      # writes _source/relevant-final.html
python3 _source/wrap_for_github.py  # writes ../index.html
```

Then commit `index.html`. See `HANDOFF_BRIEF.md` for architecture notes (i18n, GA4 setup).
