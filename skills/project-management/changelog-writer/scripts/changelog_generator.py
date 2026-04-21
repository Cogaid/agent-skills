#!/usr/bin/env python3
"""Changelog generator from conventional commits.

Parses git commit messages following the Conventional Commits standard,
categorizes them into Keep a Changelog groups, and generates formatted
changelog entries. Can also determine the appropriate version bump.

Usage:
    python changelog_generator.py --demo
    python changelog_generator.py --repo /path/to/repo --since v1.0.0
    python changelog_generator.py --demo --json
"""

import argparse
import json
import re
import subprocess
import sys
from datetime import date


COMMIT_PATTERN = re.compile(
    r"^(?P<type>\w+)"
    r"(?:\((?P<scope>[^)]+)\))?"
    r"(?P<breaking>!)?"
    r":\s*"
    r"(?P<description>.+)$"
)

TYPE_TO_CATEGORY = {
    "feat": "Added",
    "fix": "Fixed",
    "perf": "Changed",
    "refactor": "Changed",
    "docs": None,
    "style": None,
    "test": None,
    "build": None,
    "ci": None,
    "chore": None,
    "revert": "Fixed",
    "deprecate": "Deprecated",
    "remove": "Removed",
    "security": "Security",
}

CATEGORY_ORDER = ["Added", "Changed", "Deprecated", "Removed", "Fixed", "Security"]

SAMPLE_COMMITS = [
    "abc1234 feat(search): add date range filter for search results (#289)",
    "def5678 feat: add PDF export for all report types (#234)",
    "ghi9012 feat(ui): add dark mode support with system preference detection (#256)",
    "jkl3456 fix: resolve timeout when uploading files larger than 50MB (#245)",
    "mno7890 fix(tz): correct timezone display for UTC-offset zones (#251)",
    "pqr1234 fix(search): handle special characters in search queries (#263)",
    "stu5678 perf(dashboard): optimize main query reducing load time by 40% (#271)",
    "vwx9012 feat!: change API response envelope format",
    "yza3456 security: patch XSS vulnerability in comment rendering (#278)",
    "bcd7890 security: update dependencies for CVE-2026-12345 (#282)",
    "efg1234 deprecate(export): mark XML export for removal in v3.0 (#289)",
    "hij5678 chore: update eslint config",
    "klm9012 docs: update API reference for new endpoints",
    "nop3456 test: add integration tests for billing module",
    "qrs7890 refactor(auth): simplify middleware chain",
]


def parse_commit(line):
    """Parse a conventional commit message into structured data."""
    # Strip hash prefix if present
    parts = line.split(" ", 1)
    if len(parts) == 2 and re.match(r"^[a-f0-9]+$", parts[0]):
        hash_val = parts[0]
        message = parts[1]
    else:
        hash_val = ""
        message = line

    match = COMMIT_PATTERN.match(message)
    if not match:
        return None

    commit_type = match.group("type")
    scope = match.group("scope") or ""
    is_breaking = bool(match.group("breaking"))
    description = match.group("description").strip()

    # Check for BREAKING CHANGE in message
    if "BREAKING CHANGE" in line.upper() or "BREAKING:" in line.upper():
        is_breaking = True

    category = TYPE_TO_CATEGORY.get(commit_type)

    # Extract PR/issue reference
    ref_match = re.search(r"\(#(\d+)\)", description)
    reference = f"#{ref_match.group(1)}" if ref_match else ""

    return {
        "hash": hash_val,
        "type": commit_type,
        "scope": scope,
        "description": description,
        "category": category,
        "is_breaking": is_breaking,
        "reference": reference,
        "include_in_changelog": category is not None,
    }


def determine_version_bump(commits):
    """Determine the version bump type from parsed commits."""
    has_breaking = any(c["is_breaking"] for c in commits if c)
    has_feat = any(c["type"] == "feat" for c in commits if c)
    has_fix = any(c["type"] in ("fix", "security") for c in commits if c)

    if has_breaking:
        return "MAJOR"
    elif has_feat:
        return "MINOR"
    elif has_fix:
        return "PATCH"
    return "PATCH"


def bump_version(current, bump_type):
    """Apply version bump to a version string."""
    version = current.lstrip("v")
    parts = version.split(".")
    major, minor, patch = int(parts[0]), int(parts[1]), int(parts[2].split("-")[0])

    if bump_type == "MAJOR":
        return f"{major + 1}.0.0"
    elif bump_type == "MINOR":
        return f"{major}.{minor + 1}.0"
    else:
        return f"{major}.{minor}.{patch + 1}"


def generate_changelog(commits, version=None):
    """Generate changelog markdown from parsed commits."""
    # Group by category
    categories = {}
    breaking_changes = []

    for commit in commits:
        if not commit or not commit["include_in_changelog"]:
            continue
        cat = commit["category"]
        if cat not in categories:
            categories[cat] = []

        entry = commit["description"]
        if commit["is_breaking"]:
            entry = f"**BREAKING:** {entry}"
            breaking_changes.append(entry)

        categories[cat].append(entry)

    # Build markdown
    lines = []
    version_label = version or "Unreleased"
    today = date.today().isoformat()
    lines.append(f"## [{version_label}] - {today}")
    lines.append("")

    for cat in CATEGORY_ORDER:
        if cat in categories:
            lines.append(f"### {cat}")
            lines.append("")
            for entry in categories[cat]:
                lines.append(f"- {entry}")
            lines.append("")

    return "\n".join(lines)


def get_git_commits(repo_path, since_tag):
    """Get commits from git repo since a tag."""
    try:
        if since_tag:
            cmd = ["git", "-C", repo_path, "log", f"{since_tag}..HEAD", "--oneline", "--no-merges"]
        else:
            cmd = ["git", "-C", repo_path, "log", "--oneline", "--no-merges", "-50"]

        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            return result.stdout.strip().split("\n")
        return []
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return []


def main():
    parser = argparse.ArgumentParser(
        description="Generate changelog entries from conventional commits",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate from demo commits
  %(prog)s --demo

  # Generate from a git repo
  %(prog)s --repo /path/to/repo --since v1.0.0

  # Specify current version for bump calculation
  %(prog)s --demo --current-version 2.0.3

  # JSON output
  %(prog)s --demo --json
        """,
    )
    parser.add_argument("--demo", action="store_true", help="Use sample commit messages")
    parser.add_argument("--repo", type=str, help="Path to git repository")
    parser.add_argument("--since", type=str, help="Git tag to start from")
    parser.add_argument("--current-version", type=str, default="2.0.3", help="Current version (default: 2.0.3)")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    if args.demo:
        raw_commits = SAMPLE_COMMITS
    elif args.repo:
        raw_commits = get_git_commits(args.repo, args.since)
        if not raw_commits or raw_commits == [""]:
            print("No commits found.", file=sys.stderr)
            sys.exit(1)
    else:
        print("Use --demo or --repo to provide commits.")
        sys.exit(1)

    # Parse all commits
    parsed = [parse_commit(line) for line in raw_commits if line.strip()]
    valid_commits = [c for c in parsed if c]
    changelog_commits = [c for c in valid_commits if c["include_in_changelog"]]

    # Determine version bump
    bump_type = determine_version_bump(valid_commits)
    new_version = bump_version(args.current_version, bump_type)

    # Generate changelog
    changelog_md = generate_changelog(valid_commits, new_version)

    # Stats
    stats = {
        "total_commits": len(raw_commits),
        "parsed": len(valid_commits),
        "unparseable": len(raw_commits) - len(valid_commits),
        "included_in_changelog": len(changelog_commits),
        "excluded": len(valid_commits) - len(changelog_commits),
        "breaking_changes": sum(1 for c in valid_commits if c["is_breaking"]),
    }

    if args.json:
        result = {
            "current_version": args.current_version,
            "bump_type": bump_type,
            "new_version": new_version,
            "stats": stats,
            "commits": valid_commits,
            "changelog_markdown": changelog_md,
        }
        print(json.dumps(result, indent=2))
    else:
        print("=" * 60)
        print("CHANGELOG GENERATION REPORT")
        print("=" * 60)
        print()
        print(f"Current version: {args.current_version}")
        print(f"Recommended bump: {bump_type}")
        print(f"New version: {new_version}")
        print()
        print(f"Commits analyzed: {stats['total_commits']}")
        print(f"  Parsed:    {stats['parsed']}")
        print(f"  Included:  {stats['included_in_changelog']}")
        print(f"  Excluded:  {stats['excluded']} (docs, tests, chores)")
        print(f"  Breaking:  {stats['breaking_changes']}")
        print()
        print("-" * 60)
        print("GENERATED CHANGELOG")
        print("-" * 60)
        print()
        print(changelog_md)


if __name__ == "__main__":
    main()
