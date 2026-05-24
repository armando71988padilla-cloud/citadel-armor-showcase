# Citadel A.R.M.O.R. MVP11 Action Preview Plan

## Purpose

MVP11 defines the review-only action preview format required before any future action execution helper can exist.

## Safety boundary

- review only
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

- armor_action_preview.py

## Required preview fields

- preview_version
- action_id
- action_type
- target
- target_class
- allowlist_decision
- rollback_manifest_required
- operator_confirmation_required
- emergency_stop_required
- execution_ready
- execution_command_available
- created_at

## Public sample

- reports/action_preview_public_sample.json

## MVP11 rule

Action preview proves future operator-facing action details only. It must not expose an executable command or perform any action.
