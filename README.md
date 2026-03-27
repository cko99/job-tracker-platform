# Job Application Tracking System

Production-focused job search operating system with analytics, match scoring, follow-up reminders, and company intelligence.

## Tech Stack
- **Frontend**: React + Tailwind + Recharts
- **Backend**: Express.js + PostgreSQL
- **Database**: Supabase/Postgres-compatible schema

## Monorepo Structure

```text
.
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   ├── components/
│   │   ├── pages/
│   │   └── App.jsx
│   └── package.json
├── backend/
│   ├── src/
│   │   ├── routes/
│   │   ├── services/
│   │   ├── utils/
│   │   ├── db.js
│   │   └── index.js
│   └── package.json
└── database/
    └── schema.sql
```

## Core Modules Implemented
1. **Application Tracker**
   - Add jobs with all requested fields.
   - Table view + kanban status movement.
2. **Analytics Dashboard**
   - KPIs: total apps, response/interview/offer rates.
   - Pie, line, and bar charts.
3. **Strategy Insights Engine**
   - Best role/platform/day + avg response time summary.
4. **Follow-Up Reminder System**
   - Follow-up due endpoint with overdue days.
5. **Resume & Document Tracker**
   - Resume version and cover letter tracking in applications + documents table.
6. **Company Database**
   - Company list with application counts + search support.
7. **Match Scoring System**
   - Weighted score and recommendation (Apply/Consider/Skip).
8. **Weekly Performance Report**
   - API returns weekly totals, interview/rejection counts, and AI-style summary.

## Backend Setup
```bash
cd backend
npm install
cp .env.example .env  # create manually if needed
npm run dev
```

Required env var:
- `DATABASE_URL=postgresql://...`
- Optional: `DB_SSL=true`

## Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

Optional env var:
- `VITE_API_URL=http://localhost:4000/api`

## Database Setup
Run `database/schema.sql` in Supabase SQL editor or PostgreSQL.
