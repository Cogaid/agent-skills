#!/usr/bin/env python3
"""Semantic version bump calculator.

Analyzes commit messages to determine the correct version bump,
validates version strings, and supports pre-release version management.

Usage:
    python version_bump.py --current 1.2.3 --bump minor
    python version_bump.py --current 1.2.3 --commits "feat: new feature,fix: bug fix"
    python version_bump.py --demo
    python version_bump.py --demo --json
"""

import argparse
import json
import re
import sys


def parse_version(version_str):
    """Parse a semantic version string into components."""
    version = version_str.lstrip("v")
    pattern = re.compile(
        r"^(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)"
        r"(?:-(?P<prerelease>[a-zA-Z0-9.]+))?"
        r"(?:\+(?P<build>[a-zA-Z0-9.]+))?$"
    )
    match = pattern.match(version)
    if not match:
        return None

    return {
        "major": int(match.group("major")),
        "minor": int(match.group("minor")),
        "patch": int(match.group("patch")),
        "prerelease": match.group("prerelease"),
        "build": match.group("build"),
        "original": version_str,
    }


def bump_version(parsed, bump_type, prerelease_tag=None):
    """Apply a version bump and return the new version string."""
    major = parsed["major"]
    minor = parsed["minor"]
    patch = parsed["patch"]

    if bump_type == "MAJOR":
        major += 1
        minor = 0
        patch = 0
    elif bump_type == "MINOR":
        minor += 1
        patch = 0
    elif bump_type == "PATCH":
        patch += 1
    elif bump_type == "PRERELEASE":
        # Increment prerelease counter
        if parsed["prerelease"] and prerelease_tag:
            parts = parsed["prerelease"].split(".")
            if len(parts) == 2 and parts[0] == prerelease_tag:
                return f"{major}.{minor}.{patch}-{prerelease_tag}.{int(parts[1]) + 1}"
        if prerelease_tag:
            return f"{major}.{minor}.{patch}-{prerelease_tag}.1"
        return f"{major}.{minor}.{patch}-alpha.1"

    if prerelease_tag:
        return f"{major}.{minor}.{patch}-{prerelease_tag}.1"
    return f"{major}.{minor}.{patch}"


def determine_bump_from_commits(commits_str):
    """Determine version bump type from commit message prefixes."""
    commits = [c.strip() for c in commits_str.split(",") if c.strip()]

    has_breaking = False
    has_feat = False
    has_fix = False

    for commit in commits:
        lower = commit.lower()
        if "breaking" in lower or "!" in commit.split(":")[0]:
            has_breaking = True
        if lower.startswith("feat"):
            has_feat = True
        if lower.startswith("fix") or lower.startswith("security"):
            has_fix = True

    if has_breaking:
        return "MAJOR", commits
    elif has_feat:
        return "MINOR", commits
    elif has_fix:
        return "PATCH", commits
    return "PATCH", commits


def compare_versions(v1_str, v2_str):
    """Compare two version strings. Returns -1, 0, or 1."""
    v1 = parse_version(v1_str)
    v2 = parse_version(v2_str)

    if not v1 or not v2:
        return 0

    for key in ("major", "minor", "patch"):
        if v1[key] < v2[key]:
            return -1
        elif v1[key] > v2[key]:
            return 1

    # Pre-release versions have lower precedence
    if v1["prerelease"] and not v2["prerelease"]:
        return -1
    elif not v1["prerelease"] and v2["prerelease"]:
        return 1

    return 0


def validate_bump(current, new_version):
    """Validate that a version bump is semantically correct."""
    current_parsed = parse_version(current)
    new_parsed = parse_version(new_version)

    if not current_parsed or not new_parsed:
        return {"valid": False, "reason": "Invalid version format"}

    if compare_versions(new_version, current) <= 0:
        return {"valid": False, "reason": f"New version {new_version} is not greater than current {current}"}

    # Determine what kind of bump occurred
    if new_parsed["major"] > current_parsed["major"]:
        bump = "MAJOR"
    elif new_parsed["minor"] > current_parsed["minor"]:
        bump = "MINOR"
    else:
        bump = "PATCH"

    return {"valid": True, "bump_type": bump, "from": current, "to": new_version}


DEMO_SCENARIOS = [
    {"current": "1.2.3", "commits": "feat: add search filters,fix: correct date display", "description": "Minor bump (new feature)"},
    {"current": "2.0.0", "commits": "fix: resolve timeout,fix: handle null input", "description": "Patch bump (fixes only)"},
    {"current": "1.5.2", "commits": "feat!: change auth to OAuth 2.0,feat: add dark mode", "description": "Major bump (breaking change)"},
    {"current": "3.1.0", "commits": "perf: optimize query,docs: update readme", "description": "Patch bump (no features or fixes)"},
]


def main():
    parser = argparse.ArgumentParser(
        description="Semantic version bump calculator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Explicit bump
  %(prog)s --current 1.2.3 --bump minor

  # Determine bump from commits
  %(prog)s --current 1.2.3 --commits "feat: new feature,fix: bug fix"

  # Pre-release version
  %(prog)s --current 1.2.3 --bump minor --prerelease beta

  # Demo all scenarios
  %(prog)s --demo

  # JSON output
  %(prog)s --current 1.2.3 --bump major --json
        """,
    )
    parser.add_argument("--current", type=str, help="Current version string")
    parser.add_argument("--bump", type=str, choices=["major", "minor", "patch", "prerelease"],
                        help="Explicit bump type")
    parser.add_argument("--commits", type=str, help="Comma-separated commit messages")
    parser.add_argument("--prerelease", type=str, help="Pre-release tag (alpha, beta, rc)")
    parser.add_argument("--demo", action="store_true", help="Run demo scenarios")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    if args.demo:
        results = []
        for scenario in DEMO_SCENARIOS:
            parsed = parse_version(scenario["current"])
            bump_type, commits = determine_bump_from_commits(scenario["commits"])
            new_version = bump_version(parsed, bump_type)
            results.append({
                "description": scenario["description"],
                "current": scenario["current"],
                "commits": scenario["commits"],
                "bump_type": bump_type,
                "new_version": new_version,
            })

        if args.json:
            print(json.dumps({"scenarios": results}, indent=2))
        else:
            print("=" * 65)
            print("VERSION BUMP SCENARIOS")
            print("=" * 65)
            print()
            print(f"{'Scenario':<40} {'Current':>8} {'Bump':>7} {'New':>8}")
            print("-" * 65)
            for r in results:
                print(f"{r['description']:<40} {r['current']:>8} {r['bump_type']:>7} {r['new_version']:>8}")
            print()
            print("DETAILS")
            print("-" * 65)
            for r in results:
                print(f"\n  {r['description']}")
                print(f"  Commits: {r['commits']}")
                print(f"  {r['current']} -> {r['new_version']} ({r['bump_type']})")

    elif args.current:
        parsed = parse_version(args.current)
        if not parsed:
            print(f"Error: Invalid version format: {args.current}", file=sys.stderr)
            sys.exit(1)

        if args.commits:
            bump_type, commits = determine_bump_from_commits(args.commits)
        elif args.bump:
            bump_type = args.bump.upper()
        else:
            print("Provide --bump or --commits to determine version bump.")
            sys.exit(1)

        new_version = bump_version(parsed, bump_type, args.prerelease)
        validation = validate_bump(args.current, new_version)

        result = {
            "current": args.current,
            "parsed": parsed,
            "bump_type": bump_type,
            "new_version": new_version,
            "validation": validation,
        }

        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(f"Current version: {args.current}")
            print(f"Bump type: {bump_type}")
            print(f"New version: {new_version}")
            if validation["valid"]:
                print(f"Validation: PASS")
            else:
                print(f"Validation: FAIL - {validation['reason']}")
    else:
        print("Provide --current with --bump/--commits, or use --demo.")
        sys.exit(1)


if __name__ == "__main__":
    main()
