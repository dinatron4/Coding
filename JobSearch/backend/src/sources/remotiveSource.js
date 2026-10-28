import { makeExternalId } from '../services/dedup.js';

const REMOTIVE_URL = 'https://remotive.com/api/remote-jobs';

export async function fetchRemotive(keywords = []) {
  const results = [];

  for (const keyword of keywords.length ? keywords : ['']) {
    const url = keyword
      ? `${REMOTIVE_URL}?search=${encodeURIComponent(keyword)}&limit=50`
      : `${REMOTIVE_URL}?limit=50`;

    const res = await fetch(url);
    if (!res.ok) continue;

    const { jobs } = await res.json();
    for (const j of jobs) {
      results.push({
        external_id:    makeExternalId(j.url),
        title:          j.title,
        company:        j.company_name,
        description:    j.description,
        url:            j.url,
        source:         'remotive',
        posted_at:      j.publication_date ? new Date(j.publication_date).toISOString() : null,
        is_remote:      true,
        salary_min:     null,
        salary_max:     null,
        currency:       null,
      });
    }
  }

  return dedupByExternalId(results);
}

function dedupByExternalId(jobs) {
  const seen = new Set();
  return jobs.filter(j => {
    if (seen.has(j.external_id)) return false;
    seen.add(j.external_id);
    return true;
  });
}
