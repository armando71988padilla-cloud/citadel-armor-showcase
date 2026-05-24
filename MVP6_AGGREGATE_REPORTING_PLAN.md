# Citadel A.R.M.O.R. MVP 6 Aggregate Reporting Plan

## Status

Planning phase only. MVP 6 should add review-only aggregate reporting for chunked scans without adding remediation.

## Goal

Summarize multiple private chunk scan reports into one sanitized public-safe review summary.

## Current foundation

- MVP 5 batch reporting checkpoint is frozen
- chunked scan output includes sanitized clamav_status
- clamav_status reports clean, timed_out, finding_count, and needs_private_review
- chunked scans still require explicit batch-by-batch operation
- public output redacts raw scan output and private report paths
- tracked leak checks passed

## Safety boundary

MVP 6 must not quarantine, delete, purge, change permissions, modify firewall rules, disconnect Wi-Fi, disable Bluetooth, block USB devices, kill processes, auto-remediate, or enter lockdown.

## Allowed work

- read ignored private chunk reports locally
- count batches reviewed
- count clean batches
- count timed-out batches
- count batches needing private review
- sum finding_count only when safely populated
- produce public-safe aggregate output
- redact private paths and raw scan output

## Public output may show

- aggregate mode
- profile name
- total batches reviewed
- clean batch count
- timed out batch count
- needs private review count
- known finding count total when safely derivable
- review_only true
- enforcement false

## Public output must not show

- filenames
- absolute local paths
- private report paths
- raw ClamAV output
- username
- hostname

## Implemented so far

- aggregate batch review helper exists at armor/armor_review_batches.py
- helper reads ignored private quick_downloads chunk reports locally
- helper prints sanitized aggregate output only
- tracked aggregate public sample exists at armor/reports/quick_downloads_aggregate_public_sample.json
- current aggregate sample reviewed 12 private chunk reports
- current aggregate sample reports 5 clean batches
- current aggregate sample reports 0 known findings
- current aggregate sample reports 7 unknown finding-count batches from older reports without clamav_status
- public aggregate sample passed leak check

## Definition of done

MVP 6 planning is done when:

- this plan is committed
- next implementation step is limited to a review-only aggregate helper
- no remediation or enforcement work is included

## Next implementation step

Create armor/armor_review_batches.py to summarize ignored private quick_downloads chunk reports into sanitized aggregate output. Do not scan files and do not add remediation.
