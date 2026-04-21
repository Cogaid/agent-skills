#!/usr/bin/env python3
"""Generate an NDA skeleton based on type, context, and jurisdiction.

Usage:
    python generate_nda.py --type mutual --context vendor --jurisdiction delaware
    python generate_nda.py --type unilateral --context employee --output nda.json
"""

import argparse
import json
import sys
from datetime import datetime

NDA_TYPES = {
    "unilateral": {
        "name": "Unilateral NDA",
        "description": "One party discloses, the other receives",
        "parties": ["Disclosing Party", "Receiving Party"],
    },
    "mutual": {
        "name": "Mutual (Bilateral) NDA",
        "description": "Both parties may disclose and receive",
        "parties": ["Party A (Disclosing/Receiving)", "Party B (Disclosing/Receiving)"],
    },
    "multilateral": {
        "name": "Multilateral NDA",
        "description": "Three or more parties share confidential information",
        "parties": ["Party A", "Party B", "Party C", "[Additional Parties]"],
    },
}

CONTEXTS = {
    "employee": {
        "name": "Employee",
        "recommended_term": "Duration of employment + 2 years",
        "survival_period": "2 years post-termination",
        "special_clauses": [
            "Work product assignment",
            "Non-solicitation (employees and customers)",
            "Prior inventions disclosure (Exhibit A)",
            "Exit obligations and return of materials",
            "Separation acknowledgment",
        ],
        "confidential_info_focus": [
            "Trade secrets and proprietary processes",
            "Source code and technical architecture",
            "Customer lists and pricing",
            "Business strategy and plans",
            "Employee and compensation data",
        ],
    },
    "vendor": {
        "name": "Vendor",
        "recommended_term": "Contract term + 1 year",
        "survival_period": "1-2 years post-termination",
        "special_clauses": [
            "Subcontractor flow-down requirements",
            "Data handling per Company policy (Exhibit B)",
            "Audit rights (annual, 30 days notice)",
            "Cyber liability insurance requirement",
            "Compliance with data protection regulations",
        ],
        "confidential_info_focus": [
            "Technical specifications and APIs",
            "System access credentials",
            "Business processes and workflows",
            "Pricing and contract terms",
            "Customer data (as processor)",
        ],
    },
    "partner": {
        "name": "Partner / Joint Venture",
        "recommended_term": "3-5 years",
        "survival_period": "3 years post-termination",
        "special_clauses": [
            "Joint IP ownership provisions",
            "Mutual non-solicitation",
            "Competing project restrictions",
            "Joint marketing approval rights",
        ],
        "confidential_info_focus": [
            "Joint product plans and roadmaps",
            "Shared customer data",
            "Financial projections",
            "Technology integration details",
            "Market strategy",
        ],
    },
    "investor": {
        "name": "Investor / Due Diligence",
        "recommended_term": "2-3 years",
        "survival_period": "2-3 years post-termination",
        "special_clauses": [
            "Portfolio company carve-out",
            "Investment decision use only",
            "Co-investor sharing permissions",
            "No trading restrictions (insider trading note)",
            "Standstill provision (optional)",
        ],
        "confidential_info_focus": [
            "Financial statements and projections",
            "Cap table and shareholder information",
            "Revenue metrics and unit economics",
            "Legal matters and liabilities",
            "Key contracts and customer agreements",
        ],
    },
    "ma": {
        "name": "M&A Due Diligence",
        "recommended_term": "2-3 years",
        "survival_period": "2-3 years post-termination",
        "special_clauses": [
            "Standstill provision",
            "Non-solicitation of employees",
            "No public disclosure of discussions",
            "Clean team provisions",
            "Return/destruction with certification",
        ],
        "confidential_info_focus": [
            "All business information",
            "Financial records and projections",
            "Legal proceedings and liabilities",
            "Employee and compensation details",
            "IP portfolio and pending patents",
            "Customer and supplier contracts",
        ],
    },
}

JURISDICTIONS = {
    "delaware": {"name": "Delaware", "governing_law": "State of Delaware", "courts": "Court of Chancery of the State of Delaware"},
    "new_york": {"name": "New York", "governing_law": "State of New York", "courts": "state and federal courts located in New York County"},
    "california": {"name": "California", "governing_law": "State of California", "courts": "state and federal courts located in San Francisco County", "notes": "Non-competes generally unenforceable"},
    "england": {"name": "England and Wales", "governing_law": "England and Wales", "courts": "courts of England and Wales"},
    "singapore": {"name": "Singapore", "governing_law": "Republic of Singapore", "courts": "courts of the Republic of Singapore"},
}


def generate_nda(nda_type, context, jurisdiction):
    """Generate an NDA skeleton."""
    type_info = NDA_TYPES.get(nda_type, NDA_TYPES["mutual"])
    ctx = CONTEXTS.get(context, CONTEXTS["vendor"])
    jur = JURISDICTIONS.get(jurisdiction, {"name": jurisdiction, "governing_law": jurisdiction, "courts": jurisdiction})

    nda = {
        "metadata": {
            "nda_type": type_info["name"],
            "context": ctx["name"],
            "jurisdiction": jur["name"],
            "generated_date": datetime.now().strftime("%Y-%m-%d"),
            "nda_id": f"NDA-{datetime.now().strftime('%Y')}-[NNN]",
            "status": "DRAFT - REQUIRES LEGAL REVIEW",
        },
        "parties": type_info["parties"],
        "terms": {
            "recommended_term": ctx["recommended_term"],
            "survival_period": ctx["survival_period"],
            "trade_secret_duration": "Indefinite (as long as information qualifies)",
        },
        "governing_law": {
            "law": jur["governing_law"],
            "courts": jur["courts"],
            "notes": jur.get("notes", ""),
        },
        "confidential_information_categories": ctx["confidential_info_focus"],
        "special_clauses": ctx["special_clauses"],
        "standard_sections": [
            "Definition of Confidential Information",
            "Exclusions from Confidential Information",
            "Obligations of Receiving Party",
            "Term and Duration",
            "Return or Destruction",
            "Remedies",
            "No License or Warranty",
            "Governing Law and Jurisdiction",
            "General Provisions",
            "Signatures",
        ],
        "standard_exclusions": [
            "Publicly available information",
            "Prior knowledge (documented)",
            "Independent development",
            "Third-party unrestricted disclosure",
            "Legal compulsion (with notice)",
        ],
    }

    return nda


def main():
    parser = argparse.ArgumentParser(
        description="Generate an NDA skeleton based on type, context, and jurisdiction."
    )
    parser.add_argument(
        "--type",
        choices=list(NDA_TYPES.keys()),
        default="mutual",
        help="NDA type (default: mutual)",
    )
    parser.add_argument(
        "--context",
        choices=list(CONTEXTS.keys()),
        default="vendor",
        help="Business context (default: vendor)",
    )
    parser.add_argument(
        "--jurisdiction",
        default="delaware",
        help="Governing law jurisdiction (default: delaware)",
    )
    parser.add_argument(
        "--output",
        help="Output file path (default: stdout)",
    )

    args = parser.parse_args()

    nda = generate_nda(nda_type=args.type, context=args.context, jurisdiction=args.jurisdiction)
    output = json.dumps(nda, indent=2)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"NDA skeleton written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
