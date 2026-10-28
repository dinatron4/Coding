const API = '/api';

export async function fetchCandidates() {
  const r = await fetch(`${API}/candidates`);
  return r.json();
}

export async function fetchScores(candidateId, params = {}) {
  const q = new URLSearchParams(params).toString();
  const r = await fetch(`${API}/scores/${candidateId}?${q}`);
  return r.json();
}

export async function patchScore(candidateId, jobId, status) {
  const r = await fetch(`${API}/scores/${candidateId}/${jobId}`, {
    method: 'PATCH',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ status }),
  });
  return r.json();
}

export async function postFeedback(payload) {
  const r = await fetch(`${API}/feedback`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  });
  return r.json();
}

export async function fetchProfile(candidateId) {
  const r = await fetch(`${API}/candidates/${candidateId}`);
  return r.json();
}

export async function updateProfile(candidateId, profile) {
  const r = await fetch(`${API}/candidates/${candidateId}/profile`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(profile),
  });
  return r.json();
}

export async function createCandidate(payload) {
  const r = await fetch(`${API}/candidates`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  });
  return r.json();
}

export async function fetchCoverLetter(candidateId, jobId) {
  const r = await fetch(`${API}/cover-letters/${candidateId}/${jobId}`);
  if (!r.ok) return null;
  return r.json();
}

export async function generateCoverLetter(candidateId, jobId) {
  const r = await fetch(`${API}/cover-letters/${candidateId}/${jobId}`, { method: 'POST' });
  return r.json();
}
