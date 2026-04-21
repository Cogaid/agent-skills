#!/usr/bin/env python3
"""Generate a terms of service skeleton based on business model and jurisdiction.

Usage:
    python generate_tos.py --model saas --jurisdiction us,eu --company "Acme Inc"
    python generate_tos.py --model ecommerce --jurisdiction us --output tos.json
"""

import argparse
import json
import sys
from datetime import datetime

BUSINESS_MODELS = {
    "saas": {
        "name": "SaaS",
        "key_sections": [
            "subscription_terms",
            "service_level_agreement",
            "data_ownership_and_portability",
            "api_terms",
            "uptime_guarantees",
            "support_terms",
        ],
        "special_clauses": [
            "Auto-renewal and cancellation policy",
            "Service credits for downtime",
            "Data export in standard formats",
            "API rate limits by tier",
            "Beta features disclaimer",
        ],
    },
    "ecommerce": {
        "name": "E-Commerce",
        "key_sections": [
            "product_information",
            "orders_and_fulfillment",
            "returns_and_refunds",
            "shipping_terms",
            "warranties",
            "payment_terms",
        ],
        "special_clauses": [
            "Product accuracy disclaimer",
            "Order acceptance and confirmation",
            "Return window and conditions",
            "Risk of loss transfer",
            "Defective product handling",
        ],
    },
    "marketplace": {
        "name": "Marketplace",
        "key_sections": [
            "buyer_terms",
            "seller_terms",
            "commission_structure",
            "dispute_resolution_between_parties",
            "escrow_terms",
            "content_and_listing_policies",
        ],
        "special_clauses": [
            "Platform is not a party to buyer-seller transactions",
            "Seller verification and onboarding",
            "Buyer protection program",
            "Commission and fee structure",
            "Prohibited listings",
        ],
    },
    "mobile_app": {
        "name": "Mobile App",
        "key_sections": [
            "app_license",
            "in_app_purchases",
            "push_notifications",
            "device_permissions",
            "app_store_compliance",
            "offline_functionality",
        ],
        "special_clauses": [
            "App store terms incorporation",
            "In-app purchase refund policy",
            "Push notification consent",
            "Device permission usage",
            "Automatic updates",
        ],
    },
    "api": {
        "name": "API/Platform",
        "key_sections": [
            "api_license",
            "rate_limits_and_quotas",
            "versioning_and_deprecation",
            "developer_obligations",
            "data_usage_restrictions",
            "redistribution_restrictions",
        ],
        "special_clauses": [
            "Rate limit enforcement",
            "API versioning and sunset policy",
            "No competitive use restriction",
            "Attribution requirements",
            "Webhook reliability disclaimer",
        ],
    },
}

JURISDICTION_REQUIREMENTS = {
    "us": {
        "name": "United States",
        "requirements": [
            "COPPA compliance for children under 13",
            "CAN-SPAM compliance for commercial emails",
            "State-specific consumer protection laws",
            "ADA accessibility considerations",
            "Arbitration clause with opt-out window",
            "Class action waiver (if arbitration used)",
        ],
        "governing_law": "[STATE], United States",
    },
    "eu": {
        "name": "European Union",
        "requirements": [
            "Consumer Rights Directive: 14-day withdrawal right",
            "GDPR compliance provisions",
            "Unfair Contract Terms Directive compliance",
            "Platform-to-Business Regulation (P2B) for marketplaces",
            "Digital Services Act obligations",
            "Cannot mandate arbitration for consumers",
        ],
        "governing_law": "[EU MEMBER STATE]",
    },
    "uk": {
        "name": "United Kingdom",
        "requirements": [
            "Consumer Rights Act 2015",
            "UK GDPR compliance",
            "Consumer Contracts Regulations (14-day cancellation)",
            "Unfair Terms in Consumer Contracts",
            "Electronic Commerce Regulations 2002",
        ],
        "governing_law": "England and Wales",
    },
    "ca": {
        "name": "California",
        "requirements": [
            "California Automatic Renewal Law compliance",
            "CCPA/CPRA privacy provisions",
            "Clear cancellation mechanism required",
            "Price increase notification",
            "Song-Beverly Consumer Warranty Act",
        ],
        "governing_law": "California, United States",
    },
    "au": {
        "name": "Australia",
        "requirements": [
            "Australian Consumer Law compliance",
            "No unfair contract terms in standard form contracts",
            "Consumer guarantee rights cannot be excluded",
            "Mandatory refund rights for major failures",
        ],
        "governing_law": "Australia",
    },
}

STANDARD_CLAUSES = [
    "acceptance_of_terms",
    "definitions",
    "eligibility",
    "account_registration",
    "the_service",
    "fees_and_payment",
    "acceptable_use_policy",
    "intellectual_property",
    "user_content",
    "privacy",
    "third_party_services",
    "disclaimers",
    "limitation_of_liability",
    "indemnification",
    "dispute_resolution",
    "termination",
    "modifications_to_terms",
    "general_provisions",
    "contact_information",
]


def generate_tos(model, jurisdictions, company):
    """Generate a terms of service skeleton."""
    jurisdiction_list = [j.strip().lower() for j in jurisdictions.split(",")]

    model_info = BUSINESS_MODELS.get(model, BUSINESS_MODELS["saas"])

    all_requirements = []
    governing_laws = []
    for j in jurisdiction_list:
        if j in JURISDICTION_REQUIREMENTS:
            jinfo = JURISDICTION_REQUIREMENTS[j]
            all_requirements.extend(
                [{"jurisdiction": jinfo["name"], "requirement": r} for r in jinfo["requirements"]]
            )
            governing_laws.append(jinfo["governing_law"])

    sections = STANDARD_CLAUSES + model_info["key_sections"]

    tos = {
        "metadata": {
            "company": company,
            "business_model": model_info["name"],
            "jurisdictions": [JURISDICTION_REQUIREMENTS[j]["name"] for j in jurisdiction_list if j in JURISDICTION_REQUIREMENTS],
            "generated_date": datetime.now().strftime("%Y-%m-%d"),
            "version": "1.0",
            "status": "DRAFT - REQUIRES LEGAL REVIEW",
        },
        "sections": sorted(list(set(sections))),
        "special_clauses": model_info["special_clauses"],
        "jurisdiction_requirements": all_requirements,
        "governing_law_options": governing_laws,
        "enforceability_notes": [
            "Use clickwrap agreement formation for strongest enforceability",
            "Ensure conspicuous notice of material terms",
            "Provide reasonable opportunity to review before acceptance",
            "Maintain version history and change notification records",
        ],
    }

    return tos


def main():
    parser = argparse.ArgumentParser(
        description="Generate a terms of service skeleton based on business model and jurisdiction."
    )
    parser.add_argument(
        "--model",
        choices=list(BUSINESS_MODELS.keys()),
        default="saas",
        help="Business model type (default: saas)",
    )
    parser.add_argument(
        "--jurisdiction",
        default="us",
        help="Comma-separated jurisdictions: us, eu, uk, ca, au (default: us)",
    )
    parser.add_argument(
        "--company",
        default="[COMPANY NAME]",
        help="Company name",
    )
    parser.add_argument(
        "--output",
        help="Output file path (default: stdout)",
    )

    args = parser.parse_args()
    tos = generate_tos(model=args.model, jurisdictions=args.jurisdiction, company=args.company)
    output = json.dumps(tos, indent=2)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"ToS skeleton written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
