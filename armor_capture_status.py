#!/usr/bin/env python3
import json
import subprocess
import sys
import time
from pathlib import Path

ARMOR = Path(__file__).resolve().parent
ROOT = ARMOR.parent
STATUS = ARMOR / "armor_status.py"
STATE = ARMOR / "state"
REPORTS = ARMOR / "reports"

def run_status(public=False):
    cmd = [sys.executable, str(STATUS)]
    if public:
        cmd.append("--public")
    cp = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=10)
    if cp.returncode != 0:
        raise RuntimeError(cp.stderr.strip() or cp.stdout.strip() or "armor_status.py failed")
    return json.loads(cp.stdout)

def main():
    STATE.mkdir(parents=True, exist_ok=True)
    REPORTS.mkdir(parents=True, exist_ok=True)
    stamp = time.strftime("%Y%m%d_%H%M%S")
    private_path = STATE / ("status_private_" + stamp + ".json")
    public_path = REPORTS / "status_public_sample.json"

    private_data = run_status(public=False)
    public_data = run_status(public=True)

    private_path.write_text(json.dumps(private_data, indent=2, sort_keys=True) + chr(10), encoding="utf-8")
    public_path.write_text(json.dumps(public_data, indent=2, sort_keys=True) + chr(10), encoding="utf-8")

    print("ARMOR_CAPTURE_OK")
    print("PRIVATE_STATUS=" + str(private_path))
    print("PUBLIC_SAMPLE=" + str(public_path))

if __name__ == "__main__":
    main()
