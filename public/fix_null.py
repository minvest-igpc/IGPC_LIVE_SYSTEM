from pathlib import Path
import re

p = Path("index.html")
t = p.read_text(encoding="utf-8")

pat1 = r"function refreshHeader\(\)\s*\{[\s\S]*?\n\s*\}"
rep1 = (
"function refreshHeader(){\n"
"  const q=s=>document.querySelector(s);\n"
"  if(q(\"#projectId\"))q(\"#projectId\").textContent=DATA.projectId;\n"
"  if(q(\"#projectName\"))q(\"#projectName\").textContent=DATA.projectName;\n"
"  if(q(\"#depth\"))q(\"#depth\").textContent=num(DATA.depth,0)+\" m\";\n"
"  if(q(\"#commodity\"))q(\"#commodity\").textContent=DATA.commodity;\n"
" }"
)
t2, n1 = re.subn(pat1, rep1, t, count=1)

pat2 = r"function openView\(id\)\s*\{[\s\S]*?window\.scrollTo\(0,\s*0\);\s*\}"
rep2 = (
"function openView(id){\n"
"  document.querySelectorAll(\".view\").forEach(v=>v.classList.remove(\"active\"));\n"
"  const el=document.getElementById(id); if(el) el.classList.add(\"active\");\n"
"  document.querySelectorAll(\".nav button\").forEach(b=>b.classList.toggle(\"active\",b.dataset.view===id));\n"
"  const tt=titles[id]; const t1=document.getElementById(\"title\"); const t2=document.getElementById(\"subtitle\");\n"
"  if(tt&&t1)t1.textContent=tt[0]; if(tt&&t2)t2.textContent=tt[1];\n"
"  window.scrollTo(0,0);\n"
" }"
)
t3, n2 = re.subn(pat2, rep2, t2, count=1)

p.write_text(t3, encoding="utf-8")
print("refreshHeader", n1, "openView", n2)
if n1 != 1 or n2 != 1:
    for label, needle in [("refreshHeader", "function refreshHeader"), ("openView", "function openView")]:
        i = t.find(needle)
        print(label, "idx", i)
        if i >= 0:
            print(repr(t[i:i+220]))
