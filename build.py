"""Baut tagwerk-app/index.html aus tagwerk.html (derselben Datei wie das Claude-Artifact).

Aufruf:  python build.py
Danach die geänderten Dateien zu GitHub hochladen.
"""
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "tagwerk.html"
OUT = ROOT / "index.html"
FIREBASE = "10.12.2"

HEAD = f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no,viewport-fit=cover">
<meta name="theme-color" content="#EEF2EF" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0E1311" media="(prefers-color-scheme: dark)">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Tagwerk">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<link rel="manifest" href="manifest.json">
<link rel="icon" href="icons/icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
<style>:root{{color-scheme:light;box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}body{{margin:0;padding:0;font:14px -apple-system,BlinkMacSystemFont,sans-serif}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
<script src="https://www.gstatic.com/firebasejs/{FIREBASE}/firebase-app-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/{FIREBASE}/firebase-auth-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/{FIREBASE}/firebase-firestore-compat.js"></script>
<script src="firebase-config.js"></script>
</head>
<body>
"""

FOOT = """
<script>
if ('serviceWorker' in navigator) addEventListener('load', () => navigator.serviceWorker.register('sw.js').catch(() => {}));
</script>
</body>
</html>
"""

OUT.parent.mkdir(exist_ok=True)
OUT.write_text(HEAD + SRC.read_text(encoding="utf-8") + FOOT, encoding="utf-8")
print("geschrieben:", OUT)
