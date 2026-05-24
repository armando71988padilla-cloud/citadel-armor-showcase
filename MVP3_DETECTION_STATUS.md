# Citadel A.R.M.O.R. MVP 3 Detection Rules Freeze Status

## Status

MVP 3 detection rules milestone is frozen as a stable review-only checkpoint.

## Freeze commit

Current freeze base: 93dd70b

## Proven capabilities

- review-only YARA self-check rule file exists
- YARA self-check is scoped to root-level A.R.M.O.R. Python files only
- YARA exit code 1 is treated as matches_found_review_only
- YARA matches are review-only findings, not scan failures
- scan review helper emits sanitized finding_summary entries
- raw YARA output is not printed by public review output
- private scan report paths are redacted in public scan output
- tracked leak checks passed

## Safety boundary

MVP 3 does not perform quarantine, deletion, purge, permission changes, firewall changes, Wi-Fi changes, Bluetooth changes, USB blocking, process killing, auto-remediation, or lockdown.

## Known non-blockers

- only the self-check profile is executable
- broader user-folder scan profiles remain planned only
- finding summaries are intentionally generic until more rule metadata is added

## Freeze rule

Do not expand MVP 3 further without starting a new phase. Next work should be MVP 4 planning for controlled scan profile expansion or improved rule metadata, still review-only.

