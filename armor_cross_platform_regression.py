#!/usr/bin/env python3
"""Citadel A.R.M.O.R. public cross-platform regression helper."""

import argparse
import json
import subprocess
import sys
from pathlib import Path

REQUIRED_FILES = [
    "CROSS_PLATFORM_STRATEGY.md",
    "PLATFORM_CAPABILITY_MATRIX.md",
    "PLATFORM_ADAPTER_CONTRACT.md",
    "PLATFORM_ADAPTER_PUBLIC_SAMPLES.md",
    "PLATFORM_ADAPTER_VALIDATION.md",
    "CROSS_PLATFORM_RELEASE_SEAL.md",
    "CROSS_PLATFORM_VALIDATION_SEAL.md",
    "LINUX_ADAPTER_PLAN.md",
    "WINDOWS_ADAPTER_PLAN.md",
    "MACOS_ADAPTER_PLAN.md",
    "ANDROID_ADAPTER_PLAN.md",
    "IOS_ADAPTER_PLAN.md",
    "reports/platform_adapter_public_sample.json",
    "reports/platform_adapter_validation_public_sample.json",
    "armor_platform_adapter_validate.py",
]

LOCKED_FALSE_FLAGS = [
    "actions_enabled",
    "enforcement",
    "remediation_enabled",
    "target_scan_executed",
    "sample_runtime_enabled",
]


def run_adapter_validation() -> dict:
    proc = subprocess.run(
        [sys.executable, "armor_platform_adapter_validate.py", "--public-sample"],
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    parsed = None
    parse_ok = False
    if proc.stdout.strip():
        try:
            parsed = json.loads(proc.stdout)
            parse_ok = True
        except json.JSONDecodeError:
            parsed = None
    return {
        "run_ok": proc.returncode == 0,
        "parse_ok": parse_ok,
        "returncode": proc.returncode,
        "stderr_present": bool(proc.stderr.strip()),
        "parsed": parsed,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Run public ARMOR cross-platform regression checks")
    parser.add_argument("--public-sample", action="store_true", help="emit public-safe regression output")
    args = parser.parse_args()

    missing_files = [path for path in REQUIRED_FILES if not Path(path).exists()]
    validation = run_adapter_validation()
    parsed = validation.get("parsed") or {}

    locked_flags_ok = parsed.get("review_only") is True
    for flag in LOCKED_FALSE_FLAGS:
        locked_flags_ok = locked_flags_ok and parsed.get(flag) is False

    regression_passed = (
        not missing_files
        and validation.get("run_ok") is True
        and validation.get("parse_ok") is True
        and parsed.get("validation_passed") is True
        and parsed.get("platform_count") == 5
        and locked_flags_ok
    )

    result = {
        "mode": "MVP51_CROSS_PLATFORM_REGRESSION_REVIEW_ONLY",
        "review_only": True,
        "actions_enabled": False,
        "enforcement": False,
        "remediation_enabled": False,
        "target_scan_executed": False,
        "runtime_adapters_enabled": False,
        "platform_agents_enabled": False,
        "regression_executed": True,
        "required_files_ok": not missing_files,
        "missing_files": missing_files,
        "adapter_validation_run_ok": validation.get("run_ok"),
        "adapter_validation_parse_ok": validation.get("parse_ok"),
        "adapter_validation_passed": parsed.get("validation_passed") is True,
        "adapter_validation_platform_count": parsed.get("platform_count"),
        "locked_flags_ok": locked_flags_ok,
        "cross_platform_regression_passed": regression_passed,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if regression_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
