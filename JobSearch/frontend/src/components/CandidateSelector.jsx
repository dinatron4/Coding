export default function CandidateSelector({ candidates, selected, onChange }) {
  if (!candidates.length) return null;
  return (
    <select value={selected || ''} onChange={e => onChange(e.target.value)}
      style={{ width: 'auto', minWidth: '140px' }}>
      {candidates.map(c => (
        <option key={c.id} value={c.id}>{c.name}</option>
      ))}
    </select>
  );
}
