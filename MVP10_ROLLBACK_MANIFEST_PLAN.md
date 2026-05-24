# Citadel A.R.M.O.R. MVP10 Rollback Manifest Plan

## Purpose

MVP10 defines the rollback manifest structure required before any future action preview or action execution helper can exist.

## Safety boundary

- review only
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

- armor_rollback_manifest.py

## Required rollback fields

- manifest_version
- action_id
- action_type
- target
- target_class
- operator_confirmation_required
- pre_action_hash
- post_action_hash
- backup_path
- restore_preview
- emergency_stop_checked
- created_at

## Public sample

- reports/rollback_manifest_public_sample.json

## MVP10 rule

Rollback manifest design proves required undo data only. It must not execute restores or actions.
