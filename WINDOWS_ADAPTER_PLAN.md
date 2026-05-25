# Citadel A.R.M.O.R. Windows Adapter Plan

This document defines the public-safe plan for a future Windows ARMOR adapter.

## Purpose

MVP42 does not implement a Windows adapter.

It defines the review-only Windows adapter direction so ARMOR can broaden beyond Linux without adding runtime risk.

## Windows adapter goal

The future Windows adapter should report public-safe posture facts through PLATFORM_ADAPTER_CONTRACT.md without enabling enforcement, remediation, target scans, or action execution.

## Planned Windows status

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

Future Windows adapter output should preserve this public-safe shape:

```json
{
  "platform": "windows",
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

## Candidate Windows posture checks

Future review-only checks may include:

- Windows version posture
- security center posture
- built-in protection status
- startup entry inventory
- service inventory
- scheduled task inventory
- local firewall posture
- update posture
- public-safe event summary

## Required Windows invariants

- review_only: true
- actions_enabled: false
- enforcement: false
- remediation_enabled: false
- target_scan_executed: false
- no private target scans in public output
- no action execution

## Windows adapter boundaries

The future Windows adapter must not directly enable:

- enforcement
- remediation
- quarantine
- purge
- lockdown
- firewall changes
- permission changes
- process kills
- service changes
- scheduled task changes
- registry changes
- private target scans in public output

## MVP42 result

```text
windows_adapter_plan_present: true
windows_adapter_contract_alignment_defined: true
windows_adapter_runtime_enabled: false
windows_adapter_enforcement_enabled: false
windows_adapter_remediation_enabled: false
windows_adapter_private_target_scan_enabled: false
```

## Recommendation

Define Windows public-safe sample output before any Windows adapter implementation.
