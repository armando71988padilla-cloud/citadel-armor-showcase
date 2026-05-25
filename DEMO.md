# Citadel A.R.M.O.R. Public Demo

This demo shows the expected public-safe verification path and release seal output.

## Demo goal

Show that the public showcase is sealed through MVP20 while preserving review-only behavior.

## Step 1: Confirm repository state

```bash
git status -sb
git log --oneline --decorate -n 8
```

Expected current branch state:

```text
## main...origin/main
```

Expected recent public-facing commits include:

```text
Add public ARMOR release notes
Add public ARMOR artifact index
Add public ARMOR architecture overview
Add public ARMOR quickstart
```

## Step 2: Compile public helpers

```bash
python3 -m py_compile armor_public_release_seal.py armor_public_release_bundle.py armor_public_regression.py armor_pre_execution_freeze.py armor_execution_readiness.py armor_operator_confirm.py armor_emergency_stop.py armor_post_action_verify.py armor_action_ledger.py armor_action_preview.py armor_rollback_manifest.py armor_allowlist_validate.py armor_release_gate.py armor_policy.py
```

Expected: no output and exit code 0.

## Step 3: Run public release seal

```bash
python3 armor_public_release_seal.py --public-sample | grep -E '"mode":|"release_sealed":|"sealed_through":|"seal_phase":|"review_only":|"actions_enabled":|"enforcement":|"remediation_enabled":|"scan_executed":|"target_scan_executed":|"action_executed":'
```

Expected output:

```text
"action_executed": false
"actions_enabled": false
"enforcement": false
"mode": "MVP20_PUBLIC_RELEASE_SEAL_REVIEW_ONLY"
"release_sealed": true
"remediation_enabled": false
"review_only": true
"scan_executed": false
"seal_phase": "MVP20_PUBLIC_RELEASE_SEAL"
"sealed_through": "MVP19_PUBLIC_RELEASE_BUNDLE"
"target_scan_executed": false
```

## Step 4: Confirm public docs are linked

```bash
grep -nE 'quickstart: QUICKSTART.md|architecture: ARCHITECTURE.md|artifact index: ARTIFACTS.md|release notes: RELEASE_NOTES.md|verification guide: VERIFY.md' README.md
```

Expected: all linked documentation files are listed.

## Step 5: Confirm public-safe marker checks

```bash
grep -RInE 'BEGIN [O]PENSSH PRIVATE KEY|BEGIN [R]SA PRIVATE KEY|github[_]pat_|gh[p]_|AKIA[0-9A-Z]{16}|xox[baprs]-' README.md VERIFY.md QUICKSTART.md ARCHITECTURE.md ARTIFACTS.md RELEASE_NOTES.md DEMO.md || echo "NO_PUBLIC_SECRET_MARKER_MATCHES"
```

Expected:

```text
NO_PUBLIC_SECRET_MARKER_MATCHES
```

## Demo result

If all steps match expected output, the public showcase demonstrates a review-only release seal with no enforcement, remediation, target scanning, or action execution.
