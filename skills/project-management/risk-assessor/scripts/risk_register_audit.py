#!/usr/bin/env python3
"""Risk register auditor.

Audits a risk register for completeness, staleness, and quality.
Checks for missing owners, stale risks, scoring consistency, and
provides an overall register health score.

Usage:
    python risk_register_audit.py --demo
    python risk_register_audit.py --file risk-register.md
    python risk_register_audit.py --demo --json
"""

import argparse
import json
import sys
from datetime import date, timedelta


SAMPLE_REGISTER = [
    {
        "id": "R-001",
        "description": "Key backend developer may leave before project completion",
        "category": "Resource",
        "probability": 3,
        "impact": 4,
        "score": 12,
        "strategy": "Mitigate",
        "owner": "PM",
        "target_date": (date.today() + timedelta(days=25)).isoformat(),
        "status": "In Progress",
        "last_reviewed": (date.today() - timedelta(days=3)).isoformat(),
    },
    {
        "id": "R-002",
        "description": "Payment gateway API may not support required features",
        "category": "Technical",
        "probability": 2,
        "impact": 5,
        "score": 10,
        "strategy": "Avoid",
        "owner": "Tech Lead",
        "target_date": (date.today() + timedelta(days=10)).isoformat(),
        "status": "Open",
        "last_reviewed": (date.today() - timedelta(days=3)).isoformat(),
    },
    {
        "id": "R-003",
        "description": "Client may request major scope changes after UAT",
        "category": "Scope",
        "probability": 4,
        "impact": 3,
        "score": 12,
        "strategy": "Mitigate",
        "owner": "",
        "target_date": "",
        "status": "Monitoring",
        "last_reviewed": (date.today() - timedelta(days=14)).isoformat(),
    },
    {
        "id": "R-004",
        "description": "Database performance under load",
        "category": "Technical",
        "probability": 3,
        "impact": 3,
        "score": 9,
        "strategy": "Mitigate",
        "owner": "Dev Lead",
        "target_date": (date.today() + timedelta(days=30)).isoformat(),
        "status": "Open",
        "last_reviewed": (date.today() - timedelta(days=5)).isoformat(),
    },
    {
        "id": "R-005",
        "description": "",
        "category": "External",
        "probability": 2,
        "impact": 4,
        "score": 8,
        "strategy": "",
        "owner": "",
        "target_date": "",
        "status": "Open",
        "last_reviewed": (date.today() - timedelta(days=21)).isoformat(),
    },
]


def audit_risk(risk):
    """Audit a single risk entry for quality issues."""
    issues = []
    warnings = []

    # Check required fields
    if not risk.get("description"):
        issues.append("Missing risk description")
    if not risk.get("owner"):
        issues.append("No owner assigned")
    if not risk.get("strategy"):
        issues.append("No mitigation strategy defined")
    if not risk.get("target_date"):
        warnings.append("No target date set")

    # Validate scoring
    prob = risk.get("probability", 0)
    impact = risk.get("impact", 0)
    score = risk.get("score", 0)
    if prob and impact and score != prob * impact:
        issues.append(f"Score mismatch: {prob}x{impact}={prob*impact}, but recorded as {score}")

    # Check staleness
    last_reviewed = risk.get("last_reviewed")
    if last_reviewed:
        days_since_review = (date.today() - date.fromisoformat(last_reviewed)).days
        if days_since_review > 14:
            issues.append(f"Stale: not reviewed in {days_since_review} days")
        elif days_since_review > 7:
            warnings.append(f"Review due: last reviewed {days_since_review} days ago")

    # Check overdue target dates
    target = risk.get("target_date")
    if target and risk.get("status") not in ("Resolved", "Closed"):
        try:
            if date.fromisoformat(target) < date.today():
                issues.append(f"Overdue: target date {target} has passed")
        except ValueError:
            warnings.append("Invalid target date format")

    # High/critical without strategy is a problem
    if score >= 10 and not risk.get("strategy"):
        issues.append("HIGH/CRITICAL risk without mitigation strategy")

    return {
        "risk_id": risk.get("id", "Unknown"),
        "issues": issues,
        "warnings": warnings,
        "issue_count": len(issues),
        "warning_count": len(warnings),
        "grade": "FAIL" if issues else ("WARN" if warnings else "PASS"),
    }


def audit_register(risks):
    """Audit the entire risk register."""
    audits = [audit_risk(r) for r in risks]

    total_issues = sum(a["issue_count"] for a in audits)
    total_warnings = sum(a["warning_count"] for a in audits)
    pass_count = sum(1 for a in audits if a["grade"] == "PASS")
    fail_count = sum(1 for a in audits if a["grade"] == "FAIL")
    warn_count = sum(1 for a in audits if a["grade"] == "WARN")

    # Health score: start at 100, deduct for issues
    max_score = 100
    deduction_per_issue = 10
    deduction_per_warning = 3
    health_score = max(0, max_score - (total_issues * deduction_per_issue) - (total_warnings * deduction_per_warning))

    if health_score >= 80:
        health_rating = "HEALTHY"
    elif health_score >= 60:
        health_rating = "NEEDS ATTENTION"
    elif health_score >= 40:
        health_rating = "AT RISK"
    else:
        health_rating = "CRITICAL"

    # Category coverage check
    expected_categories = {"Technical", "Resource", "Schedule", "Scope", "External", "Quality"}
    covered_categories = {r.get("category") for r in risks if r.get("category")}
    missing_categories = expected_categories - covered_categories

    return {
        "audit_date": date.today().isoformat(),
        "total_risks": len(risks),
        "risk_audits": audits,
        "summary": {
            "pass": pass_count,
            "warn": warn_count,
            "fail": fail_count,
            "total_issues": total_issues,
            "total_warnings": total_warnings,
        },
        "health_score": health_score,
        "health_rating": health_rating,
        "category_coverage": {
            "covered": sorted(covered_categories),
            "missing": sorted(missing_categories),
        },
    }


def main():
    parser = argparse.ArgumentParser(
        description="Audit risk register for completeness and quality",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Audit sample register
  %(prog)s --demo

  # JSON output
  %(prog)s --demo --json
        """,
    )
    parser.add_argument("--demo", action="store_true", help="Audit sample risk register")
    parser.add_argument("--file", type=str, help="Risk register JSON file to audit")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    if args.demo:
        risks = SAMPLE_REGISTER
    elif args.file:
        try:
            with open(args.file) as f:
                risks = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error reading file: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print("Use --demo for sample data or --file to audit a register.")
        sys.exit(1)

    result = audit_register(risks)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print("=" * 60)
        print(f"RISK REGISTER AUDIT - {result['audit_date']}")
        print("=" * 60)
        print()
        print(f"Health Score: {result['health_score']}/100 ({result['health_rating']})")
        s = result["summary"]
        print(f"Risks Audited: {result['total_risks']} | "
              f"Pass: {s['pass']} | Warn: {s['warn']} | Fail: {s['fail']}")
        print()

        print("INDIVIDUAL RISK AUDITS")
        print("-" * 60)
        for a in result["risk_audits"]:
            status_icon = {"PASS": "[OK]", "WARN": "[!!]", "FAIL": "[XX]"}[a["grade"]]
            print(f"  {status_icon} {a['risk_id']}")
            for issue in a["issues"]:
                print(f"       ERROR: {issue}")
            for warning in a["warnings"]:
                print(f"       WARN:  {warning}")
        print()

        cov = result["category_coverage"]
        print("CATEGORY COVERAGE")
        print("-" * 60)
        print(f"  Covered:  {', '.join(cov['covered']) or 'None'}")
        print(f"  Missing:  {', '.join(cov['missing']) or 'None (full coverage)'}")
        print()


if __name__ == "__main__":
    main()
