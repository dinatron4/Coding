import { makeExternalId } from '../services/dedup.js';

const BASE = 'https://api.adzuna.com/v1/api/jobs';

const COUNTRIES = ['us', 'gb', 'de', 'fr', 'nl', 'at', 'be', 'pl', 'es', 'it', 'br'];

export async function fetchAdzuna(keywords = []) {
  const appId  = process.env.ADZUNA_APP_ID;
  const appKey = process.env.ADZUNA_API_KEY;
  if (!appId || !appKey) return [];

  const results = [];
  const searches = keywords.length ? keywords : ['remote'];

  for (const country of COUNTRIES) {
    for (const kw of searches) {
      const params = new URLSearchParams({
        app_id:           appId,
        app_key:          appKey,
        results_per_page: '50',
        what:             kw,
        where:            'remote',
        content_type:     'application/json',
      });
      const url = `${BASE}/${country}/search/1?${params}`;

      try {
        const res = await fetch(url);
        if (!res.ok) continue;
        const { results: jobs } = await res.json();

        for (const j of (jobs ?? [])) {
          results.push({
            external_id: makeExternalId(j.redirect_url),
            title:       j.title,
            company:     j.company?.display_name ?? 'Unknown',
            description: j.description,
            url:         j.redirect_url,
            source:      'adzuna',
            posted_at:   j.created ? new Date(j.created).toISOString() : null,
            is_remote:   true,
            salary_min:  j.salary_min ? Math.round(j.salary_min) : null,
            salary_max:  j.salary_max ? Math.round(j.salary_max) : null,
            currency:    COUNTRY_META[country]?.currency ?? 'USD',
            location:    COUNTRY_META[country]?.location ?? null,
          });
        }
      } catch {
        // skip failed search
      }

      // Small delay to avoid hammering the API across many country+keyword combos
      await new Promise(r => setTimeout(r, 200));
    }
  }

  return dedupByExternalId(results);
}

const COUNTRY_META = {
  us: { currency: 'USD', location: null },
  gb: { currency: 'GBP', location: 'United Kingdom' },
  de: { currency: 'EUR', location: 'Germany' },
  fr: { currency: 'EUR', location: 'France' },
  nl: { currency: 'EUR', location: 'Netherlands' },
  at: { currency: 'EUR', location: 'Austria' },
  be: { currency: 'EUR', location: 'Belgium' },
  pl: { currency: 'PLN', location: 'Poland' },
  es: { currency: 'EUR', location: 'Spain' },
  it: { currency: 'EUR', location: 'Italy' },
  br: { currency: 'BRL', location: 'Brazil' },
};

function dedupByExternalId(jobs) {
  const seen = new Set();
  return jobs.filter(j => {
    if (seen.has(j.external_id)) return false;
    seen.add(j.external_id);
    return true;
  });
}
