#!/usr/bin/env python3
import argparse
import json
import py_compile
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

PRODUCT = "Citadel A.R.M.O.R."

HELPERS = [
    "armor_policy.py",
    "armor_release_gate.py",
    "armor_allowlist_validate.py",
    "armor_rollback_manifest.py",
    "armor_action_preview.py",
    "armor_action_ledger.py",
    "armor_post_action_verify.py",
    "armor_emergency_stop.py",
    "armor_operator_confirm.py",
    "armor_execution_readiness.py",
    "armor_pre_execution_freeze.py",
]

PUBLIC_SAMPLE_COMMANDS = [
    ["armor_policy.py", "--public"],
    ["armor_release_gate.py", "--public"],
    ["armor_allowlist_validate.py", "--public-sample"],
    ["armor_rollback_manifest.py", "--public-sample"],
    ["armor_action_preview.py", "--public-sample"],
    ["armor_action_ledger.py", "--public-sample"],
    ["armor_post_action_verify.py", "--public-sample"],
    ["armor_emergency_stop.py", "--public-sample"],
    ["armor_operator_confirm.py", "--public-sample"],
    ["armor_execution_readiness.py", "--public-sample"],
    ["armor_pre_execution_freeze.py", "--public-sample"],
]

REQUIRED_LOCKED_FLAGS = {
    "review_only": True,
    "enforcement": False,
    "actions_enabled": False,
    "remediation_enabled": False,
    "scan_executed": False,
}

NO_ACTION_GUARDS = [
    "no_public_regression_side_effects_beyond_public_sample_refresh",
    "no_action_execution",
    "no_restore_execution",
    "no_verification_execution",
    "no_confirmation_collection",
    "no_emergency_stop_mutation",
    "no_delete",
    "no_quarantine",
    "no_purge",
    "no_permission_changes",
    "no_firewall_changes",
    "no_wifi_changes",
    "no_bluetooth_changes",
    "no_usb_changes",
    "no_process_kill",
    "no_lockdown",
    "no_scan_execution",
]

def compile_helpers() -> list:
    results = []
    for helper in HELPERS:
        path = Path(helper)
        if not path.exists():
            results.append({"helper": helper, "compile_ok": False, "reason": "missing_helper"})
            continue
        try:
            py_compile.compile(str(path), doraise=True)
            results.append({"helper": helper, "compile_ok": True, "reason": "compiled"})
        except Exception as exc:
            results.append({"helper": helper, "compile_ok": False, "reason": str(exc)})
    return results

def run_public_samples() -> list:
    results = []
    for command in PUBLIC_SAMPLE_COMMANDS:
        helper = command[0]
        path = Path(helper)
        if not path.exists():
            results.append({"helper": helper, "run_ok": False, "reason": "missing_helper"})
            continue
        completed = subprocess.run([sys.executable] + command, text=True, capture_output=True)
        run_ok = completed.returncode == 0
        parsed = None
        parse_ok = False
        locked_flags_ok = False
        reason = "ran" if run_ok else "nonzero_exit"
        if run_ok:
            try:
                parsed = json.loads(completed.stdout)
                parse_ok = True
                locked_flags_ok = all(parsed.get(k) == v for k, v in REQUIRED_LOCKED_FLAGS.items() if k in parsed)
            except json.JSONDecodeError:
                reason = "stdout_not_json"
        results.append({
            "helper": helper,
            "run_ok": run_ok,
            "parse_ok": parse_ok,
            "locked_flags_ok": locked_flags_ok,
            "reason": reason,
        })
    return results

def build_report(public: bool) -> dict:
    timestamp = "REDACTED_TIMESTAMP" if public else datetime.now(timezone.utc).isoformat()
    compile_results = compile_helpers()
    sample_results = run_public_samples()
    compile_ok = all(item["compile_ok"] for item in compile_results)
    samples_ok = all(item["run_ok"] and item["parse_ok"] and item["locked_flags_ok"] for item in sample_results)
    regression_passed = compile_ok and samples_ok
    return {
        "product": PRODUCT,
        "mode": "MVP18_PUBLIC_REGRESSION_REVIEW_ONLY",
        "regression_version": "0.1-review-only",
        "created_at": timestamp,
        "review_only": True,
        "enforcement": False,
        "actions_enabled": False,
        "remediation_enabled": False,
        "restore_executed": False,
        "scan_executed": False,
        "action_executed": False,
        "verification_executed": False,
        "confirmation_collected": False,
        "emergency_stop_modified": False,
        "public_regression_executed": True,
        "regression_passed": regression_passed,
        "compile_ok": compile_ok,
        "public_samples_ok": samples_ok,
        "helpers_checked": HELPERS,
        "compile_results": compile_results,
        "public_sample_results": sample_results,
        "required_locked_flags": REQUIRED_LOCKED_FLAGS,
        "no_action_guards": NO_ACTION_GUARDS,
        "safety_note": "Public regression aggregation compiles helpers and refreshes public samples only. It does not scan targets, expose commands, or execute actions.",
    }

def main() -> int:
    parser = argparse.ArgumentParser(description="Citadel A.R.M.O.R. review-only public regression aggregation helper")
    parser.add_argument("--public", action="store_true", help="print public-safe regression summary")
    parser.add_argument("--public-sample", action="store_true", help="write reports/public_regression_public_sample.json")
    args = parser.parse_args()
    public = args.public or args.public_sample
    report = build_report(public)
    text = json.dumps(report, indent=2, sort_keys=True)
    print(text)
    if args.public_sample:
        out = Path("reports") / "public_regression_public_sample.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text + "\n", encoding="utf-8")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
