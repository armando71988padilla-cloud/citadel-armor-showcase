#!/usr/bin/env python3
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

PRODUCT = "Citadel A.R.M.O.R."

REQUIRED_CONFIRM_FIELDS = [
    "confirmation_version",
    "confirmation_id",
    "action_id",
    "required_phrase_template",
    "provided_phrase_state",
    "confirmation_valid",
    "emergency_stop_override_allowed",
    "execution_ready",
    "ledger_event_required",
    "created_at",
]

CONFIRMATION_STATES = [
    "not_collected_review_only",
    "future_missing_blocks_execution",
    "future_mismatch_blocks_execution",
    "future_match_allows_next_gate_only",
]

NO_ACTION_GUARDS = [
    "no_confirmation_collection",
    "no_action_execution",
    "no_restore_execution",
    "no_verification_execution",
    "no_emergency_stop_override",
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

CONFIRMATION_REQUIREMENTS = [
    "exact_phrase_required_before_any_future_action_execution",
    "phrase_must_include_action_id",
    "phrase_must_include_target_class",
    "phrase_must_include_reviewed_risk_level",
    "confirmation_result_must_be_recorded_in_action_ledger",
    "confirmation_cannot_override_emergency_stop",
    "public_output_must_be_redacted",
]

def build_confirmation(public: bool, action_id: str, target_class: str, risk_level: str) -> dict:
    timestamp = "REDACTED_TIMESTAMP" if public else datetime.now(timezone.utc).isoformat()
    rendered_action_id = "REVIEW_ONLY_ACTION_ID" if public else action_id
    phrase = f"CONFIRM ARMOR ACTION {rendered_action_id} TARGET_CLASS {target_class} RISK {risk_level}"
    return {
        "product": PRODUCT,
        "mode": "MVP15_OPERATOR_CONFIRM_REVIEW_ONLY",
        "confirmation_version": "0.1-review-only",
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
        "confirmation_valid": False,
        "execution_ready": False,
        "confirmation_id": "REVIEW_ONLY_CONFIRMATION_ID" if public else "local-review-only-confirmation-id",
        "action_id": rendered_action_id,
        "target_class": target_class,
        "risk_level": risk_level,
        "required_phrase_template": phrase,
        "provided_phrase_state": "not_collected_review_only",
        "emergency_stop_override_allowed": False,
        "ledger_event_required": True,
        "required_confirm_fields": REQUIRED_CONFIRM_FIELDS,
        "confirmation_states": CONFIRMATION_STATES,
        "confirmation_requirements": CONFIRMATION_REQUIREMENTS,
        "no_action_guards": NO_ACTION_GUARDS,
        "safety_note": "Operator confirmation schema review only. No confirmation is collected and no action is executed.",
    }

def main() -> int:
    parser = argparse.ArgumentParser(description="Citadel A.R.M.O.R. review-only operator confirmation schema helper")
    parser.add_argument("--public", action="store_true", help="print public-safe redacted operator confirmation schema")
    parser.add_argument("--public-sample", action="store_true", help="write reports/operator_confirm_public_sample.json")
    parser.add_argument("--action-id", default="local-review-only-action-id", help="future action id being modeled")
    parser.add_argument("--target-class", default="public_sample", help="future target class being modeled")
    parser.add_argument("--risk-level", default="review_only", help="future reviewed risk level being modeled")
    args = parser.parse_args()
    public = args.public or args.public_sample
    report = build_confirmation(public, args.action_id, args.target_class, args.risk_level)
    text = json.dumps(report, indent=2, sort_keys=True)
    print(text)
    if args.public_sample:
        out = Path("reports") / "operator_confirm_public_sample.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text + "\n", encoding="utf-8")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
