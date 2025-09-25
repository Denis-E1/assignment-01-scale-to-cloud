
![Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python&logoColor=white)
![Jac](https://img.shields.io/badge/Jac-0.8.x-7A1FA2)
![FastAPI](https://img.shields.io/badge/FastAPI-API-009688?logo=fastapi&logoColor=white)
![Railway](https://img.shields.io/badge/Deployed_on-Railway-0B0D0E?logo=railway)

# Assignment 01: Scale to Cloud 

Expose an **unchanged Jac program** as an **HTTP service** and deploy it to the cloud.

> The Jac code remains the same. We only add a lightweight HTTP layer (FastAPI) that calls `jac run main.jac`.

-----

##  Features

This project demonstrates how to **scale a Jac program to the cloud** by wrapping it in a simple HTTP service.

-----

##  Project Structure

```bash
assignment-01-scale-to-cloud/
├─ main.jac             # The original, unchanged Jac program
├─ app.py               # A small FastAPI wrapper
├─ requirements.txt     # Dependencies for local and cloud
├─ Procfile             # How to start the service on Railway/Render
└─ .gitignore
```

-----

##  Getting Started

### Demo

The live service is available at:
`https://assignment-01-scale-to-cloud-production.up.railway.app`

  - **Health Check:** `https://.../` returns service status.
  - **Run Jac:** `https://.../run` executes `jac run main.jac` and returns the output.

\<details\>
\<summary\>\<b\>Expected responses\</b\> (click to expand)\</summary\>

**GET /**

```json
{
  "ok": true,
  "service": "jac-cloud-adapter"
}
```

**GET /run**

```json
{
  "returncode": 0,
  "stdout": "Hello from Jac — now on the cloud! 🎉\n",
  "stderr": "",
  "cmd": [
    "jac",
    "run",
    "/app/main.jac"
  ]
}
```

\</details\>

-----

##  How to Run Locally

Follow these steps to run the project on your machine.

1.  **Create and activate a virtual environment:**

    ```bash
    python3.12 -m venv .venv
    source .venv/bin/activate
    ```

2.  **Install dependencies:**

    ```bash
    python -m pip install -U pip -r requirements.txt
    ```

3.  **Run the Jac program locally (no web):**

    ```bash
    jac run main.jac
    ```

4.  **Start the HTTP service:**

    ```bash
    uvicorn app:app --host 0.0.0.0 --port 8000
    ```

Once the service is running, open your browser to test the endpoints:

  - [http://localhost:8000/](https://www.google.com/search?q=http://localhost:8000/)
  - [http://localhost:8000/run](https://www.google.com/search?q=http://localhost:8000/run)

**Troubleshooting:** If the `jac` command is not found, your virtual environment may not be active, or `jaclang` is not installed. Run `source .venv/bin/activate && pip install jaclang && which jac` to fix it.

-----

##  How to Deploy to Railway

1.  Push this repository to GitHub.

2.  Navigate to **Railway** → **New Project** → **Deploy from GitHub**.

3.  Select this repository.

4.  If prompted for a start command, use:

    ```bash
    uvicorn app:app --host 0.0.0.0 --port $PORT
    ```

5.  After deployment, go to **Service** → **Settings** → **Generate Domain** to get a public URL.

Test the `/` and `/run` endpoints on your new domain.

-----

##  How It Works

**Robust call if PATH is quirky:**
In `app.py`, you can use the full path to the Python executable to run the Jac CLI:

```python
p = subprocess.run([sys.executable, "-m", "jaclang.cli", "run", "main.jac"], ...)
```

-----

##  Troubleshooting

  - `jac: command not found`: Activate your virtual environment and install `jaclang`.
  - `No module named jaclang.__main__`: Use `python -m jaclang.cli run main.jac` instead of `jac run main.jac`.
  - `Unexposed service`: Go to **Service Settings** and **Generate Domain** on Railway.
  - `502 / crash`: Check the deployment logs on Railway for errors.

-----

##  Screenshots

<p align="center"> <img src="docs/screenshots/railway-health.png" width="650" alt="Railway: health endpoint" /> </p> <p align="center"> <img src="docs/screenshots/railway-run.png" width="650" alt="Railway: run endpoint" /> </p>

-----

##  Why this meets “Scale to Cloud”

1.  The Jac program remains unchanged, highlighting the adaptability of the code.
2.  A simple HTTP service wraps the Jac entry point, providing a scalable interface.
3.  The service is successfully deployed to a public cloud URL with working endpoints.

## 🤫 Silence
This is an open-source project, so feel free to use it, fork it, and modify it as you see fit. Contributions are welcome!