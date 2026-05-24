# Citadel A.R.M.O.R. MVP 2 Scan Plan

## Status

Planning phase only. No scanning engine install, quarantine, purge, blocking, or enforcement is implemented here.

## Goal

MVP 2 adds read-only scan awareness to A.R.M.O.R. The first implementation must detect available scan tools, define safe scan profiles, run only explicit read-only scans, and summarize results without deleting or moving anything.

## Current known state

- armor_status.py reports clamscan as missing
- baseline review reports clamscan_missing
- A.R.M.O.R. has working read-only status, capture, baseline, and baseline review helpers
- public-safe samples are tracked
- private runtime outputs are ignored by Git

## Safety boundary

MVP 2 must not:

- delete files
- quarantine files
- purge files
- change permissions
- modify firewall
- disconnect Wi-Fi
- disable Bluetooth
- block USB devices
- kill processes
- install packages without an explicit install step
- scan huge roots without an explicit profile

## Scan philosophy

Scanners detect. A.R.M.O.R. explains. The user authorizes containment later.

## Initial scan tool targets

- ClamAV for signature scanning
- YARA for rule-based pattern scanning
- Python stdlib hashing for file identity
- existing status and baseline data for context

## MVP 2 phases

### Phase 2.0 - dependency inspection

Read-only check for available tools:

- clamscan
- freshclam
- yara
- sha256sum
- file
- find

### Phase 2.1 - scan profile design

Define conservative scan profiles:

- quick_downloads
- quick_desktop
- quick_documents
- mounted_usb_review
- startup_paths_review
- citadel_armor_self_check

### Phase 2.2 - read-only scan runner

Create armor_scan.py with:

- list profiles
- run one explicit profile
- timeout controls
- capped output
- JSON report
- public-safe summary mode
- no deletion
- no quarantine

### Phase 2.3 - report capture

Save private scan reports under ignored storage:

- armor/reports/scan_private_*.json

Save sanitized samples only after review:

- armor/reports/scan_public_sample.json

## Required guardrails

- Every scan command must be explicit
- Every scan must have a timeout
- Every scan must cap output
- Every report must record the profile name
- Every suspicious finding must be marked review_only
- No finding may trigger enforcement in MVP 2

## Definition of done

MVP 2 scan planning is done when:

- this plan is committed
- dependency inspection is implemented read-only
- scan profiles are listed without executing them
- first scan runner compiles
- first scan runner can run a tiny self-check profile
- public output is sanitized
- tracked leak check passes

## Next implementation step

Create armor_scan.py with dependency inspection and profile listing only. Do not run file scans yet.

