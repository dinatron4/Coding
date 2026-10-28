# Job Search Engine

Autonomous remote job finder. Discovers jobs from multiple sources, scores them against your profile using AI, and emails you a daily digest with the top matches.

---

## Stack

| Layer | Tech |
|---|---|
| Frontend | React + Vite → Vercel |
| Backend | Express → Render |
| Database | Supabase (PostgreSQL) |
| AI (scoring/extraction) | Groq — `llama-3.1-8b-instant` |
| AI (cover letters) | Anthropic — `claude-sonnet-5-5` |
| Email | Resend |

---

## Setup

### 1. Supabase

1. Create a new Supabase project
2. Run both migrations in order via the SQL editor:
   - `supabase/migrations/001_initial_schema.sql`
   - `supabase/migrations/002_add_location.sql`

### 2. Backend environment variables

Create `backend/.env`:

```env
SUPABASE_URL=your_supabase_url
SUPABASE_SERVICE_KEY=your_supabase_service_role_key

GROQ_API_KEY=your_groq_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key

RESEND_API_KEY=your_resend_api_key
EMAIL_FROM=you@yourdomain.com

# Optional — EU + Brazil job search (£8/month after 25 test calls)
ADZUNA_APP_ID=your_adzuna_app_id
ADZUNA_API_KEY=your_adzuna_api_key

# Optional — higher Himalayas rate limits
HIMALAYAS_API_KEY=your_himalayas_api_key

FRONTEND_URL=https://your-frontend.vercel.app
BACKEND_URL=https://your-backend.onrender.com
PORT=3001
```

### 3. Running locally

```bash
# Backend
cd backend && npm install && npm run dev

# Frontend
cd frontend && npm install && npm run dev
```

---

## First run

1. Open the app and go to **Profile** — create a candidate with your CV, target roles, skills, salary range, and location preference
2. Click **Discover** in the dashboard — fetches fresh jobs from all sources (takes ~2 min)
3. Click **Run** — choose a location filter, then score jobs against your profile
4. Jobs appear in the dashboard grouped by location column (Remote / EU / country)

---

## Daily workflow

You don't need to do anything — the backend runs automatically:

| Schedule | What happens |
|---|---|
| Every 4 hours | Discovers new jobs from all sources |
| Every 4 hours (+5 min) | Scores new jobs against your profile |
| Daily at 08:00 UTC | Emails you jobs scoring ≥ 75 |
| Every Sunday 06:00 UTC | Learns from your accept/reject feedback |

The email digest contains magic links — click **Accept** or **Reject** directly from the email without logging in.

---

## Job sources

| Source | Coverage | Notes |
|---|---|---|
| Remotive | Remote, global | Free, keyword search |
| We Work Remotely | Remote, global | Free, RSS (no keyword filter) |
| Himalayas | Remote, global | Free, ~130k jobs |
| Adzuna | US + EU + Brazil | Requires API key, £8/month for full access |

---

## Dashboard

- **Discover** — manually trigger job discovery (automatic every 4h)
- **Run** — score jobs for the current candidate; prompts for a location filter:
  - *Remote only* — all remote jobs
  - *Europe / EU* — requires Adzuna EU keys to return results
  - *Country* — type any country name (e.g. Germany, Brazil)
- **▾** — run scoring for all candidates at once
- **Tabs** — New / Emailed / Accepted

### Job cards

Each card shows score (0–100), title, company, remote/salary/seniority badges, and an AI match summary. Expand a card to see:
- **What aligns** — strengths vs your profile
- **Potential gaps** — areas of uncertainty
- Skills required, role description, link to posting
- Accept / Reject / Generate Cover Letter

### Applications

After accepting a job, go to **Applications** to track progress through the pipeline: `accepted → applied → interview → offer / closed`.

---

## Groq rate limits (free tier)

| Model | TPM | TPD |
|---|---|---|
| `llama-3.1-8b-instant` | 131,072 | 500,000 |

At ~1,500 tokens per scoring call, the free tier supports ~333 scores per day. Upgrade at [console.groq.com](https://console.groq.com/settings/billing) if needed.
