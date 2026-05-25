# Citadel A.R.M.O.R. Cross-Platform Regression

This document explains the public-safe cross-platform regression helper.

## Purpose

MVP51 checks that the public cross-platform adapter layer remains present, review-only, and validated.

This helper does not implement runtime adapters or platform agents.

## Helper

- armor_cross_platform_regression.py

## Public sample output

- reports/cross_platform_regression_public_sample.json

## Regression command

```bash
python3 armor_cross_platform_regression.py --public-sample
```

## Expected highlights

```text
mode: MVP51_CROSS_PLATFORM_REGRESSION_REVIEW_ONLY
cross_platform_regression_passed: true
adapter_validation_passed: true
adapter_validation_platform_count: 5
required_files_ok: true
locked_flags_ok: true
review_only: true
actions_enabled: false
enforcement: false
remediation_enabled: false
target_scan_executed: false
runtime_adapters_enabled: false
platform_agents_enabled: false
```

## Boundary

The regression helper checks public docs, public samples, and the public adapter validator.

It does not run platform checks, scan private targets, enable enforcement, enable remediation, or execute actions.
