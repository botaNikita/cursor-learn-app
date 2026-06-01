# Cursor Learn App

Minimal single-page Python web app for practicing Cursor workflows and basic deployment.

## Quick start (local)

```powershell
cd C:\Users\nikit\projects\cursor-learn-app
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Docker

```powershell
docker build -t cursor-learn-app .
docker run --rm -p 5000:5000 cursor-learn-app
```

## Project layout

- `app.py` — Flask app and `/` route
- `templates/index.html` — the only page
- `requirements.txt` — Python dependencies
- `Dockerfile` — container image for infrastructure practice

## Ideas to try in Cursor

- Change the text in `templates/index.html` and ask the agent to preview it
- Add a health check route (`/health`) for load balancers
- Deploy the Docker image to a cloud provider or VPS
