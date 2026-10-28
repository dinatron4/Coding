import { createHash } from 'crypto';

export function makeExternalId(url) {
  return createHash('sha256').update(url).digest('hex').slice(0, 32);
}
