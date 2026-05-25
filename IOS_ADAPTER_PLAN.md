# Citadel A.R.M.O.R. iOS Adapter Plan

This document defines the public-safe plan for a future iOS ARMOR adapter.

## Purpose

MVP45 does not implement an iOS adapter.

It defines the review-only iOS companion and managed-device posture direction without adding runtime risk.

## iOS adapter goal

The future iOS path should begin as a companion and posture layer through PLATFORM_ADAPTER_CONTRACT.md without promising full endpoint control from a normal app.

## Planned iOS status

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

Future iOS adapter output should preserve this public-safe shape:

```json
{
  "platform": "ios",
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

## Candidate iOS posture checks

Future review-only checks may include:

- iOS version posture
- device security posture guidance
- screen lock posture guidance
- update posture guidance
- app-provided file review
- companion alert display
- managed-device posture status
- public-safe device summary

## Required iOS invariants

- review_only: true
- actions_enabled: false
- enforcement: false
- remediation_enabled: false
- target_scan_executed: false
- no private target scans in public output
- no action execution

## iOS adapter boundaries

The future iOS adapter must not directly enable:

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

iOS support should begin as:

- companion status view
- review-only posture reporting
- manual guidance
- app-provided file review where allowed
- managed-device posture integration later

## MVP45 result

```text
ios_adapter_plan_present: true
ios_adapter_contract_alignment_defined: true
ios_adapter_runtime_enabled: false
ios_adapter_enforcement_enabled: false
ios_adapter_remediation_enabled: false
ios_adapter_private_target_scan_enabled: false
```

## Recommendation

Define iOS public-safe sample output before any iOS adapter implementation.
