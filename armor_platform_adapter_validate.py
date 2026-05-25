#!/usr/bin/env python3
"""Citadel A.R.M.O.R. public platform adapter sample validator."""

import argparse
import json
from pathlib import Path

EXPECTED_PLATFORMS = ["linux", "windows", "macos", "android", "ios"]

LOCKED_FALSE_FLAGS = [
    "actions_enabled",
    "enforcement",
    "remediation_enabled",
    "target_scan_executed",
]

REQUIRED_ARRAY_FIELDS = [
    "platform_capabilities",
    "posture_checks",
    "denied_capabilities",
    "operator_notes",
]


def validate_sample(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    failures = []

    if data.get("mode") != "MVP46_PLATFORM_ADAPTER_PUBLIC_SAMPLES_REVIEW_ONLY":
        failures.append("unexpected_mode")
    if data.get("review_only") is not True:
        failures.append("top_review_only_not_true")
    for flag in LOCKED_FALSE_FLAGS:
        if data.get(flag) is not False:
            failures.append(f"top_{flag}_not_false")
    if data.get("sample_runtime_enabled") is not False:
        failures.append("sample_runtime_enabled_not_false")
    if data.get("adapter_samples_present") is not True:
        failures.append("adapter_samples_present_not_true")

    samples = data.get("platform_adapter_samples")
    if not isinstance(samples, list):
        failures.append("platform_adapter_samples_not_list")
        samples = []

    platforms = [item.get("platform") for item in samples if isinstance(item, dict)]
    if platforms != EXPECTED_PLATFORMS:
        failures.append("platform_order_or_set_mismatch")
    if data.get("platform_count") != len(EXPECTED_PLATFORMS):
        failures.append("platform_count_mismatch")

    platform_results = []
    for item in samples:
        item_failures = []
        if not isinstance(item, dict):
            failures.append("platform_entry_not_object")
            continue
        platform = item.get("platform")
        if platform not in EXPECTED_PLATFORMS:
            item_failures.append("unexpected_platform")
        if item.get("adapter_version") != "0.1-review-only":
            item_failures.append("adapter_version_mismatch")
        if item.get("review_only") is not True:
            item_failures.append("review_only_not_true")
        for flag in LOCKED_FALSE_FLAGS:
            if item.get(flag) is not False:
                item_failures.append(f"{flag}_not_false")
        for field in REQUIRED_ARRAY_FIELDS:
            if not isinstance(item.get(field), list):
                item_failures.append(f"{field}_not_list")
        platform_results.append({
            "platform": platform,
            "passed": not item_failures,
            "failures": item_failures,
        })
        failures.extend([f"{platform}:{failure}" for failure in item_failures])

    return {
        "mode": "MVP47_PLATFORM_ADAPTER_VALIDATION_REVIEW_ONLY",
        "review_only": True,
        "actions_enabled": False,
        "enforcement": False,
        "remediation_enabled": False,
        "target_scan_executed": False,
        "validation_executed": True,
        "sample_runtime_enabled": False,
        "sample_path": "reports/platform_adapter_public_sample.json",
        "expected_platforms": EXPECTED_PLATFORMS,
        "platform_count": len(platform_results),
        "platform_results": platform_results,
        "validation_passed": not failures,
        "failures": failures,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate public ARMOR platform adapter sample output")
    parser.add_argument("--sample", default="reports/platform_adapter_public_sample.json", help="sample JSON path to validate")
    parser.add_argument("--public-sample", action="store_true", help="emit public-safe validation output")
    args = parser.parse_args()
    result = validate_sample(Path(args.sample))
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result.get("validation_passed") else 1


if __name__ == "__main__":
    raise SystemExit(main())
