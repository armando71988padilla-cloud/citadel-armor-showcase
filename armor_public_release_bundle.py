#!/usr/bin/env python3
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

PRODUCT = "Citadel A.R.M.O.R."

PUBLIC_DOCS = [
    "MVP9_ALLOWLIST_VALIDATION_PLAN.md",
    "MVP10_ROLLBACK_MANIFEST_PLAN.md",
    "MVP11_ACTION_PREVIEW_PLAN.md",
    "MVP12_ACTION_LEDGER_PLAN.md",
    "MVP13_POST_ACTION_VERIFY_PLAN.md",
    "MVP14_EMERGENCY_STOP_PLAN.md",
    "MVP15_OPERATOR_CONFIRM_PLAN.md",
    "MVP16_EXECUTION_READINESS_PLAN.md",
    "MVP17_PRE_EXECUTION_FREEZE_PLAN.md",
    "MVP18_PUBLIC_REGRESSION_PLAN.md",
]

PUBLIC_HELPERS = [
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
    "armor_public_regression.py",
]

PUBLIC_SAMPLES = [
    "reports/policy_public_sample.json",
    "reports/release_gate_public_sample.json",
    "reports/allowlist_validation_public_sample.json",
    "reports/rollback_manifest_public_sample.json",
    "reports/action_preview_public_sample.json",
    "reports/action_ledger_public_sample.json",
    "reports/post_action_verify_public_sample.json",
    "reports/emergency_stop_public_sample.json",
    "reports/operator_confirm_public_sample.json",
    "reports/execution_readiness_public_sample.json",
    "reports/pre_execution_freeze_public_sample.json",
    "reports/public_regression_public_sample.json",
]

NO_ACTION_GUARDS = [
    "no_public_release_bundle_side_effects_beyond_public_sample_write",
    "no_action_execution",
    "no_restore_execution",
    "no_verification_execution",
    "no_confirmation_collection",
    "no_emergency_stop_mutation",
    "no_target_scan",
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
]

def presence(paths: list) -> list:
    return [{"path": path, "present": Path(path).exists()} for path in paths]

def build_bundle(public: bool) -> dict:
    timestamp = "REDACTED_TIMESTAMP" if public else datetime.now(timezone.utc).isoformat()
    doc_presence = presence(PUBLIC_DOCS)
    helper_presence = presence(PUBLIC_HELPERS)
    sample_presence = presence(PUBLIC_SAMPLES)
    bundle_complete = all(item["present"] for item in doc_presence + helper_presence + sample_presence)
    return {
        "product": PRODUCT,
        "mode": "MVP19_PUBLIC_RELEASE_BUNDLE_REVIEW_ONLY",
        "bundle_version": "0.1-review-only",
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
        "target_scan_executed": False,
        "bundle_complete": bundle_complete,
        "public_docs": doc_presence,
        "public_helpers": helper_presence,
        "public_samples": sample_presence,
        "public_boundary": "review_only_no_execution_no_remediation_no_scan",
        "latest_public_phase": "MVP18_PUBLIC_REGRESSION",
        "next_public_phase": "MVP19_PUBLIC_RELEASE_BUNDLE",
        "no_action_guards": NO_ACTION_GUARDS,
        "safety_note": "Public release bundle summary checks expected public files only. It does not scan targets, expose commands, or execute actions.",
    }

def main() -> int:
    parser = argparse.ArgumentParser(description="Citadel A.R.M.O.R. review-only public release bundle summary helper")
    parser.add_argument("--public", action="store_true", help="print public-safe release bundle summary")
    parser.add_argument("--public-sample", action="store_true", help="write reports/public_release_bundle_public_sample.json")
    args = parser.parse_args()
    public = args.public or args.public_sample
    report = build_bundle(public)
    text = json.dumps(report, indent=2, sort_keys=True)
    print(text)
    if args.public_sample:
        out = Path("reports") / "public_release_bundle_public_sample.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text + "\n", encoding="utf-8")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
