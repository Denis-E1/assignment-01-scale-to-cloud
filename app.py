# app.py
from fastapi import FastAPI
from pathlib import Path
import subprocess, sys

app = FastAPI(title="Jac Cloud Adapter", version="1.0.1")

@app.get("/")
def health():
    return {"ok": True, "service": "jac-cloud-adapter"}

@app.get("/run")
def run_main():
    # Always resolve the Jac file relative to this file
    jac_file = str(Path(__file__).resolve().parent / "main.jac")

    # Try the most reliable command first: python -m jaclang.cli
    commands = [
        [sys.executable, "-m", "jaclang.cli", "run", jac_file],
        # Fallback to the console script if PATH is set up:
        ["jac", "run", jac_file],
    ]

    last = None
    for cmd in commands:
        p = subprocess.run(cmd, capture_output=True, text=True)
        if p.returncode == 0:
            return {"returncode": p.returncode, "stdout": p.stdout, "stderr": p.stderr, "cmd": cmd}
        last = p

    # If both attempts failed, return the last error for debugging
    return {
        "returncode": last.returncode if last else -1,
        "stdout": last.stdout if last else "",
        "stderr": last.stderr if last else "no command executed",
        "tried": commands,
    }
