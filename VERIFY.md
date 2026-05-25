# Verify Citadel A.R.M.O.R. Public Showcase

This guide verifies the public-safe ARMOR showcase without running enforcement, remediation, quarantine, purge, lockdown, or target scans.

## Safety expectation

All verification commands must preserve these values:

- review_only: true
- actions_enabled: false
- enforcement: false
- remediation_enabled: false
- scan_executed: false
- target_scan_executed: false
- action_executed: false

## 1. Confirm repository state

```bash
git status -sb
git log --oneline --decorate -n 10
```

Expected:

```text
## main...origin/main
```

## 2. Compile public helper scripts

```bash
python3 -m py_compile armor_public_release_seal.py armor_public_release_bundle.py armor_public_regression.py armor_pre_execution_freeze.py armor_execution_readiness.py armor_operator_confirm.py armor_emergency_stop.py armor_post_action_verify.py armor_action_ledger.py armor_action_preview.py armor_rollback_manifest.py armor_allowlist_validate.py armor_release_gate.py armor_policy.py
```

Expected: no output and exit code 0.

## 3. Run public release seal

```bash
python3 armor_public_release_seal.py --public-sample | grep -E '"mode":|"release_sealed":|"sealed_through":|"seal_phase":|"review_only":|"actions_enabled":|"enforcement":|"remediation_enabled":|"scan_executed":|"target_scan_executed":|"action_executed":'
```

Expected:

```text
"mode": "MVP20_PUBLIC_RELEASE_SEAL_REVIEW_ONLY"
"release_sealed": true
"sealed_through": "MVP19_PUBLIC_RELEASE_BUNDLE"
"seal_phase": "MVP20_PUBLIC_RELEASE_SEAL"
"review_only": true
"actions_enabled": false
"enforcement": false
"remediation_enabled": false
"scan_executed": false
"target_scan_executed": false
"action_executed": false
```

## 4. Check public README polish

```bash
grep -nE 'MVP20 public release seal|Architecture / safety pipeline|Milestone summary|armor_public_release_seal' README.md
```

Expected: matching lines for all four phrases.

## 5. Check for public secret marker leaks

This public guide intentionally avoids storing local machine names, usernames, network identifiers, or private path literals.

```bash
grep -RInE 'BEGIN [O]PENSSH PRIVATE KEY|BEGIN [R]SA PRIVATE KEY|github[_]pat_|gh[p]_|AKIA[0-9A-Z]{16}|xox[baprs]-' . || echo "NO_PUBLIC_SECRET_MARKER_MATCHES"
```

Expected:

```text
NO_PUBLIC_SECRET_MARKER_MATCHES
```

## Verified boundary

If all checks pass, the public showcase is sealed through MVP20 as review-only public release seal output.

No enforcement or remediation behavior is present in this public showcase.

## Validate platform adapter public samples

Run the review-only platform adapter sample validator:

```bash
python3 armor_platform_adapter_validate.py --public-sample | grep -E '"mode":|"review_only":|"actions_enabled":|"enforcement":|"remediation_enabled":|"target_scan_executed":|"validation_executed":|"sample_runtime_enabled":|"validation_passed":|"platform_count":'
```

Expected highlights:

```text
"mode": "MVP47_PLATFORM_ADAPTER_VALIDATION_REVIEW_ONLY"
"validation_passed": true
"platform_count": 5
"review_only": true
"actions_enabled": false
"enforcement": false
"remediation_enabled": false
"target_scan_executed": false
"sample_runtime_enabled": false
```

This validates public-safe adapter sample shape only. It does not run platform agents, scan private targets, enable enforcement, enable remediation, or execute actions.

## Run cross-platform public regression

Run the review-only cross-platform regression helper:

```bash
python3 armor_cross_platform_regression.py --public-sample | grep -E '"mode":|"review_only":|"actions_enabled":|"enforcement":|"remediation_enabled":|"target_scan_executed":|"runtime_adapters_enabled":|"platform_agents_enabled":|"regression_executed":|"required_files_ok":|"adapter_validation_passed":|"adapter_validation_platform_count":|"locked_flags_ok":|"cross_platform_regression_passed":'
```

Expected highlights:

```text
"mode": "MVP51_CROSS_PLATFORM_REGRESSION_REVIEW_ONLY"
"cross_platform_regression_passed": true
"adapter_validation_passed": true
"adapter_validation_platform_count": 5
"required_files_ok": true
"locked_flags_ok": true
"review_only": true
"actions_enabled": false
"enforcement": false
"remediation_enabled": false
"target_scan_executed": false
"runtime_adapters_enabled": false
"platform_agents_enabled": false
```

This validates public cross-platform docs, samples, and adapter validation only. It does not run platform agents, scan private targets, enable enforcement, enable remediation, or execute actions.
