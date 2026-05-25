# Citadel A.R.M.O.R. MVP18 Public Regression Plan

## Purpose

MVP18 defines a review-only public regression aggregation helper for public-safe ARMOR helpers and samples.

## Safety boundary

- review only
- public sample refresh only
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

- armor_public_regression.py

## Checks

- compile public-safe ARMOR helper scripts
- run public-safe sample commands
- verify locked review-only flags where present
- report compile_ok
- report public_samples_ok
- report regression_passed

## Legacy command compatibility

- armor_policy.py uses --public
- armor_release_gate.py uses --public
- MVP9 and later sample helpers use --public-sample

## Public sample

- reports/public_regression_public_sample.json

## MVP18 rule

Public regression aggregation proves public helper health only. It must not scan targets, expose commands, or perform actions.
