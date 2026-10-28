import { useState, useEffect } from 'react';
import { useCandidate } from '../hooks/useCandidate.jsx';
import { fetchScores, patchScore } from '../api.js';

const PIPELINE = ['accepted','applied','interview','offer','closed'];

export default function Applications() {
  const { selected } = useCandidate();
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (!selected) return;
    setLoading(true);
    Promise.all(
      ['accepted','applied','interview','offer'].map(s =>
        fetchScores(selected, { status: s, limit: 50 })
      )
    ).then(results => setItems(results.flat().filter(Array.isArray(results[0]) ? Boolean : Boolean)))
     .finally(() => setLoading(false));
  }, [selected]);

  async function advance(item) {
    const next = PIPELINE[PIPELINE.indexOf(item.status) + 1];
    if (!next) return;
    await patchScore(selected, item.jobs.id, next);
    setItems(prev => prev.map(i => i.id === item.id ? { ...i, status: next } : i));
  }

  const statusColors = {
    accepted: 'badge-green', applied: 'badge-blue',
    interview: 'badge-gold', offer: 'badge-green', closed: 'badge-red',
  };

  if (!selected) return null;

  return (
    <div>
      <h1 style={{ fontSize: '20px', fontWeight: 700, marginBottom: '20px' }}>Applications</h1>

      {loading && <p style={{ color: 'var(--muted)' }}>Loading…</p>}

      {!loading && !items.length && (
        <p style={{ color: 'var(--muted)', textAlign: 'center', marginTop: '40px' }}>
          No applications yet. Accept jobs from the Dashboard to start tracking.
        </p>
      )}

      {items.map(item => {
        const job = item.jobs;
        const nextStatus = PIPELINE[PIPELINE.indexOf(item.status) + 1];
        return (
          <div key={item.id} className="card" style={{ marginBottom: '10px', display: 'flex', alignItems: 'center', gap: '12px' }}>
            <div style={{ flex: 1 }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap' }}>
                <span className={`badge ${statusColors[item.status] || 'badge-gray'}`}>{item.status}</span>
                <a href={job.url} target="_blank" rel="noopener noreferrer"
                   style={{ fontWeight: 600, color: 'var(--text)', fontSize: '14px' }}>
                  {job.title}
                </a>
                <span style={{ color: 'var(--muted)', fontSize: '13px' }}>@ {job.company}</span>
              </div>
            </div>
            {nextStatus && nextStatus !== 'closed' && (
              <button className="btn-ghost" style={{ fontSize: '12px' }} onClick={() => advance(item)}>
                → {nextStatus}
              </button>
            )}
          </div>
        );
      })}
    </div>
  );
}
