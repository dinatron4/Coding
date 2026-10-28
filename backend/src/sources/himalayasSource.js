import { makeExternalId } from '../services/dedup.js';

const BASE = 'https://himalayas.app/jobs/api/search';

export async function fetchHimalayas(keywords = []) {
  const apiKey = process.env.HIMALAYAS_API_KEY; // optional — works without it
  const headers = apiKey ? { Authorization: `Bearer ${apiKey}` } : {};

  const results = [];
  const searches = keywords.length ? keywords : [''];

  for (const kw of searches) {
    let page = 1;
    const maxPages = 2; // 20 results per page → up to 40 per keyword

    while (page <= maxPages) {
      const params = new URLSearchParams({ page: String(page), worldwide: 'true' });
      if (kw) params.set('q', kw);

      try {
        const res = await fetch(`${BASE}?${params}`, { headers });
        if (!res.ok) break;

        const data = await res.json();
        const jobs = data.jobs ?? [];
        if (!jobs.length) break;

        for (const j of jobs) {
          const url = j.applicationLink ?? j.url ?? '';
          if (!url) continue;

          results.push({
            external_id: makeExternalId(url),
            title:       j.title ?? '',
            company:     j.companyName ?? j.company?.name ?? 'Unknown',
            description: j.description ?? j.excerpt ?? '',
            url,
            source:      'himalayas',
            posted_at:   j.publishedAt ? new Date(j.publishedAt).toISOString() : null,
            is_remote:   true,
            salary_min:  j.salaryMin ?? null,
            salary_max:  j.salaryMax ?? null,
            currency:    j.salaryCurrency ?? null,
          });
        }

        if (jobs.length < 20) break; // last page
        page++;
      } catch {
        break;
      }

      await new Promise(r => setTimeout(r, 300));
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
