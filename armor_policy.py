#!/usr/bin/env python3
import argparse
import json
from datetime import datetime, timezone

PRODUCT = "Citadel A.R.M.O.R."

ALLOWED_PROFILE_CLASSES = [
    {
        "name": "armor_self_check",
        "scope": "root_level_armor_python_files_only",
        "execution": "review_only_scan",
        "notes": "Used to review ARMOR source safety without expanding target scope.",
    },
    {
        "name": "quick_downloads_preflight",
        "scope": "user_downloads_counts_only",
        "execution": "preflight_only_no_files_opened",
        "notes": "Counts candidate files and directories without printing filenames or opening files.",
    },
    {
        "name": "quick_downloads_chunk",
        "scope": "bounded_user_downloads_batches",
        "execution": "read_only_chunked_scan",
        "notes": "Requires explicit batch index and bounded batch size.",
    },
]

DENIED_TARGET_CLASSES = [
    "system_roots",
    "hidden_home_directories",
    "browser_profiles",
    "ssh_gpg_password_manager_wallet_token_key_credential_paths",
    "mounted_external_drives_without_separate_approval",
    "network_mounts",
    "project_vaults",
    "private_logs",
    "ignored_runtime_state",
]

FUTURE_ACTION_GATES = [
    "separate_release_path_required",
    "lockout_prevention_required",
    "explicit_allowlist_required",
    "manual_review_required",
    "no_default_remediation",
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

def build_policy(public: bool) -> dict:
    timestamp = "REDACTED_TIMESTAMP" if public else datetime.now(timezone.utc).isoformat()
    return {
        "product": PRODUCT,
        "mode": "MVP7_SAFE_TARGET_POLICY_REVIEW_ONLY",
        "timestamp": timestamp,
        "review_only": True,
        "enforcement": False,
        "scan_executed": False,
        "deny_by_default": True,
        "allowed_profile_classes": ALLOWED_PROFILE_CLASSES,
        "denied_target_classes": DENIED_TARGET_CLASSES,
        "future_action_gates": FUTURE_ACTION_GATES,
        "no_action_guards": NO_ACTION_GUARDS,
        "safety_note": "Policy review only. No files scanned, opened, moved, deleted, quarantined, or modified.",
    }

def main() -> int:
    parser = argparse.ArgumentParser(description="Citadel A.R.M.O.R. read-only safe target policy helper")
    parser.add_argument("--public", action="store_true", help="print public-safe redacted policy output")
    args = parser.parse_args()
    print(json.dumps(build_policy(args.public), indent=2, sort_keys=True))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
