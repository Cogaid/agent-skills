#!/usr/bin/env python3
"""
SEO Audit Runner -- Execute a comprehensive SEO audit for a given URL.

Usage:
    python run_audit.py --url https://example.com --depth full
    python run_audit.py --url https://example.com --depth technical --output audit.json
    python run_audit.py --url https://example.com --depth quick --format markdown
"""

import argparse
import json
import sys
from datetime import datetime
from urllib.parse import urlparse

AUDIT_DIMENSIONS = {
    "technical": {
        "weight": 0.30,
        "checks": [
            {"name": "HTTPS enabled", "category": "security", "severity": "critical"},
            {"name": "robots.txt accessible", "category": "crawlability", "severity": "high"},
            {"name": "XML sitemap present", "category": "crawlability", "severity": "high"},
            {"name": "No redirect chains (3+)", "category": "crawlability", "severity": "medium"},
            {"name": "No 5xx errors", "category": "errors", "severity": "critical"},
            {"name": "No 404 errors on internal links", "category": "errors", "severity": "high"},
            {"name": "Canonical tags present", "category": "indexing", "severity": "high"},
            {"name": "Mobile-friendly", "category": "mobile", "severity": "critical"},
            {"name": "Core Web Vitals - LCP < 2.5s", "category": "speed", "severity": "high"},
            {"name": "Core Web Vitals - INP < 200ms", "category": "speed", "severity": "high"},
            {"name": "Core Web Vitals - CLS < 0.1", "category": "speed", "severity": "medium"},
            {"name": "Structured data valid", "category": "structure", "severity": "medium"},
            {"name": "Hreflang correct (if multilingual)", "category": "indexing", "severity": "medium"},
            {"name": "No mixed content", "category": "security", "severity": "high"},
            {"name": "Clean URL structure", "category": "structure", "severity": "medium"},
        ],
    },
    "on_page": {
        "weight": 0.25,
        "checks": [
            {"name": "Unique title tags", "category": "titles", "severity": "high"},
            {"name": "Title length 30-60 chars", "category": "titles", "severity": "medium"},
            {"name": "Keywords in titles", "category": "titles", "severity": "high"},
            {"name": "Unique meta descriptions", "category": "meta", "severity": "medium"},
            {"name": "Meta desc 120-160 chars", "category": "meta", "severity": "low"},
            {"name": "H1 present and unique", "category": "headings", "severity": "high"},
            {"name": "Heading hierarchy correct", "category": "headings", "severity": "medium"},
            {"name": "Image alt text present", "category": "images", "severity": "medium"},
            {"name": "Images optimized (<200KB)", "category": "images", "severity": "medium"},
            {"name": "Internal linking adequate", "category": "links", "severity": "high"},
            {"name": "No broken internal links", "category": "links", "severity": "high"},
            {"name": "URL keywords match content", "category": "urls", "severity": "medium"},
        ],
    },
    "content": {
        "weight": 0.25,
        "checks": [
            {"name": "No thin content (<300 words)", "category": "quality", "severity": "high"},
            {"name": "No duplicate content", "category": "quality", "severity": "high"},
            {"name": "Content freshness (<12 months)", "category": "freshness", "severity": "medium"},
            {"name": "E-E-A-T signals present", "category": "trust", "severity": "high"},
            {"name": "No keyword cannibalization", "category": "keywords", "severity": "high"},
            {"name": "Target keywords covered", "category": "keywords", "severity": "high"},
            {"name": "Content gaps addressed", "category": "coverage", "severity": "medium"},
            {"name": "Author information present", "category": "trust", "severity": "medium"},
        ],
    },
    "off_page": {
        "weight": 0.20,
        "checks": [
            {"name": "Domain rating competitive", "category": "authority", "severity": "high"},
            {"name": "Referring domains growing", "category": "links", "severity": "high"},
            {"name": "No toxic backlinks (>5%)", "category": "links", "severity": "high"},
            {"name": "Anchor text diversity", "category": "links", "severity": "medium"},
            {"name": "Brand search volume exists", "category": "brand", "severity": "medium"},
            {"name": "Backlink profile vs competitors", "category": "authority", "severity": "high"},
        ],
    },
}

DEPTH_CONFIGS = {
    "quick": {
        "name": "Quick Audit",
        "description": "High-priority checks only (critical + high severity)",
        "min_severity": "high",
        "estimated_time": "30 minutes",
    },
    "standard": {
        "name": "Standard Audit",
        "description": "All standard checks across dimensions",
        "min_severity": "medium",
        "estimated_time": "2-3 hours",
    },
    "full": {
        "name": "Full Audit",
        "description": "Comprehensive audit including all checks and competitor analysis",
        "min_severity": "low",
        "estimated_time": "4-8 hours",
    },
}

SEVERITY_ORDER = {"critical": 0, "high": 1, "medium": 2, "low": 3}


def filter_checks_by_depth(checks, depth):
    """Filter checks based on audit depth."""
    min_severity = DEPTH_CONFIGS[depth]["min_severity"]
    min_level = SEVERITY_ORDER[min_severity]
    return [c for c in checks if SEVERITY_ORDER[c["severity"]] <= min_level]


def generate_audit_checklist(url, depth):
    """Generate the audit checklist based on URL and depth."""
    parsed = urlparse(url)
    domain = parsed.netloc or parsed.path

    audit = {
        "url": url,
        "domain": domain,
        "depth": depth,
        "depth_config": DEPTH_CONFIGS[depth],
        "dimensions": {},
        "total_checks": 0,
    }

    for dim_key, dim_data in AUDIT_DIMENSIONS.items():
        checks = filter_checks_by_depth(dim_data["checks"], depth)
        audit["dimensions"][dim_key] = {
            "name": dim_key.replace("_", " ").title(),
            "weight": dim_data["weight"],
            "checks": [
                {
                    "name": c["name"],
                    "category": c["category"],
                    "severity": c["severity"],
                    "status": "pending",
                    "notes": "",
                }
                for c in checks
            ],
            "total_checks": len(checks),
        }
        audit["total_checks"] += len(checks)

    return audit


def generate_sample_results(url, depth):
    """Generate sample audit results for demonstration."""
    import random

    random.seed(hash(url) % 2**32)

    audit = generate_audit_checklist(url, depth)

    for dim_key, dim_data in audit["dimensions"].items():
        passed = 0
        for check in dim_data["checks"]:
            if check["severity"] == "critical":
                is_pass = random.random() > 0.15
            elif check["severity"] == "high":
                is_pass = random.random() > 0.3
            else:
                is_pass = random.random() > 0.4

            check["status"] = "pass" if is_pass else "fail"
            if is_pass:
                passed += 1
            else:
                check["notes"] = f"Issue detected -- requires attention ({check['severity']} priority)"

        dim_data["passed"] = passed
        dim_data["failed"] = dim_data["total_checks"] - passed
        dim_data["score"] = round((passed / max(dim_data["total_checks"], 1)) * 100, 1)

    # Calculate overall score
    overall = 0
    for dim_key, dim_data in audit["dimensions"].items():
        overall += dim_data["score"] * dim_data["weight"]
    audit["overall_score"] = round(overall, 1)

    if audit["overall_score"] >= 90:
        audit["rating"] = "Excellent"
    elif audit["overall_score"] >= 75:
        audit["rating"] = "Good"
    elif audit["overall_score"] >= 60:
        audit["rating"] = "Fair"
    elif audit["overall_score"] >= 40:
        audit["rating"] = "Poor"
    else:
        audit["rating"] = "Critical"

    # Generate prioritized issues
    issues = []
    for dim_key, dim_data in audit["dimensions"].items():
        for check in dim_data["checks"]:
            if check["status"] == "fail":
                issues.append({
                    "dimension": dim_key,
                    "check": check["name"],
                    "severity": check["severity"],
                    "category": check["category"],
                })

    issues.sort(key=lambda x: SEVERITY_ORDER[x["severity"]])
    audit["prioritized_issues"] = issues

    return audit


def render_markdown(audit):
    """Render audit results as markdown."""
    lines = [
        f"# SEO Audit Report: {audit['domain']}",
        "",
        f"**URL:** {audit['url']}",
        f"**Depth:** {audit['depth_config']['name']}",
        f"**Date:** {datetime.now().strftime('%Y-%m-%d')}",
        f"**Total Checks:** {audit['total_checks']}",
        "",
    ]

    if "overall_score" in audit:
        lines.extend([
            f"## Overall Score: {audit['overall_score']}/100 ({audit['rating']})",
            "",
            "| Dimension | Score | Passed | Failed | Weight |",
            "|-----------|-------|--------|--------|--------|",
        ])
        for dim_key, dim_data in audit["dimensions"].items():
            lines.append(
                f"| {dim_data['name']} | {dim_data.get('score', 'N/A')}/100 | "
                f"{dim_data.get('passed', '-')} | {dim_data.get('failed', '-')} | "
                f"{int(dim_data['weight']*100)}% |"
            )
        lines.append("")

        if audit.get("prioritized_issues"):
            lines.extend(["## Prioritized Issues", ""])
            for i, issue in enumerate(audit["prioritized_issues"][:10], 1):
                lines.append(
                    f"{i}. **[{issue['severity'].upper()}]** {issue['check']} "
                    f"({issue['dimension']})"
                )
            lines.append("")

    for dim_key, dim_data in audit["dimensions"].items():
        lines.extend([f"## {dim_data['name']}", ""])
        for check in dim_data["checks"]:
            status_icon = "[x]" if check["status"] == "pass" else "[ ]"
            lines.append(f"- {status_icon} {check['name']} ({check['severity']})")
            if check.get("notes"):
                lines.append(f"  - {check['notes']}")
        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Run a comprehensive SEO audit for a website",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --url https://example.com --depth full
  %(prog)s --url https://example.com --depth quick --format markdown
  %(prog)s --url https://example.com --depth standard --sample --output audit.json
        """,
    )
    parser.add_argument("--url", required=True, help="Website URL to audit")
    parser.add_argument(
        "--depth",
        choices=["quick", "standard", "full"],
        default="standard",
        help="Audit depth (default: standard)",
    )
    parser.add_argument(
        "--sample",
        action="store_true",
        help="Generate sample results (for demonstration)",
    )
    parser.add_argument(
        "--format",
        choices=["json", "markdown"],
        default="json",
        help="Output format (default: json)",
    )
    parser.add_argument("--output", help="Output file (default: stdout)")

    args = parser.parse_args()

    if args.sample:
        audit = generate_sample_results(args.url, args.depth)
    else:
        audit = generate_audit_checklist(args.url, args.depth)

    result = {
        "generated_at": datetime.now().isoformat(),
        "tool": "seo-audit-reporter",
        "audit": audit,
    }

    if args.format == "markdown":
        output = render_markdown(audit)
    else:
        output = json.dumps(result, indent=2)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Audit written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
