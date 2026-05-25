# Citadel A.R.M.O.R. Public Project Summary

## One-line summary

Citadel A.R.M.O.R. is a local-first active defense showcase that proves safety gates, rollback planning, operator review, and release sealing before any action capability is considered.

## Current public state

- Public seal: MVP20_PUBLIC_RELEASE_SEAL
- Mode: review-only
- Enforcement: disabled
- Remediation: disabled
- Target scans: disabled in release seal output
- Action execution: disabled

## What is proven

- Public helper scripts compile
- Public release seal reports locked safety flags
- Public samples are review-only
- Documentation clearly explains safety boundaries
- Reviewer paths are documented
- Public local literal and secret marker checks pass

## What is intentionally not present

- production enforcement
- automatic remediation
- quarantine or purge behavior
- lockdown behavior
- firewall or device control
- permission modification
- process termination
- private endpoint scanning

## Why this matters

Security-adjacent automation should not be trusted just because it can act. ARMOR demonstrates the safer engineering order: prove scope, rollback, preview, ledgering, confirmation, emergency stop, readiness, freeze checks, regression, and release seal first.

## Best review path

1. DOCS_INDEX.md
2. QUICKSTART.md
3. VERIFY.md
4. SAFETY.md
5. ARCHITECTURE.md
6. TEST_MATRIX.md
7. REVIEWER_GUIDE.md

## Current seal highlights

```text
mode: MVP20_PUBLIC_RELEASE_SEAL_REVIEW_ONLY
release_sealed: true
sealed_through: MVP19_PUBLIC_RELEASE_BUNDLE
seal_phase: MVP20_PUBLIC_RELEASE_SEAL
review_only: true
actions_enabled: false
enforcement: false
remediation_enabled: false
scan_executed: false
target_scan_executed: false
action_executed: false
```

## Bottom line

This repository is best evaluated as a safety-first systems engineering showcase. It demonstrates disciplined release gates around risky automation, not production action execution.

## Cross-platform milestone

ARMOR now includes a public-safe cross-platform adapter planning and regression layer for Linux, Windows, macOS, Android, and iOS.

Current cross-platform proof:

- platform adapter contract is documented
- Linux, Windows, macOS, Android, and iOS adapter plans are documented
- public adapter samples exist for all 5 platforms
- adapter sample validation passes
- cross-platform regression passes
- cross-platform validation seal is present
- cross-platform regression seal is present

Current cross-platform boundary:

- runtime adapters are disabled
- platform agents are disabled
- enforcement is disabled
- remediation is disabled
- private target scans are disabled
- action execution is disabled

This keeps the project positioned as a safety-first framework before any platform-specific runtime implementation.
