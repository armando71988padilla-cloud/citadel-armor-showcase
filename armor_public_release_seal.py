#!/usr/bin/env python3
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

PRODUCT = "Citadel A.R.M.O.R."
SEALED_PHASES = [
    "MVP9_ALLOWLIST_VALIDATION",
    "MVP10_ROLLBACK_MANIFEST",
    "MVP11_ACTION_PREVIEW",
    "MVP12_ACTION_LEDGER",
    "MVP13_POST_ACTION_VERIFY",
    "MVP14_EMERGENCY_STOP",
    "MVP15_OPERATOR_CONFIRM",
    "MVP16_EXECUTION_READINESS",
    "MVP17_PRE_EXECUTION_FREEZE",
    "MVP18_PUBLIC_REGRESSION",
    "MVP19_PUBLIC_RELEASE_BUNDLE",
]
REQUIRED_PUBLIC_FILES = [
    "README.md",
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
    "MVP19_PUBLIC_RELEASE_BUNDLE_PLAN.md",
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
    "armor_public_release_bundle.py",
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
    "reports/public_release_bundle_public_sample.json",
]
NO_ACTION_GUARDS = [
    "no_public_release_seal_side_effects_beyond_public_sample_write",
    "no_action_execution",
    "no_restore_execution",
    "no_verification_execution",
    "no_gate_execution",
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

def presence(paths):
    return [{"path": path, "present": Path(path).exists()} for path in paths]

def build_seal(public):
    timestamp = "REDACTED_TIMESTAMP" if public else datetime.now(timezone.utc).isoformat()
    file_presence = presence(REQUIRED_PUBLIC_FILES)
    release_sealed = all(item["present"] for item in file_presence)
    return {
        "product": PRODUCT,
        "mode": "MVP20_PUBLIC_RELEASE_SEAL_REVIEW_ONLY",
        "seal_version": "0.1-review-only",
        "created_at": timestamp,
        "review_only": True,
        "enforcement": False,
        "actions_enabled": False,
        "remediation_enabled": False,
        "restore_executed": False,
        "scan_executed": False,
        "target_scan_executed": False,
        "action_executed": False,
        "verification_executed": False,
        "confirmation_collected": False,
        "emergency_stop_modified": False,
        "release_sealed": release_sealed,
        "sealed_through": "MVP19_PUBLIC_RELEASE_BUNDLE",
        "seal_phase": "MVP20_PUBLIC_RELEASE_SEAL",
        "public_boundary": "review_only_no_execution_no_remediation_no_scan",
        "sealed_phases": SEALED_PHASES,
        "required_public_files": file_presence,
        "no_action_guards": NO_ACTION_GUARDS,
        "safety_note": "Public release seal checks expected public showcase files only. It does not scan targets, expose commands, or execute actions.",
    }

def main():
    parser = argparse.ArgumentParser(description="Citadel A.R.M.O.R. review-only public release seal helper")
    parser.add_argument("--public", action="store_true", help="print public-safe release seal summary")
    parser.add_argument("--public-sample", action="store_true", help="write reports/public_release_seal_public_sample.json")
    args = parser.parse_args()
    public = args.public or args.public_sample
    report = build_seal(public)
    text = json.dumps(report, indent=2, sort_keys=True)
    print(text)
    if args.public_sample:
        out = Path("reports") / "public_release_seal_public_sample.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text + "\n", encoding="utf-8")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
