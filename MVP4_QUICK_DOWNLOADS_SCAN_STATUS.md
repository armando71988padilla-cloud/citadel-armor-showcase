# Citadel A.R.M.O.R. MVP 4 Quick Downloads Scan Status

## Status

Explicit quick_downloads read-only scan support is implemented.

## Implementation commit

Current implementation base: f7b309a

## Proven capabilities

- quick_downloads can be run only by explicit --run-profile quick_downloads command
- target is ~/Downloads only
- ClamAV is used for this profile
- scan is timeout-capped at 120 seconds
- scan writes a private ignored report
- public output redacts private report path
- public output redacts raw ClamAV output
- public output redacts local target path as ~/Downloads
- scan reports review_only true
- scan reports enforcement false
- no delete, quarantine, purge, permission change, or lockdown action exists
- code leak check passed before commit

## First execution result

The first explicit quick_downloads scan executed safely and hit the timeout guardrail with code 124.

This is a controlled timeout result, not a malware finding.

## Safety boundary

This implementation does not quarantine, delete, purge, change permissions, modify firewall rules, disconnect Wi-Fi, disable Bluetooth, block USB devices, kill processes, auto-remediate, or enter lockdown.

## Preflight result

The bounded quick_downloads preflight counted:

- candidate files before cleanup: 1864
- directories before cleanup: 309
- candidate files after cleanup: 1502
- directories after cleanup: 199
- file count cap hit: false
- permission errors: 0

The preflight did not print filenames or absolute local paths and did not scan files.

## Chunked scan result

The first chunked quick_downloads scan tested two batch sizes:

- batch size 100 timed out under the 60 second guardrail
- batch size 10 completed successfully with ClamAV code 0
- default chunk batch size is now 10 files
- tracked public chunk sample exists at armor/reports/quick_downloads_chunk_public_sample.json
- public chunk output redacts raw scan output and private report path

## Known non-blockers

- Downloads scan may exceed the 120 second timeout on large folders
- chunked scan mode exists, but only one explicit batch runs per command
- no public safe finding count parser exists yet

## Next implementation step

Plan chunked quick_downloads scanning before rerunning full scans. The next implementation should scan bounded batches, preserve review-only behavior, write private reports only, and keep public output sanitized.
