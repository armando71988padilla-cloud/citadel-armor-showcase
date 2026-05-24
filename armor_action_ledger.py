#!/usr/bin/env python3
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

PRODUCT = "Citadel A.R.M.O.R."

REQUIRED_LEDGER_FIELDS = [
    "ledger_version",
    "event_id",
    "action_id",
    "event_type",
    "stage",
    "target",
    "target_class",
    "allowlist_decision",
    "preview_id",
    "rollback_manifest_id",
    "operator_confirmation_state",
    "emergency_stop_checked",
    "result",
    "created_at",
]

LEDGER_EVENT_TYPES = [
    "preview_created",
    "operator_review_required",
    "rollback_manifest_required",
    "execution_blocked_review_only",
    "future_action_result_required",
]

NO_ACTION_GUARDS = [
    "no_ledger_execution_side_effects",
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

LEDGER_REQUIREMENTS = [
    "every_future_preview_requires_ledger_entry",
    "every_future_action_requires_ledger_entry_before_and_after",
    "operator_confirmation_state_must_be_recorded",
    "emergency_stop_check_result_must_be_recorded",
    "rollback_manifest_id_must_be_recorded",
    "post_action_verification_result_must_be_recorded",
    "public_output_must_be_redacted",
]

def build_ledger(public: bool, event_type: str, target: str, target_class: str, allowlist_decision: str) -> dict:
    timestamp = "REDACTED_TIMESTAMP" if public else datetime.now(timezone.utc).isoformat()
    return {
        "product": PRODUCT,
        "mode": "MVP12_ACTION_LEDGER_REVIEW_ONLY",
        "ledger_version": "0.1-review-only",
        "created_at": timestamp,
        "review_only": True,
        "enforcement": False,
        "actions_enabled": False,
        "remediation_enabled": False,
        "restore_executed": False,
        "scan_executed": False,
        "action_executed": False,
        "ledger_written_to_runtime": False,
        "event_id": "REVIEW_ONLY_EVENT_ID" if public else "local-review-only-event-id",
        "action_id": "REVIEW_ONLY_ACTION_ID" if public else "local-review-only-action-id",
        "event_type": event_type,
        "stage": "review_only_schema_preview",
        "target": target,
        "target_class": target_class,
        "allowlist_decision": allowlist_decision,
        "preview_id": "REQUIRED_BEFORE_FUTURE_ACTION",
        "rollback_manifest_id": "REQUIRED_BEFORE_FUTURE_ACTION",
        "operator_confirmation_state": "not_collected_review_only",
        "emergency_stop_checked": False,
        "result": "blocked_review_only",
        "required_ledger_fields": REQUIRED_LEDGER_FIELDS,
        "ledger_event_types": LEDGER_EVENT_TYPES,
        "ledger_requirements": LEDGER_REQUIREMENTS,
        "no_action_guards": NO_ACTION_GUARDS,
        "safety_note": "Action ledger schema review only. No runtime ledger is written and no files are scanned, restored, moved, deleted, quarantined, blocked, killed, isolated, or modified.",
    }

def main() -> int:
    parser = argparse.ArgumentParser(description="Citadel A.R.M.O.R. review-only action ledger schema helper")
    parser.add_argument("--public", action="store_true", help="print public-safe redacted action ledger schema")
    parser.add_argument("--public-sample", action="store_true", help="write reports/action_ledger_public_sample.json")
    parser.add_argument("--event-type", default="execution_blocked_review_only", choices=LEDGER_EVENT_TYPES, help="review-only event type to model")
    parser.add_argument("--target", default="reports/example_public_sample.json", help="future target being modeled as text only")
    parser.add_argument("--target-class", default="public_sample", help="future target class being modeled")
    parser.add_argument("--allowlist-decision", default="allowed", choices=["allowed", "denied", "unresolved"], help="review-only allowlist decision to model")
    args = parser.parse_args()
    public = args.public or args.public_sample
    ledger = build_ledger(public, args.event_type, args.target, args.target_class, args.allowlist_decision)
    text = json.dumps(ledger, indent=2, sort_keys=True)
    print(text)
    if args.public_sample:
        out = Path("reports") / "action_ledger_public_sample.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text + "\n", encoding="utf-8")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
