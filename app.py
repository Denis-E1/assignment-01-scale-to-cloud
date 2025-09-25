from fastapi import FastAPI
import subprocess

app = FastAPI(title="Jac Cloud Adapter", version="1.0.0")

@app.get("/")
def health():
    return {"ok": True, "service": "jac-cloud-adapter"}

@app.get("/run")
def run_main():
    p = subprocess.run(["jac", "run", "main.jac"], capture_output=True, text=True)
    return {
        "returncode": p.returncode,
        "stdout": p.stdout,
        "stderr": p.stderr
    }
