#!/usr/bin/env python3
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

PRODUCT = "Citadel A.R.M.O.R."

REQUIRED_PREVIEW_FIELDS = [
    "preview_version",
    "action_id",
    "action_type",
    "target",
    "target_class",
    "allowlist_decision",
    "rollback_manifest_required",
    "operator_confirmation_required",
    "emergency_stop_required",
    "execution_ready",
    "execution_command_available",
    "created_at",
]

NO_ACTION_GUARDS = [
    "no_action_execution",
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
    "no_scan_execution",
]

FUTURE_EXECUTION_REQUIREMENTS = [
    "allowlist_decision_must_be_allowed",
    "rollback_manifest_must_exist",
    "operator_confirmation_phrase_required",
    "emergency_stop_file_check_required",
    "action_ledger_entry_required",
    "post_action_verification_required",
    "release_freeze_checkpoint_required",
]

def build_preview(public: bool, action_type: str, target: str, target_class: str, allowlist_decision: str) -> dict:
    timestamp = "REDACTED_TIMESTAMP" if public else datetime.now(timezone.utc).isoformat()
    blockers = [
        "mvp11_review_only_no_execution_path",
        "rollback_manifest_not_attached",
        "operator_confirmation_not_collected",
        "emergency_stop_not_checked",
    ]
    if allowlist_decision != "allowed":
        blockers.append("allowlist_decision_not_allowed")
    return {
        "product": PRODUCT,
        "mode": "MVP11_ACTION_PREVIEW_REVIEW_ONLY",
        "preview_version": "0.1-review-only",
        "created_at": timestamp,
        "review_only": True,
        "enforcement": False,
        "actions_enabled": False,
        "remediation_enabled": False,
        "restore_executed": False,
        "scan_executed": False,
        "action_executed": False,
        "execution_ready": False,
        "execution_command_available": False,
        "action_id": "REVIEW_ONLY_ACTION_ID" if public else "local-review-only-action-id",
        "action_type": action_type,
        "target": target,
        "target_class": target_class,
        "allowlist_decision": allowlist_decision,
        "rollback_manifest_required": True,
        "operator_confirmation_required": True,
        "emergency_stop_required": True,
        "required_preview_fields": REQUIRED_PREVIEW_FIELDS,
        "future_execution_requirements": FUTURE_EXECUTION_REQUIREMENTS,
        "no_action_guards": NO_ACTION_GUARDS,
        "blockers": blockers,
        "safety_note": "Action preview review only. No files are scanned, restored, moved, deleted, quarantined, blocked, killed, isolated, or modified.",
    }

def main() -> int:
    parser = argparse.ArgumentParser(description="Citadel A.R.M.O.R. review-only action preview helper")
    parser.add_argument("--public", action="store_true", help="print public-safe redacted action preview")
    parser.add_argument("--public-sample", action="store_true", help="write reports/action_preview_public_sample.json")
    parser.add_argument("--action-type", default="future_review_only_action", help="future action type being previewed")
    parser.add_argument("--target", default="reports/example_public_sample.json", help="future target being previewed as text only")
    parser.add_argument("--target-class", default="public_sample", help="future target class being previewed")
    parser.add_argument("--allowlist-decision", default="allowed", choices=["allowed", "denied", "unresolved"], help="review-only allowlist decision to model")
    args = parser.parse_args()
    public = args.public or args.public_sample
    preview = build_preview(public, args.action_type, args.target, args.target_class, args.allowlist_decision)
    text = json.dumps(preview, indent=2, sort_keys=True)
    print(text)
    if args.public_sample:
        out = Path("reports") / "action_preview_public_sample.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text + "\n", encoding="utf-8")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
