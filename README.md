# Citadel A.R.M.O.R.

Autonomous Response Monitoring Operations and Resilience.

Citadel A.R.M.O.R. is a local-first active defense module for Citadel-AI.

Standalone showcase root:

- this repository
- quickstart: QUICKSTART.md
- architecture: ARCHITECTURE.md
- artifact index: ARTIFACTS.md
- verification guide: VERIFY.md

## Current status

Citadel A.R.M.O.R. is sealed through **MVP20 public release seal** as a review-only, public-safe active defense showcase.

This repository demonstrates a controlled security workflow for local-first systems:

- read-only status and baseline capture
- bounded scan planning and dry-run reporting
- safe target policy and release gate checks
- allowlist validation before any future action
- rollback manifest planning before any future action
- action preview, action ledger, and post-action verification schemas
- emergency stop and operator confirmation schemas
- execution readiness and pre-execution freeze aggregation
- public regression and release seal summaries

Current safety boundary:

- review only
- no enforcement
- no remediation
- no target scanning in release seal helpers
- no action execution
- no restore execution
- no quarantine
- no purge
- no lockdown
- no firewall changes
- no Wi-Fi changes
- no Bluetooth changes
- no USB blocking
- no permission changes
- no process kill

## Architecture / safety pipeline

```text
status / baseline
  -> scan planning and public samples
  -> safe target policy
  -> release gate
  -> allowlist validation
  -> rollback manifest
  -> action preview
  -> action ledger
  -> post-action verification plan
  -> emergency stop schema
  -> operator confirmation schema
  -> execution readiness aggregation
  -> pre-execution freeze checklist
  -> public regression aggregation
  -> public release bundle
  -> public release seal
```

Every layer is designed to prove intent, scope, rollback, operator review, and safety boundaries before any future enforcement work is considered.

## Milestone summary

| Phase | Focus | Public-safe output |
|---|---|---|
| MVP1-MVP3 | Status, baseline, detection foundation | Redacted status, baseline, and scan samples |
| MVP4-MVP6 | Bounded scan profiles and aggregate reporting | Dry-run, preflight, chunk, and aggregate samples |
| MVP7 | Safe target policy | `armor_policy.py --public` |
| MVP8 | Release gate / lockout prevention | `armor_release_gate.py --public` |
| MVP9 | Review-only allowlist validation | `armor_allowlist_validate.py --public-sample` |
| MVP10 | Rollback manifest planning | `armor_rollback_manifest.py --public-sample` |
| MVP11 | Action preview schema | `armor_action_preview.py --public-sample` |
| MVP12 | Action ledger schema | `armor_action_ledger.py --public-sample` |
| MVP13 | Post-action verification schema | `armor_post_action_verify.py --public-sample` |
| MVP14 | Emergency stop schema | `armor_emergency_stop.py --public-sample` |
| MVP15 | Operator confirmation schema | `armor_operator_confirm.py --public-sample` |
| MVP16 | Execution readiness aggregation | `armor_execution_readiness.py --public-sample` |
| MVP17 | Pre-execution freeze checklist | `armor_pre_execution_freeze.py --public-sample` |
| MVP18 | Public regression aggregation | `armor_public_regression.py --public-sample` |
| MVP19 | Public release bundle summary | `armor_public_release_bundle.py --public-sample` |
| MVP20 | Public release seal | `armor_public_release_seal.py --public-sample` |

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
- MVP9_ALLOWLIST_VALIDATION_PLAN.md
- MVP9_ALLOWLIST_VALIDATION_FREEZE_STATUS.md
- MVP10_ROLLBACK_MANIFEST_PLAN.md
- MVP10_ROLLBACK_MANIFEST_FREEZE_STATUS.md
- MVP11_ACTION_PREVIEW_PLAN.md
- MVP11_ACTION_PREVIEW_FREEZE_STATUS.md
- MVP12_ACTION_LEDGER_PLAN.md
- MVP12_ACTION_LEDGER_FREEZE_STATUS.md
- MVP13_POST_ACTION_VERIFY_PLAN.md
- MVP13_POST_ACTION_VERIFY_FREEZE_STATUS.md
- MVP14_EMERGENCY_STOP_PLAN.md
- MVP14_EMERGENCY_STOP_FREEZE_STATUS.md
- MVP15_OPERATOR_CONFIRM_PLAN.md
- MVP15_OPERATOR_CONFIRM_FREEZE_STATUS.md
- MVP16_EXECUTION_READINESS_PLAN.md
- MVP16_EXECUTION_READINESS_FREEZE_STATUS.md
- MVP17_PRE_EXECUTION_FREEZE_PLAN.md
- MVP17_PRE_EXECUTION_FREEZE_STATUS.md
- MVP18_PUBLIC_REGRESSION_PLAN.md
- MVP18_PUBLIC_REGRESSION_STATUS.md
- MVP19_PUBLIC_RELEASE_BUNDLE_PLAN.md
- MVP19_PUBLIC_RELEASE_BUNDLE_STATUS.md
- MVP20_PUBLIC_RELEASE_SEAL_PLAN.md
- MVP20_PUBLIC_RELEASE_SEAL_STATUS.md
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
- reports/allowlist_validation_public_sample.json
- reports/rollback_manifest_public_sample.json
- reports/action_preview_public_sample.json
- reports/action_ledger_public_sample.json
- reports/post_action_verify_public_sample.json
- reports/emergency_stop_public_sample.json
- reports/operator_confirm_public_sample.json
- reports/execution_readiness_public_sample.json
- reports/pre_execution_freeze_public_sample.json
- reports/public_regression_public_sample.json
- reports/public_release_bundle_public_sample.json
- reports/public_release_seal_public_sample.json

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

