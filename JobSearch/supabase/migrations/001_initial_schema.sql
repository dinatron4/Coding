-- ============================================================
-- Job Search Engine — Initial Schema
-- ============================================================

-- Candidates (multi-tenant root)
CREATE TABLE candidates (
  id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name        TEXT NOT NULL,
  email       TEXT NOT NULL UNIQUE,
  is_active   BOOLEAN NOT NULL DEFAULT TRUE,
  created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Candidate profiles (preferences, CV, salary, etc.)
CREATE TABLE candidate_profiles (
  id                    UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  candidate_id          UUID NOT NULL REFERENCES candidates(id) ON DELETE CASCADE,
  cv_text               TEXT,
  target_roles          TEXT[] NOT NULL DEFAULT '{}',
  skills                TEXT[] NOT NULL DEFAULT '{}',
  salary_min            INTEGER,
  salary_max            INTEGER,
  salary_currency       TEXT NOT NULL DEFAULT 'USD',
  location_preference   TEXT NOT NULL DEFAULT 'remote_only',
  excluded_companies    TEXT[] NOT NULL DEFAULT '{}',
  years_experience      INTEGER,
  extra_instructions    TEXT,
  scoring_hints         TEXT,
  updated_at            TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  UNIQUE(candidate_id)
);

-- Jobs (shared across candidates — discovered once, scored per-candidate)
CREATE TABLE jobs (
  id               UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  external_id      TEXT NOT NULL UNIQUE,
  title            TEXT NOT NULL,
  company          TEXT NOT NULL,
  description      TEXT NOT NULL,
  url              TEXT NOT NULL,
  source           TEXT NOT NULL,
  posted_at        TIMESTAMPTZ,
  scraped_at       TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  salary_min       INTEGER,
  salary_max       INTEGER,
  currency         TEXT,
  is_remote        BOOLEAN,
  seniority        TEXT,
  skills_required  TEXT[] NOT NULL DEFAULT '{}',
  is_active        BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE INDEX jobs_source_idx     ON jobs(source);
CREATE INDEX jobs_posted_at_idx  ON jobs(posted_at DESC);
CREATE INDEX jobs_is_active_idx  ON jobs(is_active);

-- Per-candidate scores + status
CREATE TABLE candidate_job_scores (
  id               UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  candidate_id     UUID NOT NULL REFERENCES candidates(id) ON DELETE CASCADE,
  job_id           UUID NOT NULL REFERENCES jobs(id) ON DELETE CASCADE,
  score            INTEGER NOT NULL CHECK (score BETWEEN 0 AND 100),
  score_reasoning  TEXT,
  status           TEXT NOT NULL DEFAULT 'new'
                     CHECK (status IN ('new','emailed','accepted','rejected','applied','interview','offer','closed')),
  scored_at        TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  notified_at      TIMESTAMPTZ,
  UNIQUE(candidate_id, job_id)
);

CREATE INDEX cjs_candidate_status_idx ON candidate_job_scores(candidate_id, status);
CREATE INDEX cjs_score_idx            ON candidate_job_scores(score DESC);

-- Feedback (accept/reject with optional reason)
CREATE TABLE feedback (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  candidate_id    UUID NOT NULL REFERENCES candidates(id) ON DELETE CASCADE,
  job_id          UUID NOT NULL REFERENCES jobs(id) ON DELETE CASCADE,
  feedback_type   TEXT NOT NULL CHECK (feedback_type IN ('accept','reject')),
  reject_reason   TEXT CHECK (reject_reason IN ('salary','company','role','tech_stack','seniority','location','other')),
  notes           TEXT,
  created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Cover letters
CREATE TABLE cover_letters (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  candidate_id  UUID NOT NULL REFERENCES candidates(id) ON DELETE CASCADE,
  job_id        UUID NOT NULL REFERENCES jobs(id) ON DELETE CASCADE,
  content       TEXT NOT NULL,
  version       INTEGER NOT NULL DEFAULT 1,
  created_at    TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Magic-link tokens (email accept/reject without login)
CREATE TABLE magic_tokens (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  token         TEXT NOT NULL UNIQUE DEFAULT gen_random_uuid()::TEXT,
  candidate_id  UUID NOT NULL REFERENCES candidates(id) ON DELETE CASCADE,
  job_id        UUID NOT NULL REFERENCES jobs(id) ON DELETE CASCADE,
  action        TEXT NOT NULL CHECK (action IN ('accept','reject')),
  used          BOOLEAN NOT NULL DEFAULT FALSE,
  expires_at    TIMESTAMPTZ NOT NULL DEFAULT (NOW() + INTERVAL '7 days'),
  created_at    TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Email send log
CREATE TABLE email_logs (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  candidate_id  UUID NOT NULL REFERENCES candidates(id) ON DELETE CASCADE,
  type          TEXT NOT NULL CHECK (type IN ('digest','alert')),
  job_ids       UUID[] NOT NULL DEFAULT '{}',
  sent_at       TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
