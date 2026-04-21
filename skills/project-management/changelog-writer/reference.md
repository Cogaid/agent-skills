# Changelog Writer Reference

Comprehensive reference for writing changelogs, semantic versioning, conventional commits, and audience-appropriate release notes.

## Keep a Changelog Standard

### Principles

The [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) standard defines how to maintain a human-readable changelog:

1. **Changelogs are for humans**, not machines -- write for readers, not parsers
2. **Every version gets an entry** -- even if it is a one-line patch
3. **Group by type** -- use the standard categories (Added, Changed, etc.)
4. **Most recent version first** -- reverse chronological order
5. **Include dates** -- ISO 8601 format (YYYY-MM-DD)
6. **Link to diffs** -- at the bottom, link to compare views between versions
7. **Keep an [Unreleased] section** -- accumulate changes between releases

### Category Order

Always list categories in this order (skip empty categories):

1. Added
2. Changed
3. Deprecated
4. Removed
5. Fixed
6. Security

### Writing Style

| Principle | Bad | Good |
|-----------|-----|------|
| Active voice | "A feature was added" | "Added CSV export for reports" |
| User-facing impact | "Refactored query builder" | "Search results now load 40% faster" |
| Specific | "Fixed a bug" | "Fixed crash when uploading files over 50MB" |
| Consistent tense | Mix of past/present | Past tense throughout ("Added", "Fixed") |
| Include references | No issue links | "Fixed login timeout (#245)" |
| No jargon (user-facing) | "Patched XSS in sanitizer" | "Fixed a security issue in comment display" |

## Semantic Versioning Deep Dive

### Version Number Format

```
MAJOR.MINOR.PATCH[-PRERELEASE][+BUILD]

Examples:
  1.0.0           - First stable release
  1.2.3           - Patch 3 of minor version 2
  2.0.0-alpha.1   - First alpha of next major
  2.0.0-beta.3    - Third beta of next major
  2.0.0-rc.1      - Release candidate
  1.2.3+build.456 - Build metadata (informational only)
```

### Version Lifecycle

```
0.1.0 (initial development)
  -> 0.2.0 (add features, API may change freely)
  -> 0.9.0 (approaching stability)
  -> 1.0.0 (first stable release - public API defined)
  -> 1.0.1 (patch: bug fix)
  -> 1.1.0 (minor: new backward-compatible feature)
  -> 1.2.0 (minor: another feature)
  -> 2.0.0-alpha.1 (next major, early testing)
  -> 2.0.0-beta.1 (feature complete, testing)
  -> 2.0.0-rc.1 (release candidate)
  -> 2.0.0 (breaking changes released)
```

### What Counts as a Breaking Change

| Change Type | Breaking? | Version Bump |
|------------|-----------|-------------|
| Remove a public API endpoint | Yes | MAJOR |
| Change response format/schema | Yes | MAJOR |
| Rename a required parameter | Yes | MAJOR |
| Change authentication method | Yes | MAJOR |
| Add a new optional parameter | No | MINOR |
| Add a new endpoint | No | MINOR |
| Add a new response field | No | MINOR |
| Fix incorrect behavior (matches docs) | No | PATCH |
| Fix behavior (contradicts docs) | Maybe | PATCH or MAJOR |
| Increase minimum language/runtime version | Yes | MAJOR |
| Deprecate (but keep working) | No | MINOR |

### Pre-Release Versions

| Stage | Format | Meaning | Who Uses |
|-------|--------|---------|----------|
| Alpha | `X.Y.Z-alpha.N` | Early, unstable, features incomplete | Internal team only |
| Beta | `X.Y.Z-beta.N` | Feature complete, bugs expected | Beta testers, early adopters |
| RC | `X.Y.Z-rc.N` | Release candidate, final testing | Broader testing, staging environments |
| Release | `X.Y.Z` | Stable, production-ready | All users |

## Conventional Commits

### Format

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Commit Types and Changelog Mapping

| Type | Purpose | Changelog Category | Include in Changelog? |
|------|---------|-------------------|---------------------|
| `feat` | New feature | Added | Yes |
| `fix` | Bug fix | Fixed | Yes |
| `perf` | Performance improvement | Changed | Yes |
| `refactor` | Code restructuring | Changed (if user-visible) | Sometimes |
| `docs` | Documentation only | - | Rarely |
| `style` | Code formatting | - | No |
| `test` | Tests only | - | No |
| `build` | Build system | - | No |
| `ci` | CI/CD changes | - | No |
| `chore` | Maintenance | - | No |
| `revert` | Revert a commit | Fixed or Removed | Yes |
| `deprecate` | Mark as deprecated | Deprecated | Yes |
| `security` | Security fix | Security | Yes |

### Breaking Changes

Two ways to indicate breaking changes:

1. `!` after type/scope: `feat!: change auth to OAuth 2.0`
2. `BREAKING CHANGE:` footer: 
```
feat: change authentication method

BREAKING CHANGE: API now requires OAuth 2.0 tokens instead of API keys.
See migration guide at docs/migration/auth.md
```

## Audience-Specific Changelog Formats

### Developer / API Consumer

Focus on: what changed in the interface, breaking changes, migration steps.

```markdown
## [2.0.0] - 2026-04-20

### BREAKING CHANGES

- `POST /api/auth` now requires OAuth 2.0 bearer token (was API key header)
- Response envelope changed from `{data: ...}` to `{result: ..., meta: {...}}`
- Removed deprecated `GET /api/v1/*` endpoints

### Migration Guide

1. Generate OAuth credentials at Settings > API > OAuth
2. Replace `X-API-Key` header with `Authorization: Bearer <token>`
3. Update response parsing: access data via `response.result` instead of `response.data`
```

### End User

Focus on: what they can do now, what changed in their experience.

```markdown
## What's New (April 2026)

### Export Your Reports as PDF
You can now download any report as a PDF file. Look for the download
button in the top-right corner of any report page.

### Faster Dashboard
Your dashboard now loads up to 40% faster, especially on mobile devices.

### Bug Fixes
- Fixed an issue where large file uploads could fail
- Fixed timezone display for international users
```

### Internal / Ops Team

Focus on: what to deploy, configure, monitor, and roll back.

```markdown
## v2.1.0 Deploy Notes

### Pre-Deploy
- Run migration: `rails db:migrate` (adds `users.mfa_enabled` column)
- Set env var: `PDF_SERVICE_URL=https://pdf.internal.example.com`

### Post-Deploy
- Clear Redis cache: `redis-cli FLUSHDB`
- Verify PDF export at /reports/test
- Monitor error rate for 30 minutes

### Rollback
- Reverse migration: `rails db:rollback STEP=1`
- Remove env var: `PDF_SERVICE_URL`
- Previous version: v2.0.3
```

## Changelog Automation

### Git-Based Workflow

```
1. Developer creates commit with conventional format
     git commit -m "feat(search): add date range filter (#289)"

2. CI validates commit message format (commitlint)

3. At release time, tool generates changelog:
     - Collects commits since last tag
     - Groups by type -> category
     - Generates markdown entries
     - Determines version bump from types

4. Human reviews and polishes entries:
     - Rewrites technical messages into user-friendly language
     - Groups related commits into single entries
     - Adds context for breaking changes
     - Removes internal-only changes

5. Publish:
     - Update CHANGELOG.md
     - Tag the release
     - Create GitHub release with notes
```

### Tools for Automation

| Tool | Language | Features |
|------|----------|----------|
| conventional-changelog | Node.js | Parse commits, generate changelog |
| release-please | Node.js | GitHub Action, auto-PR with changelog |
| git-cliff | Rust | Fast, customizable templates |
| python-semantic-release | Python | Version bump + changelog + publish |
| changeset | Node.js | Monorepo support, manual entries |

## References

- Keep a Changelog: https://keepachangelog.com/en/1.1.0/
- Semantic Versioning: https://semver.org/spec/v2.0.0.html
- Conventional Commits: https://www.conventionalcommits.org/en/v1.0.0/
- commitlint: https://commitlint.js.org/
- release-please: https://github.com/googleapis/release-please
