#!/usr/bin/env python3
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

PRODUCT = "Citadel A.R.M.O.R."

REQUIRED_VERIFY_FIELDS = [
    "verification_version",
    "verification_id",
    "action_id",
    "target",
    "target_class",
    "expected_state",
    "observed_state",
    "pre_action_hash",
    "post_action_hash",
    "rollback_manifest_id",
    "ledger_event_id",
    "verification_result",
    "created_at",
]

VERIFY_RESULT_STATES = [
    "blocked_review_only",
    "future_pass_required",
    "future_fail_requires_rollback_review",
    "future_inconclusive_requires_manual_review",
]

NO_ACTION_GUARDS = [
    "no_verification_execution_side_effects",
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

POST_ACTION_VERIFY_REQUIREMENTS = [
    "verify_target_exists_or_expected_absence",
    "verify_hash_or_metadata_matches_expected_state",
    "verify_ledger_entry_exists",
    "verify_rollback_manifest_is_linked",
    "verify_operator_confirmation_state_is_recorded",
    "verify_emergency_stop_check_was_recorded",
    "failures_require_manual_review_before_any_future_rollback",
    "public_output_must_be_redacted",
]

def build_verification(public: bool, target: str, target_class: str, expected_state: str) -> dict:
    timestamp = "REDACTED_TIMESTAMP" if public else datetime.now(timezone.utc).isoformat()
    return {
        "product": PRODUCT,
        "mode": "MVP13_POST_ACTION_VERIFY_REVIEW_ONLY",
        "verification_version": "0.1-review-only",
        "created_at": timestamp,
        "review_only": True,
        "enforcement": False,
        "actions_enabled": False,
        "remediation_enabled": False,
        "restore_executed": False,
        "scan_executed": False,
        "action_executed": False,
        "verification_executed": False,
        "verification_id": "REVIEW_ONLY_VERIFICATION_ID" if public else "local-review-only-verification-id",
        "action_id": "REVIEW_ONLY_ACTION_ID" if public else "local-review-only-action-id",
        "target": target,
        "target_class": target_class,
        "expected_state": expected_state,
        "observed_state": "NOT_OBSERVED_REVIEW_ONLY",
        "pre_action_hash": "REQUIRED_BEFORE_FUTURE_ACTION",
        "post_action_hash": "REQUIRED_AFTER_FUTURE_ACTION",
        "rollback_manifest_id": "REQUIRED_BEFORE_FUTURE_ACTION",
        "ledger_event_id": "REQUIRED_FOR_FUTURE_ACTION",
        "verification_result": "blocked_review_only",
        "required_verify_fields": REQUIRED_VERIFY_FIELDS,
        "verify_result_states": VERIFY_RESULT_STATES,
        "post_action_verify_requirements": POST_ACTION_VERIFY_REQUIREMENTS,
        "no_action_guards": NO_ACTION_GUARDS,
        "safety_note": "Post-action verification schema review only. No verification probe is executed and no files are scanned, restored, moved, deleted, quarantined, blocked, killed, isolated, or modified.",
    }

def main() -> int:
    parser = argparse.ArgumentParser(description="Citadel A.R.M.O.R. review-only post-action verification schema helper")
    parser.add_argument("--public", action="store_true", help="print public-safe redacted post-action verification schema")
    parser.add_argument("--public-sample", action="store_true", help="write reports/post_action_verify_public_sample.json")
    parser.add_argument("--target", default="reports/example_public_sample.json", help="future target being modeled as text only")
    parser.add_argument("--target-class", default="public_sample", help="future target class being modeled")
    parser.add_argument("--expected-state", default="future_expected_state_required", help="future expected state being modeled")
    args = parser.parse_args()
    public = args.public or args.public_sample
    report = build_verification(public, args.target, args.target_class, args.expected_state)
    text = json.dumps(report, indent=2, sort_keys=True)
    print(text)
    if args.public_sample:
        out = Path("reports") / "post_action_verify_public_sample.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text + "\n", encoding="utf-8")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
