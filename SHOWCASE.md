# Citadel A.R.M.O.R. Showcase

## What it is

Citadel A.R.M.O.R. is a local-first active defense module for Citadel-AI.

A.R.M.O.R. means Autonomous Response Monitoring Operations and Resilience.

## Core idea

Traditional security tools often feel like silent black boxes. A.R.M.O.R. is designed to show the user what is happening on the machine, explain risk in plain English, and require approval before destructive actions.

## Current milestone

MVP 1 is read-only status visibility.

Current capabilities:

- confirms Citadel UI health
- reports tool availability
- observes network listeners
- observes Wi-Fi status
- observes Bluetooth status
- observes USB device inventory
- provides public-safe redacted output
- performs no blocking, deletion, quarantine, lockdown, or device control

## Safety principles

- local-first by default
- no cloud requirement
- no automatic deletion
- no hack-back
- no silent destructive action
- user approval required for quarantine and purge
- loopback and user control must be preserved
- public showcase output must be sanitized

## Planned phases

1. Armor Status - read-only visibility
2. Armor Scan - file and system scan summaries
3. Armor Vault - reversible quarantine
4. Armor Wi-Fi, Bluetooth, and USB awareness
5. Armor Gate - controlled network response
6. Armor Countermeasures - canaries and honeypots
7. Armor Lockdown - safe emergency isolation
8. Armor Drill - safe self-test simulations

## Public demo policy

Public materials must use sanitized output only. No real hostnames, usernames, SSIDs, Bluetooth IDs, USB IDs, IP addresses, file paths, logs, vault data, whitelist data, or baselines should be published.

## Build status

Private development is active. Public release is deferred until the MVP is stable, sanitized, and reviewed.

