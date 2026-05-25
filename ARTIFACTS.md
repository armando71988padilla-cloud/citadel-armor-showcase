# Citadel A.R.M.O.R. Public Artifact Index

This index maps the public-safe ARMOR showcase files by purpose.

## Start here

| File | Purpose |
|---|---|
| README.md | Main public overview and milestone summary |
| QUICKSTART.md | Shortest safe review path |
| VERIFY.md | Public verification commands and expected outputs |
| ARCHITECTURE.md | Safety pipeline and helper layer overview |

## Release seal artifacts

| File | Purpose |
|---|---|
| MVP20_PUBLIC_RELEASE_SEAL_PLAN.md | Public release seal plan |
| MVP20_PUBLIC_RELEASE_SEAL_STATUS.md | Public release seal status |
| armor_public_release_seal.py | Review-only public release seal helper |
| reports/public_release_seal_public_sample.json | Public release seal sample output |

## Aggregation artifacts

| Phase | Plan/status | Helper | Sample |
|---|---|---|---|
| MVP18 | MVP18_PUBLIC_REGRESSION_PLAN.md / MVP18_PUBLIC_REGRESSION_STATUS.md | armor_public_regression.py | reports/public_regression_public_sample.json |
| MVP19 | MVP19_PUBLIC_RELEASE_BUNDLE_PLAN.md / MVP19_PUBLIC_RELEASE_BUNDLE_STATUS.md | armor_public_release_bundle.py | reports/public_release_bundle_public_sample.json |
| MVP20 | MVP20_PUBLIC_RELEASE_SEAL_PLAN.md / MVP20_PUBLIC_RELEASE_SEAL_STATUS.md | armor_public_release_seal.py | reports/public_release_seal_public_sample.json |

## Pre-execution safety artifacts

| Phase | Plan/status | Helper | Sample |
|---|---|---|---|
| MVP14 | MVP14_EMERGENCY_STOP_PLAN.md / MVP14_EMERGENCY_STOP_FREEZE_STATUS.md | armor_emergency_stop.py | reports/emergency_stop_public_sample.json |
| MVP15 | MVP15_OPERATOR_CONFIRM_PLAN.md / MVP15_OPERATOR_CONFIRM_FREEZE_STATUS.md | armor_operator_confirm.py | reports/operator_confirm_public_sample.json |
| MVP16 | MVP16_EXECUTION_READINESS_PLAN.md / MVP16_EXECUTION_READINESS_FREEZE_STATUS.md | armor_execution_readiness.py | reports/execution_readiness_public_sample.json |
| MVP17 | MVP17_PRE_EXECUTION_FREEZE_PLAN.md / MVP17_PRE_EXECUTION_FREEZE_STATUS.md | armor_pre_execution_freeze.py | reports/pre_execution_freeze_public_sample.json |

## Action-planning artifacts

| Phase | Plan/status | Helper | Sample |
|---|---|---|---|
| MVP9 | MVP9_ALLOWLIST_VALIDATION_PLAN.md / MVP9_ALLOWLIST_VALIDATION_FREEZE_STATUS.md | armor_allowlist_validate.py | reports/allowlist_validation_public_sample.json |
| MVP10 | MVP10_ROLLBACK_MANIFEST_PLAN.md / MVP10_ROLLBACK_MANIFEST_FREEZE_STATUS.md | armor_rollback_manifest.py | reports/rollback_manifest_public_sample.json |
| MVP11 | MVP11_ACTION_PREVIEW_PLAN.md / MVP11_ACTION_PREVIEW_FREEZE_STATUS.md | armor_action_preview.py | reports/action_preview_public_sample.json |
| MVP12 | MVP12_ACTION_LEDGER_PLAN.md / MVP12_ACTION_LEDGER_FREEZE_STATUS.md | armor_action_ledger.py | reports/action_ledger_public_sample.json |
| MVP13 | MVP13_POST_ACTION_VERIFY_PLAN.md / MVP13_POST_ACTION_VERIFY_FREEZE_STATUS.md | armor_post_action_verify.py | reports/post_action_verify_public_sample.json |

## Foundation artifacts

| Phase | Purpose | Representative files |
|---|---|---|
| MVP1-MVP3 | Status, baseline, scan, and detection foundation | MVP1_STATUS.md, MVP2_SCAN_STATUS.md, MVP3_DETECTION_STATUS.md |
| MVP4-MVP6 | Profile planning, chunking, batch, and aggregate reporting | MVP4_* files, MVP5_* files, MVP6_* files |
| MVP7 | Safe target policy | MVP7_SAFE_TARGET_POLICY_PLAN.md, armor_policy.py, reports/policy_public_sample.json |
| MVP8 | Release gate and lockout prevention | MVP8_RELEASE_PATH_LOCKOUT_PLAN.md, armor_release_gate.py, reports/release_gate_public_sample.json |

## Safety note

Public artifacts are review-only. They do not perform enforcement, remediation, quarantine, purge, lockdown, firewall changes, device blocking, permission changes, process kills, or private target scans.
