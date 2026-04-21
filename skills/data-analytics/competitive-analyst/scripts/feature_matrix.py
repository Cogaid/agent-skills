#!/usr/bin/env python3
"""Build a feature comparison matrix across competitors.

Usage:
    python feature_matrix.py --competitors "Acme,Beta,Gamma" --categories "core,advanced"
    python feature_matrix.py --competitors "Acme,Beta" --output matrix.json
"""

import argparse
import json
import sys
from datetime import datetime

SAMPLE_FEATURES = {
    "core": [
        "User authentication",
        "Dashboard",
        "Data export (CSV)",
        "API access",
        "Email notifications",
        "Mobile app",
        "Role-based access control",
    ],
    "advanced": [
        "Custom workflows",
        "Advanced analytics",
        "AI/ML features",
        "Custom integrations",
        "White-labeling",
        "Multi-tenancy",
        "Audit logging",
    ],
    "integration": [
        "Salesforce",
        "Slack",
        "Jira",
        "Google Workspace",
        "Microsoft 365",
        "Zapier",
        "REST API",
    ],
    "security": [
        "SSO (SAML/OIDC)",
        "MFA",
        "SOC 2 certified",
        "GDPR compliant",
        "Data encryption at rest",
        "IP allowlisting",
        "SCIM provisioning",
    ],
}

STATUSES = ["Full", "Partial", "Beta", "Planned", "None"]


def build_matrix(competitors, categories):
    """Build a feature comparison matrix."""
    comp_list = [c.strip() for c in competitors.split(",")]
    cat_list = [c.strip() for c in categories.split(",")]

    matrix = {
        "metadata": {
            "competitors": comp_list,
            "categories": cat_list,
            "generated_date": datetime.now().strftime("%Y-%m-%d"),
            "status": "TEMPLATE - Fill in with research",
            "legend": {
                "Full": "Generally available",
                "Partial": "Limited functionality",
                "Beta": "In testing",
                "Planned": "On roadmap",
                "None": "Not available",
            },
        },
        "categories": {},
    }

    for cat in cat_list:
        features = SAMPLE_FEATURES.get(cat, [f"[Feature {i+1}]" for i in range(5)])
        feature_rows = []
        for feature in features:
            row = {"feature": feature, "our_product": "[STATUS]"}
            for comp in comp_list:
                row[comp] = "[STATUS]"
            feature_rows.append(row)
        matrix["categories"][cat] = feature_rows

    # Summary template
    matrix["analysis"] = {
        "we_lead_in": ["[Areas where we have Full and competitors have Partial/None]"],
        "we_trail_in": ["[Areas where competitors have Full and we have Partial/None]"],
        "parity": ["[Areas where capabilities are equivalent]"],
        "strategic_gaps": ["[Critical features we lack that competitors offer]"],
        "differentiation_opportunities": ["[Unique features to develop or emphasize]"],
    }

    return matrix


def main():
    parser = argparse.ArgumentParser(
        description="Build a feature comparison matrix across competitors."
    )
    parser.add_argument(
        "--competitors",
        required=True,
        help="Comma-separated list of competitor names",
    )
    parser.add_argument(
        "--categories",
        default="core,advanced",
        help="Comma-separated feature categories: core, advanced, integration, security (default: core,advanced)",
    )
    parser.add_argument(
        "--output",
        help="Output file path (default: stdout)",
    )

    args = parser.parse_args()

    matrix = build_matrix(competitors=args.competitors, categories=args.categories)
    output = json.dumps(matrix, indent=2)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Feature matrix written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
