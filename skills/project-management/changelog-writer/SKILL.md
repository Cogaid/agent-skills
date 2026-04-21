---
name: changelog-writer
description: Generate changelogs from commits and tickets with proper formatting and audience-appropriate language. Use when user mentions "changelog," "release notes," "what changed," "version history," "semantic versioning," "keep a changelog," "release summary."
metadata:
  version: 1.0.0
  category: project-management
---

# Changelog Writer

Generate structured changelogs and release notes from commits, tickets, and pull requests with audience-appropriate language.

## Purpose

A good changelog tells users and developers what changed, why it matters, and whether they need to take action. This skill provides frameworks for writing changelogs that follow the Keep a Changelog standard, guidance on semantic versioning, patterns for parsing commit messages into changelog entries, and templates for both technical and user-facing release notes.

## Quick Reference

### Keep a Changelog Categories

| Category | Description | When to Use | Example |
|----------|-------------|-------------|---------|
| **Added** | New features or capabilities | New functionality that did not exist before | "Added dark mode support" |
| **Changed** | Modifications to existing features | Behavior or appearance updated | "Changed dashboard layout to two-column grid" |
| **Deprecated** | Features marked for future removal | Feature still works but will be removed | "Deprecated XML export in favor of JSON" |
| **Removed** | Features that have been deleted | Feature no longer available | "Removed legacy v1 API endpoints" |
| **Fixed** | Bug fixes | Something broken now works correctly | "Fixed crash when uploading files over 10MB" |
| **Security** | Vulnerability patches | Security-related changes | "Fixed XSS vulnerability in comment rendering" |

### Semantic Versioning Guide

```
MAJOR.MINOR.PATCH

Examples: 1.0.0 → 1.0.1 → 1.1.0 → 2.0.0
```

| Component | When to Increment | User Impact | Example Change |
|-----------|------------------|-------------|----------------|
| **MAJOR** (X.0.0) | Breaking changes, incompatible API changes | Must update code/config | Remove API endpoint, change response format |
| **MINOR** (0.X.0) | New features, backward-compatible additions | Can adopt new features | Add new API endpoint, new UI feature |
| **PATCH** (0.0.X) | Bug fixes, backward-compatible fixes | Recommended update | Fix crash, correct calculation, security patch |

**Pre-release versions:**
- `1.0.0-alpha.1` - Early testing, unstable
- `1.0.0-beta.1` - Feature complete, testing
- `1.0.0-rc.1` - Release candidate, final testing

### Version Decision Tree

```
Did you make a change?
  │
  ├── Does it break existing API/behavior?
  │     YES → MAJOR version bump
  │
  ├── Does it add new functionality?
  │     YES → Is it backward compatible?
  │             YES → MINOR version bump
  │             NO  → MAJOR version bump
  │
  └── Is it a bug fix or patch?
        YES → PATCH version bump
```

## Workflow

### Changelog Generation Process

1. **Collect raw inputs**
   - Git commits since last release
   - Merged pull requests
   - Resolved tickets/issues
   - Any manual notes from the team

2. **Categorize changes**
   - Map each change to a Keep a Changelog category
   - Determine version bump using semantic versioning rules
   - Flag breaking changes for special attention

3. **Write human-readable entries**
   - Transform commit messages into clear descriptions
   - Add context that helps users understand the impact
   - Group related changes together

4. **Create audience-appropriate versions**
   - Technical changelog for developers
   - User-facing release notes for end users
   - Internal notes for support/ops teams

5. **Review and publish**
   - Verify all significant changes are captured
   - Confirm version number is correct
   - Update CHANGELOG.md and publish release notes

### Commit Message Parsing Patterns

Map conventional commit prefixes to changelog categories:

| Commit Prefix | Changelog Category | Example Commit | Changelog Entry |
|--------------|-------------------|----------------|-----------------|
| `feat:` | Added | `feat: add PDF export for reports` | Added PDF export for reports |
| `fix:` | Fixed | `fix: resolve timeout on large uploads` | Fixed timeout when uploading files larger than 50MB |
| `refactor:` | Changed | `refactor: simplify auth middleware` | Changed authentication flow for improved reliability |
| `perf:` | Changed | `perf: optimize search query by 40%` | Changed search to return results up to 40% faster |
| `docs:` | (usually omit) | `docs: update API reference` | (Skip or include in internal notes) |
| `style:` | (usually omit) | `style: fix linting errors` | (Skip) |
| `test:` | (usually omit) | `test: add unit tests for billing` | (Skip) |
| `build:` | (usually omit) | `build: upgrade webpack to v5` | (Skip or note in internal changelog) |
| `ci:` | (usually omit) | `ci: add deploy pipeline` | (Skip) |
| `chore:` | (usually omit) | `chore: update dependencies` | (Skip unless notable) |
| `deprecate:` | Deprecated | `deprecate: XML export endpoint` | Deprecated XML export (use JSON export instead) |
| `remove:` | Removed | `remove: legacy dashboard` | Removed legacy dashboard (replaced by new analytics view) |
| `security:` | Security | `security: patch SQL injection in search` | Fixed SQL injection vulnerability in search endpoint |
| `BREAKING CHANGE:` | (flag in Added/Changed/Removed) | `feat!: change auth to OAuth 2.0` | **BREAKING:** Changed authentication to OAuth 2.0 (see migration guide) |

### Audience-Appropriate Language

| Audience | Tone | Detail Level | Focus On | Avoid |
|----------|------|-------------|----------|-------|
| **Developers / API consumers** | Technical, precise | High | API changes, breaking changes, migration steps | Marketing language |
| **End users** | Friendly, benefit-focused | Medium | What they can do now, what changed in their workflow | Internal implementation details |
| **Internal / Ops** | Factual, operational | Full | Infrastructure changes, config changes, rollback notes | User-facing features |
| **Executives** | High-level, outcome-focused | Low | Business impact, key metrics | Technical specifics |

## Templates

### CHANGELOG.md Template

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- New feature currently in development

## [2.1.0] - 2026-04-20

### Added
- PDF export for all report types (#234)
- Dark mode support with system preference detection (#256)
- Bulk user import via CSV upload (#267)

### Changed
- Dashboard now loads 40% faster due to query optimization (#271)
- Updated password requirements to minimum 12 characters (#280)

### Deprecated
- XML export format will be removed in v3.0.0; use JSON export instead (#289)

### Fixed
- Fixed crash when uploading files larger than 50MB (#245)
- Fixed incorrect timezone display for users in UTC-offset zones (#251)
- Fixed search not returning results with special characters (#263)

### Security
- Patched XSS vulnerability in user comment rendering (#278)
- Updated dependencies to address CVE-2026-12345 (#282)

## [2.0.0] - 2026-03-15

### Added
- New REST API v2 with consistent response format
- Webhook support for real-time event notifications
- Role-based access control (Admin, Editor, Viewer)

### Changed
- **BREAKING:** API response envelope changed from `{data: ...}` to `{result: ..., meta: ...}`
- **BREAKING:** Authentication switched from API keys to OAuth 2.0
- Minimum supported Node.js version is now 18 (was 16)

### Removed
- **BREAKING:** Removed REST API v1 endpoints (deprecated since v1.8.0)
- Removed support for Node.js 16

### Migration Guide
See [MIGRATION.md](./MIGRATION.md) for detailed upgrade instructions.

## [1.9.0] - 2026-02-01

### Added
- Search filters for date range and status

### Fixed
- Fixed memory leak in background job processor

---

[Unreleased]: https://github.com/org/repo/compare/v2.1.0...HEAD
[2.1.0]: https://github.com/org/repo/compare/v2.0.0...v2.1.0
[2.0.0]: https://github.com/org/repo/compare/v1.9.0...v2.0.0
[1.9.0]: https://github.com/org/repo/releases/tag/v1.9.0
```

### User-Facing Release Notes Template

```markdown
# What's New in [Product Name] [Version]

**Released:** [Date]

---

## Highlights

### [Feature Name] - [One-line benefit]
[2-3 sentences explaining what users can now do and why it matters.
Focus on the benefit, not the implementation.]

![Screenshot or GIF if applicable]

### [Feature Name] - [One-line benefit]
[2-3 sentences explaining the improvement.]

---

## Improvements
- **Faster dashboard:** The main dashboard now loads up to 40% faster
- **Better passwords:** Updated password requirements to keep your account more secure
- **Special character search:** Search now correctly handles queries with special characters

## Bug Fixes
- Fixed an issue where large file uploads could fail silently
- Fixed timezone display for some international users
- Corrected calculation in the monthly summary report

## Security Updates
- Addressed a security issue in comment rendering (no user action required)
- Updated third-party libraries to latest secure versions

## Coming Soon
- [Teaser for upcoming feature]
- [Another teaser]

## Deprecation Notice
- **XML export** will be removed in the next major release. Please switch to JSON export.
  [Learn how to migrate →](link)

---

Questions? Contact [support link] or visit our [help center](link).
```

### Internal Release Notes Template

```markdown
## Internal Release Notes - v[Version]

**Release Date:** [Date]
**Release Manager:** [Name]
**Deploy Window:** [Time and timezone]

### Changes Requiring Ops Attention

| Change | Action Required | Rollback Plan |
|--------|----------------|---------------|
| Database migration adds `users.mfa_enabled` column | Run migration before deploy | Reverse migration script in `db/rollback/` |
| New environment variable `PDF_SERVICE_URL` | Add to production config | Feature degrades gracefully if missing |
| Redis cache schema changed | Clear cache after deploy | No rollback needed |

### Feature Flags
- `dark_mode` - OFF by default, enable per-tenant
- `bulk_import` - ON for enterprise tier only

### Monitoring Checklist
- [ ] Watch error rate for 30 min post-deploy
- [ ] Verify PDF export works in production
- [ ] Check background job queue depth
- [ ] Confirm new environment variables loaded

### Known Issues
- Dark mode has minor contrast issue on settings page (non-blocking, fix in v2.1.1)

### Support FAQ
- Q: "How do I enable dark mode?" → Settings > Appearance > Theme
- Q: "Can I still use XML export?" → Yes, but it will be removed in v3.0
```

## Scripts & Tools

### Changelog Generator from Git Commits

```bash
#!/bin/bash
# scripts/generate-changelog.sh
# Generate changelog entries from conventional commits since last tag
# Usage: ./scripts/generate-changelog.sh [since-tag]

SINCE="${1:-$(git describe --tags --abbrev=0 2>/dev/null || echo '')}"
DATE=$(date +%Y-%m-%d)

if [ -z "$SINCE" ]; then
  COMMITS=$(git log --oneline --no-merges)
else
  COMMITS=$(git log "$SINCE"..HEAD --oneline --no-merges)
fi

echo "## [Unreleased] - $DATE"
echo ""

echo "### Added"
echo "$COMMITS" | grep -i "^[a-f0-9]* feat" | sed 's/^[a-f0-9]* feat[:(]*/- /' | sed 's/)[: ]*/: /'
echo ""

echo "### Fixed"
echo "$COMMITS" | grep -i "^[a-f0-9]* fix" | sed 's/^[a-f0-9]* fix[:(]*/- /' | sed 's/)[: ]*/: /'
echo ""

echo "### Changed"
echo "$COMMITS" | grep -iE "^[a-f0-9]* (refactor|perf)" | sed 's/^[a-f0-9]* [a-z]*[:(]*/- /' | sed 's/)[: ]*/: /'
echo ""

echo "### Security"
echo "$COMMITS" | grep -i "^[a-f0-9]* security" | sed 's/^[a-f0-9]* security[:(]*/- /' | sed 's/)[: ]*/: /'
```

### Version Bump Helper

```python
# scripts/version_bump.py
# Determine the correct version bump based on commit messages
# Usage: python scripts/version_bump.py

import subprocess
import re

def get_commits_since_tag() -> list[str]:
    """Get commit messages since the last tag."""
    try:
        last_tag = subprocess.check_output(
            ["git", "describe", "--tags", "--abbrev=0"],
            stderr=subprocess.DEVNULL
        ).decode().strip()
        result = subprocess.check_output(
            ["git", "log", f"{last_tag}..HEAD", "--oneline"]
        ).decode().strip()
    except subprocess.CalledProcessError:
        result = subprocess.check_output(
            ["git", "log", "--oneline"]
        ).decode().strip()
    return result.split("\n") if result else []

def determine_bump(commits: list[str]) -> str:
    """Determine version bump type from commit messages."""
    has_breaking = any("BREAKING" in c or "!" in c.split(":")[0] for c in commits if ":" in c)
    has_feat = any(c.split(" ", 1)[1].startswith("feat") for c in commits if " " in c)
    has_fix = any(c.split(" ", 1)[1].startswith("fix") for c in commits if " " in c)

    if has_breaking:
        return "MAJOR"
    elif has_feat:
        return "MINOR"
    elif has_fix:
        return "PATCH"
    return "PATCH"

def bump_version(current: str, bump_type: str) -> str:
    """Apply version bump."""
    parts = current.lstrip("v").split(".")
    major, minor, patch = int(parts[0]), int(parts[1]), int(parts[2])

    if bump_type == "MAJOR":
        return f"{major + 1}.0.0"
    elif bump_type == "MINOR":
        return f"{major}.{minor + 1}.0"
    else:
        return f"{major}.{minor}.{patch + 1}"

if __name__ == "__main__":
    commits = get_commits_since_tag()
    bump = determine_bump(commits)
    print(f"Commits analyzed: {len(commits)}")
    print(f"Recommended bump: {bump}")
    print(f"Relevant commits:")
    for c in commits[:10]:
        print(f"  {c}")
```

## Best Practices

### Writing Good Changelog Entries

| Principle | Bad Example | Good Example |
|-----------|-------------|-------------|
| Lead with the user impact | "Refactored query builder" | "Search results now load 40% faster" |
| Be specific | "Fixed a bug" | "Fixed crash when uploading files over 50MB" |
| Include ticket/PR references | "Fixed login issue" | "Fixed login timeout on slow connections (#245)" |
| Flag breaking changes clearly | "Changed API response format" | "**BREAKING:** API response format changed (see migration guide)" |
| Use active voice | "A feature was added for export" | "Added CSV export for analytics data" |
| Skip internal-only changes | "Updated ESLint config" | (Omit from user-facing changelog) |
| Group related changes | 5 separate "fixed search" entries | "Improved search reliability (fixed 5 edge cases)" |

### Changelog Maintenance Rules

- **One entry per user-visible change** - do not list every commit
- **Write entries as you merge** - do not try to reconstruct from git history at release time
- **Keep an [Unreleased] section** - accumulate changes between releases
- **Link to comparison views** - at the bottom of CHANGELOG.md, link to GitHub compare URLs
- **Never delete history** - old versions stay in the changelog forever
- **Date every release** - use ISO 8601 format (YYYY-MM-DD)
- **Sort categories consistently** - Added, Changed, Deprecated, Removed, Fixed, Security

### Common Mistakes

| Mistake | Impact | Prevention |
|---------|--------|------------|
| Dumping raw git log | Unreadable, no context | Curate and rewrite entries for humans |
| Forgetting breaking changes | Users' code breaks without warning | Scan for `!` and `BREAKING` in commits |
| No version in changelog | Users cannot correlate releases | Always include version number and date |
| Mixing audiences | Developers confused by marketing speak; users confused by technical details | Create separate technical and user-facing versions |
| Skipping deprecation notices | Users surprised when features disappear | Deprecate at least one major version before removal |
| Changelog only at release | Scramble to remember changes | Maintain [Unreleased] section continuously |
