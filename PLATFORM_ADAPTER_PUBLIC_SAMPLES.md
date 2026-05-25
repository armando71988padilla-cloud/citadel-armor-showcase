# Citadel A.R.M.O.R. Platform Adapter Public Samples

This document explains the public-safe sample adapter outputs for Linux, Windows, macOS, Android, and iOS.

## Purpose

MVP46 makes PLATFORM_ADAPTER_CONTRACT.md concrete without implementing runtime adapters.

The sample output shows the intended review-only shape for each platform.

## Sample file

- reports/platform_adapter_public_sample.json

## Included platforms

- Linux
- Windows
- macOS
- Android
- iOS

## Required public invariants

Every sample platform entry preserves:

- review_only: true
- actions_enabled: false
- enforcement: false
- remediation_enabled: false
- target_scan_executed: false
- no action execution
- no private target scans

## Sample intent

The sample file is not runtime evidence.

It is a public-safe contract fixture for future adapter work.

## Future use

Future platform adapters should emit records compatible with this sample shape before implementation expands beyond review-only posture reporting.
