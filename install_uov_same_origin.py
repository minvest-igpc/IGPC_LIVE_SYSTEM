
from pathlib import Path
import re, shutil

root = Path('.')
pub = root / 'public'
uov_dir = pub / 'uov'
uov_dir.mkdir(parents=True, exist_ok=True)

# copy uov page (script written beside this file)
src_html = Path('uov_index.html')
if not src_html.exists():
    raise SystemExit('uov_index.html missing next to installer')
shutil.copy(src_html, uov_dir / 'index.html')
print('Wrote public/uov/index.html')

# fix button
idx = pub / 'index.html'
t = idx.read_text(encoding='utf-8', errors='replace')
t2 = re.sub(
    r"window\.open\(\s*['\"]https?://(?:localhost|127\.0\.0\.1):\d+['\"]\s*,\s*['\"]_blank['\"]\s*\)",
    "window.open('/uov/', '_blank')",
    t,
)
idx.write_text(t2, encoding='utf-8')
print('Retargeted UOV button to /uov/' if t2 != t else 'Button already /uov/ or not found')

# patch server
server = Path('server.js')
text = server.read_text(encoding='utf-8')
if 'api/uov/run-engine' in text:
    print('server.js already has UOV routes')
else:
    insert = Path('uov_routes_snippet.js').read_text(encoding='utf-8')
    key = "/* =========================\n   FRONT-END FALLBACK"
    if key not in text:
        # try alternate
        key = "app.get(\n  '/*splat'"
    if key not in text:
        raise SystemExit('Insert point not found in server.js')
    text = text.replace(key, insert + "\n\n" + key, 1)
    server.write_text(text, encoding='utf-8')
    print('Patched server.js with /api/uov/* routes')

print('DONE — IGPC + UOV same origin. Push public/, server.js together.')
