# Citadel A.R.M.O.R. Reviewer Guide

This guide helps reviewers evaluate the public ARMOR showcase quickly and safely.

## Recommended first pass

1. Read README.md for the project overview.
2. Read QUICKSTART.md for the shortest safe review path.
3. Read SAFETY.md to confirm disabled behavior.
4. Read ARCHITECTURE.md to understand the safety pipeline.
5. Read ARTIFACTS.md to navigate docs, helpers, and reports.
6. Run VERIFY.md commands if local verification is desired.

## What to look for

- Clear review-only safety boundary
- Public release seal output
- Helper scripts that compile
- Public samples that are redacted
- No enforcement or remediation behavior
- No private runtime dumps
- Explicit rollback, operator confirmation, emergency stop, and freeze planning

## Suggested command checks

```bash
git status -sb
python3 -m py_compile armor_public_release_seal.py armor_public_release_bundle.py armor_public_regression.py armor_pre_execution_freeze.py armor_execution_readiness.py armor_operator_confirm.py armor_emergency_stop.py armor_post_action_verify.py armor_action_ledger.py armor_action_preview.py armor_rollback_manifest.py armor_allowlist_validate.py armor_release_gate.py armor_policy.py
python3 armor_public_release_seal.py --public-sample
```

## Expected release seal highlights

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

## Evaluation notes

This repository is strongest as a safety-first engineering showcase. It demonstrates disciplined scope control, staged release gates, public-safe reporting, and explicit non-execution boundaries.

## Non-goals

The public showcase is not intended to prove production enforcement, malware removal, firewall control, device blocking, or private endpoint scanning.

## Good reviewer question

The most important question is not whether ARMOR can take action. The important question is whether ARMOR proves enough safety, rollback, operator review, and verification before any future action is allowed.
