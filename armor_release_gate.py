#!/usr/bin/env python3
import argparse
import json
from datetime import datetime, timezone

PRODUCT = "Citadel A.R.M.O.R."

REQUIRED_FUTURE_GATES = [
    "allowlist_validation_helper",
    "rollback_manifest_format",
    "action_preview_format",
    "explicit_operator_confirmation_phrase",
    "emergency_stop_file_check",
    "action_ledger",
    "post_action_verification",
    "release_freeze_checkpoint",
]

LOCKOUT_PREVENTION_REQUIREMENTS = [
    "never_disable_all_network_paths",
    "never_block_loopback_services",
    "never_modify_firewall_defaults_without_restore_file",
    "never_kill_critical_user_session_shell_ssh_desktop_network_or_package_manager_processes",
    "never_change_ownership_or_permissions_recursively",
    "never_touch_credential_key_wallet_browser_profile_password_manager_or_hidden_home_paths",
    "never_modify_system_roots",
    "never_act_on_external_drives_or_network_mounts_without_separate_approval_phase",
]

FUTURE_ACTION_PRINCIPLES = [
    "opt_in_only",
    "dry_run_first",
    "preview_before_execution",
    "rollback_plan_before_execution",
    "private_local_action_report_required",
    "public_output_redacted",
    "no_action_from_broad_scan_result_alone",
    "explicit_profile_and_target_class_approval_required",
]

NO_ACTION_GUARDS = [
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

def build_release_gate(public: bool) -> dict:
    timestamp = "REDACTED_TIMESTAMP" if public else datetime.now(timezone.utc).isoformat()
    return {
        "product": PRODUCT,
        "mode": "MVP8_RELEASE_GATE_REVIEW_ONLY",
        "timestamp": timestamp,
        "review_only": True,
        "enforcement": False,
        "remediation_enabled": False,
        "scan_executed": False,
        "actions_enabled": False,
        "required_future_gates": REQUIRED_FUTURE_GATES,
        "lockout_prevention_requirements": LOCKOUT_PREVENTION_REQUIREMENTS,
        "future_action_principles": FUTURE_ACTION_PRINCIPLES,
        "no_action_guards": NO_ACTION_GUARDS,
        "safety_note": "Release gate review only. No files scanned, opened, moved, deleted, quarantined, blocked, killed, isolated, or modified.",
    }

def main() -> int:
    parser = argparse.ArgumentParser(description="Citadel A.R.M.O.R. read-only release gate helper")
    parser.add_argument("--public", action="store_true", help="print public-safe redacted release gate output")
    args = parser.parse_args()
    print(json.dumps(build_release_gate(args.public), indent=2, sort_keys=True))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
