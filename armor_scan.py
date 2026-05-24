#!/usr/bin/env python3
import argparse
import json
import shutil
import subprocess
import sys
import time
from pathlib import Path

ARMOR = Path(__file__).resolve().parent
ROOT = ARMOR.parent

TOOLS = [
    "clamscan",
    "freshclam",
    "yara",
    "sha256sum",
    "file",
    "find",
]

PROFILES = {
    "citadel_armor_self_check": {
        "description": "Review A.R.M.O.R. source files only. No scanning engine execution yet.",
        "paths": ["~/citadel-ai/armor"],
        "status": "planned_not_executed",
        "risk": "low"
    },
    "quick_downloads": {
        "description": "Future conservative scan of ~/Downloads.",
        "paths": ["~/Downloads"],
        "status": "planned_not_executed",
        "risk": "medium"
    },
    "quick_desktop": {
        "description": "Future conservative scan of ~/Desktop.",
        "paths": ["~/Desktop"],
        "status": "planned_not_executed",
        "risk": "medium"
    },
    "quick_documents": {
        "description": "Future conservative scan of ~/Documents.",
        "paths": ["~/Documents"],
        "status": "planned_not_executed",
        "risk": "medium"
    },
    "mounted_usb_review": {
        "description": "Future explicit review of mounted removable media.",
        "paths": ["/media"],
        "status": "planned_not_executed",
        "risk": "high_requires_operator_review"
    },
    "startup_paths_review": {
        "description": "Future review of user startup paths and service entries.",
        "paths": ["~/.config/autostart", "~/.config/systemd/user"],
        "status": "planned_not_executed",
        "risk": "medium"
    }
}

NO_ACTIONS = [
    "no_file_scan_execution",
    "no_delete",
    "no_quarantine",
    "no_purge",
    "no_permission_changes",
    "no_firewall_changes",
    "no_wifi_changes",
    "no_bluetooth_changes",
    "no_usb_blocking",
    "no_lockdown"
]

def dependency_status():
    return {name: ("missing" if shutil.which(name) is None else "present") for name in TOOLS}

def run_cmd(cmd, seconds=30):
    try:
        cp = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, timeout=seconds)
        return {"ok": cp.returncode == 0, "code": cp.returncode, "output": (cp.stdout or "").strip()[:4000]}
    except FileNotFoundError:
        return {"ok": False, "code": 127, "output": "missing command"}
    except subprocess.TimeoutExpired:
        return {"ok": False, "code": 124, "output": "timeout"}

def run_self_check():
    reports = ARMOR / "reports"
    reports.mkdir(parents=True, exist_ok=True)
    stamp = time.strftime("%Y%m%d_%H%M%S")
    private_path = reports / ("scan_private_self_check_" + stamp + ".json")
    result = {
        "product": "Citadel A.R.M.O.R.",
        "mode": "MVP2_READ_ONLY_SCAN",
        "profile": "citadel_armor_self_check",
        "target": str(ARMOR),
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "review_only": True,
        "enforcement": False,
        "actions": ["no_delete", "no_quarantine", "no_purge", "no_permission_changes", "no_lockdown"],
        "tools": dependency_status(),
        "clamav": {"ok": False, "code": 127, "output": "clamscan missing"},
        "yara": {"ok": False, "code": 127, "output": "yara missing"}
    }
    if shutil.which("clamscan"):
        result["clamav"] = run_cmd(["clamscan", "-r", "--infected", "--no-summary", str(ARMOR)], seconds=60)
    if shutil.which("yara"):
        rules = ARMOR / "rules" / "armor_self_check.yar"
        if rules.exists():
            source_files = sorted(str(x) for x in ARMOR.glob("*.py"))
            if source_files:
                result["yara"] = run_cmd(["yara", str(rules)] + source_files, seconds=60)
                result["yara"]["target_scope"] = "armor_root_python_files_only"
                if result["yara"].get("code") == 1:
                    result["yara"]["ok"] = True
                    result["yara"]["finding_status"] = "matches_found_review_only"
            else:
                result["yara"] = {"ok": True, "code": 0, "output": "no root python files present", "target_scope": "armor_root_python_files_only"}
        else:
            result["yara"] = {"ok": True, "code": 0, "output": "no yara self-check rules present", "target_scope": "armor_root_python_files_only"}
    private_path.write_text(json.dumps(result, indent=2, sort_keys=True) + chr(10), encoding="utf-8")
    result["private_report"] = str(private_path)
    return result

def run_quick_downloads_dry_run():
    target = Path.home() / "Downloads"
    exists = target.exists()
    is_dir = target.is_dir()
    return {
        "product": "Citadel A.R.M.O.R.",
        "mode": "MVP4_DRY_RUN_ONLY",
        "profile": "quick_downloads",
        "target": str(target),
        "target_exists": exists,
        "target_is_dir": is_dir,
        "would_scan": bool(exists and is_dir),
        "scan_executed": False,
        "review_only": True,
        "enforcement": False,
        "actions": ["no_scan_executed", "no_delete", "no_quarantine", "no_purge", "no_permission_changes", "no_lockdown"],
        "safety_note": "Dry-run only. No files were scanned, opened, moved, deleted, or modified."
    }

def run_quick_downloads_preflight():
    target = Path.home() / "Downloads"
    exists = target.exists()
    is_dir = target.is_dir()
    max_files = 5000
    file_count = 0
    dir_count = 0
    limit_hit = False
    permission_errors = 0

    if exists and is_dir:
        try:
            for item in target.rglob("*"):
                try:
                    if item.is_dir():
                        dir_count += 1
                    elif item.is_file():
                        file_count += 1
                        if file_count >= max_files:
                            limit_hit = True
                            break
                except OSError:
                    permission_errors += 1
        except OSError:
            permission_errors += 1

    return {
        "product": "Citadel A.R.M.O.R.",
        "mode": "MVP4_PREFLIGHT_ONLY",
        "profile": "quick_downloads",
        "target": str(target),
        "target_exists": exists,
        "target_is_dir": is_dir,
        "scan_executed": False,
        "review_only": True,
        "enforcement": False,
        "candidate_file_count_capped": file_count,
        "directory_count_capped": dir_count,
        "max_files_counted": max_files,
        "file_count_limit_hit": limit_hit,
        "permission_errors": permission_errors,
        "actions": ["no_scan_executed", "no_files_opened", "no_delete", "no_quarantine", "no_purge", "no_permission_changes", "no_lockdown"],
        "safety_note": "Preflight only. Counts candidates without printing filenames or absolute paths."
    }

def summarize_clamav_result(clamav):
    code = clamav.get("code") if isinstance(clamav, dict) else None
    output = clamav.get("output", "") if isinstance(clamav, dict) else ""
    finding_count = None
    if code == 1 and isinstance(output, str):
        finding_count = sum(1 for line in output.splitlines() if line.strip().endswith(" FOUND"))
    elif code == 0:
        finding_count = 0

    return {
        "clean": code == 0,
        "timed_out": code == 124,
        "finding_count": finding_count,
        "needs_private_review": code not in [0],
    }

def quick_downloads_file_list(max_files=5000):
    target = Path.home() / "Downloads"
    files = []
    if target.exists() and target.is_dir():
        for item in sorted(target.rglob("*")):
            try:
                if item.is_file():
                    files.append(item)
                    if len(files) >= max_files:
                        break
            except OSError:
                continue
    return target, files

def run_quick_downloads_chunk(batch_index=0, batch_size=100):
    reports = ARMOR / "reports"
    reports.mkdir(parents=True, exist_ok=True)
    stamp = time.strftime("%Y%m%d_%H%M%S")
    private_path = reports / ("scan_private_quick_downloads_chunk_" + stamp + ".json")

    target, files = quick_downloads_file_list(max_files=5000)
    total_candidates = len(files)
    start = max(0, int(batch_index) * int(batch_size))
    end = min(start + int(batch_size), total_candidates)
    batch = files[start:end]

    result = {
        "product": "Citadel A.R.M.O.R.",
        "mode": "MVP4_CHUNKED_READ_ONLY_SCAN",
        "profile": "quick_downloads_chunk",
        "target": str(target),
        "batch_index": int(batch_index),
        "batch_size_requested": int(batch_size),
        "batch_start": start,
        "batch_end": end,
        "batch_file_count": len(batch),
        "total_candidates_capped": total_candidates,
        "scan_executed": False,
        "review_only": True,
        "enforcement": False,
        "actions": ["no_delete", "no_quarantine", "no_purge", "no_permission_changes", "no_lockdown"],
        "tools": dependency_status(),
        "clamav": {"ok": False, "code": 127, "output": "clamscan missing"}
    }

    if not target.exists() or not target.is_dir():
        result["clamav"] = {"ok": False, "code": 2, "output": "target missing or not a directory"}
    elif not batch:
        result["clamav"] = {"ok": True, "code": 0, "output": "empty batch"}
    elif shutil.which("clamscan"):
        result["clamav"] = run_cmd(["clamscan", "--infected", "--no-summary"] + [str(x) for x in batch], seconds=60)
        result["scan_executed"] = True
        if result["clamav"].get("code") == 1:
            result["clamav"]["ok"] = True
            result["clamav"]["finding_status"] = "matches_found_review_only"

    result["clamav_status"] = summarize_clamav_result(result.get("clamav", {}))
    private_path.write_text(json.dumps(result, indent=2, sort_keys=True) + chr(10), encoding="utf-8")
    result["private_report"] = str(private_path)
    return result

def run_quick_downloads_scan():
    reports = ARMOR / "reports"
    reports.mkdir(parents=True, exist_ok=True)
    stamp = time.strftime("%Y%m%d_%H%M%S")
    private_path = reports / ("scan_private_quick_downloads_" + stamp + ".json")
    target = Path.home() / "Downloads"
    exists = target.exists()
    is_dir = target.is_dir()
    result = {
        "product": "Citadel A.R.M.O.R.",
        "mode": "MVP4_READ_ONLY_SCAN",
        "profile": "quick_downloads",
        "target": str(target),
        "target_exists": exists,
        "target_is_dir": is_dir,
        "scan_executed": False,
        "review_only": True,
        "enforcement": False,
        "actions": ["no_delete", "no_quarantine", "no_purge", "no_permission_changes", "no_lockdown"],
        "tools": dependency_status(),
        "clamav": {"ok": False, "code": 127, "output": "clamscan missing"}
    }
    if not exists or not is_dir:
        result["clamav"] = {"ok": False, "code": 2, "output": "target missing or not a directory"}
    elif shutil.which("clamscan"):
        result["clamav"] = run_cmd(["clamscan", "-r", "--infected", "--no-summary", str(target)], seconds=120)
        result["scan_executed"] = True
        if result["clamav"].get("code") == 1:
            result["clamav"]["ok"] = True
            result["clamav"]["finding_status"] = "matches_found_review_only"
    private_path.write_text(json.dumps(result, indent=2, sort_keys=True) + chr(10), encoding="utf-8")
    result["private_report"] = str(private_path)
    return result

def public_view(data):
    data = dict(data)
    data["root"] = "~/citadel-ai/armor"
    data["timestamp"] = "REDACTED_TIMESTAMP"
    if data.get("profile") in ["quick_downloads", "quick_downloads_chunk"]:
        data["target"] = "~/Downloads"
    elif "target" in data:
        data["target"] = "~/citadel-ai/armor"
    if "private_report" in data:
        data["private_report"] = "REDACTED_PRIVATE_REPORT"
    for key in ["clamav", "yara"]:
        if isinstance(data.get(key), dict) and "output" in data[key]:
            data[key]["output"] = "REDACTED_SCAN_OUTPUT"
    return data

def main():
    ap = argparse.ArgumentParser(description="Citadel A.R.M.O.R. MVP2 scan planning helper")
    ap.add_argument("--deps", action="store_true", help="show scan dependency status")
    ap.add_argument("--profiles", action="store_true", help="list planned scan profiles")
    ap.add_argument("--public", action="store_true", help="redact local root")
    ap.add_argument("--run-profile", choices=["citadel_armor_self_check", "quick_downloads"], help="run one approved read-only scan profile")
    ap.add_argument("--dry-run-profile", choices=["quick_downloads"], help="resolve one planned profile without scanning")
    ap.add_argument("--preflight-profile", choices=["quick_downloads"], help="count bounded scan candidates without scanning")
    ap.add_argument("--run-chunk-profile", choices=["quick_downloads"], help="run one bounded read-only scan batch")
    ap.add_argument("--batch-index", type=int, default=0, help="zero-based chunk batch index")
    ap.add_argument("--batch-size", type=int, default=10, help="chunk batch size, capped at 100")
    args = ap.parse_args()

    if args.run_profile == "citadel_armor_self_check":
        data = run_self_check()
        if args.public:
            data = public_view(data)
        print(json.dumps(data, indent=2, sort_keys=True))
        return

    if args.run_profile == "quick_downloads":
        data = run_quick_downloads_scan()
        if args.public:
            data = public_view(data)
        print(json.dumps(data, indent=2, sort_keys=True))
        return

    if args.dry_run_profile == "quick_downloads":
        data = run_quick_downloads_dry_run()
        if args.public:
            data = public_view(data)
        print(json.dumps(data, indent=2, sort_keys=True))
        return

    if args.preflight_profile == "quick_downloads":
        data = run_quick_downloads_preflight()
        if args.public:
            data = public_view(data)
        print(json.dumps(data, indent=2, sort_keys=True))
        return

    if args.run_chunk_profile == "quick_downloads":
        batch_size = max(1, min(int(args.batch_size), 100))
        data = run_quick_downloads_chunk(batch_index=args.batch_index, batch_size=batch_size)
        if args.public:
            data = public_view(data)
        print(json.dumps(data, indent=2, sort_keys=True))
        return

    if not args.deps and not args.profiles:
        args.deps = True
        args.profiles = True

    data = {
        "product": "Citadel A.R.M.O.R.",
        "mode": "MVP2_SCAN_PLANNING_ONLY",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "root": str(ARMOR),
        "no_action_guards": NO_ACTIONS,
        "scan_execution_enabled": False,
    }

    if args.deps:
        data["dependencies"] = dependency_status()
    if args.profiles:
        data["profiles"] = PROFILES

    if args.public:
        data = public_view(data)

    print(json.dumps(data, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
