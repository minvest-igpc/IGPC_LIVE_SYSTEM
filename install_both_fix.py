
from pathlib import Path
import re, shutil

root = Path('.')
pub = root / 'public'
# copy fixed files expected next to this script
for src, dest in [
    ('main_fixed2.html', pub / 'index.html'),
    ('uov_fixed2.html', pub / 'uov' / 'index.html'),
]:
    s = Path(src)
    if not s.exists():
        raise SystemExit(f'Missing {src}')
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(s, dest)
    print('Wrote', dest)

server = root / 'server.js'
if server.exists():
    sj = server.read_text(encoding='utf-8')
    snippet = Path('uov_api_success.js').read_text(encoding='utf-8')
    # replace existing /api/uov/run-engine handler if present
    if "app.get('/api/uov/run-engine'" in sj or 'app.get("/api/uov/run-engine"' in sj:
        sj2 = re.sub(
            r"app\.get\(['\"]/api/uov/run-engine['\"],\s*\(req,\s*res\)\s*=>\s*\{[\s\S]*?\n\}\);",
            snippet.strip() + "\n",
            sj,
            count=1,
        )
        if sj2 == sj:
            print('Could not regex-replace run-engine; inserting before FALLBACK')
            key = "/* =========================\n   FRONT-END FALLBACK"
            if key in sj and 'status: \'SUCCESS\'' not in sj and 'status: "SUCCESS"' not in sj:
                sj2 = sj.replace(key, snippet + "\n" + key, 1)
        server.write_text(sj2, encoding='utf-8')
        print('Patched server.js run-engine SUCCESS shape')
    else:
        key = "/* =========================\n   FRONT-END FALLBACK"
        if key in sj:
            server.write_text(sj.replace(key, snippet + "\n" + key, 1), encoding='utf-8')
            print('Inserted run-engine SUCCESS handler')
        else:
            print('NOTE: patch server.js manually with uov_api_success.js')
print('DONE')
