from fastapi import FastAPI
import subprocess, sys

app = FastAPI(title="Jac Cloud Adapter", version="1.0.0")

@app.get("/")
def health():
    return {"ok": True, "service": "jac-cloud-adapter"}

@app.get("/run")
def run_main():
    # Use the same Python that started FastAPI:
    p = subprocess.run(
        [sys.executable, "-m", "jaclang", "run", "main.jac"],
        capture_output=True,
        text=True
    )
    return {"returncode": p.returncode, "stdout": p.stdout, "stderr": p.stderr}
