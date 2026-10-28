import { parseString } from 'xml2js';
import { promisify } from 'util';
import { makeExternalId } from '../services/dedup.js';

const parseXml = promisify(parseString);
const WWR_RSS_URL = 'https://weworkremotely.com/remote-jobs.rss';

export async function fetchWWR() {
  const res = await fetch(WWR_RSS_URL);
  if (!res.ok) return [];

  const xml = await res.text();
  const parsed = await parseXml(xml);

  const items = parsed?.rss?.channel?.[0]?.item ?? [];
  return items.map(item => {
    const url    = item.link?.[0] ?? '';
    const title  = item.title?.[0] ?? '';
    const pubDate = item.pubDate?.[0];

    // WWR title format: "Company: Job Title"
    const colonIdx = title.indexOf(':');
    const company = colonIdx > -1 ? title.slice(0, colonIdx).trim() : 'Unknown';
    const jobTitle = colonIdx > -1 ? title.slice(colonIdx + 1).trim() : title;

    return {
      external_id: makeExternalId(url),
      title:       jobTitle,
      company,
      description: item['content:encoded']?.[0] ?? item.description?.[0] ?? '',
      url,
      source:      'wwr',
      posted_at:   pubDate ? new Date(pubDate).toISOString() : null,
      is_remote:   true,
      salary_min:  null,
      salary_max:  null,
      currency:    null,
    };
  });
}
