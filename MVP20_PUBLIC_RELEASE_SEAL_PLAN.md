# Citadel A.R.M.O.R. MVP20 Public Release Seal Plan

## Purpose

MVP20 defines a review-only public release seal summary for the public ARMOR showcase.

## Safety boundary

- review only
- public sample write only
- expected public file presence only
- no target scan
- no gate execution
- no command exposure
- no action execution
- no restore execution
- no verification execution
- no confirmation collection
- no emergency stop mutation
- no enforcement
- no remediation
- no quarantine
- no delete
- no purge
- no permission changes
- no firewall changes
- no Wi-Fi changes
- no Bluetooth changes
- no USB changes
- no process kill
- no lockdown

## Helper

- armor_public_release_seal.py

## Checks

- expected public files are present
- release_sealed is true only when all expected public files are present
- sealed_through remains MVP19_PUBLIC_RELEASE_BUNDLE
- seal_phase remains MVP20_PUBLIC_RELEASE_SEAL
- public_boundary remains review_only_no_execution_no_remediation_no_scan

## Public sample

- reports/public_release_seal_public_sample.json

## MVP20 rule

Public release seal proves public showcase seal status only. It must not scan targets, expose commands, or perform actions.
