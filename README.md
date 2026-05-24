# Citadel A.R.M.O.R.

Autonomous Response Monitoring Operations and Resilience.

Citadel A.R.M.O.R. is a local-first active defense module for Citadel-AI.

Standalone showcase root:

- this repository

## Current status

MVP 1 is frozen as a stable read-only checkpoint.

Current capabilities:

- read-only local status probe
- read-only status capture helper
- read-only known good baseline capture
- public-safe redacted status sample
- public-safe redacted baseline sample
- private runtime snapshots ignored by Git

Current safety boundary:

- no firewall changes
- no Wi-Fi changes
- no Bluetooth changes
- no USB blocking
- no quarantine
- no purge
- no lockdown
- no enforcement

## Public-safe files

- SHOWCASE.md
- MVP1_STATUS.md
- MVP2_SCAN_STATUS.md
- MVP3_DETECTION_STATUS.md
- BASELINE_PLAN.md
- MVP4_SCAN_PROFILE_PLAN.md
- MVP4_DRY_RUN_STATUS.md
- MVP4_QUICK_DOWNLOADS_SCAN_PLAN.md
- MVP4_QUICK_DOWNLOADS_SCAN_STATUS.md
- MVP4_CHUNKED_SCAN_PLAN.md
- MVP4_CHUNKED_SCAN_STATUS.md
- MVP5_BATCH_REPORTING_PLAN.md
- MVP5_BATCH_REPORTING_STATUS.md
- MVP5_BATCH_REPORTING_FREEZE_STATUS.md
- MVP6_AGGREGATE_REPORTING_PLAN.md
- MVP6_AGGREGATE_REPORTING_FREEZE_STATUS.md
- HANDOFF_MVP6_SEALED.md
- MVP7_SAFE_TARGET_POLICY_PLAN.md
- MVP7_SAFE_TARGET_POLICY_FREEZE_STATUS.md
- MVP8_RELEASE_PATH_LOCKOUT_PLAN.md
- MVP8_RELEASE_GATE_FREEZE_STATUS.md
- HANDOFF_MVP8_SEALED.md
- reports/status_public_sample.json
- reports/baseline_public_sample.json
- reports/scan_public_sample.json
- reports/self_check_public_sample.json
- reports/quick_downloads_dry_run_public_sample.json
- reports/quick_downloads_preflight_public_sample.json
- reports/quick_downloads_chunk_public_sample.json
- reports/quick_downloads_aggregate_public_sample.json
- reports/policy_public_sample.json
- reports/release_gate_public_sample.json

## Local private files

Private runtime files are intentionally ignored by Git:

- state/status_private_*.json
- baseline/baseline_private_*.json
- logs/*.log
- vault/*
- whitelist/*

## Commands

Run read-only status:

    python3 armor_status.py

Run public-safe status:

    python3 armor_status.py --public

Capture private and public-safe status:

    python3 armor_capture_status.py

Capture private and public-safe baseline:

    python3 armor_baseline.py

Review latest private baseline safely:

    python3 armor_review_baseline.py

Inspect MVP 2 scan dependencies and planned profiles:

    python3 armor_scan.py --deps --profiles --public

Dry-run the quick_downloads profile without scanning:

    python3 armor_scan.py --dry-run-profile quick_downloads --public

Preflight the quick_downloads profile without scanning:

    python3 armor_scan.py --preflight-profile quick_downloads --public

Run one bounded quick_downloads chunk scan:

    python3 armor_scan.py --run-chunk-profile quick_downloads --batch-index 0 --public

Review aggregate quick_downloads chunk reports safely:

    python3 armor_review_batches.py

Review safe target policy:

    python3 armor_policy.py --public

Review release gate requirements:

    python3 armor_release_gate.py --public

Run the approved read-only self-check scan:

    python3 armor_scan.py --run-profile citadel_armor_self_check --public

Review the latest private self-check scan safely:

    python3 armor_review_scan.py

## Development rule

Build order is inspect, backup, patch, verify, commit. No enforcement features are allowed until the whitelist, release path, and lockout prevention rules are proven.

