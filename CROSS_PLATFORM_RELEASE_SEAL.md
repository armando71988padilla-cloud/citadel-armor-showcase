# Citadel A.R.M.O.R. Cross-Platform Release Seal

This document seals the public-safe cross-platform planning layer for ARMOR.

## Seal scope

This seal covers public documentation and strategy artifacts only.

It does not introduce runtime helpers, platform agents, enforcement, remediation, scans, or action execution.

## Sealed through

- MVP37 public cross-platform strategy
- MVP38 public platform capability matrix
- MVP39 public platform adapter contract
- MVP40 public cross-platform release seal

## Required public artifacts

| Artifact | Status |
|---|---|
| CROSS_PLATFORM_STRATEGY.md | present |
| PLATFORM_CAPABILITY_MATRIX.md | present |
| PLATFORM_ADAPTER_CONTRACT.md | present |
| CROSS_PLATFORM_RELEASE_SEAL.md | present |
| ROADMAP.md cross-platform direction | present |
| README.md links | present |

## Cross-platform direction

ARMOR is now publicly framed as a platform-adapter framework.

Target platforms:

- Linux
- Windows
- macOS
- Android
- iOS

## Adapter rule

The ARMOR core should remain platform-neutral.

Platform-specific behavior belongs in adapters.

## Public safety invariants

Every public cross-platform planning artifact preserves:

- review_only: true
- actions_enabled: false
- enforcement: false
- remediation_enabled: false
- target_scan_executed: false
- no private target scans
- no action execution

## Platform status

| Platform | Public status |
|---|---|
| Linux | Existing review-only showcase reference path |
| Windows | Planned review-only adapter path |
| macOS | Planned review-only adapter path |
| Android | Planned companion and managed-device posture path |
| iOS | Planned companion and managed-device posture path |

## Disabled behavior

This cross-platform seal does not enable:

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
- private target scans

## Seal result

```text
cross_platform_strategy_present: true
platform_capability_matrix_present: true
platform_adapter_contract_present: true
cross_platform_release_seal_present: true
all_platform_paths_review_only: true
cross_platform_runtime_enabled: false
cross_platform_enforcement_enabled: false
cross_platform_remediation_enabled: false
cross_platform_release_sealed: true
```

## Recommendation

Future work should proceed with review-only platform adapter plans before any platform adapter implementation.
