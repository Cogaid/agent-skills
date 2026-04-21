#!/usr/bin/env python3
"""Calculate notification deadlines based on regulation and discovery date.

Usage:
    python notification_calc.py --regulation gdpr --discovery-date "2025-01-15T14:30:00"
    python notification_calc.py --regulation hipaa --discovery-date "2025-03-01" --output deadlines.json
    python notification_calc.py --all --discovery-date "2025-06-10"
"""

import argparse
import json
import sys
from datetime import datetime, timedelta

REGULATIONS = {
    "gdpr": {
        "name": "GDPR",
        "notifications": [
            {
                "entity": "Supervisory Authority (DPA)",
                "reference": "Article 33",
                "deadline_hours": 72,
                "deadline_description": "72 hours from awareness",
                "trigger": "Personal data breach likely to result in risk to rights and freedoms",
                "required_content": [
                    "Nature of the breach (categories, approximate numbers)",
                    "DPO or contact point name and details",
                    "Likely consequences of the breach",
                    "Measures taken or proposed to address the breach",
                ],
            },
            {
                "entity": "Affected Individuals",
                "reference": "Article 34",
                "deadline_hours": None,
                "deadline_description": "Without undue delay (when high risk)",
                "trigger": "High risk to rights and freedoms of individuals",
                "required_content": [
                    "Plain language description of the breach",
                    "DPO or contact point details",
                    "Likely consequences",
                    "Measures taken and recommended protective steps",
                ],
            },
        ],
    },
    "ccpa": {
        "name": "CCPA/CPRA",
        "notifications": [
            {
                "entity": "Affected California Residents",
                "reference": "Cal. Civ. Code 1798.82",
                "deadline_hours": None,
                "deadline_description": "In the most expedient time possible, without unreasonable delay",
                "trigger": "Unauthorized access to unencrypted personal information",
                "required_content": [
                    "Type of personal information compromised",
                    "Entity name and contact information",
                    "Types of information acquired",
                    "Steps taken and available remedies",
                ],
            },
            {
                "entity": "California Attorney General",
                "reference": "Cal. Civ. Code 1798.82(f)",
                "deadline_hours": None,
                "deadline_description": "If 500+ California residents affected",
                "trigger": "Breach affecting 500+ California residents",
                "required_content": [
                    "Sample notification letter",
                    "Scope of breach",
                ],
            },
        ],
    },
    "hipaa": {
        "name": "HIPAA",
        "notifications": [
            {
                "entity": "Affected Individuals",
                "reference": "45 CFR 164.404",
                "deadline_hours": 1440,  # 60 days
                "deadline_description": "60 days from discovery",
                "trigger": "Breach of unsecured protected health information",
                "required_content": [
                    "Brief description of what happened, including dates",
                    "Types of information involved",
                    "Steps individuals should take",
                    "What the entity is doing to investigate and mitigate",
                    "Contact information",
                ],
            },
            {
                "entity": "HHS Secretary",
                "reference": "45 CFR 164.408",
                "deadline_hours": 1440,  # 60 days if 500+, annual log if <500
                "deadline_description": "60 days if 500+ affected; annual log by March 1 if <500",
                "trigger": "Breach of unsecured PHI",
                "required_content": [
                    "Description of breach",
                    "Number of individuals affected",
                    "Types of PHI involved",
                    "Steps taken",
                ],
            },
            {
                "entity": "Media (prominent outlets in state)",
                "reference": "45 CFR 164.406",
                "deadline_hours": 1440,
                "deadline_description": "60 days if 500+ in a single state/jurisdiction",
                "trigger": "500+ individuals affected in a single state",
                "required_content": [
                    "Same content as individual notification",
                ],
            },
        ],
    },
    "pci-dss": {
        "name": "PCI-DSS",
        "notifications": [
            {
                "entity": "Card Brands and Acquiring Bank",
                "reference": "PCI-DSS Incident Response",
                "deadline_hours": 24,
                "deadline_description": "Immediately / within 24 hours",
                "trigger": "Compromise of cardholder data",
                "required_content": [
                    "Scope of compromise",
                    "Number of accounts potentially affected",
                    "Preliminary forensic findings",
                    "Containment actions taken",
                ],
            },
        ],
    },
    "sec": {
        "name": "SEC (Form 8-K)",
        "notifications": [
            {
                "entity": "SEC",
                "reference": "Item 1.05, Form 8-K",
                "deadline_hours": 96,  # 4 business days
                "deadline_description": "4 business days after determining materiality",
                "trigger": "Material cybersecurity incident",
                "required_content": [
                    "Nature and scope of the incident",
                    "Whether data was stolen, altered, or accessed",
                    "Effect on operations",
                    "Status of remediation",
                    "Material impact or reasonably likely material impact",
                ],
            },
        ],
    },
}


def calculate_deadlines(regulation, discovery_date_str):
    """Calculate notification deadlines for a regulation."""
    try:
        if "T" in discovery_date_str:
            discovery = datetime.fromisoformat(discovery_date_str.replace("Z", ""))
        else:
            discovery = datetime.strptime(discovery_date_str, "%Y-%m-%d")
    except ValueError:
        return {"error": f"Invalid date format: {discovery_date_str}. Use YYYY-MM-DD or YYYY-MM-DDTHH:MM:SS"}

    if regulation != "all" and regulation not in REGULATIONS:
        return {"error": f"Unknown regulation: {regulation}. Available: {list(REGULATIONS.keys())}"}

    regs_to_process = REGULATIONS if regulation == "all" else {regulation: REGULATIONS[regulation]}

    results = {
        "discovery_date": discovery.isoformat(),
        "deadlines": [],
    }

    for reg_key, reg_info in regs_to_process.items():
        for notif in reg_info["notifications"]:
            deadline_dt = None
            if notif["deadline_hours"]:
                deadline_dt = discovery + timedelta(hours=notif["deadline_hours"])

            results["deadlines"].append({
                "regulation": reg_info["name"],
                "entity": notif["entity"],
                "reference": notif["reference"],
                "deadline": deadline_dt.isoformat() if deadline_dt else "As soon as practicable",
                "deadline_description": notif["deadline_description"],
                "trigger": notif["trigger"],
                "required_content": notif["required_content"],
                "status": "PENDING",
            })

    # Sort by deadline (concrete deadlines first)
    results["deadlines"].sort(key=lambda x: x["deadline"] if x["deadline"] != "As soon as practicable" else "9999")

    return results


def main():
    parser = argparse.ArgumentParser(
        description="Calculate notification deadlines based on regulation and discovery date."
    )
    parser.add_argument(
        "--regulation",
        choices=list(REGULATIONS.keys()) + ["all"],
        default="gdpr",
        help="Regulation to calculate deadlines for (default: gdpr, use 'all' for all)",
    )
    parser.add_argument(
        "--discovery-date",
        required=True,
        help="Date of breach discovery (YYYY-MM-DD or YYYY-MM-DDTHH:MM:SS)",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Calculate deadlines for all regulations",
    )
    parser.add_argument(
        "--output",
        help="Output file path (default: stdout)",
    )

    args = parser.parse_args()

    regulation = "all" if args.all else args.regulation
    result = calculate_deadlines(regulation, args.discovery_date)
    output = json.dumps(result, indent=2)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Deadline calculations written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
