# Citadel A.R.M.O.R. Public Test Matrix

This matrix lists the public-safe verification surfaces for the ARMOR showcase.

## Test scope

The public test scope is documentation, helper compilation, public release seal output, and public-safe marker checks.

## Matrix

| Area | Check | Pass condition |
|---|---|---|
| Git state | git status -sb | Repository is clean and aligned with origin/main |
| Public helpers | python3 -m py_compile public helper scripts | No output and exit code 0 |
| Release seal | armor_public_release_seal.py --public-sample | release_sealed is true |
| Review mode | public release seal output | review_only is true |
| Disabled actions | public release seal output | actions_enabled is false |
| Disabled enforcement | public release seal output | enforcement is false |
| Disabled remediation | public release seal output | remediation_enabled is false |
| Disabled scans | public release seal output | scan_executed and target_scan_executed are false |
| Disabled execution | public release seal output | action_executed is false |
| Public docs | README links | Public docs are linked from README.md |
| Local literals | local literal grep | No public local literal matches |
| Secret markers | public marker grep | No public secret marker matches |

## Compile command

```bash
python3 -m py_compile armor_public_release_seal.py armor_public_release_bundle.py armor_public_regression.py armor_pre_execution_freeze.py armor_execution_readiness.py armor_operator_confirm.py armor_emergency_stop.py armor_post_action_verify.py armor_action_ledger.py armor_action_preview.py armor_rollback_manifest.py armor_allowlist_validate.py armor_release_gate.py armor_policy.py
```

## Release seal command

```bash
python3 armor_public_release_seal.py --public-sample | grep -E '"mode":|"release_sealed":|"sealed_through":|"seal_phase":|"review_only":|"actions_enabled":|"enforcement":|"remediation_enabled":|"scan_executed":|"target_scan_executed":|"action_executed":'
```

## Expected release seal highlights

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

## Boundary

This public test matrix introduces no helper changes, sample logic changes, enforcement, remediation, target scans, or action execution.
