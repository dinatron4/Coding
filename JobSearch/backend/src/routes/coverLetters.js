import { Router } from 'express';
import supabase from '../services/supabase.js';
import { generateCoverLetter } from '../agents/coverLetterAgent.js';

const router = Router();

// Get cover letter for a candidate+job
router.get('/:candidateId/:jobId', async (req, res) => {
  const { data, error } = await supabase
    .from('cover_letters')
    .select('*')
    .eq('candidate_id', req.params.candidateId)
    .eq('job_id', req.params.jobId)
    .order('version', { ascending: false })
    .limit(1)
    .single();
  if (error) return res.status(404).json({ error: 'No cover letter found' });
  res.json(data);
});

// Generate (or regenerate) a cover letter
router.post('/:candidateId/:jobId', async (req, res) => {
  const { candidateId, jobId } = req.params;

  const [{ data: profile }, { data: job }] = await Promise.all([
    supabase.from('candidate_profiles').select('*').eq('candidate_id', candidateId).single(),
    supabase.from('jobs').select('*').eq('id', jobId).single(),
  ]);

  if (!profile || !job) return res.status(404).json({ error: 'Profile or job not found' });

  const content = await generateCoverLetter({ profile, job });

  // Get current max version
  const { data: existing } = await supabase
    .from('cover_letters')
    .select('version')
    .eq('candidate_id', candidateId)
    .eq('job_id', jobId)
    .order('version', { ascending: false })
    .limit(1)
    .single();

  const version = existing ? existing.version + 1 : 1;

  const { data, error } = await supabase
    .from('cover_letters')
    .insert({ candidate_id: candidateId, job_id: jobId, content, version })
    .select()
    .single();
  if (error) return res.status(500).json({ error: error.message });

  res.status(201).json(data);
});

export default router;
