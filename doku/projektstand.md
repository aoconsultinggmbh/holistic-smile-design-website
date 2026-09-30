# Holistic Smile Design, Webseite Entwurf 1

Dentallabor in Norderstedt, Zielgruppe Zahnarztpraxen. Startseite als Onepager, fünf Leistungsseiten, drei Rechtsseiten.
Stand: 25.09.2026, Entwurf von AO Consulting.

## Öffnen

`index.html` per Doppelklick im Browser öffnen. Unter `file://` meldet die Konsole zwei
CORS-Hinweise zu den vorgeladenen Schriften. Das ist eine Eigenart des Protokolls, über
HTTP (Vorschau-Server oder Livegang) tritt der Hinweis nicht auf.

## Aufbau

| Datei | Inhalt |
|---|---|
| `index.html` | Startseite: Hero mit Inhaber, Vertrauensleiste mit Live-Öffnungsstatus, Leistungen, Ablauf, Labor, Technik, Einzugsgebiet, FAQ, Kontakt |
| `teleskoparbeiten-norderstedt.html` u. a. | Fünf Leistungsseiten (Teleskoparbeiten, All-on-4/All-on-6, Implantatschablonen und Stackable Guides, Vollkeramik, Digitaler Workflow), je mit H1 mit Ortsbezug, Nutzen, Ablauf, Technik, FAQ mit Schema, Formular |
| `werkzeug/seiten-bauen.py` | Generator für Leistungs- und Rechtsseiten sowie sitemap.xml. Kopf, Fuß und Banner-Konfiguration kommen aus index.html. **Änderungen an Unterseiten hier eintragen und neu bauen**, sonst gehen sie beim nächsten Lauf verloren. |
| `assets/stil.css`, `assets/skript.js` | Gemeinsames CSS und JS aller Seiten |
| `impressum.html`, `datenschutz.html`, `barrierefreiheit.html` | Rechtsseiten als Entwurf, Lücken gelb markiert |
| `assets/` | Einwilligungsbanner und Barrierefreiheits-Widget (AO-Standard, Farben über `--navy` und `--coral` aus der Seite) |
| `fonts/` | Jost (300 bis 600, OFL) und Amsterdam Four (aus dem gelieferten Font-Paket, Lizenz beim Kunden prüfen) |
| `img/` | 12 Fotos als WebP und JPG, lange Kante 1800 px, SEO-Dateinamen, Favicon-Set |

Neu bauen: im Projektordner `python3 werkzeug/seiten-bauen.py` ausführen.

## Farben und Schrift

- Schwarz `#242424`, Gold `#c09e12` (Vorgabe Kunde), Creme `#f7f5ef` für helle Sektionen
- Jost als Pendant zur Logoschrift (dünne geometrische Grotesk), Amsterdam Four für die
  Script-Akzente wie im Logo
- Elemente leicht abgerundet (10 und 18 px), wie im Onboarding gewünscht

## Entscheidungen

- **Öffnungsstatus** in der Vertrauensleiste wird per JavaScript aus Mo bis Fr 8 bis 18 Uhr (Europe/Berlin) berechnet. Bei Änderung der Zeiten die Konstanten OEFFNET und SCHLIESST im Skript und die Texte anpassen.

- **Kontaktformular verschickt nichts.** Pflichtfelder werden geprüft, dann Danke-Ansicht.
  Stelle für den Versand ist im Code kommentiert (`HIER beim Livegang`).
- **Google Maps erst nach Einwilligung**, über Banner oder Knopf auf der Karte. Vorher keine
  Anfrage an einen Dritten (automatisiert geprüft).
- **Schriften lokal**, keine Verbindung zu Google Fonts. Die Datenschutzerklärung sagt das zu.
- **Inhaber im Hero:** Porträt 03486 wurde als Frank Köpp zugeordnet (Mann mit Brille, bedient auf den Fotos Fräse und CAD). Beim Kunden bestätigen.
- **Teammitglieder ohne Namen**, laut Onboarding nur Vornamen. Vornamen liegen noch nicht vor,
  daher aktuell nur Frank Köpp als Inhaber. Bildrechte-Verträge (Musterverträge von Ovidiu)
  vor Livegang einholen.
- **JSON-LD:** `MedicalBusiness` (kein `Dentist`, das Labor behandelt keine Patienten) plus
  `FAQPage`. FAQ-Text und Schema sind deckungsgleich.
- **Einzugsgebiet** ist ein Vorschlag (Norderstedt, Hamburg, Segeberg, Pinneberg, Stormarn)
  und muss vom Kunden bestätigt werden.
- Impressum ohne § 18 Abs. 2 MStV, da kein journalistisches Angebot.

## Offene Punkte für den Kunden

0. Google-Profil: verlinkt ist die Google-Suche "Holistic Smile Design Norderstedt", die das Unternehmensprofil zeigt (Vorgabe Ovidiu). Ein kurzer Teilen-Link aus dem Profil (g.page) waere noch stabiler.

1. Vornamen und Rollen der vier Teammitglieder (Foto: Frau blond, Mann mit Brille und
   Tattoos, junger Mann im weißen Hemd, junge Frau, Mann mit Bart)
2. Öffnungszeiten stehen überall mit Mo bis Fr 8 bis 18 Uhr, Freitag beim Kunden bestätigen (im Gespräch fiel „ggf. bis 16 Uhr")
3. Abholung und Lieferung: Rhythmus, Kurier, Radius
4. Gründungsjahr, Anzahl Mitarbeitende
5. Materialsysteme, Hersteller und Garantie: auf Wunsch von Ovidiu vorerst nicht auf der Seite, später ergänzbar
6. (frei)
7. USt-IdNr., zuständige Handwerkskammer, Innung
8. Hoster für die Datenschutzerklärung (All-Inkl nach Transfer?), Speicherdauer der Logs
9. WhatsApp Business oder privates Konto
10. Bildnachweis Filmox Media laut Vertrag
11. Bestätigung des Einzugsgebiets
12. Lizenz der Amsterdam-Schrift für Webnutzung prüfen

## Fotos

Verwendet auf der Startseite (13 von 154): 03486 Frank Porträt (Hero), 03551 Team, 04618 Frank an der Fräsmaschine, 04551 Fräse Detail,
04643 3D-Drucker, 04472 Farbring, 03931 Teleskoparbeit, 04021 Modell, 04106 Arbeitsplatz
Mitarbeiterin, 03638 Laborraum (Hero), 04880 Fotodokumentation, 04423 CAD-Bildschirm.
Nicht verwendet: Serienaufnahmen, Blumenstrauß-Motive, Hund, Fotografen-Setup, Einzelporträts
(erst nach Freigabe der Vornamen sinnvoll). 04525 Beratung ist konvertiert, aber noch nicht
eingebaut (Reserve). Zusätzlich auf den Leistungsseiten: 03977 Teleskopgerüst, 04236 und 04225 Artikulator, 04333 Schablone, 04140 Pinsel, 04086 Modell, 04411 CAD-Arbeitsplatz, 04198 Teamabstimmung, 04292 Scanner.

## Prüfung

Playwright über HTTP: genau eine h1 je Seite, lückenlose Hierarchie, alle Bilder mit Alt-Text
und geladen, JSON-LD parst, kein `href="#"`, kein Zugriff auf fremde Hosts vor der
Einwilligung, keine Konsolenfehler, kein horizontales Scrollen bei 1920 bis 390 px, Burger
funktioniert, Banner-Knöpfe gleich groß auf einer Zeile, Formularprüfung und Danke-Ansicht,
Karte lädt nach Zustimmung.

## Livegang

- Formularversand anbinden, Danke-Ansicht an Serverantwort koppeln
- Rechtsseiten vom Kunden prüfen lassen, gelbe Stellen füllen, `noindex` auf den Rechtsseiten
  bleibt
- `sitemap.xml` und `robots.txt` liegen bei, Domain prüfen
- Google Unternehmensprofil (Zugriff bereits hergestellt) mit Website verknüpfen


## Nachtrag 25.09.2026

- **Logo:** Die vom Kunden gelieferte Datei ist das einzige vorhandene Logo (keine Vektordatei). Sie wurde freigestellt (Hintergrund transparent, Weiß und Gold getrennt) und liegt als `img/logo-holistic-smile-design-dentallabor-norderstedt.png` und `.webp` vor. Einsatz nur auf dunklem Grund, auf hellem Grund wäre der weiße Schriftzug unsichtbar.
- **Bildnachweis:** AO Consulting GmbH (Vorgabe Ovidiu).
- **Datenschutzbeauftragter:** nicht bestellt (Vorgabe Ovidiu).
- **WhatsApp und Mobilnummer entfernt:** 0163 2533330 ist Franks private Nummer. Auf der Website stehen nur Festnetz 040 94369370, E-Mail und Formular. Der WhatsApp-Abschnitt in der Datenschutzerklärung ist entfallen.


## Kundenantworten 28.09.2026 (eingearbeitet)

- **Kein festes Einzugsgebiet:** 98 Prozent der Aufträge kommen digital, Kunden u. a. in Hilden und Brieselang. Standort-Sektion, Karte 06, FAQ, Metadaten und JSON-LD (areaServed: Deutschland, Norderstedt, Hamburg) umgestellt. Neue FAQ „Arbeitet Holistic Smile Design auch mit Praxen außerhalb von Hamburg zusammen?". Die Kreis- und Stadtteilliste ist entfallen.
- **98 statt 95 Prozent** überall.
- **Gegründet 2023, Inhaber plus 5 Mitarbeitende:** im Laborteil und im JSON-LD (foundingDate, numberOfEmployees 6).
- **Keine festen Öffnungszeiten, freitags in der Regel bis 15 Uhr:** überall als „Erreichbarkeit, in der Regel Mo–Do 08:00–18:00, Fr bis 15:00 Uhr". Der Live-Status zeigt „Jetzt erreichbar" statt „geöffnet". Mo–Do 8 bis 18 Uhr stammt aus dem Onboarding und sollte kurz bestätigt werden.
- **Abholung durch das Labor** war nicht bestätigt und ist entfernt; Abformungen „können per Post oder Kurier eingeschickt werden".
- **Nicht belegte Zusagen entfernt:** „Antwort innerhalb eines Werktags" und „Parkplätze vor dem Haus".

## Anpassung 28.09.2026, zweite Runde

- Erreichbarkeit ohne „in der Regel": Mo–Do 08:00–18:00 Uhr, Fr 08:00–15:00 Uhr (Vorgabe Ovidiu).
- Hero entschlackt: Fakten-Zeile unter den Knöpfen entfernt, Einleitungssatz ohne Meister/Master, Namensschild nur „Inhaber und Zahntechnikermeister", Überzeile „Digitale Zahntechnik". Die Vertrauensleiste trägt jetzt 98 % digital, Master, Fertigung und Erreichbarkeit, jede Angabe genau einmal.

## Änderung 2 vom 30.09.2026 (Rückmeldung Frank Köpp, 29.09.)

Eingebaut: Darstellungsfehler Handy bei Leistungen 01/02 behoben (Bild in der breiten Karte hatte
eine Prozent-Höhe). Kernkompetenz Backward Planning als Karte 01 und neue Unterseite
`backward-planning-norderstedt.html`. Frank Köpp überall als M.Sc. (Master of Science).
Instagram-Knopf (Kopf, Fußzeile, Kontakt, JSON-LD): https://www.instagram.com/holistic_smile_design/
Neue Team-Seite `team.html` mit sechs Fotos aus der picdrop-Galerie von Filmox Media
(Originale unter kunden-bilder/holistic-smile-design/2026-09-30-teamfotos-picdrop).
Teleskoparbeiten zeigen vorerst das Teleskopgerüst-Foto.

Offen beim Kunden:
- Vornamen und Rollen der fünf Mitarbeitenden für team.html (gelbe Platzhalter im Generator, TEAM-Liste).
- Zuordnung der Fotos zu den Personen bestätigen, auch das Porträt von Frank Köpp.
- Echte Fotos von Teleskoparbeiten liefern (Karte 02 und Unterseite Teleskoparbeiten).
- Fachliche Freigabe der Texte zu Backward Planning (Ablaufschritte Wax-up, Mock-up, Gesichtsscanner, Smilecloud).
- Bildnachweis: Teamfotos stammen von Filmox Media GmbH, im Impressum steht bisher AO Consulting. Beim Gespräch klären.
