#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

SAFE_PROFILES = {
    "self_check": {"allowed_roots": ["status", "baseline", "reports", "rules"], "review_only": True},
    "quick_downloads": {"allowed_roots": ["reports"], "review_only": True},
    "public_showcase": {"allowed_roots": ["reports", "rules"], "review_only": True},
}

DENIED_MARKERS = [
    "/etc",
    "/boot",
    "/root",
    "/var",
    "/usr",
    "/bin",
    "/sbin",
    "/lib",
    "/lib64",
    "/dev",
    "/proc",
    "/sys",
    "~/.ssh",
    "~/.gnupg",
]

def normalize_target(raw):
    text = str(raw).strip()
    if not text:
        return ""
    return text.replace("\\", "/")

def classify_target(target, profile):
    normalized = normalize_target(target)
    if not normalized:
        return {"target": target, "decision": "unresolved", "reason": "empty_target"}
    for marker in DENIED_MARKERS:
        if normalized == marker or normalized.startswith(marker + "/"):
            return {"target": target, "decision": "denied", "reason": "denied_system_or_private_path"}
    parts = [part for part in normalized.split("/") if part]
    if ".ssh" in parts or ".gnupg" in parts:
        return {"target": target, "decision": "denied", "reason": "denied_home_credential_path"}
    profile_data = SAFE_PROFILES.get(profile)
    if profile_data is None:
        return {"target": target, "decision": "unresolved", "reason": "unknown_profile"}
    allowed_roots = profile_data["allowed_roots"]
    first = normalized.split("/", 1)[0]
    if first in allowed_roots:
        return {"target": target, "decision": "allowed", "reason": "matches_review_only_profile_root"}
    return {"target": target, "decision": "denied", "reason": "outside_profile_allowlist"}

def build_report(profile, targets):
    results = [classify_target(t, profile) for t in targets]
    allowed = [r for r in results if r["decision"] == "allowed"]
    denied = [r for r in results if r["decision"] == "denied"]
    unresolved = [r for r in results if r["decision"] == "unresolved"]
    return {
        "mode": "MVP9_ALLOWLIST_VALIDATION_REVIEW_ONLY",
        "profile": profile,
        "review_only": True,
        "enforcement": False,
        "actions_enabled": False,
        "remediation_enabled": False,
        "scan_executed": False,
        "allowed_profiles": sorted(SAFE_PROFILES.keys()),
        "allowed_targets": allowed,
        "denied_targets": denied,
        "unresolved_targets": unresolved,
        "summary": {
            "target_count": len(results),
            "allowed_count": len(allowed),
            "denied_count": len(denied),
            "unresolved_count": len(unresolved),
        },
    }

def main():
    parser = argparse.ArgumentParser(description="ARMOR MVP9 review-only allowlist validation helper")
    parser.add_argument("--profile", default="self_check", help="review-only profile to validate")
    parser.add_argument("targets", nargs="*", help="relative targets to validate")
    parser.add_argument("--public-sample", action="store_true", help="write reports/allowlist_validation_public_sample.json")
    args = parser.parse_args()
    targets = args.targets or ["status", "baseline", "reports", "rules", "/etc/passwd", "~/.ssh/id_rsa", "unknown/path"]
    report = build_report(args.profile, targets)
    text = json.dumps(report, indent=2, sort_keys=True)
    print(text)
    if args.public_sample:
        out = Path("reports") / "allowlist_validation_public_sample.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
