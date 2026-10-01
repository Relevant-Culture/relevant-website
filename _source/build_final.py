import os

BASE = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE, 'relevant-research/img')

TOKEN_TO_FILE = {
    'IMG_HERO': 'hero.dataurl.txt',
    'IMG_OCEAN': 'becomingOcean.dataurl.txt',
    'IMG_AI': 'aiExpo.dataurl.txt',
    'IMG_SOLITUDE': 'solitude.dataurl.txt',
    'IMG_DHUB': 'dhub.dataurl.txt',
    'IMG_EATACTIMPACT': 'eatActImpact.dataurl.txt',
    'IMG_BRAINS': 'brains.dataurl.txt',
    'IMG_MARS': 'mars.dataurl.txt',
    'IMG_QUANTUM': 'quantum.dataurl.txt',
    'IMG_TECHFORGOOD': 'techForGood.dataurl.txt',
    'IMG_CONNECTEDBEINGS': 'connectedBeings.dataurl.txt',
    'IMG_BIGBANGDATA': 'bigBangData.dataurl.txt',
    'IMG_GAMEPLAY': 'gamePlay.dataurl.txt',
    'IMG_RESIDENCIA': 'residencia.dataurl.txt',
    'IMG_TECLASALA': 'teclaSala.dataurl.txt',
    'IMG_CANREON': 'canReon.dataurl.txt',
    'IMG_LLETRESCATALANES': 'lletresCatalanes.dataurl.txt',
    'IMG_DEMA': 'dema.dataurl.txt',
    'IMG_CULTUREINDATA': 'cultureInData.dataurl.txt',
    'LIAISON_CCCB': 'liaison/cccb.dataurl.txt',
    'LIAISON_SOMERSET': 'liaison/somerset.dataurl.txt',
    'LIAISON_BARBICAN': 'liaison/barbican.dataurl.txt',
    'LIAISON_HKW': 'liaison/hkw.dataurl.txt',
    'LIAISON_VILLAARSON': 'liaison/villaArson.dataurl.txt',
    'LIAISON_DHUB': 'liaison/dhub.dataurl.txt',
    'LIAISON_WAAG': 'liaison/waag.dataurl.txt',
    'LIAISON_RESIDENCIA': 'liaison/residencia.dataurl.txt',
    'LIAISON_MOBILEWORLD': 'liaison/mobileWorld.dataurl.txt',
    'LIAISON_COSMOCAIXA': 'liaison/cosmocaixa.dataurl.txt',
    'LIAISON_CERVANTES': 'liaison/cervantes.dataurl.txt',
    'LIAISON_BSC': 'liaison/bsc.dataurl.txt',
    'IMG_LOGO': 'logo_relevant.dataurl.txt',
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
    with open(path, encoding='utf-8') as imgf:
        dataurl = imgf.read().strip()
    if not dataurl.startswith('data:image/'):
        missing.append((token, 'bad dataurl prefix in ' + path))
        continue
    html = html.replace(placeholder, dataurl)
    print(f'{token}: replaced {count_before} occurrence(s), {len(dataurl)} chars')

if missing:
    print('MISSING/ERRORS:', missing)
else:
    print('All tokens substituted cleanly.')

remaining = [t for t in TOKEN_TO_FILE if '{{'+t+'}}' in html]
print('Remaining unsubstituted tokens:', remaining)

with open(os.path.join(BASE, 'relevant-final.html'), 'w', encoding='utf-8') as f:
    f.write(html)

print('Final file size:', len(html), 'bytes')
