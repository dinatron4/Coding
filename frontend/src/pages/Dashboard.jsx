import { useState, useEffect, useRef } from 'react';
import { useCandidate } from '../hooks/useCandidate.jsx';
import { fetchScores } from '../api.js';
import JobCard from '../components/JobCard.jsx';

const TABS = ['new', 'emailed', 'accepted'];

const EU_LOCATIONS = new Set([
  'austria', 'belgium', 'bulgaria', 'croatia', 'czech republic',
  'denmark', 'estonia', 'finland', 'france', 'germany', 'greece', 'hungary',
  'ireland', 'italy', 'latvia', 'lithuania', 'luxembourg', 'malta',
  'netherlands', 'poland', 'portugal', 'romania', 'slovakia', 'slovenia',
  'spain', 'sweden', 'norway', 'switzerland', 'united kingdom', 'uk',
  'europe', 'eu', 'european union', 'emea',
]);

async function triggerDiscovery() {
  const res = await fetch('/api/run/discovery', { method: 'POST' });
  return res.json();
}

async function triggerScoring(candidateId = null, locationFilter = null) {
  const body = {};
  if (candidateId) body.candidateId = candidateId;
  if (locationFilter) body.locationFilter = locationFilter;
  const res = await fetch('/api/run/scoring', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });
  return res.json();
}

function bucketOf(job) {
  if (job.is_remote) return 'Remote';
  const loc = (job.location || '').toLowerCase();
  if (EU_LOCATIONS.has(loc) || loc.includes('europe')) return 'EU';
  return job.location || 'Other';
}

function LocationPicker({ forAll, onConfirm, onCancel }) {
  const [selected, setSelected] = useState('remote_only');
  const [country, setCountry] = useState('');

  function confirm() {
    const filter = selected === 'country' ? (country.trim() || null) : selected;
    onConfirm(filter);
  }

  const optBtn = (value, label) => (
    <button
      key={value}
      onClick={() => setSelected(value)}
      style={{
        padding: '8px 14px', borderRadius: 'var(--radius)', fontSize: '13px',
        fontWeight: 500, cursor: 'pointer', textAlign: 'left',
        background: selected === value ? 'var(--accent)' : 'transparent',
        border: '1px solid ' + (selected === value ? 'var(--accent)' : 'var(--border)'),
        color: selected === value ? '#fff' : 'var(--muted)',
      }}
    >{label}</button>
  );

  return (
    <div style={{
      position: 'absolute', top: '100%', right: 0, marginTop: '6px', zIndex: 20,
      background: 'var(--surface)', border: '1px solid var(--border)',
      borderRadius: 'var(--radius)', padding: '14px', minWidth: '230px',
      boxShadow: '0 4px 20px rgba(0,0,0,0.5)',
    }}>
      <div style={{ fontSize: '11px', fontWeight: 700, color: 'var(--muted)', textTransform: 'uppercase', letterSpacing: '0.07em', marginBottom: '10px' }}>
        {forAll ? 'Run for all candidates' : 'Location filter'}
      </div>
      <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
        {optBtn('remote_only', 'Remote only')}
        {optBtn('eu', 'Europe / EU')}
        {optBtn('country', 'Country…')}
      </div>
      {selected === 'country' && (
        <input
          autoFocus
          placeholder="e.g. Germany, Poland…"
          value={country}
          onChange={e => setCountry(e.target.value)}
          onKeyDown={e => e.key === 'Enter' && confirm()}
          style={{ marginTop: '8px' }}
        />
      )}
      <div style={{ display: 'flex', gap: '6px', marginTop: '12px' }}>
        <button className="btn-primary" onClick={confirm} style={{ flex: 1 }}>Start</button>
        <button className="btn-ghost" onClick={onCancel}>Cancel</button>
      </div>
    </div>
  );
}

function SplitButton({ onRequestRun, onRequestRunAll, running }) {
  const [pickerMode, setPickerMode] = useState(null); // null | 'current' | 'all'
  const ref = useRef(null);

  useEffect(() => {
    function close(e) {
      if (pickerMode && ref.current && !ref.current.contains(e.target)) setPickerMode(null);
    }
    document.addEventListener('mousedown', close);
    return () => document.removeEventListener('mousedown', close);
  }, [pickerMode]);

  return (
    <div ref={ref} style={{ position: 'relative', display: 'flex' }}>
      <button
        className="btn-primary"
        onClick={() => setPickerMode(pickerMode === 'current' ? null : 'current')}
        disabled={running}
        style={{ borderRadius: 'var(--radius) 0 0 var(--radius)', borderRight: '1px solid rgba(255,255,255,0.2)' }}
      >
        {running ? 'Running…' : 'Run'}
      </button>
      <button
        className="btn-primary"
        onClick={() => setPickerMode(pickerMode === 'all' ? null : 'all')}
        disabled={running}
        style={{ borderRadius: '0 var(--radius) var(--radius) 0', padding: '8px 10px' }}
      >
        ▾
      </button>

      {pickerMode && (
        <LocationPicker
          forAll={pickerMode === 'all'}
          onConfirm={filter => {
            const mode = pickerMode;
            setPickerMode(null);
            if (mode === 'all') onRequestRunAll(filter);
            else onRequestRun(filter);
          }}
          onCancel={() => setPickerMode(null)}
        />
      )}
    </div>
  );
}

export default function Dashboard() {
  const { selected } = useCandidate();
  const [tab, setTab] = useState('new');
  const [jobs, setJobs] = useState([]);
  const [loading, setLoading] = useState(false);
  const [running, setRunning] = useState(false);
  const [discovering, setDiscovering] = useState(false);
  const [runResult, setRunResult] = useState(null);

  function loadJobs() {
    if (!selected) return;
    setLoading(true);
    fetchScores(selected, { status: tab, min_score: tab === 'new' ? 50 : 0, limit: 50 })
      .then(data => setJobs(Array.isArray(data) ? data : []))
      .finally(() => setLoading(false));
  }

  useEffect(() => { loadJobs(); }, [selected, tab]);

  function handleStatusChange(scoreId, newStatus) {
    setJobs(prev => prev.map(j => j.id === scoreId ? { ...j, status: newStatus } : j));
  }

  async function handleDiscover() {
    setDiscovering(true);
    setRunResult(null);
    const result = await triggerDiscovery();
    setDiscovering(false);
    setRunResult({ type: 'discover', count: result.newJobs ?? 0 });
    loadJobs();
  }

  async function handleRun(candidateId, locationFilter) {
    setRunning(true);
    setRunResult(null);
    const result = await triggerScoring(candidateId, locationFilter);
    setRunning(false);
    setRunResult({ type: 'score', count: result.scored ?? 0 });
    loadJobs();
  }

  // Group jobs into location columns
  const columns = {};
  for (const item of jobs) {
    const bucket = bucketOf(item.jobs);
    if (!columns[bucket]) columns[bucket] = [];
    columns[bucket].push(item);
  }

  // Remote first, EU second, then alphabetical, "Other" last
  const columnOrder = Object.keys(columns).sort((a, b) => {
    if (a === 'Remote') return -1; if (b === 'Remote') return 1;
    if (a === 'EU')     return -1; if (b === 'EU')     return 1;
    if (a === 'Other')  return  1; if (b === 'Other')  return -1;
    return a.localeCompare(b);
  });

  const tabStyle = active => ({
    padding: '6px 16px', borderRadius: 'var(--radius)', fontSize: '14px', fontWeight: 500,
    background: active ? 'var(--accent)' : 'transparent',
    border: '1px solid ' + (active ? 'var(--accent)' : 'var(--border)'),
    color: active ? '#fff' : 'var(--muted)', cursor: 'pointer',
  });

  if (!selected) return (
    <div style={{ textAlign: 'center', marginTop: '80px', color: 'var(--muted)' }}>
      No candidates yet. Go to Profile to create one.
    </div>
  );

  return (
    <div>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          <h1 style={{ fontSize: '20px', fontWeight: 700 }}>Opportunities</h1>
          {runResult !== null && (
            <span style={{ fontSize: '13px', color: 'var(--green)' }}>
              {runResult.type === 'discover'
                ? `✓ ${runResult.count} new jobs found`
                : `✓ ${runResult.count} jobs scored`}
            </span>
          )}
        </div>
        <div style={{ display: 'flex', gap: '8px', alignItems: 'center' }}>
          {TABS.map(t => (
            <button key={t} style={tabStyle(tab === t)} onClick={() => setTab(t)}>
              {t.charAt(0).toUpperCase() + t.slice(1)}
            </button>
          ))}
          <button
            className="btn-ghost"
            onClick={handleDiscover}
            disabled={discovering || running}
            style={{ fontSize: '14px' }}
          >
            {discovering ? 'Discovering…' : 'Discover'}
          </button>
          <SplitButton
            running={running}
            onRequestRun={filter => handleRun(selected, filter)}
            onRequestRunAll={filter => handleRun(null, filter)}
          />
        </div>
      </div>

      {loading     && <p style={{ color: 'var(--muted)' }}>Loading…</p>}
      {discovering && <p style={{ color: 'var(--muted)' }}>Fetching jobs from sources, this may take a moment…</p>}
      {running     && <p style={{ color: 'var(--muted)' }}>Scoring jobs, this may take a minute…</p>}

      {!loading && !running && !jobs.length && (
        <p style={{ color: 'var(--muted)', marginTop: '40px', textAlign: 'center' }}>
          No {tab} jobs yet. Click <strong>Run</strong> to score jobs for this candidate.
        </p>
      )}

      {!loading && !running && columnOrder.length > 0 && (
        <div style={{
          display: 'grid',
          gridTemplateColumns: `repeat(${Math.min(columnOrder.length, 3)}, minmax(0, 1fr))`,
          gap: '24px',
          alignItems: 'start',
        }}>
          {columnOrder.map(bucket => (
            <div key={bucket}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '12px' }}>
                <h2 style={{ fontSize: '14px', fontWeight: 700, color: 'var(--text)' }}>{bucket}</h2>
                <span className="badge badge-gray">{columns[bucket].length}</span>
              </div>
              {columns[bucket].map(item => (
                <JobCard key={item.id} item={item} candidateId={selected} onStatusChange={handleStatusChange} />
              ))}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
