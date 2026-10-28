import { Router } from 'express';
import supabase from '../services/supabase.js';

const router = Router();

// Submit feedback for a job
router.post('/', async (req, res) => {
  const { candidate_id, job_id, feedback_type, reject_reason, notes } = req.body;
  if (!candidate_id || !job_id || !feedback_type) {
    return res.status(400).json({ error: 'candidate_id, job_id, feedback_type required' });
  }

  const { data, error } = await supabase
    .from('feedback')
    .insert({ candidate_id, job_id, feedback_type, reject_reason, notes })
    .select()
    .single();
  if (error) return res.status(500).json({ error: error.message });

  // Also update the score status to match the feedback
  const status = feedback_type === 'accept' ? 'accepted' : 'rejected';
  await supabase
    .from('candidate_job_scores')
    .update({ status })
    .eq('candidate_id', candidate_id)
    .eq('job_id', job_id);

  res.status(201).json(data);
});

// Get feedback history for a candidate
router.get('/:candidateId', async (req, res) => {
  const { data, error } = await supabase
    .from('feedback')
    .select('*, jobs(title, company)')
    .eq('candidate_id', req.params.candidateId)
    .order('created_at', { ascending: false });
  if (error) return res.status(500).json({ error: error.message });
  res.json(data);
});

export default router;
