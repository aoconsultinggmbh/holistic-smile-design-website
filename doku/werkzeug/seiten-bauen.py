# -*- coding: utf-8 -*-
"""
Baut die Unterseiten von holistic-smile-design.de aus index.html heraus:
Kopf, Fußzeile und Einwilligungs-Konfiguration werden aus index.html übernommen,
damit alle Seiten identisch bleiben. Jede Handkorrektur an Unterseiten gehört
in dieses Skript, sonst überschreibt der nächste Lauf sie.

Aufruf von überall:  python3 doku/werkzeug/seiten-bauen.py
Das Skript liegt in doku/werkzeug/, die Seite in website/. Es schreibt immer nach website/.
"""
import re, os, json, html

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'website')
os.chdir(ROOT)
src = open('index.html', encoding='utf-8').read()

def absolut(s):
    return re.sub(r'href="#(\w+)"', r'href="index.html#\1"', s)

konf = src[src.index('<script>\nwindow.AO_EINWILLIGUNG'):src.index('</script>', src.index('window.AO_EINWILLIGUNG')) + 9]
header = absolut(src[src.index('<header class="kopf">'):src.index('</header>') + 9])
i = src.index('\n<footer>\n')
footer = absolut(src[i + 1:src.index('</footer>', i) + 9])

DOMAIN = 'https://holistic-smile-design.de/'
ph = lambda t: f'<span class="ph">[PLATZHALTER: {t}]</span>'

# ---------------------------------------------------------------------------
# Leistungen
# ---------------------------------------------------------------------------
LEISTUNGEN = [
  dict(
    datei='backward-planning-norderstedt.html',
    kurz='Backward Planning',
    title='Backward Planning Norderstedt | Komplexe Sanierung digital geplant',
    desc='Komplexe Sanierungen mit Backward Planning vom Meisterlabor in Norderstedt: Fotoshooting, Gesichtsscan und KI-gestützte Visualisierung mit Smilecloud, damit Praxis und Patient das Ergebnis vor der Behandlung sehen.',
    kicker='Leistung 01, Kernkompetenz',
    ablauf_h2='So läuft eine komplexe Sanierung mit Backward Planning bei Holistic Smile Design',
    h1='Backward Planning aus Norderstedt: Komplexe Sanierungen vom Ergebnis her geplant',
    intro='Die Kernkompetenz von Holistic Smile Design ist die komplexe Sanierung mit Backward Planning. Zuerst wird das angestrebte Ergebnis festgelegt, dann wird von dort aus rückwärts jeder Behandlungsschritt geplant. Fotoshooting, Gesichtsscanner und KI-gestützte Werkzeuge wie Smilecloud zeigen dem Patienten schon vor der Behandlung, wie sein Lächeln aussehen könnte. Ein Bild sagt mehr als tausend Worte.',
    hero='fotodokumentation-zahnfarbe-dentallabor-norderstedt',
    hero_alt='Fotodokumentation im Fotostudio des Dentallabors Holistic Smile Design in Norderstedt als Grundlage für das Backward Planning',
    fuer_h2='Was Zahnarztpraxen vom Backward Planning bei Holistic Smile Design haben',
    fuer=[
      ('Das Ergebnis zuerst', 'Ästhetik, Funktion und Bisslage werden am Anfang gemeinsam festgelegt. Jeder weitere Schritt leitet sich aus diesem Ziel ab.'),
      ('Visualisierung für den Patienten', 'Aus Fotoshooting und Gesichtsscan entsteht mit KI-gestützten Werkzeugen wie Smilecloud eine Vorschau auf das geplante Lächeln, noch vor der ersten Präparation.'),
      ('Ein Plan für alle Beteiligten', 'Praxis, Chirurgie und Labor arbeiten mit demselben Datensatz. Provisorium, Schablonen und definitive Versorgung passen zueinander.'),
      ('Sichere Entscheidungen', 'Patienten sehen, wofür sie sich entscheiden. Das erleichtert die Beratung in der Praxis und die Zustimmung zu umfangreichen Sanierungen.'),
    ],
    ablauf=[
      ('Fotoshooting und Gesichtsscan', 'Der Patient kommt für standardisierte Aufnahmen und einen Gesichtsscan ins Labor nach Norderstedt oder die Praxis liefert Fotos, Intraoralscan und DVT.'),
      ('Digitale Vorschau', 'Holistic Smile Design erstellt mit KI-gestützten Werkzeugen wie Smilecloud eine Visualisierung des angestrebten Ergebnisses und stimmt sie mit Praxis und Patient ab.'),
      ('Rückwärts geplant', 'Aus dem freigegebenen Ergebnis werden Wax-up, Mock-up, Präparationshilfen, Provisorium und bei Bedarf Implantatschablonen abgeleitet.'),
      ('Umsetzung Schritt für Schritt', 'Die Sanierung folgt dem Plan. Jede Zwischenstufe wird mit der Vorschau abgeglichen, bis die definitive Versorgung eingegliedert ist.'),
    ],
    technik_h2='Fotostudio, Gesichtsscanner und KI-Werkzeuge im eigenen Haus',
    technik=('Backward Planning funktioniert nur mit guten Daten. Holistic Smile Design arbeitet deshalb mit einem eigenen Fotostudio für standardisierte Aufnahmen, einem Gesichtsscanner und KI-gestützten Planungswerkzeugen wie Smilecloud. Fotos, Scan und DVT werden zu einem Datensatz zusammengeführt, aus dem Vorschau, Provisorium und definitive Versorgung entstehen.', 'Frank Köpp ist Zahntechnikermeister und Master of Science (M.Sc.) in Digitaler Dentaltechnologie. Die komplexe Sanierung mit Backward Planning ist die Kernkompetenz seines Labors.'),
    technik_bild='cad-planung-implantatprothetik-bildschirm-norderstedt',
    technik_alt='Digitale Planung einer Versorgung am Bildschirm im Dentallabor Norderstedt',
    bild2='zahnfarbe-bestimmen-vita-farbring-dentallabor-norderstedt',
    bild2_alt='Zahnfarbbestimmung mit Farbring als Teil der Planung im Labor',
    faq=[
      ('Welches Dentallabor bei Hamburg plant komplexe Sanierungen mit Backward Planning?', 'Holistic Smile Design in der Oststraße 120, 22844 Norderstedt, hat die komplexe Sanierung mit Backward Planning als Kernkompetenz. Das Labor arbeitet mit Zahnarztpraxen in Norderstedt, Hamburg und ganz Deutschland zusammen und ist montags bis donnerstags von 8 bis 18 Uhr und freitags von 8 bis 15 Uhr unter 040 94369370 erreichbar.'),
      ('Was ist Backward Planning in der Zahntechnik?', 'Backward Planning bedeutet, eine Versorgung vom gewünschten Endergebnis her zu planen. Zuerst werden Ästhetik, Funktion und Bisslage festgelegt, dann wird rückwärts abgeleitet, welche Schritte, Provisorien und Hilfsmittel nötig sind. So passen alle Zwischenschritte zum Ziel, statt dass das Ergebnis am Ende dem Zufall überlassen bleibt.'),
      ('Wie sieht der Patient das Ergebnis vor der Behandlung?', 'Holistic Smile Design fertigt aus Fotoshooting und Gesichtsscan mit KI-gestützten Werkzeugen wie Smilecloud eine Visualisierung des geplanten Lächelns. Der Patient sieht auf einem Bild, wie das Ergebnis aussehen könnte, bevor der erste Zahn beschliffen wird.'),
      ('Muss der Patient dafür ins Labor kommen?', 'Für Fotoshooting und Gesichtsscan kann der Patient ins Labor nach Norderstedt kommen. Alternativ übermittelt die Praxis Fotos, Intraoralscan und DVT digital. Welcher Weg im Einzelfall sinnvoll ist, klärt Holistic Smile Design vorab mit der Praxis.'),
    ],
  ),
  dict(
    datei='teleskoparbeiten-norderstedt.html',
    kurz='Teleskoparbeiten',
    title='Teleskoparbeiten Norderstedt | Teleskopprothesen für Zahnarztpraxen',
    desc='Teleskoparbeiten vom Meisterlabor in Norderstedt: Primärteile digital konstruiert und gefräst, Sekundärstrukturen präzise angepasst. Für Zahnarztpraxen in Hamburg und ganz Deutschland.',
    kicker='Leistung 02',
    h1='Teleskoparbeiten aus Norderstedt: Präzision für herausnehmbaren Zahnersatz',
    intro='Teleskopprothesen sind der Schwerpunkt von Holistic Smile Design. Das Labor konstruiert Primärteile digital, fräst sie im eigenen Haus und passt die Sekundärstrukturen so an, dass die Arbeit spannungsfrei sitzt und angenehm hält. Zahnarztpraxen in Norderstedt, Hamburg und ganz Deutschland erhalten Teleskoparbeiten aus einer Hand, von der Planung bis zur Eingliederungsbegleitung.',
    hero='teleskopgeruest-zahntechniker-dentallabor-norderstedt',
    hero_alt='Zahntechniker hält ein gefrästes Teleskopgerüst im Dentallabor Holistic Smile Design in Norderstedt',
    fuer_h2='Wofür Zahnarztpraxen Teleskoparbeiten bei Holistic Smile Design anfragen',
    fuer=[
      ('Teilbezahnte Kiefer', 'Herausnehmbare Versorgung auf natürlichen Pfeilerzähnen, wenn eine festsitzende Brücke nicht in Frage kommt.'),
      ('Kombination mit Implantaten', 'Teleskope auf Implantaten und Zähnen in einer Arbeit, geplant im digitalen Datensatz.'),
      ('Erweiterbare Versorgungen', 'Konstruktionen, die bei späterem Zahnverlust erweitert werden können, ohne die Prothese neu zu fertigen.'),
      ('Hoher Tragekomfort', 'Gaumenfreie Gestaltung im Oberkiefer, wo die Pfeilersituation es zulässt.'),
    ],
    ablauf=[
      ('Präparation und Daten', 'Sie präparieren die Pfeilerzähne und übermitteln Intraoralscan oder Abformung, dazu Bissregistrat und Auftrag.'),
      ('Primärteile digital', 'Holistic Smile Design konstruiert die Primärkronen am Bildschirm, mit definierter Friktionsfläche und gemeinsamer Einschubrichtung, und fräst sie im Haus.'),
      ('Sekundärstruktur und Gerüst', 'Die Sekundärteile werden auf die Primärkronen aufgepasst, das Gerüst verbunden und die Aufstellung zur Einprobe vorbereitet.'),
      ('Fertigstellung', 'Nach Ihrer Einprobe erfolgen Fertigstellung, Politur und Endkontrolle. Bei Fragen zur Eingliederung ist das Labor direkt erreichbar.'),
    ],
    technik_h2='Digital gefräst, von Hand aufgepasst',
    technik=('Primärkronen entstehen bei Holistic Smile Design im CAD/CAM-Verfahren. Das sorgt für parallele Friktionsflächen, reproduzierbare Wandstärken und eine Einschubrichtung, die exakt der Planung entspricht. Die Sekundärteile werden anschließend von Hand aufgepasst, denn hier entscheidet das Gefühl des Zahntechnikers über Halt und Tragekomfort.', 'Frank Köpp ist Zahntechnikermeister und Master of Science (M.Sc.) in Digitaler Dentaltechnologie, abgeschlossen an der Universität Greifswald. Teleskoparbeiten sind bei Holistic Smile Design der Schwerpunkt des Labors.'),
    technik_bild='teleskoparbeit-handarbeit-zahntechniker-norderstedt',
    technik_alt='Zahntechniker prüft eine Teleskoparbeit unter der Lupe',
    bild2='artikulator-implantatmodell-dentallabor-norderstedt',
    bild2_alt='Zahntechnikermeister kontrolliert ein Modell im Artikulator im Labor in Norderstedt',
    faq=[
      ('Welches Dentallabor in Norderstedt fertigt Teleskoparbeiten für Zahnärzte?', 'Holistic Smile Design in der Oststraße 120, 22844 Norderstedt, ist ein Meisterlabor mit Schwerpunkt Teleskoparbeiten. Das Labor beliefert Zahnarztpraxen in Norderstedt, Hamburg und ganz Deutschland. Erreichbar montags bis donnerstags von 8 bis 18 Uhr und freitags von 8 bis 15 Uhr unter 040 94369370.'),
      ('Was ist eine Teleskopprothese?', 'Eine Teleskopprothese ist herausnehmbarer Zahnersatz, der über Doppelkronen auf den Pfeilerzähnen hält. Die Primärkrone sitzt fest auf dem Zahn, die Sekundärkrone in der Prothese gleitet darüber und erzeugt durch Friktion den Halt. Klammern sind nicht sichtbar, die Prothese lässt sich zur Reinigung herausnehmen.'),
      ('Werden die Primärkronen bei Holistic Smile Design gefräst oder gegossen?', 'Holistic Smile Design konstruiert Primärkronen digital und fräst sie im eigenen Haus. Das Ergebnis sind parallele Friktionsflächen und eine Einschubrichtung, die exakt der Planung entspricht.'),
      ('Kann eine Teleskopprothese später erweitert werden?', 'Ja. Teleskopprothesen lassen sich bei späterem Zahnverlust in der Regel erweitern, wenn die Konstruktion darauf ausgelegt ist. Holistic Smile Design plant Erweiterbarkeit auf Wunsch von Anfang an mit ein.'),
    ],
  ),
  dict(
    datei='all-on-4-all-on-6-norderstedt.html',
    kurz='All-on-4 und All-on-6',
    title='All-on-4 und All-on-6 Norderstedt | Implantatprothetik für Zahnärzte',
    desc='Implantatprothetik nach dem All-on-4- und All-on-6-Konzept vom Dentallabor in Norderstedt: digitale Planung, Provisorium und definitive Versorgung für Zahnarztpraxen in Hamburg und ganz Deutschland.',
    kicker='Leistung 03',
    h1='All-on-4 und All-on-6 aus Norderstedt: Festsitzende Versorgung des zahnlosen Kiefers',
    intro='Holistic Smile Design plant und fertigt festsitzende Versorgungen auf vier oder sechs Implantaten. Von der Implantatplanung über die Schablone und das Provisorium bis zur definitiven Brücke kommt alles aus einem digitalen Datensatz. Zahnarztpraxen in Norderstedt und Hamburg arbeiten damit mit einem Ansprechpartner für die gesamte Versorgung.',
    hero='cad-planung-implantatprothetik-bildschirm-norderstedt',
    hero_alt='Planung einer All-on-4-Versorgung am Bildschirm im Dentallabor Norderstedt',
    fuer_h2='Was Zahnarztpraxen von Holistic Smile Design bei All-on-4 und All-on-6 bekommen',
    fuer=[
      ('Digitale Implantatplanung', 'DVT und Intraoralscan werden zu einem Datensatz zusammengeführt, Implantatpositionen und Prothetik werden gemeinsam geplant.'),
      ('Schablone und Provisorium', 'Bohrschablone oder Stackable Guide und das Sofortprovisorium entstehen aus derselben Planung, damit sie zueinander passen.'),
      ('Definitive Brücke', 'Nach der Einheilphase fertigt das Labor die definitive Versorgung, abgestimmt auf die Situation im Mund.'),
      ('Ein Ansprechpartner', 'Chirurgie, Prothetik und Labor sprechen über denselben Datensatz. Rückfragen laufen direkt über das Labor in Norderstedt.'),
    ],
    ablauf=[
      ('Daten und Planung', 'Sie übermitteln DVT, Intraoralscan und Fotos. Holistic Smile Design plant Implantatpositionen und Prothetik im gemeinsamen Datensatz und stimmt die Planung mit Ihnen ab.'),
      ('Schablone und Provisorium', 'Aus der Planung entstehen die Bohrschablone oder Stackable Guide und das Provisorium für die Sofortversorgung.'),
      ('Operation und Sofortversorgung', 'Am Tag der Implantation wird das Provisorium eingegliedert, auf Wunsch mit Unterstützung des Labors bei der Anpassung.'),
      ('Definitive Versorgung', 'Nach der Einheilphase folgen Abformung oder Scan auf Implantatniveau, Gerüst, Einprobe und die Fertigstellung der definitiven Brücke.'),
    ],
    technik_h2='Planung, Schablone und Prothetik aus einem Datensatz',
    technik=('Bei All-on-4 und All-on-6 entscheidet die Planung über das Ergebnis. Holistic Smile Design führt DVT, Intraoralscan und Fotodokumentation in der CAD-Software zusammen und plant Implantatpositionen von der Prothetik her. So liegen Schraubenkanäle dort, wo sie ästhetisch und funktionell sinnvoll sind.', 'Schablonen und Provisorien werden im eigenen 3D-Drucker gefertigt, Gerüste und definitive Versorgungen auf der CAD/CAM-Fräsmaschine im Haus. Die Individualisierung übernimmt das Team von Hand.'),
    technik_bild='implantatversorgung-artikulator-kontrolle-norderstedt',
    technik_alt='Kontrolle einer Implantatversorgung im Artikulator',
    bild2='3d-drucker-implantatschablonen-dentallabor-norderstedt',
    bild2_alt='3D-Drucker für Schablonen und Provisorien im Dentallabor Norderstedt',
    faq=[
      ('Welches Dentallabor in der Nähe von Hamburg fertigt All-on-4-Versorgungen?', 'Holistic Smile Design in Norderstedt, Oststraße 120, plant und fertigt All-on-4- und All-on-6-Versorgungen für Zahnarztpraxen in Hamburg, Norderstedt und ganz Deutschland. Das Labor ist montags bis donnerstags von 8 bis 18 Uhr und freitags von 8 bis 15 Uhr unter 040 94369370 erreichbar.'),
      ('Was bedeutet All-on-4?', 'All-on-4 ist ein Behandlungskonzept, bei dem ein zahnloser Kiefer mit einer festsitzenden Brücke auf vier Implantaten versorgt wird. Die hinteren Implantate werden dabei angewinkelt gesetzt, um Knochen zu nutzen und Knochenaufbau zu vermeiden. All-on-6 arbeitet nach demselben Prinzip mit sechs Implantaten.'),
      ('Fertigt Holistic Smile Design auch das Sofortprovisorium?', 'Ja. Das Provisorium entsteht bei Holistic Smile Design aus derselben digitalen Planung wie die Schablone und kann am Tag der Implantation eingegliedert werden.'),
      ('Unterstützt das Labor bei der Planung?', 'Holistic Smile Design plant Implantatpositionen gemeinsam mit der Praxis von der Prothetik her und stimmt die Planung vor der Fertigung ab. Inhaber Frank Köpp ist Zahntechnikermeister und Master of Science (M.Sc.) in Digitaler Dentaltechnologie.'),
    ],
  ),
  dict(
    datei='implantatschablonen-stackable-guides-norderstedt.html',
    kurz='Implantatschablonen',
    title='Implantatschablonen und Stackable Guides Norderstedt | Guided Surgery',
    desc='Bohrschablonen und Stackable Guides aus dem 3D-Drucker vom Dentallabor in Norderstedt. Digitale Implantatplanung auf Basis von DVT und Intraoralscan für Zahnarztpraxen in Hamburg und ganz Deutschland.',
    kicker='Leistung 04',
    h1='Implantatschablonen und Stackable Guides aus Norderstedt',
    intro='Holistic Smile Design fertigt Bohrschablonen für die geführte Implantation und mehrteilige Stackable Guides für die Versorgung des zahnlosen Kiefers. Grundlage ist die digitale Planung aus DVT und Intraoralscan, gedruckt wird im eigenen 3D-Drucker in Norderstedt.',
    hero='implantatschablone-3d-druck-nachbearbeitung-norderstedt',
    hero_alt='Nachbearbeitung einer 3D-gedruckten Implantatschablone im Dentallabor Norderstedt',
    fuer_h2='Schablonen für jede Implantatsituation',
    fuer=[
      ('Bohrschablonen', 'Zahn-, schleimhaut- oder knochengetragene Schablonen für Einzelimplantate bis zur Vollversorgung, mit Hülsen für Ihr Implantatsystem.'),
      ('Stackable Guides', 'Mehrteiliges, stapelbares System: Basisschablone, Knochenreduktions-, Bohr- und Prothetikschablone für All-on-4 und All-on-6 in einer Sitzung.'),
      ('Planung von der Prothetik her', 'Implantatpositionen werden aus der geplanten Versorgung abgeleitet, damit Schraubenkanäle und Ästhetik zusammenpassen.'),
      ('Kurze Wege', 'Planung, Druck und Nachbearbeitung im eigenen Haus. Rückfragen zur Planung gehen direkt an das Labor.'),
    ],
    ablauf=[
      ('Datensatz', 'Sie übermitteln DVT, Intraoralscan oder Modellscan und den Auftrag mit Implantatsystem und gewünschter Versorgung.'),
      ('Planung', 'Holistic Smile Design überlagert die Daten, plant Implantatpositionen von der Prothetik her und stimmt die Planung mit Ihnen ab.'),
      ('Druck und Nachbearbeitung', 'Die Schablone wird im 3D-Drucker gefertigt, gereinigt, nachgehärtet, mit Hülsen versehen und auf dem Modell kontrolliert.'),
      ('Lieferung', 'Schablone und Planungsprotokoll gehen an die Praxis. Bei Stackable Guides kommt das Provisorium aus derselben Planung dazu.'),
    ],
    technik_h2='Was eine Stackable Guide leistet',
    technik=('Eine Stackable Guide ist ein stapelbares Schablonensystem für den zahnlosen Kiefer. Eine fest verankerte Basisschablone bleibt während der gesamten Operation im Mund. Darauf werden nacheinander die Knochenreduktionsschablone, die Bohrschablone und die Prothetikschablone aufgesteckt.', 'So lassen sich Knochenreduktion, Implantation und die Eingliederung des Provisoriums in einer Sitzung exakt nach der digitalen Planung umsetzen. Holistic Smile Design fertigt alle Teile aus demselben Datensatz.'),
    technik_bild='3d-gedrucktes-kiefermodell-dentallabor-norderstedt',
    technik_alt='3D-gedrucktes Kiefermodell auf dem Arbeitstisch im Dentallabor',
    bild2='3d-drucker-implantatschablonen-dentallabor-norderstedt',
    bild2_alt='3D-Drucker für Implantatschablonen im Dentallabor Norderstedt',
    faq=[
      ('Wo bekommen Zahnärzte in Hamburg und Norderstedt Implantatschablonen?', 'Holistic Smile Design in Norderstedt, Oststraße 120, fertigt Bohrschablonen und Stackable Guides im eigenen 3D-Drucker für Zahnarztpraxen in Hamburg, Norderstedt und ganz Deutschland. Erreichbar montags bis donnerstags von 8 bis 18 Uhr und freitags von 8 bis 15 Uhr unter 040 94369370.'),
      ('Was ist der Unterschied zwischen einer Bohrschablone und einer Stackable Guide?', 'Eine Bohrschablone führt die Bohrung für einzelne oder mehrere Implantate. Eine Stackable Guide ist ein mehrteiliges System für den zahnlosen Kiefer, bei dem Knochenreduktion, Bohrung und Provisorium über eine gemeinsame Basisschablone geführt werden.'),
      ('Welche Daten braucht Holistic Smile Design für eine Implantatschablone?', 'Ein DVT des Kiefers, einen Intraoralscan oder Modellscan der aktuellen Situation sowie den Auftrag mit Implantatsystem und geplanter Versorgung. Bei Bedarf zusätzlich Fotos und ein Scan der vorhandenen Prothese.'),
      ('Für welche Implantatsysteme werden Schablonen gefertigt?', 'Holistic Smile Design fertigt Schablonen für die gängigen Implantatsysteme mit den passenden Führungshülsen. ' + 'Welche Systeme im Einzelfall möglich sind, klärt das Labor vor der Planung mit der Praxis.'),
    ],
  ),
  dict(
    datei='vollkeramik-norderstedt.html',
    kurz='Vollkeramik',
    title='Vollkeramik Norderstedt | Kronen, Brücken und Veneers für Zahnärzte',
    desc='Vollkeramische Kronen, Brücken und Veneers vom Meisterlabor in Norderstedt: digital konstruiert, im Haus gefräst, von Hand individualisiert. Für Zahnarztpraxen in Hamburg und ganz Deutschland.',
    kicker='Leistung 05',
    h1='Vollkeramik aus Norderstedt: Kronen, Brücken und Veneers, die nicht auffallen',
    intro='Holistic Smile Design fertigt vollkeramischen Zahnersatz aus Zirkonoxid und Glaskeramik. Die Konstruktion erfolgt digital, gefräst wird im eigenen Haus, die Individualisierung übernimmt das Team von Hand. Für Zahnarztpraxen in Norderstedt und Hamburg, die metallfreien Zahnersatz mit natürlicher Wirkung erwarten.',
    hero='vollkeramik-individualisierung-pinsel-dentallabor-norderstedt',
    hero_alt='Zahntechnikerin individualisiert eine vollkeramische Arbeit mit dem Pinsel im Dentallabor Norderstedt',
    fuer_h2='Vollkeramische Versorgungen bei Holistic Smile Design',
    fuer=[
      ('Kronen und Brücken', 'Monolithisch oder verblendet aus Zirkonoxid, digital konstruiert und im Haus gefräst.'),
      ('Veneers und Teilkronen', 'Minimalinvasive Versorgungen aus Glaskeramik für den sichtbaren Bereich.'),
      ('Implantatkronen', 'Vollkeramische Versorgungen auf Implantaten, abgestimmt auf die Planung aus dem Labor.'),
      ('Zahnfarbe im Labor', 'Farbnahme mit Farbring und Fotodokumentation, auf Wunsch direkt im Labor in Norderstedt.'),
    ],
    ablauf=[
      ('Präparation und Scan', 'Sie präparieren und übermitteln Intraoralscan oder Abformung, dazu Zahnfarbe und Fotos. Für die Farbnahme können Patienten auch ins Labor kommen.'),
      ('Digitale Konstruktion', 'Holistic Smile Design konstruiert die Versorgung am Bildschirm, mit Blick auf Kontaktpunkte, Okklusion und Mindestwandstärken.'),
      ('Fräsen und Sintern', 'Die Arbeit wird im Haus gefräst und gesintert. Bei Verblendungen folgt der Schichtaufbau von Hand.'),
      ('Individualisierung und Kontrolle', 'Charakterisierung, Glanzbrand und Endkontrolle auf dem Modell. Danach geht die Arbeit in Ihre Praxis.'),
    ],
    technik_h2='Warum Holistic Smile Design Vollkeramik ausbaut',
    technik=('Vollkeramik ist metallfrei, lichtdurchlässig und biokompatibel. Für Zahnärzte heißt das: ästhetische Ergebnisse auch im sichtbaren Bereich und keine dunklen Ränder am Zahnfleisch. Holistic Smile Design baut diesen Bereich gezielt aus und verbindet die Präzision der CAD/CAM-Fertigung mit der Handarbeit bei der Individualisierung.', 'Die Farbnahme erfolgt mit Farbring und standardisierter Fotodokumentation. Auf Wunsch kommen Patienten dafür direkt ins Labor nach Norderstedt.'),
    technik_bild='zahnfarbe-bestimmen-vita-farbring-dentallabor-norderstedt',
    technik_alt='Zahntechnikerin mit Farbring zur Bestimmung der Zahnfarbe',
    bild2='cad-cam-fraesen-zahnersatz-dentallabor-norderstedt',
    bild2_alt='CAD/CAM-Fräsmaschine bei der Bearbeitung eines Rohlings',
    faq=[
      ('Welches Dentallabor in Norderstedt fertigt vollkeramische Arbeiten?', 'Holistic Smile Design in der Oststraße 120, 22844 Norderstedt, fertigt vollkeramische Kronen, Brücken und Veneers für Zahnarztpraxen in Norderstedt, Hamburg und ganz Deutschland. Das Labor ist montags bis donnerstags von 8 bis 18 Uhr und freitags von 8 bis 15 Uhr unter 040 94369370 erreichbar.'),
      ('Was ist der Unterschied zwischen Zirkonoxid und Glaskeramik?', 'Zirkonoxid ist eine hochfeste Oxidkeramik und eignet sich für Kronen, Brücken und Implantatversorgungen auch im Seitenzahnbereich. Glaskeramik ist lichtdurchlässiger und wird vor allem für Veneers, Teilkronen und Einzelkronen im sichtbaren Bereich eingesetzt.'),
      ('Kann die Zahnfarbe im Labor bestimmt werden?', 'Ja. Holistic Smile Design bestimmt die Zahnfarbe auf Wunsch direkt im Labor in Norderstedt, mit Farbring und Fotodokumentation. So sieht der Zahntechniker die Situation selbst und kann die Individualisierung darauf abstimmen.'),
      ('Wird die Vollkeramik im Labor selbst gefräst?', 'Ja. Holistic Smile Design konstruiert vollkeramische Arbeiten digital und fräst sie auf der eigenen CAD/CAM-Maschine in Norderstedt. Sintern, Verblendung und Individualisierung erfolgen ebenfalls im Haus.'),
    ],
  ),
  dict(
    datei='digitaler-workflow-dentallabor-norderstedt.html',
    kurz='Digitaler Workflow',
    title='Digitales Dentallabor Norderstedt | Intraoralscan, CAD/CAM und 3D-Druck',
    desc='Holistic Smile Design arbeitet zu 98 Prozent digital: Intraoralscan, DVT, CAD-Planung, CAD/CAM-Fräsen und 3D-Druck im eigenen Haus. Digitales Dentallabor für Zahnarztpraxen in Norderstedt und Hamburg.',
    kicker='Leistung 06',
    h1='Digitales Dentallabor in Norderstedt: Vom Intraoralscan bis zur fertigen Arbeit',
    intro='Holistic Smile Design ist zu 98 Prozent digital aufgestellt. Scandaten, DVT und Fotodokumentation laufen in einer durchgängigen CAD-Planung zusammen, gefertigt wird auf der eigenen Fräsmaschine und im 3D-Drucker. Für Zahnarztpraxen bedeutet das reproduzierbare Passung, kurze Abstimmungswege und nachvollziehbare Daten zu jeder Arbeit.',
    hero='zahntechnikermeister-cad-arbeitsplatz-norderstedt',
    hero_alt='Zahntechnikermeister Frank Köpp am CAD-Arbeitsplatz im digitalen Dentallabor Norderstedt',
    fuer_h2='So arbeitet Holistic Smile Design mit digitalen Praxen zusammen',
    fuer=[
      ('Intraoralscan statt Abformung', 'Scandaten der gängigen Intraoralscanner werden direkt übernommen. Welche Schnittstelle Ihre Praxis nutzt, klärt das Labor vor der ersten Arbeit.'),
      ('DVT und Fotos im Datensatz', 'Für Implantatplanung und Ästhetik werden DVT und Fotodokumentation mit dem Scan überlagert.'),
      ('Fertigung im Haus', 'CAD/CAM-Fräsmaschine, 3D-Drucker und Sinterofen stehen im Labor in Norderstedt. Kein Versand an Fertigungszentren.'),
      ('Nachvollziehbare Daten', 'Zu jeder Arbeit liegt der Planungsdatensatz vor. Nacharbeiten, Erweiterungen und Ersatz lassen sich daraus ableiten.'),
    ],
    ablauf=[
      ('Datenübermittlung', 'Sie senden Intraoralscan, DVT und Auftrag digital an das Labor. Konventionelle Abformungen werden im Labor gescannt.'),
      ('CAD-Planung', 'Holistic Smile Design konstruiert die Versorgung am Bildschirm und stimmt Planung und Details bei Bedarf mit Ihnen ab.'),
      ('Fertigung', 'Gerüste, Kronen und Primärteile werden gefräst, Modelle, Schablonen und Provisorien gedruckt.'),
      ('Handarbeit und Kontrolle', 'Individualisierung, Politur und Endkontrolle übernimmt das Team von Hand, bevor die Arbeit in Ihre Praxis geht.'),
    ],
    technik_h2='Meister und Master of Science: Digitale Dentaltechnologie mit Handwerk',
    technik=('Inhaber Frank Köpp ist Zahntechnikermeister und Master of Science (M.Sc.). Den Masterstudiengang Digitale Dentaltechnologie hat er berufsbegleitend an der Universität Greifswald abgeschlossen. Dieses Wissen prägt den Workflow des Labors: digital, wo es Präzision und Reproduzierbarkeit bringt, handwerklich, wo das Ergebnis davon profitiert.', 'Die Fotodokumentation im eigenen Fotostudio ergänzt den Datensatz um Farbe und Ästhetik. So entstehen Arbeiten, die nicht nur passen, sondern auch natürlich wirken.'),
    technik_bild='fotodokumentation-zahnfarbe-dentallabor-norderstedt',
    technik_alt='Fotodokumentation einer zahntechnischen Arbeit im Fotostudio des Labors',
    bild2='intraoralscanner-digitaler-workflow-dentallabor-norderstedt',
    bild2_alt='Digitaler Arbeitsplatz mit Scanner im Dentallabor Norderstedt',
    faq=[
      ('Welches digitale Dentallabor gibt es in Norderstedt bei Hamburg?', 'Holistic Smile Design in der Oststraße 120, 22844 Norderstedt, ist ein zu 98 Prozent digital aufgestelltes Meisterlabor mit CAD/CAM-Fräsmaschine und 3D-Druckern im eigenen Haus. Es beliefert Zahnarztpraxen in Norderstedt, Hamburg und ganz Deutschland. Erreichbar montags bis donnerstags von 8 bis 18 Uhr und freitags von 8 bis 15 Uhr unter 040 94369370.'),
      ('Welche Intraoralscanner kann das Labor verarbeiten?', 'Holistic Smile Design übernimmt Scandaten der gängigen Intraoralscanner. Welche Schnittstelle oder welches Datenformat Ihre Praxis nutzt, klärt das Labor vor der ersten Zusammenarbeit.'),
      ('Was passiert mit konventionellen Abformungen?', 'Abformungen werden per Post oder Kurier ins Labor geschickt, dort gescannt und in den digitalen Workflow übernommen. Praxen ohne Intraoralscanner können so mit Holistic Smile Design zusammenarbeiten.'),
      ('Was bedeutet ein zu 98 Prozent digitaler Workflow?', 'Bei Holistic Smile Design werden Planung, Konstruktion und Fertigung fast vollständig am Rechner und mit CAD/CAM-Maschinen und 3D-Druckern umgesetzt. Manuelle Schritte bleiben dort, wo sie das Ergebnis verbessern, etwa bei der Individualisierung von Keramik und der Endkontrolle.'),
    ],
  ),
]

# ---------------------------------------------------------------------------
# Bausteine
# ---------------------------------------------------------------------------
def kopf(title, desc, canonical, robots='index,follow', extra=''):
    return f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{DOMAIN}{canonical}">
<meta name="robots" content="{robots}">
<meta property="og:type" content="website">
<meta property="og:locale" content="de_DE">
<meta property="og:site_name" content="Holistic Smile Design">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{DOMAIN}{canonical}">
<meta name="theme-color" content="#242424">
<link rel="icon" href="img/favicon.svg?v=2" type="image/svg+xml">
<link rel="icon" href="img/favicon-32.png?v=2" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="img/apple-touch-icon.png?v=2">
<link rel="preload" href="fonts/jost-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="fonts/jost-latin-300-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/einwilligung.css?v=1">
<link rel="stylesheet" href="assets/barrierefreiheit.css?v=1">
<link rel="stylesheet" href="assets/stil.css?v=3">
{konf}
{extra}
</head>
<body>
<a class="sprung" href="#inhalt">Zum Inhalt springen</a>
<a class="sprung" href="#kontakt">Zum Kontakt springen</a>
{header}
<main id="inhalt">
"""

FUSS = f"""</main>
{footer}
<script src="assets/einwilligung.js?v=1" defer></script>
<script src="assets/barrierefreiheit.js?v=1" defer></script>
<script src="assets/skript.js?v=1" defer></script>
</body>
</html>
"""

def bild(name, alt, w=1800, h=1200, lazy=True):
    l = 'loading="lazy" decoding="async"' if lazy else 'fetchpriority="high" decoding="async"'
    return f'''<picture>
  <source srcset="img/{name}.webp" type="image/webp">
  <img src="img/{name}.jpg" alt="{html.escape(alt)}" width="{w}" height="{h}" {l}>
</picture>'''

def brot(titel):
    return f'<nav class="brot" aria-label="Brotkrumen"><ol><li><a href="index.html">Startseite</a></li><li><a href="index.html#leistungen">Leistungen</a></li><li aria-current="page">{html.escape(titel)}</li></ol></nav>'

def leistungsnav(aktiv):
    teile = []
    for l in LEISTUNGEN:
        cur = ' aria-current="page"' if l['datei'] == aktiv else ''
        teile.append(f'<li><a href="{l["datei"]}"{cur}>{html.escape(l["kurz"])}</a></li>')
    li = ''.join(teile)
    return f'<nav class="lnav" aria-label="Weitere Leistungen"><ul>{li}</ul></nav>'

def formular():
    a = src.index('<form class="formular"'); b = src.index('</form>', a) + 7
    return src[a:b]

def json_ld(l):
    faq = [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in l['faq']]
    data = {"@context": "https://schema.org", "@graph": [
        {"@type": "Service", "@id": DOMAIN + l['datei'] + '#service', "name": l['kurz'],
         "serviceType": l['kurz'], "description": l['desc'],
         "provider": {"@id": DOMAIN + "#labor"},
         "areaServed": [{"@type": "Country", "name": "Deutschland"}, {"@type": "City", "name": "Norderstedt"}, {"@type": "City", "name": "Hamburg"}],
         "url": DOMAIN + l['datei']},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Startseite", "item": DOMAIN},
            {"@type": "ListItem", "position": 2, "name": "Leistungen", "item": DOMAIN + "#leistungen"},
            {"@type": "ListItem", "position": 3, "name": l['kurz'], "item": DOMAIN + l['datei']}]},
        {"@type": "FAQPage", "mainEntity": faq}]}
    return '<script type="application/ld+json">\n' + json.dumps(data, ensure_ascii=False, indent=1) + '\n</script>'

# ---------------------------------------------------------------------------
# Leistungsseiten
# ---------------------------------------------------------------------------
for l in LEISTUNGEN:
    fuer = ''.join(f'<li><h3>{html.escape(t)}</h3><p>{html.escape(p)}</p></li>' for t, p in l['fuer'])
    ablauf = ''.join(f'<li class="schritt"><h3>{html.escape(t)}</h3><p>{html.escape(p)}</p></li>' for t, p in l['ablauf'])
    faq = ''.join(f'<details><summary><h3 class="faq__q">{html.escape(q)}</h3></summary><p>{html.escape(a)}</p></details>' for q, a in l['faq'])
    body = f"""
<section class="uhero" aria-labelledby="h1">
  <div class="container uhero-innen">
    <div>
      {brot(l['kurz'])}
      <span class="kicker">{html.escape(l['kicker'])}</span>
      <h1 id="h1">{html.escape(l['h1'])}</h1>
      <p class="lead">{html.escape(l['intro'])}</p>
      <div class="hero-cta">
        <a class="btn btn-gold" href="#kontakt">Anfrage stellen
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        <a class="btn btn-hell" href="tel:+494094369370">040 94369370</a>
      </div>
    </div>
    <div class="uhero-bild">{bild(l['hero'], l['hero_alt'], lazy=False)}</div>
  </div>
</section>

<section class="sektion" aria-labelledby="h-fuer">
  <div class="container">
    <div class="kopfzeile">
      <span class="kicker">Für Zahnarztpraxen</span>
      <h2 id="h-fuer">{html.escape(l['fuer_h2'])}</h2>
    </div>
    <ul class="punkte">{fuer}</ul>
  </div>
</section>

<section class="sektion creme" aria-labelledby="h-ablauf">
  <div class="container">
    <div class="kopfzeile">
      <span class="kicker">Ablauf</span>
      <h2 id="h-ablauf">{html.escape(l.get('ablauf_h2', 'So läuft eine ' + l['kurz'] + '-Versorgung mit Holistic Smile Design'))}</h2>
    </div>
    <ol class="schritte" style="list-style:none;padding:0;margin:0">{ablauf}</ol>
  </div>
</section>

<section class="sektion dunkel" aria-labelledby="h-technik">
  <div class="container utechnik">
    <div class="utechnik-bilder">
      {bild(l['technik_bild'], l['technik_alt'])}
      {bild(l['bild2'], l['bild2_alt'])}
    </div>
    <div>
      <span class="kicker">Qualität und Technik</span>
      <h2 id="h-technik">{html.escape(l['technik_h2'])}</h2>
      <p>{html.escape(l['technik'][0])}</p>
      <p>{html.escape(l['technik'][1])}</p>
      <a class="btn btn-gold" href="index.html#labor" style="margin-top:.6rem">Das Labor kennenlernen</a>
    </div>
  </div>
</section>

<section class="sektion creme" id="faq" aria-labelledby="h-faq">
  <div class="container">
    <div class="kopfzeile" style="margin-inline:auto;text-align:center">
      <span class="kicker">Fragen von Zahnärzten</span>
      <h2 id="h-faq">Häufige Fragen zu {html.escape(l['kurz'])}</h2>
    </div>
    <div class="faq">{faq}</div>
  </div>
</section>

<section class="sektion" aria-labelledby="h-weitere">
  <div class="container">
    <div class="kopfzeile">
      <span class="kicker">Weitere Leistungen</span>
      <h2 id="h-weitere">Was Holistic Smile Design außerdem fertigt</h2>
    </div>
    {leistungsnav(l['datei'])}
  </div>
</section>

<section class="sektion dunkel" id="kontakt" aria-labelledby="h-kontakt">
  <div class="container kontakt">
    <div class="kontakt-info">
      <span class="kicker">Kontakt</span>
      <h2 id="h-kontakt">{html.escape(l['kurz'])} <span class="script">anfragen</span></h2>
      <p>Sie möchten eine erste Arbeit in Auftrag geben oder das Labor kennenlernen? Schreiben Sie uns über das Formular oder rufen Sie an. Wir melden uns so schnell wie möglich.</p>
      <ul>
        <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/></svg><div><a href="tel:+494094369370">040 94369370</a><small>Mo–Do 08:00–18:00 Uhr, Fr 08:00–15:00 Uhr</small></div></li>
        <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg><div><a href="mailto:info@holistic-smile-design.de">info@holistic-smile-design.de</a><small>Für Anfragen und Auftragsdaten</small></div></li>
        <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M12 21s7-6.2 7-11.5A7 7 0 0 0 5 9.5C5 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></svg><div>Oststraße 120<br>22844 Norderstedt<small>Industriegebiet Norderstedt</small></div></li>
        <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg><div><a href="https://www.instagram.com/holistic_smile_design/" rel="noopener" target="_blank">@holistic_smile_design</a><small>Einblicke ins Labor auf Instagram</small></div></li>
      </ul>
    </div>
    {formular()}
  </div>
</section>
"""
    seite = kopf(l['title'], l['desc'], l['datei'], extra=json_ld(l)) + body + FUSS
    open(l['datei'], 'w', encoding='utf-8').write(seite)
    print('geschrieben', l['datei'])

# ---------------------------------------------------------------------------
# Rechtsseiten
# ---------------------------------------------------------------------------
hinweis = ''  # Entwurfskasten entfernt am 30.09.2026 auf Wunsch Ovi, alle Kundenangaben liegen vor

def rechtsseite(datei, titel, desc, inhalt):
    body = f"""
<div class="container rechts">
<nav class="brot" aria-label="Brotkrumen"><ol><li><a href="index.html">Startseite</a></li><li aria-current="page">{html.escape(titel)}</li></ol></nav>
{inhalt}
</div>
"""
    open(datei, 'w', encoding='utf-8').write(kopf(titel + ' | Holistic Smile Design, Dentallabor Norderstedt', desc, datei, robots='noindex,follow') + body + FUSS)
    print('geschrieben', datei)

rechtsseite('impressum.html', 'Impressum', 'Impressum der Holistic Smile Design GmbH, Dentallabor in Norderstedt.', f"""
<h1>Impressum</h1>
{hinweis}
<h2>Angaben gemäß § 5 DDG</h2>
<p>Holistic Smile Design GmbH<br>Oststraße 120<br>22844 Norderstedt</p>
<p>Vertreten durch den Geschäftsführer: Frank Köpp</p>
<h2>Kontakt</h2>
<p>Telefon: 040 94369370<br>E-Mail: info@holistic-smile-design.de</p>
<h2>Registereintrag</h2>
<p>Eintragung im Handelsregister<br>Registergericht: Amtsgericht Kiel<br>Registernummer: HRB 25615 KI</p>
<h2>Umsatzsteuer-ID</h2>
<p>Umsatzsteuer-Identifikationsnummer gemäß § 27a UStG: DE360767272</p>
<h2>Berufsbezeichnung und berufsrechtliche Regelungen</h2>
<p>Berufsbezeichnung: Zahntechnikermeister (verliehen in Deutschland)<br>Zuständige Handwerkskammer: Handwerkskammer Lübeck, Breite Straße 10–12, 23552 Lübeck, <a href="https://www.hwk-luebeck.de" rel="noopener">www.hwk-luebeck.de</a></p>
<p>Es gelten die Handwerksordnung (HwO) sowie das Medizinprodukterecht-Durchführungsgesetz (MPDG) und die Verordnung (EU) 2017/745 über Medizinprodukte. Zahnersatz wird als Sonderanfertigung im Sinne dieser Verordnung hergestellt.</p>
<h2>Streitschlichtung</h2>
<p>Die Europäische Kommission stellt eine Plattform zur Online-Streitbeilegung (OS) bereit: <a href="https://ec.europa.eu/consumers/odr/" rel="noopener">https://ec.europa.eu/consumers/odr/</a>. Holistic Smile Design ist nicht bereit und nicht verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.</p>
<h2>Bildnachweis</h2>
<p>Fotografie: AO Consulting GmbH</p>
<h2>Website</h2>
<p>Konzeption und Umsetzung: <a href="https://ao-consult.de" rel="noopener">AO Consulting GmbH</a></p>
""")

rechtsseite('datenschutz.html', 'Datenschutzerklärung', 'Datenschutzerklärung der Holistic Smile Design GmbH, Dentallabor in Norderstedt.', f"""
<h1>Datenschutzerklärung</h1>
{hinweis}
<h2>1. Verantwortlicher</h2>
<p>Holistic Smile Design GmbH, Oststraße 120, 22844 Norderstedt, Telefon 040 94369370, E-Mail info@holistic-smile-design.de. Vertreten durch den Geschäftsführer Frank Köpp.</p>
<p>Ein Datenschutzbeauftragter ist nicht bestellt.</p>
<h2>2. Hosting</h2>
<p>Diese Website wird bei der ALL-INKL.COM – Neue Medien Münnich, Inhaber René Münnich, Hauptstraße 68, 02742 Friedersdorf, auf Servern in Deutschland gehostet. Beim Aufruf der Website verarbeitet der Hoster in unserem Auftrag technisch notwendige Verbindungsdaten (IP-Adresse, Datum und Uhrzeit, aufgerufene Seite, Browsertyp, verweisende Seite) in Server-Logdateien. Rechtsgrundlage ist unser berechtigtes Interesse an einem sicheren und störungsfreien Betrieb der Website (Art. 6 Abs. 1 lit. f DSGVO). Die Logdateien werden nur so lange gespeichert, wie es für den sicheren Betrieb und die Abwehr von Angriffen erforderlich ist, und danach gelöscht. Mit dem Hoster besteht ein Vertrag zur Auftragsverarbeitung nach Art. 28 DSGVO.</p>
<h2>3. Schriften und Bilder</h2>
<p>Alle Schriften sind lokal auf unserem Server gespeichert. Beim Aufruf der Website wird keine Verbindung zu Google Fonts oder anderen Schriftanbietern aufgebaut.</p>
<h2>4. Einwilligung und lokaler Speicher</h2>
<p>Beim ersten Besuch fragen wir Sie, ob die Anfahrtskarte von Google Maps geladen werden darf. Ihre Entscheidung speichern wir im lokalen Speicher Ihres Browsers (localStorage) unter dem Schlüssel „ao-einwilligung-v1", ohne Cookie und ohne Kennung. Gespeichert werden nur die gewählten Kategorien und der Zeitpunkt. Die Speicherung ist erforderlich, um Ihre Entscheidung nachzuweisen und Sie nicht bei jedem Aufruf erneut zu fragen (§ 25 Abs. 2 Nr. 2 TDDDG). Die Entscheidung gilt 12 Monate. Über „Cookie-Einstellungen" in der Fußzeile können Sie sie jederzeit ändern oder widerrufen.</p>
<h2>5. Anfahrtskarte von Google Maps</h2>
<p>Die Anfahrtskarte wird erst geladen, wenn Sie im Einwilligungsfenster oder durch Klick auf „Karte laden" zugestimmt haben (Art. 6 Abs. 1 lit. a DSGVO, § 25 Abs. 1 TDDDG). Anbieter ist Google Ireland Limited, Gordon House, Barrow Street, Dublin 4, Irland. Beim Laden werden Ihre IP-Adresse und Browserdaten an Google übertragen, auch in die USA. Google ist nach dem EU-US Data Privacy Framework zertifiziert. Weitere Informationen: <a href="https://policies.google.com/privacy" rel="noopener">https://policies.google.com/privacy</a>.</p>
<h2>6. Kontaktformular, E-Mail und Telefon</h2>
<p>Wenn Sie uns über das Kontaktformular, per E-Mail oder telefonisch kontaktieren, verarbeiten wir die von Ihnen mitgeteilten Daten (Praxisname, Name, Telefonnummer, E-Mail-Adresse, Interessen, Nachricht) zur Bearbeitung Ihrer Anfrage. Rechtsgrundlage ist Art. 6 Abs. 1 lit. b DSGVO, soweit die Anfrage auf eine Zusammenarbeit zielt, sonst Art. 6 Abs. 1 lit. f DSGVO. Die Daten werden gelöscht, sobald die Anfrage abschließend bearbeitet ist und keine gesetzlichen Aufbewahrungspflichten entgegenstehen.</p>
<p>So läuft der Versand ab: Ihre Angaben werden verschlüsselt an unseren Webserver übertragen und von dort als E-Mail an uns weitergeleitet. Auf dem Server werden sie nicht gespeichert, es gibt keine Datenbank und keinen Formulardienst eines Drittanbieters. Zum Schutz vor automatisierten Nachrichten enthält das Formular ein für Sie unsichtbares Feld und prüft, wie viel Zeit zwischen Aufruf und Absenden vergangen ist. Dabei werden keine personenbezogenen Daten ausgewertet und keine Cookies gesetzt.</p>
<p>Bitte senden Sie uns über das Formular keine Patientendaten und keine Gesundheitsdaten. Für alles, was einen konkreten Fall betrifft, nutzen Sie bitte den üblichen Weg über Ihre Praxis-Software oder das Telefon.</p>
<h2>7. Links zu Google und Instagram</h2>
<p>Die Website verlinkt auf unser Unternehmensprofil bei Google und auf unser Profil bei Instagram (Meta Platforms Ireland Limited, Merrion Road, Dublin 4, Irland). Es handelt sich um einfache Links, nicht um Einbettungen: Beim Aufruf unserer Website werden keine Daten an Google oder Meta übertragen. Erst mit dem Klick auf einen Link verlassen Sie unsere Website, dann gelten die Datenschutzbestimmungen des jeweiligen Anbieters.</p>
<h2>8. Empfänger und Auftragsverarbeiter</h2>
<p>Hoster (siehe Ziffer 2), Google (nur nach Einwilligung, Ziffer 5, oder nach Klick auf einen Link, Ziffer 7), Meta (nur nach Klick auf den Instagram-Link, Ziffer 7). Eine Übermittlung an weitere Dritte findet nicht statt.</p>
<h2>9. Ihre Rechte</h2>
<p>Sie haben das Recht auf Auskunft (Art. 15 DSGVO), Berichtigung (Art. 16), Löschung (Art. 17), Einschränkung der Verarbeitung (Art. 18), Datenübertragbarkeit (Art. 20) und Widerspruch (Art. 21 DSGVO). Eine erteilte Einwilligung können Sie jederzeit mit Wirkung für die Zukunft widerrufen. Sie haben außerdem das Recht, sich bei einer Aufsichtsbehörde zu beschweren. Zuständig ist das Unabhängige Landeszentrum für Datenschutz Schleswig-Holstein (ULD), Holstenstraße 98, 24103 Kiel.</p>
<h2>10. Stand</h2>
<p>Diese Datenschutzerklärung hat den Stand 30. September 2026.</p>
""")

rechtsseite('barrierefreiheit.html', 'Erklärung zur Barrierefreiheit', 'Erklärung zur Barrierefreiheit der Website von Holistic Smile Design, Dentallabor in Norderstedt.', f"""
<h1>Erklärung zur Barrierefreiheit</h1>
{hinweis}
<p>Die Holistic Smile Design GmbH ist bemüht, ihre Website barrierefrei zugänglich zu machen. Diese Erklärung gilt für holistic-smile-design.de.</p>
<h2>Stand der Vereinbarkeit</h2>
<p>Die Website wurde nach den Anforderungen der EN 301 549 und der WCAG 2.1 auf Stufe AA gestaltet: semantische Struktur, Tastaturbedienung, sichtbare Fokusmarkierungen, ausreichende Kontraste, Alternativtexte für Bilder und ein Einstellungsfenster für Kontrast, Schriftgröße und Bewegung. Die Website wurde im September 2026 mit automatisierten Werkzeugen sowie manuell per Tastatur geprüft. Wesentliche Barrieren wurden dabei nicht festgestellt. Wir prüfen die Website nach jeder größeren Änderung erneut.</p>
<h2>Nicht barrierefreie Inhalte</h2>
<p>Die eingebettete Anfahrtskarte von Google Maps kann nicht vollständig barrierefrei bedient werden. Die Adresse steht daher zusätzlich als Text auf der Seite.</p>
<h2>Feedback und Kontakt</h2>
<p>Wenn Ihnen Barrieren auffallen, schreiben Sie an info@holistic-smile-design.de oder rufen Sie an unter 040 94369370. Wir antworten innerhalb von 14 Tagen.</p>
<h2>Geltungsbereich und Durchsetzungsverfahren</h2>
<p>Diese Website richtet sich an Zahnarztpraxen und damit an Geschäftskunden. Sie bietet keine Verbraucherverträge und keinen Online-Handel an. Nach unserer Einschätzung fällt sie deshalb nicht in den Anwendungsbereich des Barrierefreiheitsstärkungsgesetzes (BFSG). Diese Erklärung geben wir freiwillig ab. Ein förmliches Durchsetzungsverfahren vor einer Schlichtungsstelle ist dafür nicht vorgesehen. Wenden Sie sich bei Barrieren bitte direkt an uns, wir kümmern uns darum.</p>
<p>Diese Erklärung wurde am 30. September 2026 erstellt.</p>
""")

# ---------------------------------------------------------------------------
# Team-Seite
# Vornamen und Rollen kommen vom Kunden. Bis dahin stehen gelbe Platzhalter.
# Die Zuordnung Foto zu Person muss der Kunde bestätigen, auch bei Frank Köpp.
# ---------------------------------------------------------------------------
TEAM = [
  dict(bild='team-frank-koepp-zahntechnikermeister-dentallabor-norderstedt', name='Frank', rolle='Inhaber, Zahntechnikermeister, M.Sc.',
       text='Zahntechnikermeister und Master of Science in Digitaler Dentaltechnologie. Frank hat Holistic Smile Design 2023 gegründet und plant komplexe Sanierungen mit Backward Planning, von der ersten Visualisierung bis zur Eingliederung.',
       alt='Frank Köpp, Inhaber und Zahntechnikermeister von Holistic Smile Design in Norderstedt', inhaber=True),
  dict(bild='team-zahntechnikerin-3-dentallabor-norderstedt', name=None, rolle=None, alt='Mitarbeiterin von Holistic Smile Design im Dentallabor in Norderstedt'),
  dict(bild='team-zahntechniker-1-dentallabor-norderstedt', name=None, rolle=None, alt='Mitarbeiter von Holistic Smile Design im Dentallabor in Norderstedt'),
  dict(bild='team-zahntechnikerin-2-dentallabor-norderstedt', name=None, rolle=None, alt='Mitarbeiterin von Holistic Smile Design im Dentallabor in Norderstedt'),
  dict(bild='team-zahntechniker-4-dentallabor-norderstedt', name=None, rolle=None, alt='Mitarbeiter von Holistic Smile Design im Dentallabor in Norderstedt'),
]

def teamseite():
    karten = []
    for t in TEAM:
        name = html.escape(t['name']) if t['name'] else ph('Vorname')
        rolle = html.escape(t['rolle']) if t['rolle'] else ph('Rolle, z. B. Zahntechnikerin')
        text = f"<p>{html.escape(t['text'])}</p>" if t.get('text') else ''
        kl = ' person-inhaber' if t.get('inhaber') else ''
        karten.append(f'<li class="person{kl}">{bild(t["bild"], t["alt"], 1200, 1500)}<div class="person-text"><span class="rolle">{rolle}</span><h2>{name}</h2>{text}</div></li>')
    body = f"""
<section class="uhero" aria-labelledby="h1">
  <div class="container uhero-innen">
    <div>
      <nav class="brot" aria-label="Brotkrumen"><ol><li><a href="index.html">Startseite</a></li><li aria-current="page">Team</li></ol></nav>
      <span class="kicker">Das Team</span>
      <h1 id="h1">Das Team von Holistic Smile Design in Norderstedt</h1>
      <p class="lead">Ein Team, ein Anspruch: Zahnersatz, der passt und natürlich wirkt. Hier lernen Sie kennen, wer bei Holistic Smile Design plant, fräst, druckt und von Hand vollendet. Für jede Praxis gibt es einen festen Ansprechpartner.</p>
      <div class="hero-cta">
        <a class="btn btn-gold" href="#kontakt">Kennenlerntermin anfragen
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        <a class="btn btn-insta" href="https://www.instagram.com/holistic_smile_design/" rel="noopener" target="_blank"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg>Auf Instagram folgen</a>
      </div>
    </div>
    <div class="uhero-bild breit">{bild('team-holistic-smile-design-gruppenbild-dentallabor-norderstedt', 'Das Team von Holistic Smile Design im Dentallabor in Norderstedt', 1800, 1200, lazy=False)}</div>
  </div>
</section>

<section class="sektion dunkel" aria-labelledby="h-team">
  <div class="container">
    <div class="kopfzeile">
      <span class="kicker">Wer hier arbeitet</span>
      <h2 id="h-team">Meisterhand und <span class="script">Digital</span> in einem Team</h2>
      <p>Holistic Smile Design ist ein inhabergeführtes Meisterlabor. Alle Arbeiten entstehen im eigenen Haus in Norderstedt, geplant am Bildschirm und vollendet von Hand.</p>
    </div>
    <ul class="team-raster">{''.join(karten)}</ul>
  </div>
</section>

<section class="sektion creme" aria-labelledby="h-werte">
  <div class="container">
    <div class="kopfzeile">
      <span class="kicker">So arbeiten wir</span>
      <h2 id="h-werte">Was Praxen von der Zusammenarbeit mit dem Team erwarten können</h2>
    </div>
    <ol class="schritte" style="list-style:none;padding:0;margin:0">
      <li class="schritt"><h3>Fester Ansprechpartner</h3><p>Jede Praxis hat eine Person im Labor, die den Fall kennt und Rückfragen direkt beantwortet.</p></li>
      <li class="schritt"><h3>Digital geplant</h3><p>98 Prozent der Aufträge kommen digital ins Labor. Planung und Fertigung laufen in einem Datensatz.</p></li>
      <li class="schritt"><h3>Von Hand vollendet</h3><p>Individualisierung, Politur und Endkontrolle übernimmt das Team von Hand, bevor eine Arbeit das Haus verlässt.</p></li>
      <li class="schritt"><h3>Kurze Wege</h3><p>Fotoshooting, Farbnahme und Beratung sind im Labor in Norderstedt möglich, wenige Minuten von Hamburg entfernt.</p></li>
    </ol>
  </div>
</section>

<section class="sektion dunkel" id="kontakt" aria-labelledby="h-kontakt">
  <div class="container kontakt">
    <div class="kontakt-info">
      <span class="kicker">Kontakt</span>
      <h2 id="h-kontakt">Das Team <span class="script">kennenlernen</span></h2>
      <p>Sie möchten Holistic Smile Design kennenlernen? Schreiben Sie uns über das Formular oder rufen Sie an. Gern kommen wir auch zu Ihnen in die Praxis.</p>
      <ul>
        <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/></svg><div><a href="tel:+494094369370">040 94369370</a><small>Mo–Do 08:00–18:00 Uhr, Fr 08:00–15:00 Uhr</small></div></li>
        <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg><div><a href="mailto:info@holistic-smile-design.de">info@holistic-smile-design.de</a><small>Für Anfragen und Auftragsdaten</small></div></li>
        <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M12 21s7-6.2 7-11.5A7 7 0 0 0 5 9.5C5 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></svg><div>Oststraße 120<br>22844 Norderstedt<small>Industriegebiet Norderstedt</small></div></li>
        <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg><div><a href="https://www.instagram.com/holistic_smile_design/" rel="noopener" target="_blank">@holistic_smile_design</a><small>Einblicke ins Labor auf Instagram</small></div></li>
      </ul>
    </div>
    {formular()}
  </div>
</section>
"""
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "AboutPage", "@id": DOMAIN + "team.html", "name": "Das Team von Holistic Smile Design", "url": DOMAIN + "team.html", "about": {"@id": DOMAIN + "#labor"}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Startseite", "item": DOMAIN},
            {"@type": "ListItem", "position": 2, "name": "Team", "item": DOMAIN + "team.html"}]}]}
    extra = '<script type="application/ld+json">\n' + json.dumps(ld, ensure_ascii=False, indent=1) + '\n</script>'
    seite = kopf('Team | Holistic Smile Design, Dentallabor Norderstedt', 'Das Team von Holistic Smile Design: Zahntechnikermeister Frank Köpp, M.Sc., und sein Team im digitalen Dentallabor in Norderstedt bei Hamburg.', 'team.html', extra=extra) + body + FUSS
    open('team.html', 'w', encoding='utf-8').write(seite)
    print('geschrieben team.html')

teamseite()

# Sitemap
urls = [''] + [l['datei'] for l in LEISTUNGEN] + ['team.html']
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for u in urls:
    sm += f'  <url><loc>{DOMAIN}{u}</loc><lastmod>2026-09-30</lastmod><changefreq>monthly</changefreq><priority>{"1.0" if u=="" else "0.8"}</priority></url>\n'
open('sitemap.xml', 'w', encoding='utf-8').write(sm + '</urlset>\n')
print('sitemap.xml aktualisiert')
