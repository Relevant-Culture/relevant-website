import os

BASE = os.path.dirname(os.path.abspath(__file__))
# Images are published as separate files under assets/img/ at the site root.
# Each {{TOKEN}} in the prototype becomes a relative URL to its file.
IMG_DIR = os.path.join(BASE, '..', 'assets', 'img')
IMG_URL = 'assets/img/'

TOKEN_TO_FILE = {
    'IMG_HERO': 'hero.webp',
    'IMG_OCEAN': 'becomingOcean.webp',
    'IMG_AI': 'aiExpo.webp',
    'IMG_SOLITUDE': 'solitude.webp',
    'IMG_DHUB': 'dhub.jpg',
    'IMG_EATACTIMPACT': 'eatActImpact.webp',
    'IMG_BRAINS': 'brains.webp',
    'IMG_MARS': 'mars.webp',
    'IMG_QUANTUM': 'quantum.webp',
    'IMG_TECHFORGOOD': 'techForGood.webp',
    'IMG_CONNECTEDBEINGS': 'connectedBeings.webp',
    'IMG_BIGBANGDATA': 'bigBangData.jpg',
    'IMG_GAMEPLAY': 'gamePlay.webp',
    'IMG_RESIDENCIA': 'residencia.jpg',
    'IMG_TECLASALA': 'teclaSala.webp',
    'IMG_CANREON': 'canReon.jpg',
    'IMG_LLETRESCATALANES': 'lletresCatalanes.jpg',
    'IMG_DEMA': 'dema.jpg',
    'IMG_CULTUREINDATA': 'cultureInData.webp',
    'LIAISON_CCCB': 'liaison/cccb.webp',
    'LIAISON_SOMERSET': 'liaison/somerset.webp',
    'LIAISON_BARBICAN': 'liaison/barbican.webp',
    'LIAISON_HKW': 'liaison/hkw.webp',
    'LIAISON_VILLAARSON': 'liaison/villaArson.jpg',
    'LIAISON_DHUB': 'liaison/dhub.webp',
    'LIAISON_WAAG': 'liaison/waag.webp',
    'LIAISON_RESIDENCIA': 'liaison/residencia.webp',
    'LIAISON_MOBILEWORLD': 'liaison/mobileWorld.webp',
    'LIAISON_COSMOCAIXA': 'liaison/cosmocaixa.webp',
    'LIAISON_CERVANTES': 'liaison/cervantes.webp',
    'LIAISON_BSC': 'liaison/bsc.jpg',
    'IMG_LOGO': 'logo_relevant.webp',
}

with open(os.path.join(BASE, 'relevant-prototype.html'), encoding='utf-8') as f:
    html = f.read()

missing = []
for token, fname in TOKEN_TO_FILE.items():
    path = os.path.join(IMG_DIR, fname)
    placeholder = '{{' + token + '}}'
    count_before = html.count(placeholder)
    if count_before == 0:
        missing.append((token, 'placeholder not found in html'))
        continue
    if not os.path.exists(path):
        missing.append((token, 'file missing: ' + path))
        continue
    html = html.replace(placeholder, IMG_URL + fname)
    print(f'{token}: replaced {count_before} occurrence(s) -> {IMG_URL}{fname}')

if missing:
    print('MISSING/ERRORS:', missing)
else:
    print('All tokens substituted cleanly.')

remaining = [t for t in TOKEN_TO_FILE if '{{'+t+'}}' in html]
print('Remaining unsubstituted tokens:', remaining)

with open(os.path.join(BASE, 'relevant-final.html'), 'w', encoding='utf-8') as f:
    f.write(html)

print('Final file size:', len(html), 'bytes')
