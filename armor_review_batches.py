#!/usr/bin/env python3
import json
from pathlib import Path

ARMOR = Path(__file__).resolve().parent
ROOT = ARMOR.parent
REPORTS = ARMOR / "reports"

def load_private_chunk_reports():
    files = sorted(REPORTS.glob("scan_private_quick_downloads_chunk_*.json"))
    reports = []
    for path in files:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        if data.get("profile") == "quick_downloads_chunk":
            reports.append(data)
    return reports

def summarize(reports):
    clean_batches = 0
    timed_out_batches = 0
    needs_private_review_batches = 0
    unknown_finding_count_batches = 0
    known_finding_count_total = 0

    for report in reports:
        status = report.get("clamav_status", {})
        if status.get("clean") is True:
            clean_batches += 1
        if status.get("timed_out") is True:
            timed_out_batches += 1
        if status.get("needs_private_review") is True:
            needs_private_review_batches += 1

        finding_count = status.get("finding_count")
        if isinstance(finding_count, int):
            known_finding_count_total += finding_count
        else:
            unknown_finding_count_batches += 1

    return {
        "product": "Citadel A.R.M.O.R.",
        "mode": "MVP6_AGGREGATE_REVIEW_ONLY",
        "profile": "quick_downloads_chunk",
        "reports_reviewed": len(reports),
        "clean_batches": clean_batches,
        "timed_out_batches": timed_out_batches,
        "needs_private_review_batches": needs_private_review_batches,
        "known_finding_count_total": known_finding_count_total,
        "unknown_finding_count_batches": unknown_finding_count_batches,
        "review_only": True,
        "enforcement": False,
        "safety_note": "Aggregate review only. No files scanned, opened, moved, deleted, quarantined, or modified.",
    }

def main():
    reports = load_private_chunk_reports()
    print(json.dumps(summarize(reports), indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
