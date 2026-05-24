# Citadel A.R.M.O.R. MVP 3 Detection Rules Plan

## Status

Planning phase only. No containment, quarantine, deletion, purge, blocking, firewall changes, USB control, Bluetooth control, Wi-Fi control, process killing, or lockdown is implemented here.

## Goal

MVP 3 adds review-only detection rules to A.R.M.O.R. The system may identify suspicious patterns and explain why they deserve review, but it must not take destructive or restrictive action.

## Current foundation

- MVP 1 read-only status is frozen
- MVP 2 scan milestone is frozen
- ClamAV is installed and detected
- YARA is installed and detected
- self-check scan runs only against ~/citadel-ai/armor
- scan review helper summarizes private scan reports safely
- public samples are sanitized and tracked

## Safety boundary

MVP 3 must not:

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
- run broad user-folder scans by default
- treat review-only findings as confirmed malware

## Detection philosophy

Rules should classify signals, not make final judgments. A.R.M.O.R. should explain why something is suspicious and require user approval before any later containment phase.

## Initial rule categories

- suspicious executable names
- suspicious script extensions
- suspicious archive nesting
- suspicious startup locations
- suspicious double extensions
- suspicious world-writable files
- suspicious recently modified files in sensitive paths
- YARA self-check rules for A.R.M.O.R. source safety

## MVP 3 phases

### Phase 3.0 - rule schema

Define a small JSON-safe rule result schema:

- rule_id
- severity
- category
- path_redacted
- reason
- evidence_summary
- review_only
- recommended_next_step

### Phase 3.1 - YARA self-check rules

Create a tiny tracked YARA rule file under armor/rules/ for safe project self-check scanning.

Rules must be review-only and focused on obvious risky strings inside A.R.M.O.R. source code.

### Phase 3.2 - scan review normalization

Teach armor_review_scan.py to report whether ClamAV or YARA produced output without exposing raw private paths.

### Phase 3.3 - public sample refresh

Regenerate sanitized public self-check sample after rules are added.

## Implemented so far

- review-only YARA self-check rule file exists at armor/rules/armor_self_check.yar
- YARA self-check is scoped to root-level A.R.M.O.R. Python files only
- YARA exit code 1 is treated as matches_found_review_only, not a scan error
- public self-check sample reflects review-only YARA finding semantics
- scan review helper emits sanitized finding_summary entries

## Definition of done

MVP 3 planning is done when:

- this plan is committed
- at least one review-only YARA self-check rule exists
- self-check scan still runs only against ~/citadel-ai/armor
- scan output remains sanitized
- review helper reports findings without raw paths
- tracked leak checks pass

## Next implementation step

Add normalized review-only finding summaries to armor_review_scan.py. The review output should explain YARA matches without printing raw private paths or raw scan output. Do not expand scan targets yet.
