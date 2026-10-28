import { useState, useEffect, createContext, useContext } from 'react';
import { fetchCandidates } from '../api.js';

const CandidateContext = createContext(null);

export function CandidateProvider({ children }) {
  const [candidates, setCandidates] = useState([]);
  const [selected, setSelected] = useState(null);

  async function refresh(selectId = null) {
    const data = await fetchCandidates();
    if (!Array.isArray(data)) return;
    setCandidates(data);
    if (selectId) {
      setSelected(selectId);
    } else if (!selected && data.length) {
      setSelected(data[0].id);
    }
  }

  useEffect(() => { refresh(); }, []);

  return (
    <CandidateContext.Provider value={{ candidates, selected, setSelected, refresh }}>
      {children}
    </CandidateContext.Provider>
  );
}

export function useCandidate() {
  return useContext(CandidateContext);
}
