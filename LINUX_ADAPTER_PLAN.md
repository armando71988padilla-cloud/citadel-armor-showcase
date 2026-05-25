# Citadel A.R.M.O.R. Linux Adapter Plan

This document aligns the existing Linux-first ARMOR showcase with the public platform adapter contract.

## Purpose

The current public ARMOR showcase remains the Linux reference path.

MVP41 does not implement a new adapter. It defines how the existing Linux path should align with PLATFORM_ADAPTER_CONTRACT.md before future adapter code is introduced.

## Current Linux status

| Area | Status |
|---|---|
| Public release seal | Present |
| Review-only posture | Present through public helper outputs |
| Safe target policy | Present |
| Allowlist validation | Present |
| Rollback manifest planning | Present |
| Action preview schema | Present |
| Action ledger schema | Present |
| Post-action verification schema | Present |
| Emergency stop schema | Present |
| Operator confirmation schema | Present |
| Execution readiness aggregation | Present |
| Pre-execution freeze checklist | Present |
| Enforcement | Disabled |
| Remediation | Disabled |
| Private target scanning | Disabled in public seal output |

## Adapter alignment target

Future Linux adapter output should preserve this public-safe shape:

```json
{
  "platform": "linux",
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

## Required Linux invariants

- review_only: true
- actions_enabled: false
- enforcement: false
- remediation_enabled: false
- target_scan_executed: false
- no private target scans in public output
- no action execution

## Linux adapter boundaries

The future Linux adapter must not directly enable:

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
- private target scans in public output

## Future Linux adapter work

Future work may define Linux posture checks for services, packages, logs, startup entries, permissions, and public-safe target classes.

Those checks must remain review-only until allowlist, rollback, emergency stop, operator confirmation, post-action verification, regression, and release freeze rules are proven.

## MVP41 result

```text
linux_adapter_plan_present: true
linux_reference_path_present: true
linux_adapter_contract_alignment_defined: true
linux_adapter_runtime_enabled: false
linux_adapter_enforcement_enabled: false
linux_adapter_remediation_enabled: false
linux_adapter_private_target_scan_enabled: false
```

## Recommendation

Use the existing Linux showcase as the reference adapter path, but keep implementation deferred until contract samples are designed.
