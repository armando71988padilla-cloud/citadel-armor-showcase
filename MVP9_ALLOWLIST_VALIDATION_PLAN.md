# Citadel A.R.M.O.R. MVP9 Allowlist Validation Plan

## Purpose

MVP9 adds a review-only allowlist validation helper before any future action system exists.

## Safety boundary

- review only
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
- no scan execution

## Helper

- armor_allowlist_validate.py

## Required behavior

- classify explicitly allowed profile targets as allowed
- deny system roots
- deny credential and hidden home paths
- deny unknown paths by default
- report unresolved targets only when input cannot be classified
- keep actions_enabled false
- keep remediation_enabled false
- keep enforcement false
- keep scan_executed false

## Public sample

- reports/allowlist_validation_public_sample.json

## MVP9 rule

Allowlist validation proves target decisions only. It must not perform actions.
