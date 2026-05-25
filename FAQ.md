# Citadel A.R.M.O.R. Public FAQ

## What is Citadel A.R.M.O.R.?

Citadel A.R.M.O.R. is a local-first active defense showcase focused on safety gates, review-only planning, rollback requirements, operator confirmation, and public-safe verification.

## Is this an enforcement tool?

No. The public showcase is review-only.

## Does it quarantine, purge, lock down, or remediate anything?

No. Those behaviors are intentionally disabled and out of scope for the public showcase.

## Why build review-only layers first?

Security-adjacent automation can cause damage if action paths exist before safety boundaries. ARMOR builds policy, release gates, allowlists, rollback manifests, previews, ledgers, verification plans, emergency stop checks, operator confirmation, and freeze checks before any future action capability is considered.

## What does MVP20 seal mean?

MVP20 public release seal means the public showcase can prove expected files and safety flags for the review-only release chain.

Expected seal highlights:

```text
mode: MVP20_PUBLIC_RELEASE_SEAL_REVIEW_ONLY
release_sealed: true
sealed_through: MVP19_PUBLIC_RELEASE_BUNDLE
review_only: true
actions_enabled: false
enforcement: false
remediation_enabled: false
scan_executed: false
target_scan_executed: false
action_executed: false
```

## What should reviewers read first?

Start with DOCS_INDEX.md, QUICKSTART.md, and VERIFY.md.

## What is the fastest command check?

Run the public release seal helper:

```bash
python3 armor_public_release_seal.py --public-sample
```

## Are public samples sanitized?

Yes. The showcase uses public-safe sample outputs and avoids private runtime dumps.

## Why are there many documentation files?

The project is safety-sensitive. Separate docs make the safety boundary, verification path, artifact map, architecture, roadmap, and reviewer expectations easy to inspect without changing runtime behavior.

## What would future enforcement require?

Future enforcement would require a separate private design phase, explicit authorization, allowlist boundaries, rollback completeness, dry-run parity, emergency stop readiness, post-action verification, regression proof, and release freeze approval.

## What is the main engineering takeaway?

ARMOR demonstrates proof-before-action: risky automation should prove scope, rollback, confirmation, verification, and release safety before it can act.
