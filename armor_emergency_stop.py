#!/usr/bin/env python3
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

PRODUCT = "Citadel A.R.M.O.R."

REQUIRED_EMERGENCY_STOP_FIELDS = [
    "check_version",
    "check_id",
    "action_id",
    "stop_file_path_policy",
    "stop_state",
    "operator_override_allowed",
    "execution_blocked",
    "action_required",
    "ledger_event_required",
    "created_at",
]

STOP_STATES = [
    "blocked_review_only",
    "future_stop_file_present_blocks_execution",
    "future_stop_file_absent_allows_next_gate",
    "future_stop_state_unknown_blocks_execution",
]

NO_ACTION_GUARDS = [
    "no_emergency_stop_file_created_or_removed",
    "no_action_execution",
    "no_restore_execution",
    "no_verification_execution",
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

EMERGENCY_STOP_REQUIREMENTS = [
    "check_must_run_before_any_future_action_execution",
    "present_stop_file_blocks_execution",
    "unknown_stop_state_blocks_execution",
    "check_result_must_be_recorded_in_action_ledger",
    "operator_confirmation_cannot_override_stop_file",
    "public_output_must_be_redacted",
]

def build_check(public: bool, stop_state: str, action_id: str) -> dict:
    timestamp = "REDACTED_TIMESTAMP" if public else datetime.now(timezone.utc).isoformat()
    return {
        "product": PRODUCT,
        "mode": "MVP14_EMERGENCY_STOP_REVIEW_ONLY",
        "check_version": "0.1-review-only",
        "created_at": timestamp,
        "review_only": True,
        "enforcement": False,
        "actions_enabled": False,
        "remediation_enabled": False,
        "restore_executed": False,
        "scan_executed": False,
        "action_executed": False,
        "verification_executed": False,
        "emergency_stop_checked": False,
        "emergency_stop_modified": False,
        "check_id": "REVIEW_ONLY_CHECK_ID" if public else "local-review-only-check-id",
        "action_id": "REVIEW_ONLY_ACTION_ID" if public else action_id,
        "stop_file_path_policy": "REDACTED_PUBLIC_POLICY" if public else "local_policy_path_required_before_future_action",
        "stop_state": stop_state,
        "operator_override_allowed": False,
        "execution_blocked": True,
        "action_required": "remain_review_only",
        "ledger_event_required": True,
        "required_emergency_stop_fields": REQUIRED_EMERGENCY_STOP_FIELDS,
        "stop_states": STOP_STATES,
        "emergency_stop_requirements": EMERGENCY_STOP_REQUIREMENTS,
        "no_action_guards": NO_ACTION_GUARDS,
        "safety_note": "Emergency stop check schema review only. No stop file is created, removed, read from disk, or modified. No action is executed.",
    }

def main() -> int:
    parser = argparse.ArgumentParser(description="Citadel A.R.M.O.R. review-only emergency stop schema helper")
    parser.add_argument("--public", action="store_true", help="print public-safe redacted emergency stop schema")
    parser.add_argument("--public-sample", action="store_true", help="write reports/emergency_stop_public_sample.json")
    parser.add_argument("--stop-state", default="blocked_review_only", choices=STOP_STATES, help="review-only emergency stop state to model")
    parser.add_argument("--action-id", default="local-review-only-action-id", help="future action id being modeled")
    args = parser.parse_args()
    public = args.public or args.public_sample
    report = build_check(public, args.stop_state, args.action_id)
    text = json.dumps(report, indent=2, sort_keys=True)
    print(text)
    if args.public_sample:
        out = Path("reports") / "emergency_stop_public_sample.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text + "\n", encoding="utf-8")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
