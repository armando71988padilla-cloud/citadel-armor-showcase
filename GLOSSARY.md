# Citadel A.R.M.O.R. Public Glossary

This glossary defines recurring terms used in the public ARMOR showcase.

## Review-only

A mode where helpers report state, plans, boundaries, or readiness without executing enforcement, remediation, scans, or actions.

## Public-safe

Content designed for the public showcase. Public-safe files avoid private runtime dumps, local machine details, secrets, credentials, and private target data.

## Release seal

A review-only summary that reports whether the expected public release files and safety flags are present.

## Public release bundle

A review-only summary that checks expected public documents, helpers, and sample reports.

## Public regression

A review-only aggregation check that confirms public helpers compile and public samples preserve locked safety flags.

## Pre-execution freeze

A final review checkpoint that verifies readiness blockers before any future execution path could be considered.

## Execution readiness

An aggregation layer that reports whether required safety components are present before future execution work.

## Operator confirmation

A modeled requirement that future risky actions must require explicit operator review and confirmation.

## Emergency stop

A modeled safety boundary for halting or preventing future risky action paths.

## Post-action verification

A planned verification layer describing what must be checked after a future action. In this public showcase, it is schema-only and does not execute actions.

## Action ledger

A modeled audit trail for future action records. In this public showcase, it records structure only.

## Action preview

A review-only representation of what a future action would intend to do before any action is allowed.

## Rollback manifest

A plan describing rollback information that must exist before future risky changes are considered.

## Allowlist validation

A review-only classification step that separates allowed targets from denied or out-of-scope targets.

## Release gate

A review-only checkpoint that reports whether release requirements are satisfied before moving forward.

## Safe target policy

A policy layer defining which target classes are considered safe to review in public helper output.

## Disabled behavior

Behavior intentionally absent from the public showcase, including enforcement, remediation, quarantine, purge, lockdown, firewall changes, device blocking, permission changes, process kills, and private target scans.

## Current public seal

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
