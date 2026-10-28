import Groq from 'groq-sdk';

const groq = new Groq({ apiKey: process.env.GROQ_API_KEY });
const MODEL = 'openai/gpt-oss-120b';

export async function generateCoverLetter({ profile, job }) {
  const response = await groq.chat.completions.create({
    model: MODEL,
    messages: [{
      role: 'user',
      content: `Write a tailored cover letter for this job application.

Candidate:
- CV: ${(profile.cv_text || '').slice(0, 2000)}
- Skills: ${(profile.skills || []).join(', ')}
- Years of experience: ${profile.years_experience ?? 'unknown'}
${profile.extra_instructions ? `- Extra instructions: ${profile.extra_instructions}` : ''}

Job:
- Title: ${job.title}
- Company: ${job.company}
- Description: ${(job.description || '').slice(0, 2000)}

Write a 3-paragraph cover letter:
1. Strong opening that connects the candidate's background to this specific role
2. 2–3 concrete examples of relevant experience or skills
3. Brief closing that expresses enthusiasm and next steps

Tone: professional but warm. Do NOT use generic phrases like "I am writing to express my interest."
Output only the cover letter text, no subject line or salutation beyond "Dear Hiring Team,".`,
    }],
    temperature: 0.7,
    max_tokens: 1024,
  });

  return response.choices[0].message.content;
}
