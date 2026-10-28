import { Router } from 'express';
import supabase from '../services/supabase.js';

const router = Router();

// Top jobs for a candidate (sorted by score)
router.get('/:candidateId', async (req, res) => {
  const { status, min_score = 0, limit = 50, location } = req.query;

  let query = supabase
    .from('candidate_job_scores')
    .select('*, jobs(*)')
    .eq('candidate_id', req.params.candidateId)
    .gte('score', Number(min_score))
    .order('score', { ascending: false })
    .limit(Number(limit));

  if (status) query = query.eq('status', status);
  if (location === 'remote') query = query.eq('jobs.is_remote', true);
  else if (location) query = query.ilike('jobs.location', `%${location}%`);

  const { data, error } = await query;
  if (error) return res.status(500).json({ error: error.message });
  res.json(data);
});

// Update status for a candidate+job
router.patch('/:candidateId/:jobId', async (req, res) => {
  const { status } = req.body;
  const allowed = ['new','emailed','accepted','rejected','applied','interview','offer','closed'];
  if (!allowed.includes(status)) return res.status(400).json({ error: 'invalid status' });

  const { data, error } = await supabase
    .from('candidate_job_scores')
    .update({ status })
    .eq('candidate_id', req.params.candidateId)
    .eq('job_id', req.params.jobId)
    .select()
    .single();
  if (error) return res.status(500).json({ error: error.message });
  res.json(data);
});

export default router;
