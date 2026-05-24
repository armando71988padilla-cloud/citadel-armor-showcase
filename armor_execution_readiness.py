#!/usr/bin/env python3
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

PRODUCT = "Citadel A.R.M.O.R."

REQUIRED_READINESS_FIELDS = [
    "readiness_version",
    "readiness_id",
    "action_id",
    "gate_results",
    "blocking_reasons",
    "execution_ready",
    "execution_command_available",
    "release_freeze_required",
    "operator_review_required",
    "created_at",
]

REQUIRED_GATES = [
    "allowlist_validation",
    "rollback_manifest",
    "action_preview",
    "emergency_stop_check",
    "operator_confirmation",
    "action_ledger",
    "post_action_verification_plan",
]

NO_ACTION_GUARDS = [
    "no_execution_readiness_side_effects",
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

READINESS_REQUIREMENTS = [
    "all_future_gates_must_pass_before_execution_ready",
    "any_unknown_gate_blocks_execution",
    "any_review_only_gate_blocks_execution",
    "emergency_stop_blocks_execution_when_present_or_unknown",
    "operator_confirmation_must_be_valid_and_recorded",
    "rollback_manifest_must_be_present",
    "action_ledger_entry_must_be_ready",
    "public_output_must_be_redacted",
]

def build_gate_results() -> list:
    return [
        {"gate": gate, "state": "required_before_future_action", "passed": False}
        for gate in REQUIRED_GATES
    ]

def build_readiness(public: bool, action_id: str, target_class: str) -> dict:
    timestamp = "REDACTED_TIMESTAMP" if public else datetime.now(timezone.utc).isoformat()
    rendered_action_id = "REVIEW_ONLY_ACTION_ID" if public else action_id
    gate_results = build_gate_results()
    blocking_reasons = [
        "mvp16_review_only_no_execution_path",
        "required_gates_not_executed",
        "operator_confirmation_not_collected",
        "emergency_stop_not_checked",
        "rollback_manifest_not_attached",
        "action_ledger_not_written",
        "post_action_verification_not_available",
    ]
    return {
        "product": PRODUCT,
        "mode": "MVP16_EXECUTION_READINESS_REVIEW_ONLY",
        "readiness_version": "0.1-review-only",
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
        "execution_ready": False,
        "execution_command_available": False,
        "release_freeze_required": True,
        "operator_review_required": True,
        "readiness_id": "REVIEW_ONLY_READINESS_ID" if public else "local-review-only-readiness-id",
        "action_id": rendered_action_id,
        "target_class": target_class,
        "required_readiness_fields": REQUIRED_READINESS_FIELDS,
        "required_gates": REQUIRED_GATES,
        "gate_results": gate_results,
        "blocking_reasons": blocking_reasons,
        "readiness_requirements": READINESS_REQUIREMENTS,
        "no_action_guards": NO_ACTION_GUARDS,
        "safety_note": "Execution readiness schema review only. No gates are executed, no command is exposed, and no action is executed.",
    }

def main() -> int:
    parser = argparse.ArgumentParser(description="Citadel A.R.M.O.R. review-only execution readiness schema helper")
    parser.add_argument("--public", action="store_true", help="print public-safe redacted execution readiness schema")
    parser.add_argument("--public-sample", action="store_true", help="write reports/execution_readiness_public_sample.json")
    parser.add_argument("--action-id", default="local-review-only-action-id", help="future action id being modeled")
    parser.add_argument("--target-class", default="public_sample", help="future target class being modeled")
    args = parser.parse_args()
    public = args.public or args.public_sample
    report = build_readiness(public, args.action_id, args.target_class)
    text = json.dumps(report, indent=2, sort_keys=True)
    print(text)
    if args.public_sample:
        out = Path("reports") / "execution_readiness_public_sample.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text + "\n", encoding="utf-8")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
