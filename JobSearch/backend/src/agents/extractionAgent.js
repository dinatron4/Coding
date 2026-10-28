import Groq from 'groq-sdk';

const groq = new Groq({ apiKey: process.env.GROQ_API_KEY });
const MODEL = 'openai/gpt-oss-20b';

export async function extractJobData(description) {
  try {
    const response = await groq.chat.completions.create({
      model: MODEL,
      messages: [{
        role: 'user',
        content: `Extract structured data from this job description. Return ONLY a JSON object with these exact keys:
{
  "seniority": "junior|mid|senior|lead|staff|principal|director|any",
  "skills_required": ["skill1", "skill2"],
  "salary_min": null or integer (annual USD),
  "salary_max": null or integer (annual USD),
  "is_remote": true or false,
  "location": "country or region name (e.g. 'Germany', 'United Kingdom', 'Europe'), or 'Remote' if fully remote, or null if unknown"
}

If a field can't be determined, use null or empty array.

Job description:
${description.slice(0, 4000)}`,
      }],
      temperature: 0.1,
      max_tokens: 512,
    });

    const text = response.choices[0].message.content;
    const json = text.match(/\{[\s\S]*\}/)?.[0];
    return json ? JSON.parse(json) : {};
  } catch {
    return {};
  }
}
