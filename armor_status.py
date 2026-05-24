#!/usr/bin/env python3
import argparse
import copy
import json
import os
import platform
import shutil
import socket
import subprocess
import time
from pathlib import Path
from urllib.request import urlopen

ARMOR = Path(__file__).resolve().parent
ROOT = ARMOR.parent
NO_ACTIONS = [
    "no_firewall_changes",
    "no_wifi_changes",
    "no_bluetooth_changes",
    "no_usb_changes",
    "no_quarantine",
    "no_purge",
    "no_lockdown",
]

def run(cmd, seconds=2):
    try:
        cp = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, timeout=seconds)
        return {"ok": cp.returncode == 0, "code": cp.returncode, "output": (cp.stdout or "").strip()[:1600]}
    except FileNotFoundError:
        return {"ok": False, "code": 127, "output": "missing command"}
    except subprocess.TimeoutExpired:
        return {"ok": False, "code": 124, "output": "timeout"}

def ping():
    try:
        with urlopen("http://127.0.0.1:8787/api/ping", timeout=2) as r:
            return {"ok": True, "code": r.status, "body": r.read(500).decode("utf-8", errors="replace")}
    except Exception as e:
        return {"ok": False, "code": 0, "body": e.__class__.__name__}

def read_text(path):
    try:
        return Path(path).read_text(encoding="utf-8", errors="replace").strip()[:200]
    except Exception:
        return "unknown"

def usb_sample():
    base = Path("/sys/bus/usb/devices")
    items = []
    if not base.exists():
        return {"ok": False, "count": 0, "sample": items}
    for x in sorted(base.iterdir(), key=lambda q: q.name)[:60]:
        vendor = read_text(x / "idVendor")
        product = read_text(x / "idProduct")
        name = read_text(x / "product")
        if vendor == "unknown" and product == "unknown" and name == "unknown":
            continue
        items.append({"node": x.name, "vendor": vendor, "product": product, "name": name})
    return {"ok": True, "count": len(items), "sample": items[:20]}

def public_view(data):
    data = copy.deepcopy(data)
    data["root"] = "~/citadel-ai/armor"
    data["timestamp"] = "REDACTED_TIMESTAMP"
    if "host" in data:
        data["host"]["user"] = "REDACTED_USER"
        data["host"]["hostname"] = "REDACTED_HOST"
        data["host"]["platform"] = "REDACTED_PLATFORM"
        data["host"]["kernel"] = "REDACTED_KERNEL"
    fw = data.get("firewall", {})
    if isinstance(fw, dict):
        fw["output"] = "REDACTED_FIREWALL_OUTPUT"
    wifi = data.get("wifi", {})
    if isinstance(wifi, dict):
        wifi["output"] = "REDACTED_WIFI_OUTPUT"
    bt = data.get("bluetooth", {})
    if isinstance(bt, dict):
        bt["output"] = "REDACTED_BLUETOOTH_OUTPUT"
    usb = data.get("usb", {})
    if isinstance(usb, dict):
        usb["count"] = "REDACTED_USB_COUNT"
        usb["sample"] = []
    net = data.get("network", {})
    if isinstance(net, dict):
        net["loopback_services"] = ["REDACTED_LOOPBACK_SERVICES"]
        net["listeners_sample"] = ["REDACTED_LISTENERS_SAMPLE"]
    tools = data.get("tools", {})
    if isinstance(tools, dict):
        data["tools"] = {k: ("missing" if v == "missing" else "present") for k, v in tools.items()}
    return data

def main():
    tools = ["python3", "nmcli", "bluetoothctl", "rfkill", "clamscan", "ufw", "ss"]
    ss = run(["ss", "-lntp"], seconds=3)
    ss_lines = ss["output"].splitlines()
    data = {
        "product": "Citadel A.R.M.O.R.",
        "mode": "MVP1_READ_ONLY_STATUS",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "root": str(ARMOR),
        "no_action_guards": NO_ACTIONS,
        "host": {
            "user": os.environ.get("USER", "unknown"),
            "hostname": socket.gethostname(),
            "platform": platform.platform(),
            "kernel": platform.release(),
        },
        "citadel": {
            "root_exists": ROOT.exists(),
            "armor_exists": ARMOR.exists(),
            "ui_ping": ping(),
        },
        "tools": {name: shutil.which(name) or "missing" for name in tools},
        "network": {
            "ss_ok": ss["ok"],
            "loopback_services": [x for x in ss_lines if "127.0.0.1:8787" in x or "127.0.0.1:11434" in x],
            "listeners_sample": [x for x in ss_lines if "LISTEN" in x][:25],
        },
        "firewall": run(["ufw", "status"], seconds=3) if shutil.which("ufw") else {"ok": False, "output": "ufw missing"},
        "wifi": run(["nmcli", "-t", "-f", "DEVICE,TYPE,STATE,CONNECTION", "dev", "status"], seconds=3) if shutil.which("nmcli") else {"ok": False, "output": "nmcli missing"},
        "bluetooth": run(["bluetoothctl", "show"], seconds=3) if shutil.which("bluetoothctl") else {"ok": False, "output": "bluetoothctl missing"},
        "usb": usb_sample(),
    }
    ap = argparse.ArgumentParser(description="Citadel A.R.M.O.R. read-only status probe")
    ap.add_argument("--public", action="store_true", help="redact machine-specific values")
    args = ap.parse_args()
    if args.public:
        data = public_view(data)
    print(json.dumps(data, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
