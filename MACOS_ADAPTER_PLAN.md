# Citadel A.R.M.O.R. macOS Adapter Plan

This document defines the public-safe plan for a future macOS ARMOR adapter.

## Purpose

MVP43 does not implement a macOS adapter.

It defines the review-only macOS adapter direction so ARMOR can broaden beyond Linux and Windows without adding runtime risk.

## macOS adapter goal

The future macOS adapter should report public-safe posture facts through PLATFORM_ADAPTER_CONTRACT.md without enabling enforcement, remediation, target scans, or action execution.

## Planned macOS status

| Area | Planned public-safe status |
|---|---|
| Public release seal | Planned through cross-platform seal path |
| Review-only posture | Planned |
| Safe target policy | Planned |
| Allowlist validation | Planned |
| Rollback manifest planning | Planned |
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

Future macOS adapter output should preserve this public-safe shape:

```json
{
  "platform": "macos",
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

## Candidate macOS posture checks

Future review-only checks may include:

- macOS version posture
- Gatekeeper posture
- FileVault posture
- firewall posture
- startup item inventory
- launch agent inventory
- launch daemon inventory
- privacy permission posture
- update posture
- public-safe log summary

## Required macOS invariants

- review_only: true
- actions_enabled: false
- enforcement: false
- remediation_enabled: false
- target_scan_executed: false
- no private target scans in public output
- no action execution

## macOS adapter boundaries

The future macOS adapter must not directly enable:

- enforcement
- remediation
- quarantine
- purge
- lockdown
- firewall changes
- permission changes
- process kills
- launch agent changes
- launch daemon changes
- privacy permission changes
- private target scans in public output

## MVP43 result

```text
macos_adapter_plan_present: true
macos_adapter_contract_alignment_defined: true
macos_adapter_runtime_enabled: false
macos_adapter_enforcement_enabled: false
macos_adapter_remediation_enabled: false
macos_adapter_private_target_scan_enabled: false
```

## Recommendation

Define macOS public-safe sample output before any macOS adapter implementation.
