export default function ScoreBadge({ score }) {
  const cls = score >= 90 ? 'badge-gold' : score >= 75 ? 'badge-green' : score >= 50 ? 'badge-blue' : 'badge-gray';
  return <span className={`badge ${cls}`}>{score}</span>;
}
