# Citadel A.R.M.O.R. Quickstart

This quickstart shows the shortest public-safe path for reviewing the ARMOR showcase.

## What this project is

Citadel A.R.M.O.R. is a local-first active defense showcase focused on controlled review, safety gates, rollback planning, and public-safe verification.

The public showcase is sealed through MVP20 as review-only output.

## What this project is not

- not an enforcement tool
- not a remediation tool
- not a quarantine tool
- not a purge tool
- not a lockdown tool
- not a firewall manager
- not a Wi-Fi, Bluetooth, or USB blocker
- not a private runtime dump

## Fast verification

Run the verification guide:

```bash
sed -n '1,220p' VERIFY.md
```

Then run the public release seal check:

```bash
python3 armor_public_release_seal.py --public-sample | grep -E '"mode":|"release_sealed":|"sealed_through":|"seal_phase":|"review_only":|"actions_enabled":|"enforcement":|"remediation_enabled":|"scan_executed":|"target_scan_executed":|"action_executed":'
```

Expected highlights:

```text
"mode": "MVP20_PUBLIC_RELEASE_SEAL_REVIEW_ONLY"
"release_sealed": true
"sealed_through": "MVP19_PUBLIC_RELEASE_BUNDLE"
"review_only": true
"actions_enabled": false
"enforcement": false
"remediation_enabled": false
"scan_executed": false
"target_scan_executed": false
"action_executed": false
```

## Recommended review order

1. README.md
2. VERIFY.md
3. MVP20_PUBLIC_RELEASE_SEAL_PLAN.md
4. reports/public_release_seal_public_sample.json
5. armor_public_release_seal.py

## Safety boundary

Every public helper is designed to preserve review-only behavior. Public verification must not execute actions, scan private targets, change firewall state, alter devices, or modify permissions.
