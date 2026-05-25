# Citadel A.R.M.O.R. Public Safety Boundary

This document defines the public-safe safety boundary for the ARMOR showcase.

## Current public mode

- mode: MVP20_PUBLIC_RELEASE_SEAL_REVIEW_ONLY
- release_sealed: true
- sealed_through: MVP19_PUBLIC_RELEASE_BUNDLE
- seal_phase: MVP20_PUBLIC_RELEASE_SEAL
- review_only: true

## Disabled behavior

The public showcase does not perform:

- enforcement
- remediation
- quarantine
- purge
- lockdown
- firewall changes
- Wi-Fi changes
- Bluetooth changes
- USB blocking
- permission changes
- process kills
- restore execution
- action execution
- private target scans

## Public helper expectations

Public helpers are expected to preserve:

- actions_enabled: false
- enforcement: false
- remediation_enabled: false
- scan_executed: false
- target_scan_executed: false
- action_executed: false
- restore_executed: false

## Why the project is structured this way

ARMOR is built around proof-before-action. The public showcase demonstrates planning, validation, rollback requirements, operator confirmation, emergency stop modeling, execution readiness, freeze checks, and release sealing before any future enforcement work is considered.

## Review-only chain

```text
allowlist validation
  -> rollback manifest
  -> action preview
  -> action ledger
  -> post-action verification plan
  -> emergency stop schema
  -> operator confirmation schema
  -> execution readiness
  -> pre-execution freeze
  -> public regression
  -> public release bundle
  -> public release seal
```

## Verification

Use VERIFY.md to validate the public release seal and public-safe marker checks.

Use QUICKSTART.md for the shortest safe review path.

## Safety summary

The public repository is a review-only showcase. It is designed to be safe to inspect, compile, and verify without executing defensive actions or touching private runtime targets.
