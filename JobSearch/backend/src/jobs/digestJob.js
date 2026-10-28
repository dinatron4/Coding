import supabase from '../services/supabase.js';
import { sendDigest } from '../services/emailService.js';

const MIN_SCORE = 75;
const MAX_JOBS_PER_EMAIL = 10;

export async function runDigest() {
  console.log('[digest] Starting email digest...');

  const { data: candidates } = await supabase
    .from('candidates')
    .select('*')
    .eq('is_active', true);

  for (const candidate of (candidates ?? [])) {
    const { data: topJobs } = await supabase
      .from('candidate_job_scores')
      .select('*, jobs(*)')
      .eq('candidate_id', candidate.id)
      .eq('status', 'new')
      .gte('score', MIN_SCORE)
      .order('score', { ascending: false })
      .limit(MAX_JOBS_PER_EMAIL);

    if (!topJobs?.length) {
      console.log(`[digest] No new jobs above threshold for candidate ${candidate.id}`);
      continue;
    }

    try {
      await sendDigest({ candidate, jobs: topJobs });
      console.log(`[digest] Sent ${topJobs.length} jobs to ${candidate.email}`);
    } catch (err) {
      console.error(`[digest] Failed to send to ${candidate.email}:`, err.message);
    }
  }
}
