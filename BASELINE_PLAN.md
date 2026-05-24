# Citadel A.R.M.O.R. Known Good Baseline Plan

## Status

Planning phase only. No enforcement is implemented here.

## Purpose

The Known Good Baseline defines what normal looks like on this machine before A.R.M.O.R. begins warning, quarantining, blocking, or locking down anything.

## Baseline rule

Baseline only trusted, intentional, expected state. Do not baseline random devices, borrowed USB drives, unknown Bluetooth devices, temporary networks, mystery adapters, or one-time experiments.

## Baseline categories

- Citadel root and A.R.M.O.R. root presence
- Citadel UI health
- local loopback services
- expected listening ports
- firewall status
- Wi-Fi current connection and trusted network identity
- Bluetooth controller state and trusted paired devices
- trusted USB keyboard and mouse
- trusted USB storage devices
- trusted audio devices
- trusted systemd user services
- startup entries
- shell profiles
- key tool availability

## Never break user control

A.R.M.O.R. must never lock out the user. Future enforcement must preserve:

- local keyboard control
- local mouse control
- trusted accessibility devices
- local dashboard loopback access
- terminal access
- ability to release lockdown
- ability to review logs
- ability to restore network intentionally

## Private artifacts

Private baseline captures must stay ignored by Git:

- armor/baseline/baseline_private_*.json
- armor/state/status_private_*.json
- armor/whitelist/*.json

## Public artifacts

Public baseline examples must be sanitized before tracking. They must not include real hostnames, usernames, SSIDs, Bluetooth IDs, USB serials, MAC addresses, IP addresses, local paths, or device fingerprints.

## Operator checklist before first real baseline

1. Remove random or untrusted USB devices.
2. Keep trusted keyboard and mouse connected.
3. Keep trusted primary storage connected only if it should be normal.
4. Confirm Wi-Fi network is the trusted normal network.
5. Keep Bluetooth off unless trusted Bluetooth devices should be normal.
6. Run read-only status capture.
7. Review private baseline before using it.
8. Do not enable blocking until whitelist and release path are proven.

## Next implementation step

Create armor_baseline.py in read-only capture mode. It should write private baseline JSON to ignored storage and produce a sanitized public summary only after review.

