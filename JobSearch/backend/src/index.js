import 'dotenv/config';
import express from 'express';
import cors from 'cors';

import candidatesRouter from './routes/candidates.js';
import jobsRouter from './routes/jobs.js';
import scoresRouter from './routes/scores.js';
import feedbackRouter from './routes/feedback.js';
import coverLettersRouter from './routes/coverLetters.js';
import magicRouter from './routes/magic.js';

import { startScheduler } from './jobs/scheduler.js';
import { runDiscovery } from './jobs/discoveryJob.js';
import { runScoring } from './jobs/scoringJob.js';
import { runDigest } from './jobs/digestJob.js';
import { extractJobData } from './agents/extractionAgent.js';
import supabase from './services/supabase.js';

const app = express();

app.use(cors({ origin: process.env.FRONTEND_URL || 'http://localhost:5173' }));
app.use(express.json());

app.get('/health', (_req, res) => res.json({ ok: true }));

app.use('/api/candidates',    candidatesRouter);
app.use('/api/jobs',          jobsRouter);
app.use('/api/scores',        scoresRouter);
app.use('/api/feedback',      feedbackRouter);
app.use('/api/cover-letters', coverLettersRouter);
app.use('/api/magic',         magicRouter);

// Debug: list available Groq models
app.get('/api/debug/groq-models', async (_req, res) => {
  try {
    const Groq = (await import('groq-sdk')).default;
    const groq = new Groq({ apiKey: process.env.GROQ_API_KEY });
    const models = await groq.models.list();
    res.json(models.data.map(m => m.id).sort());
  } catch (err) {
    res.json({ error: err.message });
  }
});

// Debug: test Groq connection
app.get('/api/debug/groq', async (_req, res) => {
  try {
    const Groq = (await import('groq-sdk')).default;
    const groq = new Groq({ apiKey: process.env.GROQ_API_KEY });
    const response = await groq.chat.completions.create({
      model: 'openai/gpt-oss-120b',
      messages: [{ role: 'user', content: 'Say "ok" and nothing else.' }],
      max_tokens: 10,
    });
    res.json({ ok: true, response: response.choices[0].message.content, key_set: !!process.env.GROQ_API_KEY });
  } catch (err) {
    res.json({ ok: false, error: err.message, key_set: !!process.env.GROQ_API_KEY });
  }
});


// One-off backfill: re-extract location for jobs that have location = null
app.post('/api/run/backfill-location', async (req, res) => {
  const limit = Math.min(Number(req.body?.limit) || 20, 200);

  const { data: jobs, error } = await supabase
    .from('jobs')
    .select('id, description')
    .is('location', null)
    .order('scraped_at', { ascending: false })
    .limit(limit);

  if (error) return res.status(500).json({ error: error.message });
  if (!jobs?.length) return res.json({ ok: true, updated: 0 });

  let updated = 0;
  for (const job of jobs) {
    try {
      const extracted = await extractJobData(job.description);
      if (extracted.location) {
        await supabase.from('jobs').update({ location: extracted.location }).eq('id', job.id);
        updated++;
      }
    } catch { /* skip */ }
    await new Promise(r => setTimeout(r, 2000));
  }
  res.json({ ok: true, updated, total: jobs.length });
});

app.post('/api/run/discovery', async (_req, res) => {
  const count = await runDiscovery();
  res.json({ ok: true, newJobs: count });
});

app.post('/api/run/scoring', async (req, res) => {
  const { candidateId, locationFilter } = req.body || {};
  const count = await runScoring(candidateId || null, locationFilter || null);
  res.json({ ok: true, scored: count });
});

app.post('/api/run/digest', async (_req, res) => {
  await runDigest();
  res.json({ ok: true });
});

app.post('/api/run/all', async (_req, res) => {
  const newJobs = await runDiscovery();
  const scored  = await runScoring();
  await runDigest();
  res.json({ ok: true, newJobs, scored });
});

const PORT = process.env.PORT || 3001;
app.listen(PORT, () => {
  console.log(`Backend running on port ${PORT}`);
  startScheduler();
});
