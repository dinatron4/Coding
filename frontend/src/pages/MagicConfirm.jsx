import { useSearchParams } from 'react-router-dom';

export default function MagicConfirm() {
  const [params] = useSearchParams();
  const action = params.get('action');

  return (
    <div style={{
      display: 'flex', flexDirection: 'column', alignItems: 'center',
      justifyContent: 'center', minHeight: '100vh', gap: '16px',
      background: 'var(--bg)', color: 'var(--text)',
    }}>
      <div style={{ fontSize: '48px' }}>{action === 'accept' ? '✅' : '❌'}</div>
      <h1 style={{ fontSize: '22px', fontWeight: 700 }}>
        {action === 'accept' ? 'Job accepted!' : 'Job rejected.'}
      </h1>
      <p style={{ color: 'var(--muted)' }}>
        {action === 'accept'
          ? 'This job has been added to your accepted list. You can view it on the Dashboard.'
          : 'Got it. This job won\'t appear in future emails.'}
      </p>
      <a href="/dashboard" style={{
        marginTop: '8px', padding: '10px 20px', background: 'var(--accent)',
        color: '#fff', borderRadius: 'var(--radius)', fontSize: '14px',
      }}>
        Go to Dashboard →
      </a>
    </div>
  );
}
