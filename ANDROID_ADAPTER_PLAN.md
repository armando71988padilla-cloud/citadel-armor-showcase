# Citadel A.R.M.O.R. Android Adapter Plan

This document defines the public-safe plan for a future Android ARMOR adapter.

## Purpose

MVP44 does not implement an Android adapter.

It defines the review-only Android companion and managed-device posture direction without adding runtime risk.

## Android adapter goal

The future Android path should begin as a companion and posture layer through PLATFORM_ADAPTER_CONTRACT.md without promising full endpoint control from a normal app.

## Planned Android status

| Area | Planned public-safe status |
|---|---|
| Public release seal | Planned through cross-platform seal path |
| Review-only posture | Planned |
| Safe target policy | Limited |
| Allowlist validation | Limited |
| Rollback manifest planning | Limited |
| Action preview schema | Planned |
| Action ledger schema | Planned |
| Post-action verification schema | Planned |
| Emergency stop schema | Planned |
| Operator confirmation schema | Planned |
| Execution readiness aggregation | Planned |
| Pre-execution freeze checklist | Planned |
| Enforcement | Disabled |
| Remediation | Disabled |
| Private target scanning | Disabled in public output |

## Adapter alignment target

Future Android adapter output should preserve this public-safe shape:

```json
{
  "platform": "android",
  "adapter_version": "0.1-review-only",
  "review_only": true,
  "actions_enabled": false,
  "enforcement": false,
  "remediation_enabled": false,
  "target_scan_executed": false,
  "platform_capabilities": [],
  "posture_checks": [],
  "denied_capabilities": [],
  "operator_notes": []
}
```

## Candidate Android posture checks

Future review-only checks may include:

- Android version posture
- app permission review guidance
- device security posture
- screen lock posture
- update posture
- app-provided file review
- companion alert display
- managed-device posture status
- public-safe device summary

## Required Android invariants

- review_only: true
- actions_enabled: false
- enforcement: false
- remediation_enabled: false
- target_scan_executed: false
- no private target scans in public output
- no action execution

## Android adapter boundaries

The future Android adapter must not directly enable:

- enforcement
- remediation
- quarantine
- purge
- lockdown
- firewall changes
- permission changes
- process kills
- device-wide file scanning from a normal app
- private target scans in public output

## Mobile boundary

Android support should begin as:

- companion status view
- review-only posture reporting
- manual guidance
- app-provided file review where allowed
- managed-device posture integration later

## MVP44 result

```text
android_adapter_plan_present: true
android_adapter_contract_alignment_defined: true
android_adapter_runtime_enabled: false
android_adapter_enforcement_enabled: false
android_adapter_remediation_enabled: false
android_adapter_private_target_scan_enabled: false
```

## Recommendation

Define Android public-safe sample output before any Android adapter implementation.
