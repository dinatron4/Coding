import cron from 'node-cron';
import { runDiscovery } from './discoveryJob.js';
import { runScoring } from './scoringJob.js';
import { runDigest } from './digestJob.js';
import { runFeedbackLearner } from '../agents/feedbackLearner.js';

export function startScheduler() {
  // Discovery: every 4 hours
  cron.schedule('0 */4 * * *', async () => {
    console.log('[scheduler] Running discovery job');
    await runDiscovery();
  });

  // Scoring: every 4 hours, 5 minutes after discovery
  cron.schedule('5 */4 * * *', async () => {
    console.log('[scheduler] Running scoring job');
    await runScoring();
  });

  // Digest: daily at 08:00
  cron.schedule('0 8 * * *', async () => {
    console.log('[scheduler] Running digest job');
    await runDigest();
  });

  // Feedback learner: weekly on Sunday 06:00
  cron.schedule('0 6 * * 0', async () => {
    console.log('[scheduler] Running feedback learner');
    await runFeedbackLearner();
  });

  console.log('[scheduler] All cron jobs registered');
}

// Allow manual trigger via API for testing
export async function runAll() {
  await runDiscovery();
  await runScoring();
  await runDigest();
}
