import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'relevant-final.html')
OUT = os.path.join(HERE, '..', 'index.html')

with open(SRC, 'r', encoding='utf-8') as f:
    content = f.read()

# Split off the leading <title>...</title> and <style>...</style> blocks (these
# belong in <head>); everything after that is body content.
title_match = re.match(r'\s*<title>.*?</title>\s*', content, re.DOTALL)
assert title_match, "couldn't find leading <title> tag"
title_block = title_match.group(0).strip()
rest = content[title_match.end():]

style_match = re.match(r'\s*<style>.*?</style>\s*', rest, re.DOTALL)
assert style_match, "couldn't find leading <style> tag"
style_block = style_match.group(0).strip()
body_content = rest[style_match.end():]

doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Relevant — creating content for culture. We advise, curate and produce exhibitions, content and programmes for leading cultural institutions across Europe.">
{title_block}
<link rel="preload" href="assets/fonts/hanken-grotesk-600-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/hanken-grotesk-400-latin.woff2" as="font" type="font/woff2" crossorigin>
{style_block}
</head>
<body>
{body_content.rstrip()}
<!-- Cloudflare Web Analytics --><script type='module' src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{{"token": "64f36d742d664a7c9ab14d21df5825d3"}}'></script><!-- End Cloudflare Web Analytics -->
</body>
</html>
"""

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(doc)

print(f"Wrote {OUT}: {len(doc):,} bytes")
