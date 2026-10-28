import supabase from '../services/supabase.js';
import { fetchRemotive } from '../sources/remotiveSource.js';
import { fetchWWR } from '../sources/wwrSource.js';
import { fetchAdzuna } from '../sources/adzunaSource.js';
import { fetchHimalayas } from '../sources/himalayasSource.js';
import { extractJobData } from '../agents/extractionAgent.js';

export async function runDiscovery() {
  console.log('[discovery] Starting job discovery...');

  // Build keyword list from all active candidate target roles
  const { data: profiles } = await supabase
    .from('candidate_profiles')
    .select('target_roles')
    .not('target_roles', 'eq', '{}');

  const keywords = [...new Set(
    (profiles ?? []).flatMap(p => p.target_roles ?? [])
  )];

  const [remotive, wwr, adzuna, himalayas] = await Promise.all([
    fetchRemotive(keywords).catch(() => []),
    fetchWWR().catch(() => []),
    fetchAdzuna(keywords).catch(() => []),
    fetchHimalayas(keywords).catch(() => []),
  ]);

  const all = [...remotive, ...wwr, ...adzuna, ...himalayas];
  console.log(`[discovery] Fetched ${all.length} jobs from sources`);

  // Filter out already-known external_ids
  const externalIds = all.map(j => j.external_id);
  const { data: existing } = await supabase
    .from('jobs')
    .select('external_id')
    .in('external_id', externalIds);

  const existingSet = new Set((existing ?? []).map(j => j.external_id));
  const newJobs = all.filter(j => !existingSet.has(j.external_id));

  console.log(`[discovery] ${newJobs.length} new jobs to insert`);
  if (!newJobs.length) return 0;

  // Extract structured data for each new job (in small batches to avoid rate limits)
  const enriched = [];
  for (const job of newJobs) {
    try {
      const extracted = await extractJobData(job.description);
      enriched.push({
        ...job,
        seniority:       extracted.seniority       ?? null,
        skills_required: extracted.skills_required ?? [],
        is_remote:       extracted.is_remote       ?? job.is_remote ?? true,
        salary_min:      extracted.salary_min      ?? job.salary_min ?? null,
        salary_max:      extracted.salary_max      ?? job.salary_max ?? null,
        location:        extracted.location        ?? job.location   ?? null,
      });
    } catch {
      enriched.push(job);
    }
  }

  // Insert in chunks of 50
  for (let i = 0; i < enriched.length; i += 50) {
    const chunk = enriched.slice(i, i + 50);
    const { error } = await supabase.from('jobs').insert(chunk);
    if (error) console.error('[discovery] Insert error:', error.message);
  }

  console.log(`[discovery] Inserted ${enriched.length} new jobs`);
  return enriched.length;
}
