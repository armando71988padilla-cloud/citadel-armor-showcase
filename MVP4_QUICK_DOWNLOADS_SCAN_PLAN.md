# Citadel A.R.M.O.R. MVP 4 Quick Downloads Scan Plan

## Status

Planning phase only. This document defines guardrails for a future explicit read-only quick_downloads scan.

## Goal

Allow A.R.M.O.R. to scan ~/Downloads with ClamAV only when explicitly requested, while preserving review-only behavior and avoiding private data leakage in public output.

## Current foundation

- MVP 4 quick_downloads dry-run is implemented
- dry-run public output redacts the target as ~/Downloads
- dry-run reports scan_executed false
- dry-run reports review_only true
- dry-run reports enforcement false
- dry-run sample is tracked and sanitized

## Hard safety boundary

The real quick_downloads scan must not:

- delete files
- quarantine files
- purge files
- change permissions
- modify firewall rules
- disconnect Wi-Fi
- disable Bluetooth
- block USB devices
- kill processes
- auto-remediate findings
- print raw file names in public output
- print absolute local paths in public output

## Required scan limits

Initial quick_downloads scan must use:

- explicit operator command only
- target path: ~/Downloads only
- ClamAV only at first
- timeout: 120 seconds maximum
- output cap: 4000 characters private report maximum per tool result
- public output redaction for raw scan output
- private report under armor/reports/scan_private_quick_downloads_*.json
- review_only true
- enforcement false
- scan profile name recorded as quick_downloads

## Public output rules

Public output may show:

- profile name
- scan_executed true or false
- review_only true
- enforcement false
- target as ~/Downloads
- tool status
- finding count if safely derived
- redaction markers

Public output must not show:

- real local paths
- raw ClamAV infected file names
- raw file names
- private report path
- username
- hostname

## Failure behavior

If the scan times out, fails, or reports a finding, A.R.M.O.R. must still perform no action. The result is review-only and should direct the operator to inspect the private report locally.

## Definition of done

Planning is done when:

- this plan is committed
- dry-run checkpoint remains clean
- implementation patch is limited to explicit quick_downloads scan execution only
- public output remains sanitized
- tracked leak checks pass

## Next implementation step

Patch armor_scan.py to allow --run-profile quick_downloads as an explicit read-only ClamAV scan with timeout, private report, and public redaction. Do not add YARA, quarantine, delete, or enforcement.
