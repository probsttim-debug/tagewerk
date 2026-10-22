# Tagwerk

Persönliche Alltags-App: To-dos, Kalender, Ziele, Gewohnheiten, Tagebuch, Gebetsliste, Fokus-Timer, Listen, Finanzen, Rückblick und jeden Tag ein Bibelvers (Lutherbibel 1912).

Aufgebaut wie Eisenlog: dieselbe App läuft als Claude-Artifact und als installierbare Web-App (GitHub Pages) mit eigenem Konto über Firebase.

## Dateien

| Datei | Zweck |
|---|---|
| `index.html` | Die App (wird mit `python build.py` aus `tagwerk.html` erzeugt) |
| `firebase-config.js` | Deine Firebase-Zugangsdaten |
| `manifest.json`, `icons/` | Damit sich die App auf dem Handy installieren lässt |
| `sw.js` | Offline-Speicher |
| `firestore.rules` | Datenbank-Regeln: Jede Person sieht nur ihre eigenen Daten |

## 1. Firebase einrichten

1. Auf https://console.firebase.google.com ein neues Projekt anlegen, zum Beispiel `tagwerk`.
2. **Authentication** → Jetzt starten → Anbieter **E-Mail/Passwort** aktivieren.
3. **Firestore Database** → Datenbank erstellen (Standort `eur3` oder `europe-west3`).
4. In Firestore → **Regeln** den Inhalt von `firestore.rules` einfügen und veröffentlichen.
5. Projekteinstellungen → Allgemein → „Meine Apps“ → **Web-App hinzufügen** (`</>`). Die angezeigten Werte (`apiKey`, `authDomain` …) in `firebase-config.js` eintragen.
6. Authentication → Einstellungen → **Autorisierte Domains** → `DEIN-NAME.github.io` hinzufügen.

Solange `apiKey` leer ist, läuft die App ohne Anmeldung und speichert nur auf dem Gerät.

## 2. Auf GitHub Pages veröffentlichen

1. Neues Repository anlegen, zum Beispiel `tagwerk`.
2. Den Inhalt dieses Ordners hochladen.
3. Settings → Pages → Branch `main`, Ordner `/ (root)` → Save.
4. Nach etwa einer Minute ist die App unter `https://DEIN-NAME.github.io/tagwerk/` erreichbar.

## 3. Auf dem Handy installieren

- **iPhone (Safari):** Teilen → „Zum Home-Bildschirm“.
- **Android (Chrome):** Menü → „App installieren“.

## Updates

1. `tagwerk.html` ändern.
2. `python build.py` ausführen.
3. In `sw.js` die `VERSION` hochzählen (z. B. `tagwerk-v2`).
4. Geänderte Dateien zu GitHub hochladen.
