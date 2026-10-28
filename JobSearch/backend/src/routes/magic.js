import { Router } from 'express';
import supabase from '../services/supabase.js';

const router = Router();

// Magic link handler — email accept/reject without login
router.get('/:token', async (req, res) => {
  const { data: token, error } = await supabase
    .from('magic_tokens')
    .select('*')
    .eq('token', req.params.token)
    .single();

  if (error || !token) return res.status(404).send('Link not found.');
  if (token.used)      return res.status(410).send('This link has already been used.');
  if (new Date(token.expires_at) < new Date()) return res.status(410).send('This link has expired.');

  // Mark token used
  await supabase.from('magic_tokens').update({ used: true }).eq('id', token.id);

  // Record feedback
  const feedback_type = token.action;
  await supabase.from('feedback').insert({
    candidate_id: token.candidate_id,
    job_id:       token.job_id,
    feedback_type,
  });

  // Update score status
  const status = feedback_type === 'accept' ? 'accepted' : 'rejected';
  await supabase
    .from('candidate_job_scores')
    .update({ status })
    .eq('candidate_id', token.candidate_id)
    .eq('job_id', token.job_id);

  const frontendUrl = process.env.FRONTEND_URL || 'http://localhost:5173';
  res.redirect(`${frontendUrl}/magic-confirm?action=${feedback_type}`);
});

export default router;
