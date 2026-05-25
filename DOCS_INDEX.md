# Citadel A.R.M.O.R. Public Docs Index

This index gives reviewers one ordered path through the public ARMOR showcase.

## Fast path

1. README.md
2. QUICKSTART.md
3. VERIFY.md
4. DEMO.md

## Architecture and safety path

1. SAFETY.md
2. ARCHITECTURE.md
3. ARTIFACTS.md
4. ROADMAP.md

## Reviewer path

1. REVIEWER_GUIDE.md
2. CASE_STUDY.md
3. RELEASE_NOTES.md

## Runtime seal path

1. MVP20_PUBLIC_RELEASE_SEAL_PLAN.md
2. MVP20_PUBLIC_RELEASE_SEAL_STATUS.md
3. armor_public_release_seal.py
4. reports/public_release_seal_public_sample.json

## What each public doc answers

| File | Question answered |
|---|---|
| README.md | What is this project and what is sealed? |
| QUICKSTART.md | What is the fastest safe review path? |
| VERIFY.md | How do I verify the public release seal? |
| DEMO.md | What should expected output look like? |
| SAFETY.md | What behavior is disabled? |
| ARCHITECTURE.md | How is the safety pipeline structured? |
| ARTIFACTS.md | Where are docs, helpers, and samples? |
| ROADMAP.md | What is complete and what is deferred? |
| REVIEWER_GUIDE.md | How should a reviewer evaluate this? |
| CASE_STUDY.md | What engineering problem does this solve? |
| RELEASE_NOTES.md | What changed recently? |

## Current seal

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

## Boundary

This docs index is public-only documentation. It introduces no helper changes, sample changes, enforcement, remediation, target scans, or action execution.
