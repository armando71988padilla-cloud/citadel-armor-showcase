#!/usr/bin/env python3
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

PRODUCT = "Citadel A.R.M.O.R."

REQUIRED_FREEZE_FIELDS = [
    "freeze_version",
    "freeze_id",
    "action_id",
    "freeze_decision",
    "freeze_required",
    "execution_ready",
    "execution_command_available",
    "checklist_items",
    "blocking_reasons",
    "operator_review_required",
    "created_at",
]

FREEZE_CHECKS = [
    "allowlist_validation_reviewed",
    "rollback_manifest_attached",
    "action_preview_reviewed",
    "emergency_stop_checked",
    "operator_confirmation_valid",
    "action_ledger_ready",
    "post_action_verification_plan_ready",
    "execution_readiness_reviewed",
]

NO_ACTION_GUARDS = [
    "no_pre_execution_freeze_side_effects",
    "no_gate_execution",
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

FREEZE_REQUIREMENTS = [
    "freeze_required_when_any_gate_is_missing",
    "freeze_required_when_any_gate_is_unknown",
    "freeze_required_when_any_gate_is_review_only",
    "freeze_required_when_emergency_stop_is_present_or_unknown",
    "freeze_required_when_operator_confirmation_is_missing_or_invalid",
    "freeze_required_when_rollback_manifest_is_missing",
    "freeze_required_when_action_ledger_is_not_ready",
    "freeze_required_when_post_action_verification_plan_is_missing",
    "public_output_must_be_redacted",
]

def build_checklist() -> list:
    return [
        {"check": check, "state": "required_before_future_execution", "passed": False}
        for check in FREEZE_CHECKS
    ]

def build_freeze(public: bool, action_id: str, target_class: str) -> dict:
    timestamp = "REDACTED_TIMESTAMP" if public else datetime.now(timezone.utc).isoformat()
    rendered_action_id = "REVIEW_ONLY_ACTION_ID" if public else action_id
    checklist_items = build_checklist()
    blocking_reasons = [
        "mvp17_review_only_no_execution_path",
        "pre_execution_checks_not_executed",
        "execution_readiness_not_passed",
        "operator_confirmation_not_valid",
        "emergency_stop_not_checked",
        "rollback_manifest_not_attached",
        "action_ledger_not_ready",
        "post_action_verification_plan_not_ready",
    ]
    return {
        "product": PRODUCT,
        "mode": "MVP17_PRE_EXECUTION_FREEZE_REVIEW_ONLY",
        "freeze_version": "0.1-review-only",
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
        "pre_execution_checks_executed": False,
        "execution_ready": False,
        "execution_command_available": False,
        "freeze_required": True,
        "freeze_decision": "freeze_required_review_only",
        "operator_review_required": True,
        "freeze_id": "REVIEW_ONLY_FREEZE_ID" if public else "local-review-only-freeze-id",
        "action_id": rendered_action_id,
        "target_class": target_class,
        "required_freeze_fields": REQUIRED_FREEZE_FIELDS,
        "freeze_checks": FREEZE_CHECKS,
        "checklist_items": checklist_items,
        "blocking_reasons": blocking_reasons,
        "freeze_requirements": FREEZE_REQUIREMENTS,
        "no_action_guards": NO_ACTION_GUARDS,
        "safety_note": "Pre-execution freeze checklist schema review only. No gates are executed, no command is exposed, and no action is executed.",
    }

def main() -> int:
    parser = argparse.ArgumentParser(description="Citadel A.R.M.O.R. review-only pre-execution freeze checklist helper")
    parser.add_argument("--public", action="store_true", help="print public-safe redacted pre-execution freeze checklist")
    parser.add_argument("--public-sample", action="store_true", help="write reports/pre_execution_freeze_public_sample.json")
    parser.add_argument("--action-id", default="local-review-only-action-id", help="future action id being modeled")
    parser.add_argument("--target-class", default="public_sample", help="future target class being modeled")
    args = parser.parse_args()
    public = args.public or args.public_sample
    report = build_freeze(public, args.action_id, args.target_class)
    text = json.dumps(report, indent=2, sort_keys=True)
    print(text)
    if args.public_sample:
        out = Path("reports") / "pre_execution_freeze_public_sample.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text + "\n", encoding="utf-8")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
