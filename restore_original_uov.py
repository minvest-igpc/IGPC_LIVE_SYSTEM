# -*- coding: utf-8 -*-
"""
Restore ORIGINAL UOV dashboard (igpc_portal) into IGPC Live public/uov/
and retarget API calls to same-origin /api/uov/* so it works on Render.
"""
from pathlib import Path
import re

home = Path.home()
candidates = [
    home / "Desktop" / "igpc_portal" / "templates" / "index.html",
    Path(r"C:\Users\Shop\Desktop\igpc_portal\templates\index.html"),
]

src = None
for c in candidates:
    if c.exists():
        src = c
        break

if src is None:
    desk = home / "Desktop"
    if desk.exists():
        for p in desk.rglob("index.html"):
            try:
                text = p.read_text(encoding="utf-8", errors="replace")[:3000]
            except Exception:
                continue
            if (
                "Master Operations" in text
                or "IGPC Master" in text
                or ("body-bg" in text and "0b0f19" in text)
            ):
                src = p
                break

if src is None:
    raise SystemExit(
        "ORIGINAL UOV NOT FOUND.\n"
        "Expected: Desktop\\igpc_portal\\templates\\index.html\n"
        "Confirm that folder exists, then re-run."
    )

root = Path.cwd()
if (root / "public").is_dir():
    dest_dir = root / "public" / "uov"
else:
    dest_dir = root / "uov"

dest_dir.mkdir(parents=True, exist_ok=True)
dest = dest_dir / "index.html"

html = src.read_text(encoding="utf-8", errors="replace")
print("Source: {} ({} chars)".format(src, len(html)))

back_bar = (
    '\n<div id="igpc-back-bar" style="position:sticky;top:0;z-index:9999;'
    "display:flex;gap:10px;align-items:center;justify-content:space-between;"
    "flex-wrap:wrap;padding:10px 16px;background:#0f172a;border-bottom:1px solid #334155;"
    'font-family:system-ui,sans-serif">'
    '<a href="/" style="color:#38bdf8;text-decoration:none;font-weight:700;font-size:13px">'
    "← Back to IGPC Live System</a>"
    '<span style="color:#94a3b8;font-size:12px">'
    "UNIVERSAL OPERATIONAL VAULT (original portal)</span></div>\n"
)

if "Back to IGPC Live" not in html and "igpc-back-bar" not in html:
    if re.search(r"<body[^>]*>", html, re.I):
        html = re.sub(
            r"(<body[^>]*>)", r"\1" + back_bar, html, count=1, flags=re.I
        )
    else:
        html = back_bar + html

repls = [
    ("/api/run-engine", "/api/uov/run-engine"),
    ("/api/get-delays", "/api/uov/get-delays"),
    ("/api/toggle-alert-opened", "/api/uov/toggle-alert-opened"),
    ("/api/log-delay", "/api/uov/log-delay"),
    ("/api/signoff", "/api/uov/signoff"),
    ("/api/tarp-qc-release", "/api/uov/tarp-qc-release"),
    ("/api/import-p6-file", "/api/uov/import-p6-file"),
    ("/api/export-p6", "/api/uov/export-p6"),
    ("/api/export-powerbi", "/api/uov/exports"),
]
for a, b in repls:
    html = html.replace(a, b)

html = html.replace("/api/uov/uov/", "/api/uov/")

dest.write_text(html, encoding="utf-8")
print("Restored original UOV -> {} ({} chars)".format(dest, len(html)))

server = None
for s in [root / "server.js", root.parent / "server.js"]:
    if s.exists():
        server = s
        break

if server:
    sj = server.read_text(encoding="utf-8")
    if "api/uov/get-delays" not in sj:
        extra = """
/* =========================
   UOV original portal API aliases
========================= */
app.get('/api/uov/get-delays', (req, res) => {
  res.json({ delays: [], ok: true });
});
app.post('/api/uov/toggle-alert-opened', (req, res) => {
  res.json({ ok: true });
});
app.post('/api/uov/log-delay', (req, res) => {
  res.json({ ok: true });
});
app.post('/api/uov/signoff', (req, res) => {
  res.json({ ok: true });
});
app.post('/api/uov/tarp-qc-release', (req, res) => {
  res.json({ ok: true });
});
app.post('/api/uov/import-p6-file', (req, res) => {
  res.json({ ok: true, message: 'P6 import accepted (demo)' });
});
app.get('/api/uov/export-p6', (req, res) => {
  res.json({ ok: true, rows: [] });
});
"""
        key = "/* =========================\n   FRONT-END FALLBACK"
        if key in sj:
            sj = sj.replace(key, extra + "\n" + key, 1)
            server.write_text(sj, encoding="utf-8")
            print("Patched API aliases into {}".format(server))
        else:
            print("NOTE: insert point not found in server.js")
    else:
        print("server.js already has UOV portal API aliases")
else:
    print("NOTE: server.js not found — only HTML restored")

print("DONE: Original UOV dashboard restored at public/uov/")
