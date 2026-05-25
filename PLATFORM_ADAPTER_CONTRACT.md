# Citadel A.R.M.O.R. Platform Adapter Contract

This document defines the public-safe adapter output contract for future ARMOR platform adapters.

## Purpose

ARMOR is moving toward a platform-adapter framework. Each platform adapter should report the same safety shape so the ARMOR core can evaluate posture without embedding platform-specific behavior.

## Supported adapter targets

- Linux
- Windows
- macOS
- Android
- iOS

## Contract goals

- preserve review-only defaults
- separate platform facts from ARMOR core decisions
- report capabilities without executing actions
- report denied or unsupported capabilities honestly
- avoid private runtime data in public output
- keep enforcement and remediation disabled

## Required top-level fields

| Field | Type | Required | Meaning |
|---|---|---|---|
| platform | string | yes | linux, windows, macos, android, or ios |
| adapter_version | string | yes | adapter version identifier |
| review_only | boolean | yes | must remain true for public adapters |
| actions_enabled | boolean | yes | must remain false for public adapters |
| enforcement | boolean | yes | must remain false for public adapters |
| remediation_enabled | boolean | yes | must remain false for public adapters |
| target_scan_executed | boolean | yes | must remain false for public public-safe output |
| platform_capabilities | array | yes | capabilities the adapter can report |
| posture_checks | array | yes | review-only posture checks |
| denied_capabilities | array | yes | capabilities not available or not allowed |
| operator_notes | array | yes | public-safe review notes |

## Minimal public adapter JSON

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

## Capability record shape

```json
{
  "name": "release_seal_status",
  "supported": true,
  "review_only": true,
  "notes": "Reports seal state without executing actions"
}
```

## Posture check record shape

```json
{
  "check_id": "adapter_review_only_lock",
  "status": "pass",
  "summary": "Adapter preserves review-only safety flags"
}
```

## Denied capability record shape

```json
{
  "name": "remediation",
  "denied": true,
  "reason": "Public adapter contract keeps remediation disabled"
}
```

## Safety invariants

Every public adapter must preserve:

- review_only: true
- actions_enabled: false
- enforcement: false
- remediation_enabled: false
- target_scan_executed: false

## Platform-specific notes

| Platform | Adapter note |
|---|---|
| Linux | Existing showcase path remains reference implementation for review-only public output |
| Windows | Future adapter should begin with posture reporting only |
| macOS | Future adapter should begin with posture reporting only and respect sandbox and permission boundaries |
| Android | Future adapter should begin as companion and managed-device posture reporting |
| iOS | Future adapter should begin as companion and managed-device posture reporting |

## Non-goals

This contract does not introduce enforcement, remediation, quarantine, purge, lockdown, firewall changes, device blocking, permission changes, process kills, or private target scans.

## Current recommendation

Build adapters only after this contract is stable and verified by public-safe sample outputs.
