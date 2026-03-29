# 02 ClinicalIntelChat Backend

Minimal FastAPI backend scaffold for local development.

## Run locally

1. Create a virtual environment
2. Install dependencies
3. Start the app

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Endpoints

- `GET /health`
- `POST /api/normalize`
- `POST /api/clinical-intel`
