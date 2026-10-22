import express from 'express';
import multer from 'multer';
import cors from 'cors';
import pg from 'pg';
import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';

const { Pool } = pg;
const app = express();
const PORT = process.env.PORT || 10000;
const PUBLIC = path.join(process.cwd(), 'public');

const upload = multer({
  storage: multer.memoryStorage(),
  limits: {
    files: 20,
    fileSize: 25 * 1024 * 1024
  }
});

app.use(cors());
app.use(express.json({ limit: '2mb' }));
app.use(express.static(PUBLIC, { extensions: ['html'] }));

let pool = null;

if (process.env.DATABASE_URL) {
  pool = new Pool({
    connectionString: process.env.DATABASE_URL,
    ssl:
      process.env.NODE_ENV === 'production'
        ? { rejectUnauthorized: false }
        : false
  });
}

const memory = {
  submissions: new Map(),
  files: []
};

const allowedTypes = {
  OPERATIONAL_MINE: [
    'Project_ID',
    'Project_Name',
    'Project_Type',
    'Commodity',
    'Asset_Area',
    'Record_ID',
    'Record_Date'
  ],
  EXPLORATION: [
    'Project_ID',
    'Project_Name',
    'Project_Type',
    'Commodity',
    'Asset_Area',
    'Record_ID'
  ],
  FINANCIAL_MODELLING: [
    'Project_ID',
    'Project_Name',
    'Project_Type',
    'Commodity',
    'Asset_Area',
    'Record_ID'
  ]
};

function detectDelimiter(s) {
  const line =
    s
      .replace(/^\uFEFF/, '')
      .split(/\r?\n/)
      .find((x) => x.trim()) || '';

  return [',', ';', '\t', '|']
    .map((d) => ({
      d,
      n: (line.match(new RegExp('\\' + d, 'g')) || []).length
    }))
    .sort((a, b) => b.n - a.n)[0].d;
}

function parseCSV(text, delimiter) {
  const rows = [];
  let row = [];
  let cell = '';
  let quoted = false;

  text = text.replace(/^\uFEFF/, '');

  for (let i = 0; i < text.length; i++) {
    const c = text[i];

    if (c === '"') {
      if (quoted && text[i + 1] === '"') {
        cell += '"';
        i++;
      } else {
        quoted = !quoted;
      }
    } else if (c === delimiter && !quoted) {
      row.push(cell);
      cell = '';
    } else if ((c === '\n' || c === '\r') && !quoted) {
      if (c === '\r' && text[i + 1] === '\n') i++;

      row.push(cell);
      cell = '';

      if (row.some((v) => String(v).trim() !== '')) {
        rows.push(row);
      }

      row = [];
    } else {
      cell += c;
    }
  }

  if (cell !== '' || row.length) {
    row.push(cell);

    if (row.some((v) => String(v).trim() !== '')) {
      rows.push(row);
    }
  }

  if (!rows.length) {
    return {
      headers: [],
      records: []
    };
  }

  const headers = rows[0].map((x) => String(x).trim());

  const records = rows.slice(1).map((r) =>
    Object.fromEntries(
      headers.map((h, i) => [
        h,
        (r[i] ?? '').trim()
      ])
    )
  );

  return {
    headers,
    records
  };
}

function validate(text, projectId) {
  const out = {
    corrupted: {
      pass: true,
      detail: 'Readable text'
    },
    duplicate: {
      pass: true,
      detail: 'No duplicate submission detected'
    },
    mismatched: {
      pass: true,
      detail: 'Project ID consistent'
    },
    blank: {
      pass: true,
      detail: 'No blank required rows'
    },
    undefined: {
      pass: true,
      detail: 'Defined schema'
    }
  };

  if (!text || text.length < 2) {
    out.corrupted = {
      pass: false,
      detail: 'Empty or unreadable file'
    };
  }

  let delimiter = '';
  let parsed = {
    headers: [],
    records: []
  };

  try {
    delimiter = detectDelimiter(text);
    parsed = parseCSV(text, delimiter);
  } catch (e) {
    out.corrupted = {
      pass: false,
      detail: e.message
    };

    return {
      out,
      delimiter,
      parsed
    };
  }

  if (!parsed.headers.includes('Project_ID')) {
    out.undefined = {
      pass: false,
      detail: 'Project_ID column missing'
    };
  }

  const ids = [
    ...new Set(
      parsed.records
        .map((r) => r.Project_ID)
        .filter(Boolean)
    )
  ];

  if (
    ids.length &&
    ids.some((id) => id !== projectId)
  ) {
    out.mismatched = {
      pass: false,
      detail: `Received ${ids.join(', ')}; expected ${projectId}`
    };
  }

  const blanks = parsed.records
    .map((r, i) => ({
      row: i + 2,
      missing: Object.entries(r)
        .filter(([k, v]) => !String(v).trim())
        .map(([k]) => k)
    }))
    .filter((x) => x.missing.length);

  if (blanks.length) {
    out.blank = {
      pass: false,
      detail: `${blanks.length} row(s) contain blank fields`,
      rows: blanks.slice(0, 20)
    };
  }

  if (parsed.headers.some((h) => !h)) {
    out.undefined = {
      pass: false,
      detail: 'Undefined column name'
    };
  }

  const seen = new Set();
  const dups = [];

  for (const r of parsed.records) {
    const k = r.Record_ID || JSON.stringify(r);

    if (seen.has(k)) {
      dups.push(k);
    }

    seen.add(k);
  }

  if (dups.length) {
    out.duplicate = {
      pass: false,
      detail: `${dups.length} duplicate record(s)`,
      records: dups.slice(0, 20)
    };
  }

  return {
    out,
    delimiter,
    parsed
  };
}

async function db(q, params = []) {
  if (!pool) {
    throw new Error('DATABASE_URL is not configured');
  }

  return pool.query(q, params);
}

async function ensureSchema() {
  if (pool) {
    const sql = fs.readFileSync(
      path.join(process.cwd(), 'sql/schema.sql'),
      'utf8'
    );

    await pool.query(sql);
  }
}

function submissionId() {
  return (
    'SUB-' +
    crypto
      .randomBytes(4)
      .toString('hex')
      .toUpperCase()
  );
}

/* =========================
   HEALTH
========================= */

app.get('/api/health', (req, res) => {
  res.json({
    ok: true,
    service: 'IGPC Live System',
    database: Boolean(pool),
    time: new Date().toISOString()
  });
});

/* =========================
   PROJECTS
========================= */

app.get('/api/projects', async (req, res) => {
  try {
    if (pool) {
      const r = await db(
        `SELECT
          project_id,
          max(created_at) latest,
          max(status) status
         FROM submissions
         GROUP BY project_id
         ORDER BY latest DESC`
      );

      return res.json(r.rows);
    }

    res.json([
      ...memory.submissions.values()
    ]);
  } catch (e) {
    res.status(500).json({
      error: e.message
    });
  }
});

/* =========================
   LATEST RELEASED PROJECT
========================= */

app.get(
  '/api/project/:projectId/latest',
  async (req, res) => {
    try {
      const p = req.params.projectId;

      if (pool) {
        const s = await db(
          `SELECT *
           FROM submissions
           WHERE project_id=$1
           AND status='RELEASED'
           ORDER BY released_at DESC NULLS LAST,
                    created_at DESC
           LIMIT 1`,
          [p]
        );

        if (!s.rows[0]) {
          return res.status(404).json({
            error: 'No released submission'
          });
        }

        const f = await db(
          `SELECT *
           FROM files
           WHERE submission_id=$1
           ORDER BY id`,
          [s.rows[0].submission_id]
        );

        return res.json({
          submission: s.rows[0],
          files: f.rows
        });
      }

      const s = [
        ...memory.submissions.values()
      ]
        .filter(
          (x) =>
            x.project_id === p &&
            x.status === 'RELEASED'
        )
        .sort(
          (a, b) =>
            new Date(b.created_at) -
            new Date(a.created_at)
        )[0];

      if (!s) {
        return res.status(404).json({
          error: 'No released submission'
        });
      }

      return res.json({
        submission: s,
        files: memory.files.filter(
          (f) =>
            f.submission_id === s.submission_id
        )
      });
    } catch (e) {
      res.status(500).json({
        error: e.message
      });
    }
  }
);

/* =========================
   CSV UPLOAD
========================= */

app.post(
  '/api/upload',
  upload.array('files', 20),
  async (req, res) => {
    try {
      const projectId = String(
        req.body.project_id || ''
      ).trim();

      if (!projectId) {
        return res.status(400).json({
          error: 'project_id required'
        });
      }

      if (!req.files?.length) {
        return res.status(400).json({
          error: 'At least one CSV/TXT file required'
        });
      }

      const sid = submissionId();

      let overall = 'PASSED';
      const results = [];

      for (const file of req.files) {
        const text = file.buffer.toString('utf8');

        const v = validate(
          text,
          projectId
        );

        const failed = Object.values(
          v.out
        ).some((x) => !x.pass);

        if (failed) {
          overall = 'ON_HOLD';
        }

        results.push({
          file_name: file.originalname,
          rows: v.parsed.records.length,
          delimiter: v.delimiter,
          columns: v.parsed.headers,
          tests: v.out,
          passed: !failed,
          raw_text: text
        });
      }

      const projectType =
        results
          .map((x) =>
            x.raw_text.match(
              /Project_Type[,;\t|]([^,;\t|\r\n]+)/
            )?.[1]
          )
          .find(Boolean) ||
        'UNDEFINED';

      const submission = {
        submission_id: sid,
        client: req.body.client || '',
        project_id: projectId,
        project_type: projectType,
        status: overall,
        version: 1,
        created_at:
          new Date().toISOString()
      };

      if (pool) {
        await db('BEGIN');

        try {
          await db(
            `INSERT INTO submissions
            (
              submission_id,
              client,
              project_id,
              project_type,
              status,
              version
            )
            VALUES
            ($1,$2,$3,$4,$5,$6)`,
            [
              sid,
              submission.client,
              projectId,
              projectType,
              overall,
              1
            ]
          );

          for (const f of results) {
            await db(
              `INSERT INTO files
              (
                submission_id,
                file_name,
                raw_text,
                delimiter,
                row_count,
                columns_json,
                validation_json
              )
              VALUES
              ($1,$2,$3,$4,$5,$6,$7)`,
              [
                sid,
                f.file_name,
                f.raw_text,
                f.delimiter,
                f.rows,
                JSON.stringify(f.columns),
                JSON.stringify(f.tests)
              ]
            );
          }

          await db('COMMIT');
        } catch (e) {
          await db('ROLLBACK');
          throw e;
        }
      } else {
        memory.submissions.set(
          sid,
          submission
        );

        results.forEach((f) =>
          memory.files.push({
            ...f,
            submission_id: sid
          })
        );
      }

      res.json({
        submission,
        files: results.map(
          ({ raw_text, ...x }) => x
        )
      });
    } catch (e) {
      res.status(500).json({
        error: e.message
      });
    }
  }
);

/* =========================
   RELEASE SUBMISSION
========================= */

app.post(
  '/api/submission/:sid/release',
  async (req, res) => {
    try {
      const sid = req.params.sid;

      if (pool) {
        const r = await db(
          `UPDATE submissions
           SET
             status='RELEASED',
             released_at=NOW()
           WHERE submission_id=$1
           RETURNING *`,
          [sid]
        );

        if (!r.rows[0]) {
          return res.status(404).json({
            error: 'Submission not found'
          });
        }

        return res.json({
          submission: r.rows[0]
        });
      }

      const s =
        memory.submissions.get(sid);

      if (!s) {
        return res.status(404).json({
          error: 'Submission not found'
        });
      }

      s.status = 'RELEASED';
      s.released_at =
        new Date().toISOString();

      memory.submissions.set(
        sid,
        s
      );

      res.json({
        submission: s
      });
    } catch (e) {
      res.status(500).json({
        error: e.message
      });
    }
  }
);


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


/* =========================
   FRONT-END FALLBACK
   Express 5 compatible
========================= */

app.get(
  '/*splat',
  (req, res) => {
    res.sendFile(
      path.join(
        PUBLIC,
        'index.html'
      )
    );
  }
);

/* =========================
   START SERVER
========================= */

ensureSchema()
  .then(() => {
    app.listen(
      PORT,
      () => {
        console.log(
          `IGPC Live System listening on ${PORT}`
        );
      }
    );
  })
  .catch((e) => {
    console.error(e);
    process.exit(1);
  });