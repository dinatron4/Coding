import { Router } from 'express';
import supabase from '../services/supabase.js';

const router = Router();

// List all candidates
router.get('/', async (_req, res) => {
  const { data, error } = await supabase
    .from('candidates')
    .select('*, candidate_profiles(*)')
    .order('created_at');
  if (error) return res.status(500).json({ error: error.message });
  res.json(data);
});

// Get one candidate
router.get('/:id', async (req, res) => {
  const { data, error } = await supabase
    .from('candidates')
    .select('*, candidate_profiles(*)')
    .eq('id', req.params.id)
    .single();
  if (error) return res.status(404).json({ error: error.message });
  res.json(data);
});

// Create candidate + profile
router.post('/', async (req, res) => {
  const { name, email, profile = {} } = req.body;
  if (!name || !email) return res.status(400).json({ error: 'name and email required' });

  const { data: candidate, error: ce } = await supabase
    .from('candidates')
    .insert({ name, email })
    .select()
    .single();
  if (ce) return res.status(500).json({ error: ce.message });

  const { error: pe } = await supabase
    .from('candidate_profiles')
    .insert({ candidate_id: candidate.id, ...profile });
  if (pe) return res.status(500).json({ error: pe.message });

  res.status(201).json(candidate);
});

// Update profile
router.put('/:id/profile', async (req, res) => {
  const { data, error } = await supabase
    .from('candidate_profiles')
    .update({ ...req.body, updated_at: new Date().toISOString() })
    .eq('candidate_id', req.params.id)
    .select()
    .single();
  if (error) return res.status(500).json({ error: error.message });
  res.json(data);
});

export default router;
