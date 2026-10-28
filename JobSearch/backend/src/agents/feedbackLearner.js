import Groq from 'groq-sdk';
import supabase from '../services/supabase.js';

const groq = new Groq({ apiKey: process.env.GROQ_API_KEY });
const MODEL = 'openai/gpt-oss-120b';

export async function runFeedbackLearner() {
  const { data: candidates } = await supabase
    .from('candidates')
    .select('id')
    .eq('is_active', true);

  for (const candidate of (candidates ?? [])) {
    const { data: feedbackItems } = await supabase
      .from('feedback')
      .select('*, jobs(title, company, seniority, skills_required, salary_min, salary_max)')
      .eq('candidate_id', candidate.id)
      .order('created_at', { ascending: false })
      .limit(40);

    if (!feedbackItems?.length) continue;

    const feedbackText = feedbackItems.map(f =>
      `${f.feedback_type.toUpperCase()}: "${f.jobs?.title}" at ${f.jobs?.company}` +
      (f.reject_reason ? ` (reason: ${f.reject_reason})` : '') +
      (f.notes ? ` — ${f.notes}` : '')
    ).join('\n');

    try {
      const response = await groq.chat.completions.create({
        model: MODEL,
        messages: [{
          role: 'user',
          content: `Analyze this job seeker's accept/reject history and write 3–5 concise bullet points describing their patterns and preferences. These will be injected into future job scoring prompts.

Feedback history:
${feedbackText}

Write only bullet points starting with "-". Be specific and actionable.
Example: "- Rejects roles at companies with fewer than 100 employees"`,
        }],
        temperature: 0.3,
        max_tokens: 256,
      });

      const hints = response.choices[0].message.content;
      await supabase
        .from('candidate_profiles')
        .update({ scoring_hints: hints, updated_at: new Date().toISOString() })
        .eq('candidate_id', candidate.id);

      console.log(`[feedbackLearner] Updated hints for candidate ${candidate.id}`);
    } catch (err) {
      console.error(`[feedbackLearner] Error for candidate ${candidate.id}:`, err.message);
    }
  }
}
