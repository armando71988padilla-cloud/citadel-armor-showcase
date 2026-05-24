# Citadel A.R.M.O.R. MVP 4 Controlled Scan Profile Plan

## Status

Planning phase only. MVP 4 expands scan profiles carefully, but remains review-only.

## Goal

MVP 4 adds controlled scan profile expansion beyond A.R.M.O.R. self-check. Each profile must be explicit, bounded, timeout-limited, output-capped, and safe to review.

## Current foundation

- MVP 1 read-only status is frozen
- MVP 2 scan milestone is frozen
- MVP 3 detection rules milestone is frozen
- ClamAV and YARA are installed and detected
- self-check scan is review-only and scoped
- scan review helper emits sanitized finding_summary entries
- public samples are sanitized and tracked

## Safety boundary

MVP 4 must not:

- delete files
- quarantine files
- purge files
- change permissions
- modify firewall
- disconnect Wi-Fi
- disable Bluetooth
- block USB devices
- kill processes
- auto-remediate findings
- scan broad roots by default
- scan mounted USB without explicit operator action

## Approved first expansion

The first profile expansion should be quick_downloads, but only after path existence and scan bounds are implemented.

## Profile guardrails

Every executable profile must have:

- explicit profile name
- explicit path list
- path existence check
- max runtime timeout
- output cap
- private report output only
- public redaction mode
- review_only true
- enforcement false
- no action list

## MVP 4 phases

### Phase 4.0 - profile execution schema

Normalize executable profile results so self-check and future profiles share the same fields.

### Phase 4.1 - quick_downloads dry-run

Add a dry-run mode that resolves ~/Downloads and prints what would be scanned without scanning.

### Phase 4.2 - quick_downloads read-only scan

Run ClamAV against ~/Downloads only when explicitly requested.

### Phase 4.3 - public sample refresh

Generate sanitized public samples showing review-only behavior without leaking file names or paths.

## Implemented so far

- quick_downloads dry-run is implemented
- quick_downloads dry-run resolves ~/Downloads without scanning
- quick_downloads dry-run public output redacts the local path as ~/Downloads
- quick_downloads dry-run sample is tracked at armor/reports/quick_downloads_dry_run_public_sample.json
- dry-run behavior keeps scan_executed false, review_only true, and enforcement false

## Definition of done

MVP 4 planning is done when:

- this plan is committed
- quick_downloads dry-run is implemented
- dry-run output is sanitized
- no broad scans are possible by default
- tracked leak checks pass

## Next implementation step

Add quick_downloads dry-run only. Do not run Downloads scanning yet.
