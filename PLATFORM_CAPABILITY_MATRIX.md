# Citadel A.R.M.O.R. Platform Capability Matrix

This matrix defines the public-safe cross-platform capability direction for ARMOR.

## Purpose

ARMOR is being broadened from a Linux-first showcase into a platform-adapter framework.

This matrix prevents overpromising by separating current public proof from planned review-only adapter work.

## Current status

| Platform | Current public status | Adapter state |
|---|---|---|
| Linux | Existing public showcase reference path | Present as current ARMOR showcase foundation |
| Windows | Planned review-only posture adapter | Not implemented in public showcase yet |
| macOS | Planned review-only posture adapter | Not implemented in public showcase yet |
| Android | Planned companion and managed-device posture path | Not implemented in public showcase yet |
| iOS | Planned companion and managed-device posture path | Not implemented in public showcase yet |

## Capability matrix

| Capability | Linux | Windows | macOS | Android | iOS |
|---|---|---|---|---|---|
| Public release seal | Present | Planned | Planned | Planned | Planned |
| Review-only posture report | Present | Planned | Planned | Planned | Planned |
| Platform adapter contract | Planned | Planned | Planned | Planned | Planned |
| Safe target policy | Present | Planned | Planned | Limited | Limited |
| Allowlist validation | Present | Planned | Planned | Limited | Limited |
| Rollback manifest planning | Present | Planned | Planned | Limited | Limited |
| Action preview schema | Present | Planned | Planned | Planned | Planned |
| Action ledger schema | Present | Planned | Planned | Planned | Planned |
| Emergency stop schema | Present | Planned | Planned | Planned | Planned |
| Operator confirmation schema | Present | Planned | Planned | Planned | Planned |
| Execution readiness aggregation | Present | Planned | Planned | Planned | Planned |
| Pre-execution freeze checklist | Present | Planned | Planned | Planned | Planned |
| Enforcement | Disabled | Disabled | Disabled | Disabled | Disabled |
| Remediation | Disabled | Disabled | Disabled | Disabled | Disabled |
| Private target scanning | Disabled in public seal | Disabled | Disabled | Disabled | Disabled |

## Mobile boundary

Android and iOS support should begin as companion and posture layers.

Mobile support should not promise full endpoint control from a normal app.

Initial mobile-safe goals:

- show release seal state
- show review-only posture
- explain safety status
- guide manual review
- inspect app-provided files where allowed
- support managed-device posture later

## Desktop boundary

Desktop adapters may eventually expose richer posture checks than mobile adapters, but every platform must preserve review-only defaults until adapter limits, rollback requirements, emergency stop behavior, operator confirmation, and verification are proven.

## Disabled for all platforms

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

## MVP path

| Phase | Output |
|---|---|
| MVP37 | Cross-platform strategy |
| MVP38 | Platform capability matrix |
| MVP39 | Platform adapter contract schema |
| MVP40 | Cross-platform release seal |

## Current recommendation

Keep every platform review-only until safety contracts are proven per platform.
