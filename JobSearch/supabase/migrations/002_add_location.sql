-- Add location field to jobs for geographic grouping in dashboard
ALTER TABLE jobs ADD COLUMN IF NOT EXISTS location TEXT;
