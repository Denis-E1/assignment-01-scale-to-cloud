# Assignment 01 — Scale to Cloud

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python&logoColor=white)
![Jac](https://img.shields.io/badge/Jac-0.8.x-7A1FA2)
![FastAPI](https://img.shields.io/badge/FastAPI-API-009688?logo=fastapi&logoColor=white)
![Railway](https://img.shields.io/badge/Deployed_on-Railway-0B0D0E?logo=railway)

Expose an **unchanged Jac program** as an **HTTP service** and deploy it to the cloud.  
> The Jac code stays the same. We only add a tiny HTTP layer (FastAPI) that calls `jac run main.jac`.

---

## Demo

**Live service:** `https://assignment-01-scale-to-cloud-production.up.railway.app`  
- **Health:** `/` → returns service status  
- **Run Jac:** `/run` → executes `jac run main.jac` and returns output  

<details>
<summary><b>Expected responses</b> (click)</summary>

**GET /**  
```json
{ "ok": true, "service": "jac-cloud-adapter" }

GET /run
{
  "returncode": 0,
  "stdout": "Hello from Jac — now on the cloud! 🎉\n",
  "stderr": "",
  "cmd": ["jac", "run", "/app/main.jac"]
}

Project structure

assignment-01-scale-to-cloud/
├─ main.jac            # your unchanged Jac program
├─ app.py              # small FastAPI wrapper that runs main.jac
├─ requirements.txt    # deps for local + cloud
├─ Procfile            # how to start the service on Railway/Render
└─ .gitignore

Run locally (step-by-step)

# 1) Create & activate venv
python3.12 -m venv .venv
source .venv/bin/activate

# 2) Install dependencies
python -m pip install -U pip -r requirements.txt

# 3) Quick sanity: run Jac locally (no web)
jac run main.jac

# 4) Start the HTTP service
uvicorn app:app --host 0.0.0.0 --port 8000

Open:
 → health
http://localhost:8000/  

 → executes jac run main.jac
http://localhost:8000/run

If jac isn’t found, your venv isn’t active or jaclang isn’t installed.
Fix: source .venv/bin/activate && pip install jaclang && which jac.

Deploy to Railway (cloud)

1. Push this repo to GitHub.

2. Railway → New Project → Deploy from GitHub → select this repo.

3. If asked, Start command:
   uvicorn app:app --host 0.0.0.0 --port $PORT
4. After deploy: Service → Settings → Generate Domain to get a public URL.
5. Test /<nothing> and /run on your domain.

How it works (one picture)

flowchart LR
  A[main.jac (Jac code)] -->|jac run| B[Local execution]
  A -->|called by| C[FastAPI app.py]
  C -->|/run endpoint| B
  C --> D[Railway Cloud]
  D --> E[Public URL]

Troubleshooting

jac: command not found
Activate venv or install jaclang in it:
source .venv/bin/activate && pip install jaclang && which jac

No module named jaclang.__main__
Use python -m jaclang.cli run main.jac instead of python -m jaclang run ....

Railway says “Unexposed service”
Service → Settings → Generate Domain to get a public URL.

502 / crash
Railway → Deployments → View logs.

<p align="center"> <img src="docs/screenshots/railway-health.png" width="650" alt="Railway: health endpoint" /> </p> <p align="center"> <img src="docs/screenshots/railway-run.png" width="650" alt="Railway: run endpoint" /> </p>