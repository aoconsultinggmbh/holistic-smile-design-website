# -*- coding: utf-8 -*-
"""
Baut eine einzelne Vorschau-Datei, die alle Seiten enthält:
Startseite, fünf Leistungsseiten, drei Rechtsseiten. Bilder, Schriften, CSS und JS
sind eingebettet, Seitenwechsel laufen über die Adresszeile (#teleskoparbeiten usw.).
Nur für die Vorschau, nicht für den Livegang.

Aufruf im Projektordner:  python3 werkzeug/alles-in-einer-datei.py  [Zieldatei]
"""
import re, os, sys, base64, mimetypes

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
ZIEL = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, '..', 'vorschau-komplett.html')

SEITEN = [  # (datei, kurzname)
    ('teleskoparbeiten-norderstedt.html', 'teleskoparbeiten'),
    ('all-on-4-all-on-6-norderstedt.html', 'all-on-4'),
    ('implantatschablonen-stackable-guides-norderstedt.html', 'implantatschablonen'),
    ('vollkeramik-norderstedt.html', 'vollkeramik'),
    ('digitaler-workflow-dentallabor-norderstedt.html', 'digitaler-workflow'),
    ('impressum.html', 'impressum'),
    ('datenschutz.html', 'datenschutz'),
    ('barrierefreiheit.html', 'barrierefreiheit'),
]
DATEI2SLUG = {d: s for d, s in SEITEN}
DATEI2SLUG['index.html'] = 'start'

def b64(p):
    mt = mimetypes.guess_type(p)[0] or 'application/octet-stream'
    if p.endswith('.woff2'): mt = 'font/woff2'
    if p.endswith('.svg'): mt = 'image/svg+xml'
    return 'data:' + mt + ';base64,' + base64.b64encode(open(p, 'rb').read()).decode()

def main_von(html):
    a = html.index('<main id="inhalt">') + len('<main id="inhalt">')
    b = html.index('</main>')
    return html[a:b]

def links_umschreiben(h, slug):
    """Dateilinks zu Hash-Links; interne Anker der Unterseite bekommen ein Suffix."""
    def link(m):
        datei, frag = m.group(1), m.group(2)
        ziel = DATEI2SLUG.get(datei)
        if ziel is None:
            return m.group(0)
        if frag:
            return 'href="#' + (frag if ziel == 'start' else frag + '-' + ziel) + '"'
        return 'href="#' + ziel + '"'
    h = re.sub(r'href="([a-z0-9\-]+\.html)(?:#([\w\-]+))?"', link, h)
    if slug != 'start':
        h = re.sub(r'\bid="([\w\-]+)"', lambda m: f'id="{m.group(1)}-{slug}"', h)
        h = re.sub(r'\bhref="#([\w\-]+)"', lambda m: m.group(0) if m.group(1) in DATEI2SLUG.values() or re.search(r'-(%s)$' % '|'.join(DATEI2SLUG.values()), m.group(1)) else f'href="#{m.group(1)}-{slug}"', h)
        h = re.sub(r'\b(aria-labelledby|aria-controls|for)="([\w\-]+)"', lambda m: f'{m.group(1)}="{m.group(2)}-{slug}"', h)
    return h

index = open('index.html', encoding='utf-8').read()

# Kopfbereich aus index.html, alles einbetten
kopf = index[:index.index('<body>') + 6]
kopf = re.sub(r'<link rel="preload"[^>]+>\n', '', kopf)
css = open('assets/stil.css', encoding='utf-8').read().replace('url(../fonts/', 'url(fonts/')
css = re.sub(r'url\((fonts/[^)]+)\)', lambda m: 'url(' + b64(m.group(1)) + ')', css)
kopf = kopf.replace('<link rel="stylesheet" href="assets/stil.css?v=1">', '<style>' + css + '</style>')
for a in ['einwilligung', 'barrierefreiheit']:
    kopf = kopf.replace(f'<link rel="stylesheet" href="assets/{a}.css?v=1">', '<style>' + open(f'assets/{a}.css', encoding='utf-8').read() + '</style>')
kopf = re.sub(r'href="(img/[^"]+)"', lambda m: 'href="' + b64(m.group(1)) + '"', kopf)
kopf = kopf.replace('<title>', '<title>VORSCHAU ALLE SEITEN | ')
kopf += """
<style>
.seite{display:none}.seite[data-aktiv="true"]{display:block}
.vorschau-hinweis{position:fixed;left:50%;transform:translateX(-50%);bottom:.8rem;z-index:800;background:#fff3b0;color:#5a4b00;font-size:.8rem;padding:.4rem .7rem;border-radius:8px;box-shadow:0 6px 18px rgba(0,0,0,.25)}
</style>
"""

# Kopfzeile und Fußzeile einmal
header = index[index.index('<header class="kopf">'):index.index('</header>') + 9]
i = index.index('\n<footer>\n')
footer = index[i + 1:index.index('</footer>', i) + 9]
header = links_umschreiben(header, 'start')
footer = links_umschreiben(footer, 'start')

# Seiten
teile = ['<div class="seite" id="seite-start" data-aktiv="true">' + links_umschreiben(main_von(index), 'start') + '</div>']
for datei, slug in SEITEN:
    h = open(datei, encoding='utf-8').read()
    teile.append(f'<div class="seite" id="{slug}">' + links_umschreiben(main_von(h), slug) + '</div>')
body = '\n'.join(teile)

# Bilder einbetten (nur WebP, JPG-Fallback entfernen)
body = re.sub(r'<source srcset="(img/[^"]+\.webp)" type="image/webp">\s*<img src="img/[^"]+\.jpg"', lambda m: '<img src="' + b64(m.group(1)) + '"', body)
body = body.replace('loading="lazy"', '')  # versteckte Seiten sollen beim Umschalten sofort Bilder zeigen

# Skripte
js = open('assets/skript.js', encoding='utf-8').read()
js = js.replace("var form=document.getElementById('formular');\n  if(form){", "document.querySelectorAll('form.formular').forEach(function(form){")
js = js.replace("var f=inp.closest('.feld');if(f)f.setAttribute('data-fehler','false');});});\n  }\n})();", "var f=inp.closest('.feld');if(f)f.setAttribute('data-fehler','false');});});\n  });\n})();")
assert "forEach(function(form){" in js and "  });\n})();" in js
router = """
<script>
/* Seitenwechsel über die Adresszeile, nur für diese Vorschau-Datei */
(function(){
  var seiten=document.querySelectorAll('.seite');
  function zeige(hash){
    var id=(hash||'#start').slice(1)||'start';
    var el=document.getElementById(id);
    var seite=el?el.closest('.seite'):null;
    if(!seite){seite=document.getElementById('seite-start');el=null;}
    seiten.forEach(function(s){s.setAttribute('data-aktiv',s===seite?'true':'false');});
    if(el&&el!==seite){el.scrollIntoView({behavior:'auto',block:'start'});}else{window.scrollTo(0,0);}
    var h1=seite.querySelector('h1');if(h1){document.title=h1.textContent.trim()+' | Vorschau';}
  }
  window.addEventListener('hashchange',function(){zeige(location.hash);});
  zeige(location.hash);
})();
</script>"""
skripte = ''
for a in ['einwilligung', 'barrierefreiheit']:
    skripte += '<script>' + open(f'assets/{a}.js', encoding='utf-8').read().replace('</script>', '<\\/script>') + '</script>\n'
skripte += '<script>' + js + '</script>\n' + router

hinweis = '<div class="vorschau-hinweis" aria-hidden="true">Vorschau: alle Seiten in einer Datei</div>'
seite = kopf + '\n<a class="sprung" href="#inhalt">Zum Inhalt springen</a>\n' + header + '\n<main id="inhalt">\n' + body + '\n</main>\n' + footer + '\n' + hinweis + '\n' + skripte + '\n</body>\n</html>\n'
# Restliche Bilder (Logo in Kopf und Fuß) einbetten
seite = re.sub(r'<source srcset="(img/[^"]+\.webp)" type="image/webp">\s*<img src="img/[^"]+\.(?:jpg|png)"', lambda m: '<img src="' + b64(m.group(1)) + '"', seite)
seite = re.sub(r'src="(img/[^"]+)"', lambda m: 'src="' + b64(m.group(1)) + '"', seite)
open(ZIEL, 'w', encoding='utf-8').write(seite)
print('geschrieben', ZIEL, len(seite) // 1024, 'KB')
