import { useState, useEffect } from 'react';
import { useCandidate } from '../hooks/useCandidate.jsx';
import { fetchProfile, updateProfile, createCandidate } from '../api.js';

export default function Profile() {
  const { candidates, selected, setSelected, refresh } = useCandidate();
  const [form, setForm] = useState({
    cv_text: '', target_roles: '', skills: '',
    salary_min: '', salary_max: '', salary_currency: 'USD',
    location_preference: 'remote_only', years_experience: '',
    excluded_companies: '', extra_instructions: '',
  });
  const [newName, setNewName] = useState('');
  const [newEmail, setNewEmail] = useState('');
  const [saving, setSaving] = useState(false);
  const [saved, setSaved] = useState(false);
  const [creating, setCreating] = useState(false);

  const selectedCandidate = candidates.find(c => c.id === selected);

  useEffect(() => {
    if (!selected) return;
    fetchProfile(selected).then(data => {
      const p = data.candidate_profiles || {};
      setForm({
        cv_text:              p.cv_text || '',
        target_roles:         (p.target_roles || []).join(', '),
        skills:               (p.skills || []).join(', '),
        salary_min:           p.salary_min || '',
        salary_max:           p.salary_max || '',
        salary_currency:      p.salary_currency || 'USD',
        location_preference:  p.location_preference || 'remote_only',
        years_experience:     p.years_experience || '',
        excluded_companies:   (p.excluded_companies || []).join(', '),
        extra_instructions:   p.extra_instructions || '',
      });
    });
  }, [selected]);

  async function handleSave(e) {
    e.preventDefault();
    setSaving(true);
    await updateProfile(selected, {
      cv_text:             form.cv_text,
      target_roles:        form.target_roles.split(',').map(s => s.trim()).filter(Boolean),
      skills:              form.skills.split(',').map(s => s.trim()).filter(Boolean),
      salary_min:          form.salary_min ? Number(form.salary_min) : null,
      salary_max:          form.salary_max ? Number(form.salary_max) : null,
      salary_currency:     form.salary_currency,
      location_preference: form.location_preference,
      years_experience:    form.years_experience ? Number(form.years_experience) : null,
      excluded_companies:  form.excluded_companies.split(',').map(s => s.trim()).filter(Boolean),
      extra_instructions:  form.extra_instructions,
    });
    setSaving(false);
    setSaved(true);
    setTimeout(() => setSaved(false), 2000);
  }

  async function handleCreate(e) {
    e.preventDefault();
    setCreating(true);
    const data = await createCandidate({ name: newName, email: newEmail });
    setCreating(false);
    setNewName(''); setNewEmail('');
    if (data.id) await refresh(data.id);
  }

  const field = (label, key, type = 'text', hint) => (
    <div style={{ marginBottom: '16px' }}>
      <label style={{ display: 'block', fontSize: '13px', color: 'var(--muted)', marginBottom: '4px' }}>
        {label}
      </label>
      <input type={type} value={form[key]} onChange={e => setForm(p => ({ ...p, [key]: e.target.value }))} />
      {hint && <small style={{ color: 'var(--muted)', fontSize: '12px' }}>{hint}</small>}
    </div>
  );

  return (
    <div>
      <h1 style={{ fontSize: '20px', fontWeight: 700, marginBottom: '20px' }}>Profile</h1>

      {/* Add candidate */}
      <div className="card" style={{ marginBottom: '24px' }}>
        <h2 style={{ fontSize: '15px', fontWeight: 600, marginBottom: '12px' }}>Add Candidate</h2>
        <form onSubmit={handleCreate} style={{ display: 'flex', gap: '8px', flexWrap: 'wrap' }}>
          <input placeholder="Name" value={newName} onChange={e => setNewName(e.target.value)} style={{ flex: 1, minWidth: '140px' }} required />
          <input placeholder="Email" type="email" value={newEmail} onChange={e => setNewEmail(e.target.value)} style={{ flex: 1, minWidth: '200px' }} required />
          <button type="submit" className="btn-primary" disabled={creating}>{creating ? 'Creating…' : 'Add'}</button>
        </form>
      </div>

      {selected && (
        <form onSubmit={handleSave}>
          <div style={{
            display: 'flex', alignItems: 'center', justifyContent: 'space-between',
            marginBottom: '20px', padding: '10px 14px',
            background: 'var(--surface)', border: '1px solid var(--border)', borderRadius: 'var(--radius)',
          }}>
            <span style={{ fontSize: '14px', color: 'var(--muted)' }}>
              Editing profile for <strong style={{ color: 'var(--text)' }}>{selectedCandidate?.name}</strong>
            </span>
            <span style={{ fontSize: '12px', color: 'var(--muted)' }}>{selectedCandidate?.email}</span>
          </div>

          <div style={{ marginBottom: '16px' }}>
            <label style={{ display: 'block', fontSize: '13px', color: 'var(--muted)', marginBottom: '4px' }}>CV / Resume</label>
            <textarea rows={8} value={form.cv_text}
              onChange={e => setForm(p => ({ ...p, cv_text: e.target.value }))}
              placeholder="Paste your CV text here…" />
          </div>

          {field('Target Roles', 'target_roles', 'text', 'Comma-separated, e.g. "Senior Data Analyst, BI Engineer"')}
          {field('Skills', 'skills', 'text', 'Comma-separated, e.g. "Python, SQL, dbt"')}

          <div style={{ display: 'flex', gap: '12px' }}>
            <div style={{ flex: 1 }}>{field('Salary Min (USD)', 'salary_min', 'number')}</div>
            <div style={{ flex: 1 }}>{field('Salary Max (USD)', 'salary_max', 'number')}</div>
          </div>

          {field('Years of Experience', 'years_experience', 'number')}

          <div style={{ marginBottom: '16px' }}>
            <label style={{ display: 'block', fontSize: '13px', color: 'var(--muted)', marginBottom: '4px' }}>Location Preference</label>
            <select value={form.location_preference} onChange={e => setForm(p => ({ ...p, location_preference: e.target.value }))}>
              <option value="remote_only">Remote only</option>
              <option value="remote_eu">Remote (EU timezone)</option>
              <option value="hybrid">Hybrid</option>
              <option value="any">Any</option>
            </select>
          </div>

          {field('Excluded Companies', 'excluded_companies', 'text', 'Companies to never show, comma-separated')}

          <div style={{ marginBottom: '20px' }}>
            <label style={{ display: 'block', fontSize: '13px', color: 'var(--muted)', marginBottom: '4px' }}>Extra Instructions for AI</label>
            <textarea rows={3} value={form.extra_instructions}
              onChange={e => setForm(p => ({ ...p, extra_instructions: e.target.value }))}
              placeholder="e.g. Prefer product companies over agencies. No startups under 50 people." />
          </div>

          <button type="submit" className="btn-primary" disabled={saving}>
            {saving ? 'Saving…' : saved ? 'Saved ✓' : 'Save Profile'}
          </button>
        </form>
      )}
    </div>
  );
}
