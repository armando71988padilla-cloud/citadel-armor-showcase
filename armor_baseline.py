#!/usr/bin/env python3
import json
import subprocess
import sys
import time
from pathlib import Path

ARMOR = Path(__file__).resolve().parent
ROOT = ARMOR.parent
STATUS = ARMOR / "armor_status.py"
BASELINE = ARMOR / "baseline"
REPORTS = ARMOR / "reports"

def run_status(public=False):
    cmd = [sys.executable, str(STATUS)]
    if public:
        cmd.append("--public")
    cp = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=10)
    if cp.returncode != 0:
        raise RuntimeError(cp.stderr.strip() or cp.stdout.strip() or "armor_status.py failed")
    return json.loads(cp.stdout)

def build_baseline(public=False):
    status = run_status(public=public)
    return {
        "product": "Citadel A.R.M.O.R.",
        "baseline_mode": "READ_ONLY_KNOWN_GOOD_CAPTURE",
        "schema": 1,
        "created": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "enforcement": {
            "enabled": False,
            "firewall_changes": False,
            "wifi_changes": False,
            "bluetooth_changes": False,
            "usb_changes": False,
            "quarantine": False,
            "purge": False,
            "lockdown": False
        },
        "operator_warning": "Review this baseline before using it for trust or enforcement.",
        "status": status
    }

def main():
    BASELINE.mkdir(parents=True, exist_ok=True)
    REPORTS.mkdir(parents=True, exist_ok=True)
    stamp = time.strftime("%Y%m%d_%H%M%S")
    private_path = BASELINE / ("baseline_private_" + stamp + ".json")
    public_path = REPORTS / "baseline_public_sample.json"

    private_data = build_baseline(public=False)
    public_data = build_baseline(public=True)
    public_data["created"] = "REDACTED_TIMESTAMP"

    private_path.write_text(json.dumps(private_data, indent=2, sort_keys=True) + chr(10), encoding="utf-8")
    public_path.write_text(json.dumps(public_data, indent=2, sort_keys=True) + chr(10), encoding="utf-8")

    print("ARMOR_BASELINE_CAPTURE_OK")
    print("PRIVATE_BASELINE=" + str(private_path))
    print("PUBLIC_BASELINE_SAMPLE=" + str(public_path))

if __name__ == "__main__":
    main()
