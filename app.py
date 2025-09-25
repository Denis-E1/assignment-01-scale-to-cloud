from fastapi import FastAPI, Query
from pathlib import Path
import subprocess, sys, os

app = FastAPI(title="Jac Cloud Adapter", version="1.1.1")

@app.get("/")
def health():
    return {"ok": True, "service": "jac-cloud-adapter"}

@app.get("/run")
def run_main(guess: int | None = Query(None, ge=1, le=100)):
    jac_file = str(Path(__file__).resolve().parent / "main.jac")

    # pass guess through env if you want (Jac code can read it if you later add that)
    env = os.environ.copy()
    if guess is not None:
        env["GUESS"] = str(guess)

    # 1st try: python -m jaclang.cli.cli …  (works even if PATH doesn't have "jac")
    # 2nd try: "jac …"  (console script, if PATH is set)
    commands = [
        [sys.executable, "-m", "jaclang.cli.cli", "run", jac_file],
        ["jac", "run", jac_file],
    ]

    last = None
    for cmd in commands:
        p = subprocess.run(cmd, capture_output=True, text=True, env=env)
        if p.returncode == 0:
            return {"returncode": p.returncode, "stdout": p.stdout, "stderr": p.stderr, "cmd": cmd, "guess": guess}
        last = p

    return {
        "returncode": last.returncode if last else -1,
        "stdout": last.stdout if last else "",
        "stderr": last.stderr if last else "no command executed",
        "tried": commands,
        "guess": guess,
    }
