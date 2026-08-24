# SentinelTrace V2 — Hackathon Prototype

## What is new
This version expands the MVP into an investigation workbench:
- Dashboard with case KPIs
- Risk-ranked synthetic cases
- Search across synthetic entities/cases
- Entity detail view
- Explainable risk-factor breakdown
- Interactive relationship graph
- Alert/timeline data
- Case report generator
- Downloadable JSON case report
- Explicit human-in-the-loop safeguards

## Run

Requires Python 3.9+.

### Full-stack app (`sentineltrace/`)

1. Backend:
   ```
   cd sentineltrace/backend
   pip install -r requirements.txt
   python3 -m uvicorn app.main:app --host 127.0.0.1 --port 8000
   ```
2. Frontend:
   ```
   cd sentineltrace/frontend
   npm install
   npm run dev
   ```
3. Open: http://127.0.0.1:5173

### Legacy single-file prototype

```
python3 server.py   # serves http://127.0.0.1:8010
```

No external Python packages are required.

## Demo script
1. Dashboard: explain fragmentation of intelligence.
2. Search: search `greenparcel`.
3. Select it and show the explainable risk factors.
4. Open Network Graph and explain the cluster.
5. Open Case Report and generate the JSON report.
6. Explain that the prototype only prioritises leads; it does not establish identity or guilt.

## Safety/legality boundary
All records are synthetic. The prototype does not access Tor, dark-web marketplaces, encrypted/private services, real vendors, real wallet addresses, or illicit operational sources. A real deployment would require authorised data sources, legal process, privacy controls, access control and audit logging.
