import { Outlet, NavLink } from 'react-router-dom';
import { CandidateProvider, useCandidate } from '../hooks/useCandidate.jsx';
import CandidateSelector from './CandidateSelector.jsx';

function Nav() {
  const { candidates, selected, setSelected } = useCandidate();
  const navStyle = ({ isActive }) => ({
    color: isActive ? 'var(--accent)' : 'var(--muted)',
    fontWeight: isActive ? '600' : '400',
    fontSize: '14px',
    textDecoration: 'none',
  });

  return (
    <nav style={{
      display: 'flex', alignItems: 'center', gap: '24px',
      padding: '12px 24px', borderBottom: '1px solid var(--border)',
      background: 'var(--surface)',
    }}>
      <span style={{ fontWeight: 700, fontSize: '15px', color: 'var(--text)' }}>
        Remote Jobs
      </span>
      <NavLink to="/dashboard"    style={navStyle}>Dashboard</NavLink>
      <NavLink to="/applications" style={navStyle}>Applications</NavLink>
      <NavLink to="/profile"      style={navStyle}>Profile</NavLink>
      <div style={{ marginLeft: 'auto' }}>
        <CandidateSelector candidates={candidates} selected={selected} onChange={setSelected} />
      </div>
    </nav>
  );
}

export default function Layout() {
  return (
    <CandidateProvider>
      <div style={{ minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
        <Nav />
        <main style={{ flex: 1, padding: '24px', maxWidth: '900px', margin: '0 auto', width: '100%' }}>
          <Outlet />
        </main>
      </div>
    </CandidateProvider>
  );
}
