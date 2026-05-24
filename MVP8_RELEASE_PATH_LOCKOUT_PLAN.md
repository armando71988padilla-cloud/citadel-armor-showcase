# Citadel A.R.M.O.R. MVP 8 Release Path and Lockout Prevention Plan

## Status

Planning phase only. MVP 8 defines release-path and lockout-prevention requirements for any future enforcement or remediation work. No remediation or enforcement is allowed in this phase.

## Goal

Create a documented safety gate that must be satisfied before A.R.M.O.R. can ever quarantine, delete, block, disable, kill, isolate, or modify anything.

## Current foundation

- MVP 1 read-only status is frozen
- MVP 2 scan planning and self-check scan are frozen
- MVP 3 review-only detection rules are frozen
- MVP 4 dry-run, preflight, and chunked scans are frozen
- MVP 5 sanitized batch reporting is frozen
- MVP 6 aggregate reporting is frozen
- MVP 7 safe target policy is frozen
- public ARMOR showcase is synced through MVP 7

## Safety boundary

MVP 8 must not quarantine, delete, purge, change permissions, modify firewall rules, disconnect Wi-Fi, disable Bluetooth, block USB devices, kill processes, auto-remediate, or enter lockdown.

## Release-path principles

- every future action must be opt-in
- every future action must have a dry-run mode first
- every future action must have a preview output before execution
- every future action must have a rollback plan before execution
- every future action must write a private local action report
- public output must stay redacted
- no action may run from a broad scan result alone
- no action may run without explicit profile and target class approval

## Lockout-prevention requirements

- never disable all network paths
- never block loopback services
- never modify firewall defaults without a restore file
- never kill critical user-session, shell, SSH, desktop, network, or package-manager processes
- never change ownership or permissions recursively
- never touch credential, key, wallet, browser-profile, password-manager, or hidden-home paths
- never modify system roots
- never act on external drives or network mounts without a separate approval phase

## Required future gates before enforcement

- allowlist validation helper
- rollback manifest format
- action preview format
- explicit operator confirmation phrase
- emergency stop file check
- action ledger
- post-action verification
- release freeze checkpoint

## MVP 8 deliverables

- this plan committed to Git
- README references this plan
- next implementation step limited to a read-only release gate helper
- no enforcement or remediation behavior added

## Implemented so far

- release path and lockout prevention plan is committed
- README references the MVP 8 plan
- read-only release gate helper exists at armor/armor_release_gate.py
- release gate helper public output reports MVP8_RELEASE_GATE_REVIEW_ONLY
- release gate helper reports review_only true
- release gate helper reports enforcement false
- release gate helper reports remediation_enabled false
- release gate helper reports scan_executed false
- release gate helper reports actions_enabled false
- release gate public sample is tracked at armor/reports/release_gate_public_sample.json
- release gate sample passed leak check
- README documents the release gate helper entry point

## Definition of done

MVP 8 planning is done when:

- this plan is committed
- README references this plan
- the next implementation step is limited to a read-only helper that reports release gates and lockout-prevention requirements

## Next implementation step

Create armor/armor_release_gate.py with a read-only --public mode that reports required future gates, lockout-prevention requirements, review_only true, enforcement false, and remediation_enabled false. Do not scan files and do not add remediation.
