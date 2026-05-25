# Citadel A.R.M.O.R. Public Release Notes

This file summarizes public-safe showcase milestones.

## Current public state

- Current public seal: MVP20_PUBLIC_RELEASE_SEAL
- Current mode: review-only
- Enforcement: disabled
- Remediation: disabled
- Target scans in release seal: disabled
- Action execution: disabled

## Recent public-facing polish

| Phase | Change | Purpose |
|---|---|---|
| MVP21 | README polish after MVP20 seal | Updated the public overview from MVP1-era status to MVP20 seal status |
| MVP22 | VERIFY.md | Added public verification commands and expected outputs |
| MVP23 | QUICKSTART.md | Added the shortest safe review path for public reviewers |
| MVP24 | ARCHITECTURE.md | Added safety pipeline and helper-layer overview |
| MVP25 | ARTIFACTS.md | Added public artifact map across docs, helpers, and reports |

## Sealed runtime line

The public runtime showcase is sealed through MVP20 as review-only release seal output.

Key expected values:

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

## Public documentation set

- README.md
- QUICKSTART.md
- VERIFY.md
- ARCHITECTURE.md
- ARTIFACTS.md
- RELEASE_NOTES.md

## Safety note

Public release notes describe review-only showcase state. They do not introduce helper changes, sample changes, enforcement, remediation, or private target scanning.

## MVP54 public cross-platform summary update

Public-facing docs now reflect the sealed cross-platform regression layer.

Recent sealed milestones:

- MVP50 public cross-platform validation seal
- MVP51 public cross-platform regression helper
- MVP52 public cross-platform regression verification wiring
- MVP53 public cross-platform regression seal

Current cross-platform safety status:

- adapter validation passes
- cross-platform regression passes
- platform count remains 5
- runtime adapters remain disabled
- platform agents remain disabled
- enforcement remains disabled
- remediation remains disabled
- private target scans remain disabled
- action execution remains disabled

Boundary: this release note is documentation-only. It introduces no helper changes, sample changes, runtime adapters, platform agents, enforcement, remediation, target scans, or action execution.
