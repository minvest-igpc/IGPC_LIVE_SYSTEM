CREATE TABLE IF NOT EXISTS submissions (
  id BIGSERIAL PRIMARY KEY,
  submission_id TEXT NOT NULL UNIQUE,
  client TEXT,
  project_id TEXT NOT NULL,
  project_type TEXT,
  status TEXT NOT NULL,
  version INTEGER NOT NULL DEFAULT 1,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  released_at TIMESTAMPTZ
);
CREATE TABLE IF NOT EXISTS files (
  id BIGSERIAL PRIMARY KEY,
  submission_id TEXT NOT NULL REFERENCES submissions(submission_id) ON DELETE CASCADE,
  file_name TEXT NOT NULL,
  raw_text TEXT NOT NULL,
  delimiter TEXT,
  row_count INTEGER,
  columns_json JSONB NOT NULL DEFAULT '[]'::jsonb,
  validation_json JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
CREATE INDEX IF NOT EXISTS idx_submissions_project ON submissions(project_id, created_at DESC);
CREATE INDEX IF NOT EXISTS idx_files_submission ON files(submission_id);
