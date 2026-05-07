#!/usr/bin/env python3
"""Generate a privacy policy skeleton based on platform type, regulations, and data practices.

Usage:
    python generate_privacy_policy.py --platform web --regulations gdpr,ccpa --company "Acme Inc"
    python generate_privacy_policy.py --platform mobile --regulations gdpr --company "Acme Inc" --output policy.json
"""

import argparse
import json
import sys
from datetime import datetime

REGULATION_SECTIONS = {
    "gdpr": {
        "name": "GDPR",
        "jurisdiction": "EU/EEA",
        "required_sections": [
            "lawful_basis_for_processing",
            "data_subject_rights",
            "data_protection_officer",
            "international_transfers",
            "data_protection_impact_assessments",
            "breach_notification_72h",
            "right_to_lodge_complaint",
        ],
        "user_rights": [
            "Right of access (Art. 15)",
            "Right to rectification (Art. 16)",
            "Right to erasure (Art. 17)",
            "Right to restrict processing (Art. 18)",
            "Right to data portability (Art. 20)",
            "Right to object (Art. 21)",
            "Rights related to automated decision-making (Art. 22)",
        ],
    },
    "ccpa": {
        "name": "CCPA/CPRA",
        "jurisdiction": "California, USA",
        "required_sections": [
            "categories_of_personal_information",
            "right_to_know",
            "right_to_delete",
            "right_to_opt_out_of_sale",
            "do_not_sell_link",
            "non_discrimination",
            "financial_incentives",
        ],
        "user_rights": [
            "Right to know what PI is collected",
            "Right to delete personal information",
            "Right to opt-out of sale/sharing",
            "Right to non-discrimination",
            "Right to correct inaccurate PI",
            "Right to limit sensitive PI use",
        ],
    },
    "pipeda": {
        "name": "PIPEDA",
        "jurisdiction": "Canada",
        "required_sections": [
            "accountability_principle",
            "consent_requirements",
            "limiting_collection",
            "limiting_use_disclosure_retention",
            "accuracy",
            "safeguards",
            "openness",
            "individual_access",
            "challenging_compliance",
        ],
        "user_rights": [
            "Right to access personal information",
            "Right to challenge accuracy",
            "Right to withdraw consent",
            "Right to complain to Privacy Commissioner",
        ],
    },
    "lgpd": {
        "name": "LGPD",
        "jurisdiction": "Brazil",
        "required_sections": [
            "legal_basis_for_processing",
            "data_subject_rights",
            "international_transfers",
            "data_protection_officer",
            "security_measures",
        ],
        "user_rights": [
            "Right to confirmation of processing",
            "Right to access",
            "Right to correction",
            "Right to anonymization or deletion",
            "Right to data portability",
            "Right to information about sharing",
            "Right to revoke consent",
        ],
    },
}

PLATFORM_DATA_CATEGORIES = {
    "web": [
        {"category": "Identity Data", "examples": "Name, email, username", "sensitivity": "Medium"},
        {"category": "Technical Data", "examples": "IP address, browser type, cookies", "sensitivity": "Low"},
        {"category": "Usage Data", "examples": "Pages viewed, click patterns", "sensitivity": "Low"},
        {"category": "Communication Data", "examples": "Support tickets, form submissions", "sensitivity": "Medium"},
    ],
    "mobile": [
        {"category": "Identity Data", "examples": "Name, email, phone number", "sensitivity": "Medium"},
        {"category": "Device Data", "examples": "Device model, OS version, device ID", "sensitivity": "Medium"},
        {"category": "Location Data", "examples": "GPS coordinates, IP-based location", "sensitivity": "High"},
        {"category": "Usage Data", "examples": "App usage patterns, session duration", "sensitivity": "Low"},
        {"category": "Notification Data", "examples": "Push notification tokens", "sensitivity": "Low"},
    ],
    "saas": [
        {"category": "Identity Data", "examples": "Name, email, company, role", "sensitivity": "Medium"},
        {"category": "Account Data", "examples": "Subscription tier, billing info", "sensitivity": "High"},
        {"category": "Content Data", "examples": "Files uploaded, content created", "sensitivity": "High"},
        {"category": "Usage Data", "examples": "Feature usage, API calls, sessions", "sensitivity": "Low"},
        {"category": "Integration Data", "examples": "Third-party account connections", "sensitivity": "Medium"},
    ],
    "iot": [
        {"category": "Identity Data", "examples": "Name, email, account info", "sensitivity": "Medium"},
        {"category": "Device Data", "examples": "Device ID, firmware version, MAC address", "sensitivity": "Medium"},
        {"category": "Sensor Data", "examples": "Temperature, motion, audio, video", "sensitivity": "High"},
        {"category": "Location Data", "examples": "Device location, geofencing data", "sensitivity": "High"},
        {"category": "Usage Data", "examples": "Device usage patterns, schedules", "sensitivity": "Medium"},
    ],
}

STANDARD_SECTIONS = [
    "introduction_and_scope",
    "information_we_collect",
    "how_we_use_information",
    "how_we_share_information",
    "data_retention",
    "your_rights",
    "security_measures",
    "international_transfers",
    "childrens_privacy",
    "cookie_policy",
    "changes_to_policy",
    "contact_information",
]


def generate_policy(platform, regulations, company, include_cookies=True):
    """Generate a privacy policy skeleton."""
    reg_list = [r.strip().lower() for r in regulations.split(",")]

    all_rights = []
    all_required_sections = set(STANDARD_SECTIONS)
    applicable_regulations = []

    for reg in reg_list:
        if reg in REGULATION_SECTIONS:
            info = REGULATION_SECTIONS[reg]
            applicable_regulations.append(info)
            all_rights.extend(info["user_rights"])
            all_required_sections.update(info["required_sections"])

    data_categories = PLATFORM_DATA_CATEGORIES.get(platform, PLATFORM_DATA_CATEGORIES["web"])

    policy = {
        "metadata": {
            "company": company,
            "platform": platform,
            "regulations": [r["name"] for r in applicable_regulations],
            "generated_date": datetime.now().strftime("%Y-%m-%d"),
            "version": "1.0",
            "status": "DRAFT - REQUIRES LEGAL REVIEW",
        },
        "sections": sorted(list(all_required_sections)),
        "data_categories": data_categories,
        "user_rights": sorted(list(set(all_rights))),
        "compliance_checklist": [],
        "cookie_categories": [],
    }

    for reg_info in applicable_regulations:
        for section in reg_info["required_sections"]:
            policy["compliance_checklist"].append({
                "regulation": reg_info["name"],
                "requirement": section.replace("_", " ").title(),
                "status": "TODO",
            })

    if include_cookies:
        policy["cookie_categories"] = [
            {"category": "Strictly Necessary", "consent_required": False, "examples": ["session_id", "csrf_token"]},
            {"category": "Analytics", "consent_required": True, "examples": ["_ga", "_gid"]},
            {"category": "Functionality", "consent_required": True, "examples": ["lang", "theme"]},
            {"category": "Advertising", "consent_required": True, "examples": ["_fbp", "IDE"]},
        ]

    return policy


def main():
    parser = argparse.ArgumentParser(
        description="Generate a privacy policy skeleton based on platform, regulations, and data practices."
    )
    parser.add_argument(
        "--platform",
        choices=["web", "mobile", "saas", "iot"],
        default="web",
        help="Platform type (default: web)",
    )
    parser.add_argument(
        "--regulations",
        default="gdpr",
        help="Comma-separated list of regulations: gdpr, ccpa, pipeda, lgpd (default: gdpr)",
    )
    parser.add_argument(
        "--company",
        default="[COMPANY NAME]",
        help="Company name to use in the policy",
    )
    parser.add_argument(
        "--no-cookies",
        action="store_true",
        help="Exclude cookie policy section",
    )
    parser.add_argument(
        "--output",
        help="Output file path (default: stdout)",
    )

    args = parser.parse_args()

    policy = generate_policy(
        platform=args.platform,
        regulations=args.regulations,
        company=args.company,
        include_cookies=not args.no_cookies,
    )

    output = json.dumps(policy, indent=2)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Policy skeleton written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
