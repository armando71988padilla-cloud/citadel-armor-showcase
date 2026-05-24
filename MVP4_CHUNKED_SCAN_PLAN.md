# Citadel A.R.M.O.R. MVP 4 Chunked Scan Plan

## Status

Planning phase only. No chunked scan implementation is added by this document.

## Goal

Replace one large recursive quick_downloads scan with smaller explicit review-only batches so timeouts are predictable and public output remains sanitized.

## Current evidence

- full quick_downloads scan support exists
- first full quick_downloads scan hit timeout code 124
- preflight counted candidate files without printing filenames or absolute paths
- quick_downloads preflight sample is tracked and sanitized

## Safety boundary

Chunked scan must not delete, quarantine, purge, change permissions, modify firewall rules, disconnect Wi-Fi, disable Bluetooth, block USB devices, kill processes, auto-remediate, or enter lockdown.

## Required chunk guardrails

- explicit operator command only
- target remains ~/Downloads only
- ClamAV only at first
- batch size must be capped
- per-batch timeout must be capped
- private report only for raw ClamAV output
- public output must not show filenames or absolute local paths
- public output may show batch number, counts, timeout status, and redaction markers
- review_only true
- enforcement false

## Initial chunk policy

- batch size cap: 100 files maximum
- default batch size: 10 files
- per-batch timeout: 60 seconds maximum
- max batches per command: 1 initially
- no automatic continuation
- no retries without explicit operator command

## Implemented so far

- quick_downloads chunked scan command exists
- batch index 0 with 100 files timed out under the 60 second guardrail
- default batch size was reduced to 10 files
- batch index 0 with 10 files completed successfully with ClamAV code 0
- public chunk output redacts raw scan output and private report path
- tracked public chunk sample exists at armor/reports/quick_downloads_chunk_public_sample.json

## Public output rules

Public output may show:

- profile: quick_downloads_chunk
- target: ~/Downloads
- batch_index
- batch_size
- scan_executed
- timeout or return code
- redacted output marker

Public output must not show:

- file names
- absolute local paths
- private report paths
- usernames
- hostnames

## Definition of done

Planning is done when:

- this plan is committed
- Downloads move has completed
- a fresh preflight is run after the move
- no implementation starts until new preflight counts are known

## Next implementation step

After the Downloads move finishes, rerun quick_downloads preflight only. Do not implement chunked scan until the post-move count is known.
