// Offline-Speicher für Tagwerk. Bei jeder neuen Version VERSION hochzählen.
const VERSION = 'tagwerk-v1';
const SHELL = ['./', './index.html', './manifest.json', './firebase-config.js', './icons/icon.svg', './icons/icon-192.png', './icons/icon-512.png', './icons/apple-touch-icon.png'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(VERSION).then(c => c.addAll(SHELL)).then(() => self.skipWaiting()));
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== VERSION).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener('fetch', e => {
  const req = e.request, url = new URL(req.url);
  if (req.method !== 'GET') return;
  // Firebase-Verbindungen (Anmeldung, Datenbank) nie zwischenspeichern
  if (/firestore\.googleapis|identitytoolkit|securetoken|googleapis\.com\/identity/.test(url.href)) return;
  if (url.origin === location.origin) {
    // Eigene Dateien: erst Netz (für Updates), sonst Offline-Kopie
    e.respondWith(fetch(req).then(r => { const c = r.clone(); caches.open(VERSION).then(x => x.put(req, c)); return r; })
      .catch(() => caches.match(req).then(r => r || caches.match('./index.html'))));
  } else if (/gstatic\.com|fonts\.googleapis\.com/.test(url.host)) {
    // Schriften und Firebase-Bibliothek: Kopie sofort, im Hintergrund aktualisieren
    e.respondWith(caches.open(VERSION).then(c => c.match(req).then(hit => {
      const net = fetch(req).then(r => { if (r.ok || r.type === 'opaque') c.put(req, r.clone()); return r; }).catch(() => hit);
      return hit || net;
    })));
  }
});
