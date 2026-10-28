import { useState } from 'react';
import ScoreBadge from './ScoreBadge.jsx';
import { postFeedback, generateCoverLetter, fetchCoverLetter, patchScore } from '../api.js';

function stripHtml(html) {
  return (html || '')
    .replace(/<[^>]*>/g, ' ')
    .replace(/&nbsp;/gi, ' ')
    .replace(/&amp;/gi, '&')
    .replace(/&lt;/gi, '<')
    .replace(/&gt;/gi, '>')
    .replace(/&[a-z]+;/gi, ' ')
    .replace(/\s+/g, ' ')
    .trim();
}

function splitReasoning(text) {
  if (!text) return { positive: '', gap: '' };
  const match = text.match(
    /^(.*?)[.!?]?\s+(While|However|But|Although|Despite|The lack|Note:|That said,|Unfortunately)(.*)/is
  );
  if (match) {
    return {
      positive: match[1].replace(/\.$/, '').trim(),
      gap: (match[2] + match[3]).trim(),
    };
  }
  return { positive: text, gap: '' };
}

function formatSalary(job) {
  if (!job.salary_min) return null;
  const fmt = n => `$${(n / 1000).toFixed(0)}k`;
  if (job.salary_max) return `${fmt(job.salary_min)}–${fmt(job.salary_max)} ${job.currency || 'USD'}`;
  return `${fmt(job.salary_min)}+ ${job.currency || 'USD'}`;
}

const statusColors = {
  accepted: 'badge-green', rejected: 'badge-red', applied: 'badge-blue',
  emailed: 'badge-gray', new: 'badge-gray',
};

export default function JobCard({ item, candidateId, onStatusChange }) {
  const job = item.jobs;
  const [loading, setLoading] = useState(false);
  const [coverLetter, setCoverLetter] = useState(null);
  const [showCoverLetter, setShowCoverLetter] = useState(false);
  const [expanded, setExpanded] = useState(false);

  async function handleFeedback(type) {
    setLoading(true);
    await postFeedback({ candidate_id: candidateId, job_id: job.id, feedback_type: type });
    onStatusChange(item.id, type === 'accept' ? 'accepted' : 'rejected');
    setLoading(false);
  }

  async function handleMarkApplied() {
    setLoading(true);
    await patchScore(candidateId, job.id, 'applied');
    onStatusChange(item.id, 'applied');
    setLoading(false);
  }

  async function handleCoverLetter() {
    if (coverLetter) { setShowCoverLetter(v => !v); return; }
    setLoading(true);
    let cl = await fetchCoverLetter(candidateId, job.id);
    if (!cl) cl = await generateCoverLetter(candidateId, job.id);
    setCoverLetter(cl);
    setShowCoverLetter(true);
    setLoading(false);
  }

  const salary = formatSalary(job);
  const { positive, gap } = splitReasoning(item.score_reasoning);
  const description = stripHtml(job.description);

  return (
    <div className="card" style={{ marginBottom: '12px' }}>

      {/* ── Collapsed header ── */}
      <div style={{ display: 'flex', alignItems: 'flex-start', gap: '12px' }}>
        <div style={{ flex: 1, minWidth: 0 }}>

          {/* Title + status badge */}
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap' }}>
            <ScoreBadge score={item.score} />
            <a href={job.url} target="_blank" rel="noopener noreferrer"
               style={{ fontWeight: 700, fontSize: '15px', color: 'var(--text)' }}>
              {job.title}
            </a>
            {item.status !== 'new' && (
              <span className={`badge ${statusColors[item.status] || 'badge-gray'}`}>{item.status}</span>
            )}
          </div>

          {/* Company + quick meta */}
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap', marginTop: '5px' }}>
            <span style={{ fontWeight: 600, fontSize: '13px', color: 'var(--text)' }}>{job.company}</span>
            {job.is_remote && <span className="badge badge-blue">Remote</span>}
            {salary && <span style={{ fontSize: '13px', color: 'var(--muted)' }}>{salary}</span>}
            {job.seniority && <span className="badge badge-gray">{job.seniority}</span>}
          </div>

          {/* Reasoning summary */}
          {item.score_reasoning && (
            <p style={{ fontSize: '13px', color: 'var(--muted)', marginTop: '8px', lineHeight: 1.5, fontStyle: 'italic' }}>
              {item.score_reasoning}
            </p>
          )}
        </div>

        <button className="btn-ghost" onClick={() => setExpanded(v => !v)}
          style={{ fontSize: '12px', padding: '4px 10px', flexShrink: 0, marginTop: '2px' }}>
          {expanded ? 'Less' : 'More'}
        </button>
      </div>

      {/* ── Expanded section ── */}
      {expanded && (
        <div style={{ marginTop: '16px', borderTop: '1px solid var(--border)', paddingTop: '16px', display: 'flex', flexDirection: 'column', gap: '14px' }}>

          {/* What aligns */}
          {positive && (
            <div style={{ borderLeft: '3px solid var(--green)', paddingLeft: '12px' }}>
              <div style={{ fontSize: '11px', fontWeight: 700, color: 'var(--green)', textTransform: 'uppercase', letterSpacing: '0.07em', marginBottom: '4px' }}>
                What aligns
              </div>
              <p style={{ fontSize: '13px', color: 'var(--text)', lineHeight: 1.55 }}>{positive}</p>
            </div>
          )}

          {/* Potential gaps */}
          {gap && (
            <div style={{ borderLeft: '3px solid var(--gold)', paddingLeft: '12px' }}>
              <div style={{ fontSize: '11px', fontWeight: 700, color: 'var(--gold)', textTransform: 'uppercase', letterSpacing: '0.07em', marginBottom: '4px' }}>
                Potential gaps
              </div>
              <p style={{ fontSize: '13px', color: 'var(--text)', lineHeight: 1.55 }}>{gap}</p>
            </div>
          )}

          {/* Skills required */}
          {job.skills_required?.length > 0 && (
            <div>
              <div style={{ fontSize: '11px', fontWeight: 700, color: 'var(--muted)', textTransform: 'uppercase', letterSpacing: '0.07em', marginBottom: '6px' }}>
                Skills required
              </div>
              <div style={{ display: 'flex', gap: '4px', flexWrap: 'wrap' }}>
                {job.skills_required.map(s => (
                  <span key={s} className="badge badge-gray">{s}</span>
                ))}
              </div>
            </div>
          )}

          {/* About the role */}
          {description && (
            <div>
              <div style={{ fontSize: '11px', fontWeight: 700, color: 'var(--muted)', textTransform: 'uppercase', letterSpacing: '0.07em', marginBottom: '6px' }}>
                About the role
              </div>
              <p style={{ fontSize: '13px', color: 'var(--muted)', lineHeight: 1.65, maxHeight: '180px', overflow: 'auto' }}>
                {description.length > 900 ? description.slice(0, 900) + '…' : description}
              </p>
            </div>
          )}

          {/* Action bar */}
          <div style={{
            display: 'flex', gap: '8px', flexWrap: 'wrap', alignItems: 'center',
            paddingTop: '12px', borderTop: '1px solid var(--border)',
          }}>
            {(item.status === 'new' || item.status === 'emailed') && (
              <>
                <button className="btn-green" onClick={() => handleFeedback('accept')} disabled={loading}>Accept</button>
                <button className="btn-red"   onClick={() => handleFeedback('reject')} disabled={loading}>Reject</button>
              </>
            )}
            {item.status === 'accepted' && (
              <button className="btn-primary" onClick={handleMarkApplied} disabled={loading}>Mark Applied</button>
            )}
            <button className="btn-ghost" onClick={handleCoverLetter} disabled={loading}>
              {coverLetter ? (showCoverLetter ? 'Hide Letter' : 'Show Letter') : 'Generate Cover Letter'}
            </button>
            <a href={job.url} target="_blank" rel="noopener noreferrer"
               style={{ marginLeft: 'auto', fontSize: '13px', color: 'var(--accent)', fontWeight: 500 }}>
              View posting ↗
            </a>
          </div>

          {/* Cover letter */}
          {showCoverLetter && coverLetter && (
            <div style={{
              background: 'var(--bg)', border: '1px solid var(--border)',
              borderRadius: 'var(--radius)', padding: '16px', fontSize: '13px',
              lineHeight: 1.7, whiteSpace: 'pre-wrap', color: 'var(--text)',
            }}>
              {coverLetter.content}
            </div>
          )}
        </div>
      )}
    </div>
  );
}
