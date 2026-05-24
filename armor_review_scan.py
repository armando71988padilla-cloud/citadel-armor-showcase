#!/usr/bin/env python3
import json
from pathlib import Path

ARMOR = Path(__file__).resolve().parent
ROOT = ARMOR.parent
REPORTS = ARMOR / "reports"

def load_latest():
    files = sorted(REPORTS.glob("scan_private_self_check_*.json"))
    if not files:
        raise SystemExit("NO_PRIVATE_SELF_CHECK_SCAN_FOUND")
    path = files[-1]
    data = json.loads(path.read_text(encoding="utf-8"))
    return path, data

def tool_summary(item):
    if not isinstance(item, dict):
        return {"ok": False, "code": None, "output_present": False}
    output = (item.get("output") or "").strip()
    return {
        "ok": item.get("ok"),
        "code": item.get("code"),
        "output_present": bool(output),
        "output_line_count": len(output.splitlines()) if output else 0
    }

def main():
    path, data = load_latest()
    clamav = data.get("clamav", {})
    yara = data.get("yara", {})
    clamav_output = (clamav.get("output") or "").strip() if isinstance(clamav, dict) else ""
    yara_output = (yara.get("output") or "").strip() if isinstance(yara, dict) else ""
    attention = []
    if isinstance(clamav, dict) and clamav.get("code") == 1:
        attention.append("clamav_detected_infection_review_private_report")
    if isinstance(clamav, dict) and clamav.get("code") not in [0, 1]:
        attention.append("clamav_scan_error_or_timeout")
    if yara_output and yara_output != "no yara self-check rules present":
        attention.append("yara_match_output_present_review_private_report")
    if isinstance(yara, dict) and yara.get("code") not in [0, 1]:
        attention.append("yara_scan_error_or_timeout")
    finding_summary = []
    if isinstance(yara, dict) and yara.get("code") == 1:
        finding_summary.append({
            "tool": "yara",
            "status": "matches_found_review_only",
            "severity": "review",
            "raw_output_redacted": True,
            "recommended_next_step": "Review the private scan report locally before changing rules or taking action."
        })
    if isinstance(clamav, dict) and clamav.get("code") == 1:
        finding_summary.append({
            "tool": "clamav",
            "status": "infection_reported_review_only",
            "severity": "high",
            "raw_output_redacted": True,
            "recommended_next_step": "Review the private scan report locally. Do not delete or quarantine from this helper."
        })
    summary = {
        "review_mode": "READ_ONLY_SCAN_REVIEW",
        "scan_file": path.name,
        "product": data.get("product"),
        "mode": data.get("mode"),
        "profile": data.get("profile"),
        "review_only": data.get("review_only"),
        "enforcement": data.get("enforcement"),
        "clamav": tool_summary(clamav),
        "yara": tool_summary(yara),
        "attention": attention,
        "finding_summary": finding_summary,
        "safety_note": "No raw scan output or private paths printed. This review performs no enforcement."
    }
    print(json.dumps(summary, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
