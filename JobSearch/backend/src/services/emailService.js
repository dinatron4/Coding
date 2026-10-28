import { Resend } from 'resend';
import supabase from './supabase.js';

const resend = new Resend(process.env.RESEND_API_KEY);
const FROM   = process.env.EMAIL_FROM || 'jobs@yourdomain.com';
const BACKEND_URL = process.env.BACKEND_URL || 'http://localhost:3001';
const FRONTEND_URL = process.env.FRONTEND_URL || 'http://localhost:5173';

// Creates a magic-link token in DB and returns the URL
async function createMagicLink(candidate_id, job_id, action) {
  const { data } = await supabase
    .from('magic_tokens')
    .insert({ candidate_id, job_id, action })
    .select('token')
    .single();
  return `${BACKEND_URL}/api/magic/${data.token}`;
}

export async function sendDigest({ candidate, jobs }) {
  if (!jobs.length) return;

  const jobRows = await Promise.all(jobs.map(async (item) => {
    const job = item.jobs;
    const acceptUrl = await createMagicLink(candidate.id, job.id, 'accept');
    const rejectUrl = await createMagicLink(candidate.id, job.id, 'reject');
    const stars = item.score >= 90 ? '⭐⭐' : item.score >= 80 ? '⭐' : '';

    return `
      <tr>
        <td style="padding:12px 0; border-bottom:1px solid #eee;">
          <strong><a href="${job.url}" style="color:#1a1a1a;text-decoration:none;">${job.title}</a></strong>
          <span style="color:#666;"> @ ${job.company}</span>
          ${stars ? `<span style="margin-left:6px">${stars}</span>` : ''}<br>
          <small style="color:#888;">${item.score}/100 match${job.salary_min ? ` · $${job.salary_min.toLocaleString()}–$${job.salary_max.toLocaleString()}` : ''}</small><br>
          <small style="color:#555;font-style:italic;">${item.score_reasoning}</small><br>
          <a href="${acceptUrl}" style="display:inline-block;margin-top:6px;padding:4px 12px;background:#22c55e;color:#fff;border-radius:4px;text-decoration:none;font-size:13px;">Accept</a>
          <a href="${rejectUrl}" style="display:inline-block;margin-top:6px;margin-left:6px;padding:4px 12px;background:#ef4444;color:#fff;border-radius:4px;text-decoration:none;font-size:13px;">Reject</a>
        </td>
      </tr>`;
  }));

  const html = `
<!DOCTYPE html>
<html>
<body style="font-family:sans-serif;max-width:600px;margin:0 auto;padding:20px;color:#1a1a1a;">
  <h2 style="border-bottom:2px solid #1a1a1a;padding-bottom:8px;">
    ${jobs.length} new remote ${jobs.length === 1 ? 'job' : 'jobs'} matched your profile
  </h2>
  <table style="width:100%;border-collapse:collapse;">
    ${jobRows.join('')}
  </table>
  <p style="margin-top:24px;">
    <a href="${FRONTEND_URL}/dashboard" style="color:#3b82f6;">View all opportunities →</a>
  </p>
  <p style="font-size:12px;color:#aaa;margin-top:32px;">
    You're receiving this because you have an active job search profile.
  </p>
</body>
</html>`;

  const { error } = await resend.emails.send({
    from:    FROM,
    to:      candidate.email,
    subject: `${jobs.length} new remote job${jobs.length > 1 ? 's' : ''} — top match: ${jobs[0].score}/100`,
    html,
  });

  if (error) throw new Error(`Resend error: ${error.message}`);

  // Log the send
  await supabase.from('email_logs').insert({
    candidate_id: candidate.id,
    type: 'digest',
    job_ids: jobs.map(j => j.jobs.id),
  });

  // Mark jobs as emailed
  const scoreIds = jobs.map(j => j.id);
  await supabase
    .from('candidate_job_scores')
    .update({ status: 'emailed', notified_at: new Date().toISOString() })
    .in('id', scoreIds);
}
