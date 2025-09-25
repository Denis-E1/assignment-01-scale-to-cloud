# Assignment 01 — Scale to Cloud

Goal: expose an **unchanged Jac program** as an **HTTP service** and deploy it.

## Run locally
```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip -r requirements.txt

jac run main.jac                     # quick check
uvicorn app:app --host 0.0.0.0 --port 8000

