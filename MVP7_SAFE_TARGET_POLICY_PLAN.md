# Citadel A.R.M.O.R. MVP 7 Safe Target Policy Plan

## Status

Planning phase only. MVP 7 defines safe target and whitelist policy for future scan expansion. No remediation or enforcement is allowed in this phase.

## Goal

Create a review-only policy layer that decides which paths may be scanned, which paths must never be scanned, and which future actions are blocked unless explicitly allowed.

## Current foundation

- MVP 1 read-only status is frozen
- MVP 2 scan planning and self-check scan are frozen
- MVP 3 review-only detection rules are frozen
- MVP 4 dry-run, preflight, and chunked scans are frozen
- MVP 5 sanitized batch reporting is frozen
- MVP 6 aggregate reporting is frozen
- public showcase exists separately from the private working repo

## Safety boundary

MVP 7 must not quarantine, delete, purge, change permissions, modify firewall rules, disconnect Wi-Fi, disable Bluetooth, block USB devices, kill processes, auto-remediate, or enter lockdown.

## Policy principles

- deny by default
- scan targets must be explicitly named profiles
- profile targets must resolve inside approved user-space locations
- private runtime reports stay ignored
- public output must never include filenames, absolute paths, usernames, hostnames, device identifiers, network identifiers, or raw scan output
- future remediation must require a separate release path and lockout prevention plan

## Initial allowed profile classes

- armor_self_check: root-level ARMOR Python files only
- quick_downloads_preflight: counts candidates without opening files
- quick_downloads_chunk: bounded read-only scan batches under user Downloads only

## Initial denied target classes

- system roots such as /, /bin, /boot, /dev, /etc, /proc, /root, /run, /sbin, /sys, /usr, /var
- hidden home directories unless explicitly approved later
- browser profiles
- SSH, GPG, password manager, wallet, token, key, and credential paths
- mounted external drives unless separately approved later
- network mounts
- project vaults, whitelists, private logs, and ignored runtime state

## MVP 7 deliverables

- a policy document committed to Git
- a read-only policy helper that lists allowed and denied classes
- a public-safe policy sample
- regression checks proving no enforcement behavior exists

## Implemented so far

- safe target policy plan is committed
- README references the MVP 7 policy plan
- read-only policy helper exists at armor/armor_policy.py
- policy helper public output reports MVP7_SAFE_TARGET_POLICY_REVIEW_ONLY
- policy helper reports deny_by_default true
- policy helper reports review_only true
- policy helper reports enforcement false
- policy helper reports scan_executed false
- policy public sample is tracked at armor/reports/policy_public_sample.json
- policy sample passed leak check

## Definition of done

MVP 7 planning is done when:

- this plan is committed
- README references this plan
- the next implementation step is limited to a read-only policy helper

## Next implementation step

Create armor/armor_policy.py with a read-only --public mode that prints allowed profile classes, denied target classes, review_only true, and enforcement false. Do not scan files and do not add remediation.
