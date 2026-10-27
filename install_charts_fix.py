
from pathlib import Path
import shutil
root = Path('.')
pub = root / 'public'
(pub / 'uov').mkdir(parents=True, exist_ok=True)
shutil.copy('main_charts_fixed.html', pub / 'index.html')
shutil.copy('uov_charts_fixed.html', pub / 'uov' / 'index.html')
if Path('server_fixed.js').exists():
    shutil.copy('server_fixed.js', root / 'server.js')
print('Installed main, uov, server')
print('Analytics points to /analytics.html (2.2MB MINVEST IGPC SYSTEM)')
print('UOV opens https://igpc-live-system.onrender.com/uov/ in new tab')
print('Charts use original renderPlotly3D/renderWaterfall/renderFriction/renderGantt')
