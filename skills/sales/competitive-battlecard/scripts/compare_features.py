#!/usr/bin/env python3
"""Generate a feature comparison matrix between your product and a competitor.

Produces a structured feature-by-feature comparison with scoring and advantage analysis.

Usage:
    python compare_features.py --competitor "Acme Corp" --categories all
    python compare_features.py --competitor "Acme Corp" --categories core,integrations
    python compare_features.py --competitor "Acme Corp" --format markdown
"""

import argparse
import json
from datetime import datetime


# Sample product feature data
OUR_FEATURES = {
    "core": {
        "category": "Core Platform",
        "features": [
            {"name": "Real-time dashboard", "status": "full", "detail": "Live updating, customizable widgets"},
            {"name": "Workflow automation", "status": "full", "detail": "Visual builder, 50+ triggers"},
            {"name": "Custom fields", "status": "full", "detail": "Unlimited custom fields and objects"},
            {"name": "Role-based access", "status": "full", "detail": "Granular permissions, SSO, SCIM"},
            {"name": "Audit trail", "status": "full", "detail": "Full activity history, exportable"},
            {"name": "Multi-language", "status": "partial", "detail": "12 languages, adding more quarterly"},
        ],
    },
    "integrations": {
        "category": "Integrations",
        "features": [
            {"name": "REST API", "status": "full", "detail": "Full CRUD, webhooks, rate limiting"},
            {"name": "Native CRM connectors", "status": "full", "detail": "Salesforce, HubSpot, Dynamics"},
            {"name": "Marketing platforms", "status": "full", "detail": "Marketo, Pardot, Mailchimp"},
            {"name": "Data warehouse sync", "status": "full", "detail": "Snowflake, BigQuery, Redshift"},
            {"name": "Custom integrations", "status": "full", "detail": "iPaaS support, Zapier, Workato"},
            {"name": "ERP connectors", "status": "partial", "detail": "SAP (beta), NetSuite (GA)"},
        ],
    },
    "analytics": {
        "category": "Analytics & Reporting",
        "features": [
            {"name": "Custom reports", "status": "full", "detail": "Drag-and-drop builder, scheduling"},
            {"name": "Predictive analytics", "status": "full", "detail": "ML-powered forecasting"},
            {"name": "Embedded analytics", "status": "full", "detail": "Iframe and SDK embedding"},
            {"name": "Data export", "status": "full", "detail": "CSV, Excel, API, scheduled exports"},
            {"name": "Real-time alerts", "status": "full", "detail": "Threshold-based, Slack/email/SMS"},
            {"name": "Natural language queries", "status": "roadmap", "detail": "Expected Q3 2025"},
        ],
    },
    "security": {
        "category": "Security & Compliance",
        "features": [
            {"name": "SOC 2 Type II", "status": "full", "detail": "Certified annually"},
            {"name": "GDPR compliance", "status": "full", "detail": "Data residency options, DPA"},
            {"name": "HIPAA compliance", "status": "full", "detail": "BAA available, PHI safeguards"},
            {"name": "SSO/SAML", "status": "full", "detail": "Okta, Azure AD, OneLogin"},
            {"name": "Data encryption", "status": "full", "detail": "AES-256 at rest, TLS 1.3 in transit"},
            {"name": "FedRAMP", "status": "none", "detail": "Not currently pursuing"},
        ],
    },
    "support": {
        "category": "Support & Services",
        "features": [
            {"name": "24/7 support", "status": "full", "detail": "All plans, <1hr response SLA"},
            {"name": "Dedicated CSM", "status": "full", "detail": "Pro and Enterprise plans"},
            {"name": "Implementation services", "status": "full", "detail": "Avg 4-week implementation"},
            {"name": "Training academy", "status": "full", "detail": "Self-paced + live workshops"},
            {"name": "Community forum", "status": "full", "detail": "5,000+ active members"},
            {"name": "Professional services", "status": "partial", "detail": "Limited capacity, partner network"},
        ],
    },
}

# Sample competitor feature data
COMPETITOR_FEATURES = {
    "Acme Corp": {
        "core": {
            "features": [
                {"name": "Real-time dashboard", "status": "full", "detail": "Dashboard with manual refresh option"},
                {"name": "Workflow automation", "status": "partial", "detail": "Rule-based only, no visual builder"},
                {"name": "Custom fields", "status": "full", "detail": "Up to 200 custom fields per object"},
                {"name": "Role-based access", "status": "full", "detail": "Standard roles, limited customization"},
                {"name": "Audit trail", "status": "partial", "detail": "90-day retention, no export"},
                {"name": "Multi-language", "status": "full", "detail": "25 languages supported"},
            ],
        },
        "integrations": {
            "features": [
                {"name": "REST API", "status": "full", "detail": "CRUD operations, basic webhooks"},
                {"name": "Native CRM connectors", "status": "full", "detail": "Salesforce, HubSpot"},
                {"name": "Marketing platforms", "status": "partial", "detail": "Marketo only"},
                {"name": "Data warehouse sync", "status": "partial", "detail": "Snowflake only, batch sync"},
                {"name": "Custom integrations", "status": "full", "detail": "Zapier, custom API"},
                {"name": "ERP connectors", "status": "full", "detail": "SAP, Oracle, NetSuite all GA"},
            ],
        },
        "analytics": {
            "features": [
                {"name": "Custom reports", "status": "full", "detail": "Template-based, limited customization"},
                {"name": "Predictive analytics", "status": "none", "detail": "Not available"},
                {"name": "Embedded analytics", "status": "partial", "detail": "Iframe only, no SDK"},
                {"name": "Data export", "status": "full", "detail": "CSV and Excel export"},
                {"name": "Real-time alerts", "status": "full", "detail": "Email alerts only"},
                {"name": "Natural language queries", "status": "full", "detail": "Basic NLQ available"},
            ],
        },
        "security": {
            "features": [
                {"name": "SOC 2 Type II", "status": "full", "detail": "Certified"},
                {"name": "GDPR compliance", "status": "full", "detail": "EU data center option"},
                {"name": "HIPAA compliance", "status": "partial", "detail": "BAA available, limited controls"},
                {"name": "SSO/SAML", "status": "full", "detail": "Major IdPs supported"},
                {"name": "Data encryption", "status": "full", "detail": "AES-256 at rest, TLS 1.2+"},
                {"name": "FedRAMP", "status": "full", "detail": "FedRAMP Moderate authorized"},
            ],
        },
        "support": {
            "features": [
                {"name": "24/7 support", "status": "partial", "detail": "Enterprise plan only, 4hr SLA"},
                {"name": "Dedicated CSM", "status": "partial", "detail": "Enterprise plan only"},
                {"name": "Implementation services", "status": "full", "detail": "8-12 week typical implementation"},
                {"name": "Training academy", "status": "full", "detail": "Self-paced learning portal"},
                {"name": "Community forum", "status": "full", "detail": "Large community, slower response"},
                {"name": "Professional services", "status": "full", "detail": "Large PS organization"},
            ],
        },
    },
    "BetaTools": {
        "core": {
            "features": [
                {"name": "Real-time dashboard", "status": "full", "detail": "Modern UI, real-time"},
                {"name": "Workflow automation", "status": "partial", "detail": "Basic automation rules"},
                {"name": "Custom fields", "status": "partial", "detail": "Limited to 50 per object"},
                {"name": "Role-based access", "status": "partial", "detail": "Admin and User roles only"},
                {"name": "Audit trail", "status": "none", "detail": "Not available"},
                {"name": "Multi-language", "status": "partial", "detail": "5 languages"},
            ],
        },
        "integrations": {
            "features": [
                {"name": "REST API", "status": "full", "detail": "Well-documented, modern API"},
                {"name": "Native CRM connectors", "status": "partial", "detail": "HubSpot only"},
                {"name": "Marketing platforms", "status": "partial", "detail": "Mailchimp only"},
                {"name": "Data warehouse sync", "status": "none", "detail": "Not available"},
                {"name": "Custom integrations", "status": "full", "detail": "Zapier, Make"},
                {"name": "ERP connectors", "status": "none", "detail": "Not available"},
            ],
        },
        "analytics": {
            "features": [
                {"name": "Custom reports", "status": "partial", "detail": "Pre-built templates only"},
                {"name": "Predictive analytics", "status": "none", "detail": "Not available"},
                {"name": "Embedded analytics", "status": "none", "detail": "Not available"},
                {"name": "Data export", "status": "full", "detail": "CSV export"},
                {"name": "Real-time alerts", "status": "partial", "detail": "Email only, limited triggers"},
                {"name": "Natural language queries", "status": "none", "detail": "Not available"},
            ],
        },
        "security": {
            "features": [
                {"name": "SOC 2 Type II", "status": "full", "detail": "Certified"},
                {"name": "GDPR compliance", "status": "full", "detail": "Compliant"},
                {"name": "HIPAA compliance", "status": "none", "detail": "Not available"},
                {"name": "SSO/SAML", "status": "partial", "detail": "Google SSO only"},
                {"name": "Data encryption", "status": "full", "detail": "Standard encryption"},
                {"name": "FedRAMP", "status": "none", "detail": "Not available"},
            ],
        },
        "support": {
            "features": [
                {"name": "24/7 support", "status": "none", "detail": "Business hours only"},
                {"name": "Dedicated CSM", "status": "none", "detail": "Not available"},
                {"name": "Implementation services", "status": "partial", "detail": "Self-serve setup, 1hr onboarding call"},
                {"name": "Training academy", "status": "partial", "detail": "Video tutorials only"},
                {"name": "Community forum", "status": "full", "detail": "Active Slack community"},
                {"name": "Professional services", "status": "none", "detail": "Not available"},
            ],
        },
    },
}

STATUS_LABELS = {
    "full": "Full Support",
    "partial": "Partial/Limited",
    "none": "Not Available",
    "roadmap": "On Roadmap",
}

STATUS_SYMBOLS = {
    "full": "FULL",
    "partial": "PARTIAL",
    "none": "NONE",
    "roadmap": "ROADMAP",
}


def determine_advantage(our_status, their_status):
    """Determine who has the advantage for a feature."""
    rank = {"full": 3, "partial": 2, "roadmap": 1, "none": 0}
    our_rank = rank.get(our_status, 0)
    their_rank = rank.get(their_status, 0)
    if our_rank > their_rank:
        return "Us"
    elif their_rank > our_rank:
        return "Them"
    return "Tie"


def compare_features(competitor_name, categories):
    """Generate feature comparison for specified categories."""
    competitor_data = COMPETITOR_FEATURES.get(competitor_name)
    if not competitor_data:
        return {"error": f"No feature data available for '{competitor_name}'"}

    comparison = []
    scoring = {"us_leading": 0, "tied": 0, "them_leading": 0}

    for cat_key, our_cat in OUR_FEATURES.items():
        if categories != ["all"] and cat_key not in categories:
            continue

        their_cat = competitor_data.get(cat_key, {})
        their_features = {f["name"]: f for f in their_cat.get("features", [])}

        category_comparison = {
            "category": our_cat["category"],
            "features": [],
        }

        for our_feature in our_cat["features"]:
            name = our_feature["name"]
            their_feature = their_features.get(name, {"status": "none", "detail": "Not available"})
            advantage = determine_advantage(our_feature["status"], their_feature["status"])

            if advantage == "Us":
                scoring["us_leading"] += 1
            elif advantage == "Them":
                scoring["them_leading"] += 1
            else:
                scoring["tied"] += 1

            category_comparison["features"].append({
                "feature": name,
                "us_status": our_feature["status"],
                "us_detail": our_feature["detail"],
                "them_status": their_feature["status"],
                "them_detail": their_feature["detail"],
                "advantage": advantage,
            })

        comparison.append(category_comparison)

    return {
        "competitor": competitor_name,
        "categories_analyzed": [c["category"] for c in comparison],
        "total_features": scoring["us_leading"] + scoring["tied"] + scoring["them_leading"],
        "scoring": scoring,
        "comparison": comparison,
    }


def format_markdown(result):
    """Format comparison as markdown table."""
    lines = []
    lines.append(f"# Feature Comparison: Us vs. {result['competitor']}")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d')}")
    lines.append("")
    lines.append(f"**Summary:** Us Leading: {result['scoring']['us_leading']} | "
                 f"Tied: {result['scoring']['tied']} | "
                 f"Them Leading: {result['scoring']['them_leading']}")
    lines.append("")

    for category in result["comparison"]:
        lines.append(f"## {category['category']}")
        lines.append("")
        lines.append("| Feature | Us | Them | Advantage | Notes |")
        lines.append("|---------|-----|------|-----------|-------|")
        for feat in category["features"]:
            us_label = STATUS_SYMBOLS[feat["us_status"]]
            them_label = STATUS_SYMBOLS[feat["them_status"]]
            notes = feat["us_detail"] if feat["advantage"] == "Us" else feat["them_detail"]
            lines.append(f"| {feat['feature']} | {us_label} | {them_label} | {feat['advantage']} | {notes} |")
        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Generate feature comparison matrix between your product and a competitor.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python compare_features.py --competitor "Acme Corp" --categories all
  python compare_features.py --competitor "Acme Corp" --categories core,integrations
  python compare_features.py --competitor "BetaTools" --format markdown
  python compare_features.py --list-competitors
  python compare_features.py --list-categories
        """,
    )
    parser.add_argument(
        "--competitor",
        type=str,
        help="Competitor name to compare against",
    )
    parser.add_argument(
        "--categories",
        type=str,
        default="all",
        help="Comma-separated categories to compare (default: all)",
    )
    parser.add_argument(
        "--format",
        type=str,
        choices=["json", "markdown"],
        default="json",
        help="Output format (default: json)",
    )
    parser.add_argument(
        "--list-competitors",
        action="store_true",
        help="List available competitors with feature data",
    )
    parser.add_argument(
        "--list-categories",
        action="store_true",
        help="List available feature categories",
    )

    args = parser.parse_args()

    if args.list_competitors:
        competitors = list(COMPETITOR_FEATURES.keys())
        print(json.dumps({"available_competitors": competitors}, indent=2))
        return

    if args.list_categories:
        categories = {k: v["category"] for k, v in OUR_FEATURES.items()}
        print(json.dumps({"available_categories": categories}, indent=2))
        return

    if not args.competitor:
        parser.error("--competitor is required (use --list-competitors to see options)")

    categories = [c.strip() for c in args.categories.split(",")]
    result = compare_features(args.competitor, categories)

    if "error" in result:
        print(json.dumps(result, indent=2))
        return

    result["metadata"] = {
        "generated": datetime.now().isoformat(),
        "competitor": args.competitor,
        "categories_requested": args.categories,
    }

    if args.format == "json":
        print(json.dumps(result, indent=2))
    else:
        print(format_markdown(result))


if __name__ == "__main__":
    main()
