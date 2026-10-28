import Groq from 'groq-sdk';

const groq = new Groq({ apiKey: process.env.GROQ_API_KEY });
const MODEL = 'openai/gpt-oss-20b';

export async function scoreJob({ job, profile, feedbackHistory = [] }) {
  const feedbackContext = feedbackHistory.length
    ? `\nRecent feedback from this candidate:\n${feedbackHistory.map(f =>
        `- ${f.feedback_type.toUpperCase()} "${f.jobs?.title}" at ${f.jobs?.company}${f.reject_reason ? ` (reason: ${f.reject_reason})` : ''}${f.notes ? ` — ${f.notes}` : ''}`
      ).join('\n')}\n${profile.scoring_hints ? `\nLearned preferences:\n${profile.scoring_hints}` : ''}`
    : '';

  const prompt = `You are a job matching engine. Score how well this job fits the candidate.

Return ONLY a JSON object:
{
  "score": <integer 0-100>,
  "reasoning": "<2-3 sentences explaining the score>"
}

Candidate profile:
- CV summary: ${(profile.cv_text || '').slice(0, 2000)}
- Target roles: ${(profile.target_roles || []).join(', ')}
- Skills: ${(profile.skills || []).join(', ')}
- Years of experience: ${profile.years_experience ?? 'unknown'}
- Salary range: ${profile.salary_min ? `$${profile.salary_min}–$${profile.salary_max} ${profile.salary_currency}` : 'not specified'}
- Location preference: ${profile.location_preference}
- Excluded companies: ${(profile.excluded_companies || []).join(', ') || 'none'}
${profile.extra_instructions ? `- Extra instructions: ${profile.extra_instructions}` : ''}
${feedbackContext}

Job:
- Title: ${job.title}
- Company: ${job.company}
- Seniority: ${job.seniority || 'unknown'}
- Skills required: ${(job.skills_required || []).join(', ')}
- Salary: ${job.salary_min ? `$${job.salary_min}–$${job.salary_max} ${job.currency || 'USD'}` : 'not specified'}
- Remote: ${job.is_remote ? 'yes' : 'no'}
- Description excerpt: ${(job.description || '').slice(0, 2000)}

Score 90–100: near-perfect match. 70–89: strong match. 50–69: partial match. Below 50: poor fit.
Give extra weight to: salary range fit, role title match, remote requirement, excluded companies.
If the company is in the excluded list, score must be 0.`;

  try {
    const response = await groq.chat.completions.create({
      model: MODEL,
      messages: [{ role: 'user', content: prompt }],
      temperature: 0.1,
      max_tokens: 512,
    });

    const text = response.choices[0].message.content;
    const json = text.match(/\{[\s\S]*\}/)?.[0];
    const parsed = json ? JSON.parse(json) : {};
    return {
      score:           Math.min(100, Math.max(0, Number(parsed.score) || 0)),
      score_reasoning: parsed.reasoning || '',
    };
  } catch (err) {
    console.error(`[scoringAgent] Failed: ${err.message}`);
    return { score: 0, score_reasoning: 'Scoring failed.' };
  }
}
