#!/usr/bin/env python3
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

PRODUCT = "Citadel A.R.M.O.R."

REQUIRED_ROLLBACK_FIELDS = [
    "manifest_version",
    "action_id",
    "action_type",
    "target",
    "target_class",
    "operator_confirmation_required",
    "pre_action_hash",
    "post_action_hash",
    "backup_path",
    "restore_preview",
    "emergency_stop_checked",
    "created_at",
]

NO_ACTION_GUARDS = [
    "no_restore_execution",
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

ROLLBACK_REQUIREMENTS = [
    "backup_must_exist_before_action",
    "target_hash_must_be_recorded_before_action",
    "restore_preview_must_be_human_readable",
    "emergency_stop_file_must_be_checked",
    "action_ledger_entry_required",
    "post_action_verification_required",
    "manual_confirmation_required_before_any_future_restore",
]

def build_manifest(public: bool, action_type: str, target: str, target_class: str) -> dict:
    timestamp = "REDACTED_TIMESTAMP" if public else datetime.now(timezone.utc).isoformat()
    return {
        "product": PRODUCT,
        "mode": "MVP10_ROLLBACK_MANIFEST_REVIEW_ONLY",
        "manifest_version": "0.1-review-only",
        "created_at": timestamp,
        "review_only": True,
        "enforcement": False,
        "actions_enabled": False,
        "remediation_enabled": False,
        "restore_executed": False,
        "scan_executed": False,
        "action_id": "REVIEW_ONLY_ACTION_ID" if public else "local-review-only-action-id",
        "action_type": action_type,
        "target": target,
        "target_class": target_class,
        "operator_confirmation_required": True,
        "required_rollback_fields": REQUIRED_ROLLBACK_FIELDS,
        "rollback_requirements": ROLLBACK_REQUIREMENTS,
        "no_action_guards": NO_ACTION_GUARDS,
        "pre_action_hash": "REQUIRED_BEFORE_FUTURE_ACTION",
        "post_action_hash": "REQUIRED_AFTER_FUTURE_ACTION",
        "backup_path": "REQUIRED_BEFORE_FUTURE_ACTION",
        "restore_preview": {
            "available": False,
            "reason": "MVP10 is review-only and does not generate executable restore commands.",
        },
        "emergency_stop_checked": False,
        "safety_note": "Rollback manifest review only. No files are restored, moved, deleted, quarantined, blocked, killed, isolated, or modified.",
    }

def main() -> int:
    parser = argparse.ArgumentParser(description="Citadel A.R.M.O.R. review-only rollback manifest helper")
    parser.add_argument("--public", action="store_true", help="print public-safe redacted rollback manifest")
    parser.add_argument("--public-sample", action="store_true", help="write reports/rollback_manifest_public_sample.json")
    parser.add_argument("--action-type", default="future_review_only_action", help="future action type being modeled")
    parser.add_argument("--target", default="reports/example_public_sample.json", help="future target being modeled as text only")
    parser.add_argument("--target-class", default="public_sample", help="future target class being modeled")
    args = parser.parse_args()
    public = args.public or args.public_sample
    manifest = build_manifest(public, args.action_type, args.target, args.target_class)
    text = json.dumps(manifest, indent=2, sort_keys=True)
    print(text)
    if args.public_sample:
        out = Path("reports") / "rollback_manifest_public_sample.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text + "\n", encoding="utf-8")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
