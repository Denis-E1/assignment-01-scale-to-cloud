from fastapi import FastAPI, Query
from pathlib import Path
import subprocess, sys, os

app = FastAPI(title="Jac Cloud Adapter", version="1.1.0")

@app.get("/")
def health():
    return {"ok": True, "service": "jac-cloud-adapter"}

@app.get("/run")
def run_main(guess: int | None = Query(None, ge=1, le=100)):
    jac_file = str(Path(__file__).resolve().parent / "main.jac")
    env = os.environ.copy()
    if guess is not None:
        env["GUESS"] = str(guess)

    # run using the Python that launched FastAPI
    p = subprocess.run(
        [sys.executable, "-m", "jaclang.cli", "run", jac_file],
        capture_output=True, text=True, env=env
    )
    return {"returncode": p.returncode, "stdout": p.stdout, "stderr": p.stderr, "guess": guess}
