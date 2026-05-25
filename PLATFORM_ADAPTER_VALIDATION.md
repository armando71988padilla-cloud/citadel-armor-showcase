# Citadel A.R.M.O.R. Platform Adapter Validation

This document explains the public-safe platform adapter sample validator.

## Purpose

MVP47 validates reports/platform_adapter_public_sample.json against the public adapter contract invariants.

This validator does not implement platform adapters.

## Helper

- armor_platform_adapter_validate.py

## Public sample output

- reports/platform_adapter_validation_public_sample.json

## Validation command

```bash
python3 armor_platform_adapter_validate.py --public-sample
```

## Expected validation result

```text
validation_passed: true
review_only: true
actions_enabled: false
enforcement: false
remediation_enabled: false
target_scan_executed: false
sample_runtime_enabled: false
platform_count: 5
```

## Checked platforms

- linux
- windows
- macos
- android
- ios

## Boundary

The validator reads a public sample JSON file and reports whether public-safe adapter invariants hold.

It does not run platform checks, scan private targets, enable enforcement, enable remediation, or execute actions.
