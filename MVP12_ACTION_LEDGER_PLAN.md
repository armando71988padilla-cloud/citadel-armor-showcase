# Citadel A.R.M.O.R. MVP12 Action Ledger Plan

## Purpose

MVP12 defines the review-only action ledger schema required before any future action execution helper can exist.

## Safety boundary

- review only
- no runtime ledger write
- no action execution
- no restore execution
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

- armor_action_ledger.py

## Required ledger fields

- ledger_version
- event_id
- action_id
- event_type
- stage
- target
- target_class
- allowlist_decision
- preview_id
- rollback_manifest_id
- operator_confirmation_state
- emergency_stop_checked
- result
- created_at

## Public sample

- reports/action_ledger_public_sample.json

## MVP12 rule

Action ledger schema proves required future audit records only. It must not write runtime logs or perform any action.
