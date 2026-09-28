# Webseite Holistic Smile Design

Die Webseite des Dentallabors **Holistic Smile Design** in Norderstedt.
Zielgruppe sind Zahnarztpraxen. Geplante Adresse: **holistic-smile-design.de**

Reine HTML-Seite, ohne Baukasten, ohne Datenbank, ohne fremde Tracker.
Entwurf und Inhalt: Ovidiu Rieger, AO Consulting.

---

## Zwei Adressen, zwei Zweige

| Zweig | Wohin | Adresse |
|---|---|---|
| `main` | Vorschau bei GitHub Pages | https://holistic-smile-design.vorschau.ao-consult.de |
| `live` | echter Server bei All-Inkl | https://holistic-smile-design.de |

**Nichts geht ohne Freigabe live.** Änderungen landen zuerst auf `main`.
Erst wenn `live` auf den Stand von `main` gesetzt wird, lädt GitHub die Dateien
per verschlüsseltem FTP zum Hoster.

Die Vorschau sperrt sich selbst gegen Google aus: der Ablauf
`.github/workflows/vorschau.yml` setzt beim Bauen in jede Seite einen
`noindex`-Hinweis und ersetzt die `robots.txt`. **In den Quelldateien steht
kein `noindex`** – ausgenommen die drei Rechtsseiten, die auch später nicht in
die Suche gehören.

---

## Aufbau

```
website/            die Seite. Nur was hier liegt, geht online.
  index.html        Startseite als Onepager
  *-norderstedt.html   fünf Leistungsseiten
  impressum.html datenschutz.html barrierefreiheit.html
  assets/           CSS und JavaScript
  img/ fonts/       Bilder und Schriften, alles lokal
  sitemap.xml robots.txt
doku/               Unterlagen, gehen NICHT online
  werkzeug/         die Skripte, mit denen die Unterseiten erzeugt werden
  projektstand.md   Ovis Arbeitsprotokoll mit allen Entscheidungen
```

### Wichtig: die Unterseiten sind erzeugt, nicht getippt

Die fünf Leistungsseiten, die drei Rechtsseiten und `sitemap.xml` werden von
`doku/werkzeug/seiten-bauen.py` erzeugt. Kopf, Fuß und Banner kommen dabei aus
`index.html`.

**Änderungen an einer Unterseite gehören in das Skript**, nicht in die fertige
HTML-Datei. Sonst sind sie beim nächsten Lauf des Generators weg.
Für Textkorrekturen an `index.html` gilt das nicht, die kann man direkt ändern.

Das Skript lag im Entwurf unter `website/werkzeug/` und liegt jetzt unter
`doku/werkzeug/`. Sonst wären die Python-Dateien mit online gegangen.

---

## Was diese Seite bewusst NICHT tut

- kein Google Analytics, kein Meta-Pixel, kein reCAPTCHA
- keine Schriften von fremden Servern, Jost und Amsterdam Four liegen im Paket
- keine Cookies außer dem Speicher für die Einwilligungs-Entscheidung

**Google Maps lädt erst nach Zustimmung**, über das Banner oder den Knopf auf
der Karte. Vorher geht keine einzige Anfrage dorthin.

---

## Vor dem Livegang zu erledigen

Aus `doku/projektstand.md`. Die Punkte 1 bis 5 blockieren den Livegang.

### Muss

- [ ] **Das Kontaktformular verschickt nichts.** Es prüft die Pflichtfelder und
      zeigt eine Danke-Ansicht, mehr nicht. Die Stelle für den Versand ist im
      Code mit `HIER beim Livegang` markiert. Vorher fällt jede Anfrage ins Leere.
- [ ] **Rechtsseiten vom Kunden prüfen lassen**, die gelb markierten Lücken
      füllen: USt-IdNr., zuständige Handwerkskammer, Innung.
- [ ] **Hoster in der Datenschutzerklärung** eintragen und Speicherdauer der
      Logs, sobald der Server feststeht.
- [ ] **Bildrechte:** Verträge für die Mitarbeiterfotos einholen,
      Bildnachweis Filmox Media laut Vertrag prüfen.
- [ ] **Lizenz der Schrift Amsterdam Four** für die Webnutzung prüfen.
- [ ] **Domain holistic-smile-design.de**: wo liegt sie, wer hat Zugang,
      wo liegen die Postfächer.

### Sollte

- [ ] Vornamen und Rollen der Teammitglieder – aktuell steht nur Frank Köpp
      als Inhaber auf der Seite.
- [ ] Zuordnung des Porträts zu Frank Köpp beim Kunden bestätigen.
- [ ] Erreichbarkeit Mo–Do 08:00–18:00, Fr bis 15:00 Uhr bestätigen lassen.
- [ ] Google Unternehmensprofil mit der Webseite verknüpfen.
- [ ] Search Console anlegen, `sitemap.xml` einreichen.

---

## Wenn etwas kaputt ist

**Die Vorschau zeigt die alte Seite.** Erst messen, dann erklären: im Browser
`Strg + Umschalt + R`, und wenn das nicht hilft, im Reiter „Actions"
nachsehen, ob der letzte Lauf grün war.

**Der Livegang-Ablauf ist rot.** Meistens stimmt eines der vier Secrets nicht.
GitHub → Settings → Secrets and variables → Actions.

---

*Angelegt am 28.09.2026 von Admir Renz. Entwurf und Inhalt: Ovidiu Rieger.*
