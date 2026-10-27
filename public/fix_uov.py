from pathlib import Path
import re

p = Path("index.html")
t = p.read_text(encoding="utf-8", errors="replace")

# Restore non-module grids to 5 columns
t = t.replace("grid-template-columns:repeat(6,1fr)", "grid-template-columns:repeat(5,1fr)")

# Keep modules at 6 columns
t = t.replace(
    ".modules{display:grid;grid-template-columns:repeat(5,1fr)",
    ".modules{display:grid;grid-template-columns:repeat(6,1fr)",
)

# Clean modules block
block = """<div class="modules">
<div class="module library" onclick="openView('library')"><div class="num">01</div><h3>VIRTUAL LIBRARY</h3><p>Secure bridge between client information and IGPC project intelligence, without touching the client's server.</p><div class="go">OPEN VIRTUAL LIBRARY \u2192</div></div>
<div class="module files" onclick="openView('projectfiles')"><div class="num">02</div><h3>PROJECT FILES</h3><p>Master project entry point with the three IGPC core operational boxes and the structured project architecture.</p><div class="go">OPEN PROJECT FILES \u2192</div></div>
<div class="module analytics" onclick="openView('analytics')"><div class="num">03</div><h3>ANALYTICS</h3><p>W1-W10, Layers 1-4, F08 and PCV1-PCV4. This is the integrated analytics dashboard already built.</p><div class="go">OPEN ANALYTICS \u2192</div></div>
<div class="module diagnostics" onclick="openView('diagnostics')"><div class="num">04</div><h3>DIAGNOSTICS</h3><p>Moves from an identified problem or deviation to the most likely causes, probabilities and diagnostic evidence.</p><div class="go">OPEN DIAGNOSTICS \u2192</div></div>
<div class="module reports" onclick="openView('reports')"><div class="num">05</div><h3>REPORTS</h3><p>Controlled reporting from the same project information, analytics, evidence and specialist intelligence.</p><div class="go">OPEN REPORTS \u2192</div></div>
<div class="module uov" onclick="window.open('http://localhost:5001', '_blank')"><div class="num">06</div><h3>UNIVERSAL OPERATIONAL VAULT (UOV)</h3><p>Project-level bottleneck and financial bleed analysis engine. Identifies what is causing the project to lose time and money.</p><div class="go">OPEN UOV \u2192</div></div>
</div>"""

t2, n = re.subn(
    r'<div class="modules">.*?</div>\s*(?=<div class="card")',
    block + "\n",
    t,
    count=1,
    flags=re.S,
)

if n == 0:
    # fallback: remove broken uov cards then insert after reports closing pattern
    t2 = re.sub(r'<div class="module uov"[^>]*>.*?</div>', '', t, flags=re.S)
    t2 = re.sub(
        r'(<div class="module reports".*?</div>)',
        r'\1' + '\n<div class="module uov" onclick="window.open(\'http://localhost:5001\', \'_blank\')"><div class="num">06</div><h3>UNIVERSAL OPERATIONAL VAULT (UOV)</h3><p>Project-level bottleneck and financial bleed analysis engine. Identifies what is causing the project to lose time and money.</p><div class="go">OPEN UOV \u2192</div></div>',
        t2,
        count=1,
        flags=re.S,
    )
    print("Fallback used")
else:
    print("Modules block replaced:", n)

p.write_text(t2, encoding="utf-8")
print("Done")