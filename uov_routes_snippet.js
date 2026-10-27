
/* =========================
   UOV — same-origin module
========================= */

function readCsv(relPath) {
  const full = path.join(PUBLIC, 'data', relPath);
  if (!fs.existsSync(full)) return [];
  const text = fs.readFileSync(full, 'utf8').replace(/^\uFEFF/, '');
  const delim = text.includes(';') && !text.includes(',') ? ';' : ',';
  const lines = text.split(/\r?\n/).filter((l) => l.trim());
  if (lines.length < 2) return [];
  const headers = lines[0].split(delim).map((h) => h.trim());
  return lines.slice(1).map((line) => {
    const cols = line.split(delim);
    return Object.fromEntries(headers.map((h, i) => [h, (cols[i] ?? '').trim()]));
  });
}

app.get('/api/uov/run-engine', (req, res) => {
  try {
    const master = readCsv(path.join('uov', 'uov_powerbi_master.csv'));
    const incidents = readCsv(path.join('uov', 'uov_powerbi_incidents.csv'));
    const summaryRows = readCsv(path.join('uov', 'uov_powerbi_summary.csv'));
    const summaryMap = Object.fromEntries(
      summaryRows.map((r) => [r.Metric, r.Value])
    );
    const totalLeak = master.reduce(
      (s, r) => s + (Number(r.Total_Financial_Leakage_ZAR) || 0),
      0
    );
    res.json({
      ok: true,
      timestamp: new Date().toISOString(),
      summary: {
        op_status: summaryMap.Op_Status || 'GREEN - OPTIMIZED',
        primary_driver: summaryMap.Primary_Bleed_Driver || 'NORMAL',
        mean_rmr: summaryMap.Mean_RMR || null,
        total_leakage_zar: Number(summaryMap.Total_Financial_Leakage) || totalLeak,
        rows: master.length,
        recommendation:
          summaryMap.Recommendation ||
          'Support strategy optimal. Proceed with planned face advance.'
      },
      master,
      incidents
    });
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

app.get('/api/uov/exports', (req, res) => {
  const base = path.join(PUBLIC, 'data', 'uov');
  const files = fs.existsSync(base)
    ? fs.readdirSync(base).filter((f) => f.endsWith('.csv')).map((f) => 'data/uov/' + f)
    : [];
  res.json({ ok: true, files });
});
