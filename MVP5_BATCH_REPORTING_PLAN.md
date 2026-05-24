# Citadel A.R.M.O.R. MVP 5 Batch Reporting Plan

## Status

Planning phase only. MVP 5 should improve review-only reporting for chunked scans without adding remediation.

## Goal

Add safe batch reporting and finding-count parsing so A.R.M.O.R. can summarize chunked scan results without exposing filenames, absolute paths, usernames, hostnames, or private report paths.

## Current foundation

- MVP 4 chunked quick_downloads scan checkpoint is frozen
- quick_downloads preflight reports 1502 candidate files and 199 directories
- chunked scan default batch size is 10 files
- chunked scan runs only one explicit batch per command
- batch 0 completed with ClamAV code 0
- public output redacts raw scan output and private report path
- tracked leak checks passed

## Safety boundary

MVP 5 must not quarantine, delete, purge, change permissions, modify firewall rules, disconnect Wi-Fi, disable Bluetooth, block USB devices, kill processes, auto-remediate, or enter lockdown.

## Allowed work

- parse ClamAV return codes into safe review statuses
- report whether a batch is clean, timed out, failed, or has review-only findings
- count findings only when safely derivable
- keep raw scan output in private ignored reports only
- keep public output sanitized
- add review helper fields such as finding_count, timed_out, clean, and needs_private_review

## Public output may show

- batch index
- batch size
- scan executed true or false
- ClamAV return code
- clean true or false
- timed_out true or false
- finding_count if safely derived
- needs_private_review true or false

## Public output must not show

- filenames
- absolute local paths
- private report paths
- raw ClamAV output
- username
- hostname

## Implemented so far

- chunked scan output includes sanitized clamav_status
- clamav_status reports clean, timed_out, finding_count, and needs_private_review
- tracked chunk public sample includes clamav_status
- public output still redacts raw scan output and private report path

## Definition of done

MVP 5 planning is done when:

- this plan is committed
- next implementation step is limited to safe status parsing
- no remediation or enforcement work is included

## Next implementation step

Patch armor_scan.py to add sanitized ClamAV status fields for chunked scan output: clean, timed_out, finding_count, and needs_private_review. Do not expose raw output and do not add remediation.
