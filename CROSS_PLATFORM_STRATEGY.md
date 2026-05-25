# Citadel A.R.M.O.R. Cross-Platform Strategy

This document defines the public-safe strategy for broadening ARMOR beyond a Linux-first showcase.

## Direction

ARMOR should become a platform-adapter framework, not a Linux-only tool ported later.

The review-only safety chain remains the core product:

- policy
- release gate
- allowlist validation
- rollback manifest
- action preview
- action ledger
- post-action verification plan
- emergency stop schema
- operator confirmation schema
- execution readiness aggregation
- pre-execution freeze checklist
- public regression
- release bundle
- release seal

## Architecture target

```text
ARMOR Core
  platform-neutral safety policy
  platform-neutral allowlist decisions
  platform-neutral rollback requirements
  platform-neutral preview, ledger, verification, readiness, freeze, and seal logic

Platform Adapters
  Linux adapter
  Windows adapter
  macOS adapter
  Android adapter
  iOS adapter

Shared Interface
  desktop dashboard
  mobile companion
  local web view
  public verification output
```

## Core rule

The core must not directly depend on Linux services, Windows services, macOS launch agents, Android APIs, iOS APIs, shell paths, package managers, or device-specific controls.

Platform-specific details belong in adapters.

## Adapter contract

Every future adapter should report the same high-level shape:

```json
{
  "platform": "linux_or_windows_or_macos_or_android_or_ios",
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

## Platform starting points

| Platform | Public-safe starting point | Notes |
|---|---|---|
| Linux | Existing ARMOR review-only showcase | Keep as reference adapter path |
| Windows | Review-only posture adapter | Avoid enforcement until permissions, rollback, and operator review are proven |
| macOS | Review-only posture adapter | Respect app sandboxing, permissions, and platform security boundaries |
| Android | Mobile companion and managed-device posture | Avoid promising full endpoint control from a normal app |
| iOS | Mobile companion and managed-device posture | Avoid promising full endpoint control from a normal app |

## Mobile boundary

Mobile support should begin as a companion and posture layer, not a full endpoint defender.

Initial mobile-safe functions:

- show public release seal state
- explain risk and safety status
- display verification output
- guide manual review
- inspect app-provided files where allowed
- integrate with managed-device posture later

## Deferred behavior

Cross-platform support does not mean enabling:

- enforcement
- remediation
- quarantine
- purge
- lockdown
- firewall control
- device blocking
- process termination
- permission modification
- private target scans

## Future MVP path

| Phase | Purpose |
|---|---|
| MVP37 | Public cross-platform strategy |
| MVP38 | Public platform capability matrix |
| MVP39 | Public adapter contract schema |
| MVP40 | Public cross-platform release seal |
| MVP41 | Linux adapter contract alignment |
| MVP42 | Windows review-only adapter plan |
| MVP43 | macOS review-only adapter plan |
| MVP44 | Android companion posture plan |
| MVP45 | iOS companion posture plan |

## Safety rule

Every platform must prove review-only posture, adapter limits, rollback requirements, emergency stop behavior, operator confirmation, and release freeze rules before any future action capability is considered.

## Current recommendation

Keep the public showcase sealed as review-only while expanding the roadmap toward platform adapters.
