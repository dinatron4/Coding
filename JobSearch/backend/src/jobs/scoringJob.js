import supabase from '../services/supabase.js';
import { scoreJob } from '../agents/scoringAgent.js';

const BATCH_SIZE = 10;

const EU_LOCATIONS = new Set([
  'austria', 'belgium', 'bulgaria', 'croatia', 'cyprus', 'czech republic',
  'denmark', 'estonia', 'finland', 'france', 'germany', 'greece', 'hungary',
  'ireland', 'italy', 'latvia', 'lithuania', 'luxembourg', 'malta',
  'netherlands', 'poland', 'portugal', 'romania', 'slovakia', 'slovenia',
  'spain', 'sweden', 'norway', 'switzerland', 'united kingdom', 'uk',
  'europe', 'eu', 'european union', 'emea',
]);

function matchesLocation(job, filter) {
  if (!filter || filter === 'any') return true;
  if (filter === 'remote_only') return job.is_remote === true;
  if (filter === 'eu') {
    const loc = (job.location || '').toLowerCase();
    return EU_LOCATIONS.has(loc) || loc.includes('europe');
  }
  // Specific country match
  const loc = (job.location || '').toLowerCase();
  return loc.includes(filter.toLowerCase());
}

// Only score a job for a candidate if the job title matches their target roles
function isRelevant(job, profile, locationFilter) {
  if (!matchesLocation(job, locationFilter)) return false;

  const targetRoles = (profile.target_roles || []);
  if (!targetRoles.length) return true;

  const jobText = `${job.title} ${(job.skills_required || []).join(' ')}`.toLowerCase();

  return targetRoles.some(role => {
    const keywords = role.toLowerCase().split(/\s+/).filter(w => w.length > 3);
    return keywords.some(kw => jobText.includes(kw));
  });
}

export async function runScoring(filterCandidateId = null, locationFilter = null) {
  console.log('[scoring] Starting scoring job...' + (filterCandidateId ? ` (candidate ${filterCandidateId})` : ' (all candidates)'));

  let query = supabase
    .from('candidates')
    .select('id, candidate_profiles(*)')
    .eq('is_active', true);

  if (filterCandidateId) query = query.eq('id', filterCandidateId);

  const { data: candidates } = await query;

  let totalScored = 0;

  for (const candidate of (candidates ?? [])) {
    const profile = Array.isArray(candidate.candidate_profiles)
      ? candidate.candidate_profiles[0]
      : candidate.candidate_profiles;
    if (!profile) continue;

    // Get jobs not yet scored for this candidate
    const { data: scoredJobIds } = await supabase
      .from('candidate_job_scores')
      .select('job_id')
      .eq('candidate_id', candidate.id);

    const scored = new Set((scoredJobIds ?? []).map(s => s.job_id));

    const { data: jobs } = await supabase
      .from('jobs')
      .select('*')
      .eq('is_active', true)
      .order('scraped_at', { ascending: false })
      .limit(200);

    // Use provided locationFilter or fall back to the candidate's profile preference
    const effectiveLocationFilter = locationFilter ?? profile.location_preference ?? null;

    const unscored = (jobs ?? []).filter(j => !scored.has(j.id));
    const locationPassed = unscored.filter(j => matchesLocation(j, effectiveLocationFilter));
    const relevant = locationPassed.filter(j => isRelevant(j, profile, effectiveLocationFilter));

    console.log(`[scoring] candidate ${candidate.id}: ${unscored.length} unscored → ${locationPassed.length} pass location (${effectiveLocationFilter ?? 'any'}) → ${relevant.length} pass keyword filter`);

    if (!relevant.length) {
      continue;
    }

    const batch = relevant.slice(0, BATCH_SIZE);
    console.log(`[scoring] ${relevant.length} relevant jobs found, scoring ${batch.length} for candidate ${candidate.id}`);

    // Load recent feedback for context
    const { data: feedbackHistory } = await supabase
      .from('feedback')
      .select('*, jobs(title, company)')
      .eq('candidate_id', candidate.id)
      .order('created_at', { ascending: false })
      .limit(20);

    for (const job of batch) {
      console.log(`[scoring] Scoring "${job.title}" @ ${job.company}...`);
      try {
        const { score, score_reasoning } = await scoreJob({ job, profile, feedbackHistory: feedbackHistory ?? [] });

        await supabase.from('candidate_job_scores').insert({
          candidate_id:    candidate.id,
          job_id:          job.id,
          score,
          score_reasoning,
        });

        console.log(`[scoring] → score: ${score}`);
        totalScored++;
      } catch (err) {
        console.error(`[scoring] Error scoring job ${job.id}:`, err.message);
      }
      await new Promise(r => setTimeout(r, 1000));
    }
  }

  console.log(`[scoring] Scored ${totalScored} total job-candidate pairs`);
  return totalScored;
}
