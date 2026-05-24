# Citadel A.R.M.O.R. Dependencies

## MVP 2 scan dependency status

A.R.M.O.R. MVP 2 scan planning now detects the following scan dependencies as present:

- clamscan
- freshclam
- yara
- sha256sum
- file
- find

## Installed package set

The MVP 2 scan dependency install used Ubuntu packages:

- clamav
- clamav-freshclam
- yara
- file
- findutils
- coreutils

## Current scan behavior

Scan execution is still disabled.

A.R.M.O.R. currently lists dependencies and planned profiles only. It does not scan files, quarantine files, delete files, purge files, change permissions, change firewall rules, disable Wi-Fi, disable Bluetooth, block USB devices, or enter lockdown.

## Notes

- clamav-daemon is not installed or required for the current MVP 2 planning stage.
- install logs are local runtime artifacts and are intentionally ignored by Git.
- public dependency output must remain sanitized.

## Verification command

    python3 armor/armor_scan.py --deps --profiles --public

