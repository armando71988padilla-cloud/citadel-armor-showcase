# Citadel A.R.M.O.R. Public Case Study

This case study explains the public ARMOR showcase as an engineering project.

## Problem

Security-adjacent automation can become dangerous if action paths are added before boundaries, rollback, operator review, and verification are proven.

ARMOR approaches that problem by building the safety chain first.

## Goal

Create a local-first active defense workflow that can demonstrate controlled planning and review without enabling enforcement, remediation, quarantine, purge, lockdown, or private target scans.

## Constraints

- public-safe repository only
- no private runtime dumps
- no secret material
- no enforcement behavior
- no remediation behavior
- no device control behavior
- no destructive actions
- review-only helper outputs

## Design approach

ARMOR was built as a staged safety pipeline:

```text
policy
  -> release gate
  -> allowlist validation
  -> rollback manifest
  -> action preview
  -> action ledger
  -> post-action verification
  -> emergency stop
  -> operator confirmation
  -> execution readiness
  -> pre-execution freeze
  -> public regression
  -> release bundle
  -> release seal
```

Each layer answers one safety question before the next layer is trusted.

## Result

The public showcase is sealed through MVP20 as review-only release seal output.

Current expected seal values:

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

## Engineering value

This showcase demonstrates:

- incremental delivery
- explicit safety boundaries
- public/private separation
- repeatable verification
- rollback-first planning
- operator confirmation modeling
- release seal discipline
- documentation for reviewers

## Tradeoff

The public showcase intentionally prioritizes safety proof over action capability. That means it does not demonstrate production enforcement. It demonstrates whether the system can prove enough safety before future enforcement is considered.

## Reviewer takeaway

ARMOR is strongest as a disciplined safety-first systems engineering example. It shows how to build trust gates around risky automation before allowing that automation to act.
