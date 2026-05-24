#!/usr/bin/env python3
import json
from pathlib import Path

ARMOR = Path(__file__).resolve().parent
ROOT = ARMOR.parent
BASELINE = ARMOR / "baseline"

def load_latest():
    files = sorted(BASELINE.glob("baseline_private_*.json"))
    if not files:
        raise SystemExit("NO_PRIVATE_BASELINE_FOUND")
    path = files[-1]
    data = json.loads(path.read_text(encoding="utf-8"))
    return path, data

def main():
    path, data = load_latest()
    status = data.get("status", {})
    tools = status.get("tools", {})
    usb = status.get("usb", {})
    wifi = status.get("wifi", {})
    bluetooth = status.get("bluetooth", {})
    firewall = status.get("firewall", {})
    citadel = status.get("citadel", {})
    network = status.get("network", {})
    enforcement = data.get("enforcement", {})

    attention = []
    if tools.get("clamscan") == "missing":
        attention.append("clamscan_missing")
    if firewall.get("ok") is not True:
        attention.append("firewall_status_not_readable_unprivileged")
    if citadel.get("ui_ping", {}).get("ok") is not True:
        attention.append("citadel_ui_ping_not_ok")
    if network.get("ss_ok") is not True:
        attention.append("socket_listener_probe_not_ok")

    summary = {
        "review_mode": "READ_ONLY_BASELINE_REVIEW",
        "baseline_file": path.name,
        "product": data.get("product"),
        "schema": data.get("schema"),
        "baseline_mode": data.get("baseline_mode"),
        "enforcement_enabled": enforcement.get("enabled"),
        "citadel_ui_ok": citadel.get("ui_ping", {}).get("ok"),
        "tool_presence": {k: ("missing" if v == "missing" else "present") for k, v in tools.items()},
        "wifi_probe_ok": wifi.get("ok"),
        "bluetooth_probe_ok": bluetooth.get("ok"),
        "usb_probe_ok": usb.get("ok"),
        "usb_seen_count": usb.get("count"),
        "network_probe_ok": network.get("ss_ok"),
        "attention": attention,
        "safety_note": "No raw identifiers printed. This review performs no enforcement."
    }
    print(json.dumps(summary, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
