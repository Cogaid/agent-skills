#!/usr/bin/env python3
"""Run quality audit on all templates in the response library.

Usage:
    python scripts/audit_library.py --check-links --check-variables --report
    python scripts/audit_library.py --category troubleshooting --verbose
    python scripts/audit_library.py --report --format summary
"""

import argparse
import json
import random
import re
import sys
from datetime import datetime, timedelta

random.seed(42)

# Simulated template library with audit-relevant metadata
TEMPLATES = [
    {
        "id": "GREET-001",
        "name": "Standard Welcome",
        "category": "greeting",
        "last_updated": "2024-01-15",
        "usage_count_30d": 412,
        "avg_csat": 4.3,
        "body": "Hi {{customer_name}}, Thank you for reaching out to {{company_name}} support! My name is {{agent_name}}...",
        "variables": ["customer_name", "company_name", "agent_name", "issue_summary"],
        "links": [],
        "owner": "Support Team",
    },
    {
        "id": "GREET-002",
        "name": "Returning Customer Welcome",
        "category": "greeting",
        "last_updated": "2024-01-15",
        "usage_count_30d": 234,
        "avg_csat": 4.5,
        "body": "Hi {{customer_name}}, Welcome back! I can see you've been with us since {{join_date}}...",
        "variables": ["customer_name", "company_name", "join_date", "issue_summary"],
        "links": [],
        "owner": "Support Team",
    },
    {
        "id": "TRBL-001",
        "name": "Step-by-Step Instructions",
        "category": "troubleshooting",
        "last_updated": "2023-11-20",
        "usage_count_30d": 567,
        "avg_csat": 4.1,
        "body": "Hi {{customer_name}}, I'd like to walk you through a few steps...",
        "variables": ["customer_name", "step_1_action", "step_1_detail", "step_2_action", "step_2_detail", "step_3_action", "step_3_detail"],
        "links": [],
        "owner": "Technical Team",
    },
    {
        "id": "TRBL-002",
        "name": "Request Diagnostic Information",
        "category": "troubleshooting",
        "last_updated": "2023-09-01",
        "usage_count_30d": 445,
        "avg_csat": 3.9,
        "body": "Hi {{customer_name}}, To help me diagnose this issue... Browser/App version...",
        "variables": ["customer_name"],
        "links": [],
        "owner": "Technical Team",
    },
    {
        "id": "TRBL-003",
        "name": "Known Issue Acknowledgment",
        "category": "troubleshooting",
        "last_updated": "2024-02-01",
        "usage_count_30d": 89,
        "avg_csat": 3.8,
        "body": "Hi {{customer_name}}, This is a known issue... visit https://status.example.com for updates...",
        "variables": ["customer_name", "issue_description", "impact_description", "workaround_steps", "eta_description"],
        "links": ["https://status.example.com"],
        "owner": "Technical Team",
    },
    {
        "id": "RSLV-001",
        "name": "Issue Resolved",
        "category": "resolution",
        "last_updated": "2024-01-10",
        "usage_count_30d": 723,
        "avg_csat": 4.6,
        "body": "Hi {{customer_name}}, Great news - the issue with {{issue_summary}} has been resolved!...",
        "variables": ["customer_name", "issue_summary", "action_taken", "expected_outcome"],
        "links": [],
        "owner": "Support Team",
    },
    {
        "id": "RSLV-002",
        "name": "Issue Resolved with Compensation",
        "category": "resolution",
        "last_updated": "2023-08-15",
        "usage_count_30d": 3,
        "avg_csat": 4.4,
        "body": "Hi {{customer_name}}, I'm pleased to let you know... compensation... see https://billing.oldurl.com/credits...",
        "variables": ["customer_name", "issue_summary", "impact_description", "compensation_details", "compensation_specifics"],
        "links": ["https://billing.oldurl.com/credits"],
        "owner": "Billing Team",
    },
    {
        "id": "APOL-001",
        "name": "Service Disruption Apology",
        "category": "apology",
        "last_updated": "2024-02-10",
        "usage_count_30d": 45,
        "avg_csat": 3.7,
        "body": "Hi {{customer_name}}, I sincerely apologize for the disruption...",
        "variables": ["customer_name", "service_name", "impact_on_customer", "root_cause", "corrective_action", "compensation_if_applicable"],
        "links": [],
        "owner": "Support Team",
    },
    {
        "id": "APOL-002",
        "name": "Billing Error Apology",
        "category": "apology",
        "last_updated": "2023-06-20",
        "usage_count_30d": 12,
        "avg_csat": 4.0,
        "body": "Hi {{customer_name}}, I owe you an apology... billing error...",
        "variables": ["customer_name", "billing_error_description", "correction_action", "refund_details", "refund_timeline"],
        "links": [],
        "owner": "Billing Team",
    },
    {
        "id": "CLOS-001",
        "name": "Standard Close",
        "category": "closing",
        "last_updated": "2024-01-05",
        "usage_count_30d": 1102,
        "avg_csat": 4.3,
        "body": "Is there anything else I can help you with today?...",
        "variables": ["day_period", "company_name"],
        "links": [],
        "owner": "Support Team",
    },
    {
        "id": "CLOS-002",
        "name": "Close with Survey",
        "category": "closing",
        "last_updated": "2023-12-01",
        "usage_count_30d": 654,
        "avg_csat": 4.2,
        "body": "I'm glad I could help! ...survey... {{survey_url}}...",
        "variables": ["customer_name", "day_period", "survey_url"],
        "links": ["{{survey_url}}"],
        "owner": "Support Team",
    },
]

# Known problematic links for simulation
BROKEN_LINKS = ["https://billing.oldurl.com/credits"]
KNOWN_VARIABLES = [
    "customer_name", "agent_name", "company_name", "issue_summary", "ticket_id",
    "day_period", "join_date", "survey_url", "resolution_date",
]


def check_staleness(template, stale_days=90):
    """Check if template hasn't been updated recently."""
    last_updated = datetime.strptime(template["last_updated"], "%Y-%m-%d")
    days_since_update = (datetime.utcnow() - last_updated).days
    return {
        "is_stale": days_since_update > stale_days,
        "days_since_update": days_since_update,
        "last_updated": template["last_updated"],
    }


def check_usage(template, min_usage=5):
    """Check if template is actively used."""
    return {
        "is_low_usage": template["usage_count_30d"] < min_usage,
        "usage_count_30d": template["usage_count_30d"],
        "recommendation": "Archive" if template["usage_count_30d"] < min_usage else "Active",
    }


def check_links(template):
    """Check for broken or outdated links."""
    issues = []
    for link in template.get("links", []):
        if link in BROKEN_LINKS:
            issues.append({"link": link, "status": "broken", "error": "404 Not Found"})
        elif link.startswith("{{"):
            issues.append({"link": link, "status": "variable", "note": "Dynamic link - verify at runtime"})
    return {"has_issues": len(issues) > 0, "link_issues": issues}


def check_variables(template):
    """Check variable placeholders for issues."""
    issues = []
    for var in template.get("variables", []):
        if var not in KNOWN_VARIABLES and not var.startswith("step_"):
            issues.append({
                "variable": var,
                "status": "custom",
                "note": "Verify this variable resolves correctly in your system",
            })
    return {"custom_variable_count": len(issues), "variable_notes": issues}


def check_csat(template, threshold=3.5):
    """Check if template CSAT is below threshold."""
    return {
        "below_threshold": template["avg_csat"] < threshold,
        "avg_csat": template["avg_csat"],
        "threshold": threshold,
    }


def audit_template(template, check_links_flag=True, check_vars_flag=True):
    """Run full audit on a single template."""
    issues = []
    warnings = []

    # Staleness check
    staleness = check_staleness(template)
    if staleness["is_stale"]:
        warnings.append(f"Template not updated in {staleness['days_since_update']} days")

    # Usage check
    usage = check_usage(template)
    if usage["is_low_usage"]:
        warnings.append(f"Low usage ({usage['usage_count_30d']} uses in 30 days) - consider archiving")

    # Link check
    link_result = {"has_issues": False, "link_issues": []}
    if check_links_flag:
        link_result = check_links(template)
        if link_result["has_issues"]:
            for issue in link_result["link_issues"]:
                if issue["status"] == "broken":
                    issues.append(f"Broken link: {issue['link']}")
                else:
                    warnings.append(f"Dynamic link: {issue['link']} - verify at runtime")

    # Variable check
    var_result = {"custom_variable_count": 0, "variable_notes": []}
    if check_vars_flag:
        var_result = check_variables(template)
        if var_result["custom_variable_count"] > 0:
            warnings.append(f"{var_result['custom_variable_count']} custom variables - verify resolution")

    # CSAT check
    csat_result = check_csat(template)
    if csat_result["below_threshold"]:
        issues.append(f"CSAT ({csat_result['avg_csat']}) below threshold ({csat_result['threshold']})")

    status = "pass" if not issues else "fail"
    if not issues and warnings:
        status = "warning"

    return {
        "template_id": template["id"],
        "template_name": template["name"],
        "category": template["category"],
        "status": status,
        "issues": issues,
        "warnings": warnings,
        "details": {
            "staleness": staleness,
            "usage": usage,
            "links": link_result,
            "variables": var_result,
            "csat": csat_result,
        },
    }


def main():
    parser = argparse.ArgumentParser(
        description="Run quality audit on all templates in the response library"
    )
    parser.add_argument(
        "--check-links",
        action="store_true",
        help="Check for broken links in templates",
    )
    parser.add_argument(
        "--check-variables",
        action="store_true",
        help="Validate variable placeholders",
    )
    parser.add_argument(
        "--report",
        action="store_true",
        help="Generate summary report",
    )
    parser.add_argument(
        "--category",
        choices=["greeting", "troubleshooting", "resolution", "follow-up", "closing", "apology"],
        help="Audit only a specific category",
    )
    parser.add_argument(
        "--format",
        choices=["full", "summary", "issues-only"],
        default="full",
        help="Output format (default: full)",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Include detailed audit information",
    )

    args = parser.parse_args()

    templates = TEMPLATES
    if args.category:
        templates = [t for t in templates if t["category"] == args.category]

    audit_results = []
    for template in templates:
        result = audit_template(template, args.check_links, args.check_variables)
        audit_results.append(result)

    # Summary statistics
    total = len(audit_results)
    passed = sum(1 for r in audit_results if r["status"] == "pass")
    warnings = sum(1 for r in audit_results if r["status"] == "warning")
    failed = sum(1 for r in audit_results if r["status"] == "fail")

    if args.format == "issues-only":
        issues_only = [r for r in audit_results if r["status"] in ["fail", "warning"]]
        output = {
            "audit_date": datetime.utcnow().isoformat() + "Z",
            "templates_with_issues": len(issues_only),
            "issues": issues_only,
        }
    elif args.format == "summary":
        output = {
            "audit_date": datetime.utcnow().isoformat() + "Z",
            "total_templates": total,
            "passed": passed,
            "warnings": warnings,
            "failed": failed,
            "health_score": round(passed / total * 100, 1) if total > 0 else 0,
            "top_issues": [
                r["issues"][0] for r in audit_results if r["issues"]
            ][:5],
        }
    else:
        output = {
            "audit_date": datetime.utcnow().isoformat() + "Z",
            "summary": {
                "total_templates": total,
                "passed": passed,
                "warnings": warnings,
                "failed": failed,
                "health_score": round(passed / total * 100, 1) if total > 0 else 0,
            },
            "results": audit_results if args.verbose else [
                {"id": r["template_id"], "name": r["template_name"], "status": r["status"],
                 "issues": r["issues"], "warnings": r["warnings"]}
                for r in audit_results
            ],
            "recommendations": [
                "Update stale templates (>90 days without revision)",
                "Archive templates with <5 uses in 30 days",
                "Fix broken links in RSLV-002",
                "Review low-CSAT templates for tone and content improvements",
            ],
        }

    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
