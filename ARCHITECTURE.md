# Citadel A.R.M.O.R. Architecture

This document summarizes the public-safe ARMOR showcase architecture.

## Design goal

Citadel A.R.M.O.R. is designed as a local-first active defense workflow that proves safety boundaries before any future enforcement work is considered.

The public showcase is intentionally review-only.

## Safety-first pipeline

```text
status and baseline
  -> scan planning
  -> public-safe samples
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

## Core principle

No future action should be trusted unless the system can first prove:

- the target is allowed
- rollback data is planned
- the action can be previewed
- the action can be logged
- post-action verification is defined
- emergency stop behavior is checked
- operator confirmation is valid
- execution readiness is aggregated
- pre-execution freeze checks pass

## Public helper layers

| Layer | Helper | Purpose |
|---|---|---|
| Safe target policy | armor_policy.py | Defines review-only policy boundaries |
| Release gate | armor_release_gate.py | Reports release safety requirements |
| Allowlist validation | armor_allowlist_validate.py | Classifies allowed and denied targets |
| Rollback manifest | armor_rollback_manifest.py | Models required rollback data |
| Action preview | armor_action_preview.py | Describes future action intent without execution |
| Action ledger | armor_action_ledger.py | Models future audit trail entries |
| Post-action verification | armor_post_action_verify.py | Defines verification expectations |
| Emergency stop | armor_emergency_stop.py | Models stop-state requirements |
| Operator confirmation | armor_operator_confirm.py | Models confirmation requirements |
| Execution readiness | armor_execution_readiness.py | Aggregates readiness blockers |
| Pre-execution freeze | armor_pre_execution_freeze.py | Aggregates final freeze checks |
| Public regression | armor_public_regression.py | Verifies public helper health |
| Public release bundle | armor_public_release_bundle.py | Checks expected public files |
| Public release seal | armor_public_release_seal.py | Reports final public seal state |

## Current public seal

The public showcase is sealed through MVP20:

- mode: MVP20_PUBLIC_RELEASE_SEAL_REVIEW_ONLY
- release_sealed: true
- sealed_through: MVP19_PUBLIC_RELEASE_BUNDLE
- seal_phase: MVP20_PUBLIC_RELEASE_SEAL
- review_only: true
- actions_enabled: false
- enforcement: false
- remediation_enabled: false
- scan_executed: false
- target_scan_executed: false
- action_executed: false

## Non-goals

The public showcase does not perform enforcement, remediation, quarantine, purge, lockdown, firewall changes, device blocking, permission changes, process kills, or private target scans.

## Review path

Recommended public review order:

1. README.md
2. QUICKSTART.md
3. VERIFY.md
4. ARCHITECTURE.md
5. MVP20_PUBLIC_RELEASE_SEAL_PLAN.md
6. reports/public_release_seal_public_sample.json
7. armor_public_release_seal.py
