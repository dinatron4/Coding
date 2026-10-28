import { Router } from 'express';
import supabase from '../services/supabase.js';

const router = Router();

// List jobs (with optional search/filter)
router.get('/', async (req, res) => {
  const { source, is_remote, search, limit = 50, offset = 0 } = req.query;

  let query = supabase
    .from('jobs')
    .select('*')
    .eq('is_active', true)
    .order('posted_at', { ascending: false })
    .range(Number(offset), Number(offset) + Number(limit) - 1);

  if (source)    query = query.eq('source', source);
  if (is_remote) query = query.eq('is_remote', is_remote === 'true');
  if (search)    query = query.ilike('title', `%${search}%`);

  const { data, error } = await query;
  if (error) return res.status(500).json({ error: error.message });
  res.json(data);
});

// Get single job
router.get('/:id', async (req, res) => {
  const { data, error } = await supabase
    .from('jobs')
    .select('*')
    .eq('id', req.params.id)
    .single();
  if (error) return res.status(404).json({ error: error.message });
  res.json(data);
});

export default router;
