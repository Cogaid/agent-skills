#!/usr/bin/env python3
"""Browse and retrieve NDA clauses from a clause library.

Usage:
    python nda_clauses.py --list-all
    python nda_clauses.py --category employee --clause non-solicitation
    python nda_clauses.py --category investor --output clauses.json
"""

import argparse
import json
import sys

CLAUSE_LIBRARY = {
    "standard": {
        "confidential_information_definition": {
            "name": "Confidential Information Definition",
            "text": (
                '"Confidential Information" means any information disclosed by either party '
                '("Disclosing Party") to the other ("Receiving Party"), whether orally, in writing, '
                "electronically, or by inspection, that is designated as confidential or that a "
                "reasonable person would understand to be confidential given the nature of the "
                "information and circumstances of disclosure."
            ),
            "notes": "Broad but bounded; includes reasonable person standard",
        },
        "standard_exclusions": {
            "name": "Standard Exclusions",
            "text": (
                "Confidential Information does not include information that: "
                "(a) is or becomes publicly available through no fault of the Receiving Party; "
                "(b) was known to the Receiving Party prior to disclosure, as documented by written records; "
                "(c) is independently developed by the Receiving Party without use of Confidential Information; "
                "(d) is disclosed to the Receiving Party by a third party without restriction; "
                "(e) is required to be disclosed by law, regulation, or court order, provided the Receiving Party "
                "gives prompt notice and cooperates to obtain protective orders."
            ),
            "notes": "All five exclusions are standard and expected in any NDA",
        },
        "injunctive_relief": {
            "name": "Injunctive Relief",
            "text": (
                "The parties acknowledge that breach may cause irreparable harm not adequately compensated "
                "by monetary damages. The Disclosing Party shall be entitled to seek injunctive relief, "
                "including temporary restraining orders and preliminary injunctions, without posting bond, "
                "in addition to all other remedies available at law or in equity."
            ),
            "notes": "Essential for enforcement; bond waiver strengthens clause",
        },
    },
    "employee": {
        "work_product_assignment": {
            "name": "Work Product Assignment",
            "text": (
                "All inventions, discoveries, works of authorship, designs, improvements, and other "
                "intellectual property ('Work Product') created by Employee during employment and relating "
                "to the Company's business or created using Company resources are the exclusive property of "
                "the Company. Employee hereby assigns all rights, title, and interest in such Work Product "
                "to the Company."
            ),
            "notes": "Ensure compliance with state-specific invention assignment laws (e.g., CA Labor Code 2870)",
        },
        "non_solicitation": {
            "name": "Non-Solicitation (Employees and Customers)",
            "text": (
                "For [12] months following termination, Employee shall not: "
                "(a) directly or indirectly solicit, recruit, or hire any employee or contractor of the Company "
                "with whom Employee had material contact during the last 12 months of employment; "
                "(b) solicit business from any customer or client of the Company with whom Employee had "
                "material contact during the last 12 months of employment."
            ),
            "notes": "Duration and scope should be reasonable for jurisdiction",
        },
        "exit_obligations": {
            "name": "Exit Obligations",
            "text": (
                "Upon termination of employment, Employee shall: "
                "(a) return all Company property, documents, devices, and materials; "
                "(b) delete all Company data from personal devices and accounts; "
                "(c) provide written certification of return and deletion; "
                "(d) participate in an exit interview; "
                "(e) sign a separation acknowledgment confirming understanding of post-employment obligations."
            ),
            "notes": "Include BYOD policy compliance if applicable",
        },
    },
    "investor": {
        "portfolio_carveout": {
            "name": "Portfolio Company Carve-Out",
            "text": (
                "Investor's confidentiality obligations do not prevent sharing Confidential Information "
                "with portfolio companies, provided: (a) such companies are bound by similar confidentiality "
                "obligations; (b) the information is not shared with direct competitors of the Company; "
                "and (c) Investor remains responsible for any breach by such portfolio companies."
            ),
            "notes": "Common in VC/PE NDAs; define 'direct competitor' carefully",
        },
        "investment_use_only": {
            "name": "Investment Decision Use Only",
            "text": (
                "Investor may use Confidential Information solely to evaluate a potential investment in the "
                "Company and shall not use such information for any trading purpose or for the benefit of "
                "any other investment or business activity."
            ),
            "notes": "Include insider trading acknowledgment if company is public or pre-IPO",
        },
        "coinvestor_sharing": {
            "name": "Co-Investor Sharing",
            "text": (
                "Investor may share Confidential Information with potential co-investors for the purpose of "
                "evaluating a joint investment, subject to each co-investor's execution of a substantially "
                "similar non-disclosure agreement prior to receiving any Confidential Information."
            ),
            "notes": "Require NDA execution before sharing, not just agreement to terms",
        },
    },
    "vendor": {
        "subcontractor_flowdown": {
            "name": "Subcontractor Flow-Down",
            "text": (
                "Vendor shall ensure all subcontractors with access to Confidential Information are bound "
                "by written confidentiality obligations at least as protective as this Agreement. Vendor "
                "shall provide a list of approved subcontractors upon request and remains fully responsible "
                "for any breach by its subcontractors."
            ),
            "notes": "Essential for vendor NDAs; align with data processing requirements",
        },
        "audit_rights": {
            "name": "Audit Rights",
            "text": (
                "Company may audit Vendor's compliance with this Agreement upon [30] days written notice, "
                "no more than once per year during the term. Vendor shall cooperate with such audits and "
                "provide reasonable access to relevant records, systems, and personnel."
            ),
            "notes": "Annual limit with notice period is standard; more frequent for high-risk vendors",
        },
    },
    "ma": {
        "standstill": {
            "name": "Standstill Provision",
            "text": (
                "For [12] months from the Effective Date, without prior written consent, Receiving Party "
                "shall not: (a) acquire or propose to acquire any securities or assets of the Company; "
                "(b) propose any merger, business combination, or similar transaction; "
                "(c) make any public announcement regarding any of the foregoing; "
                "(d) form or participate in any group with respect to the Company's securities."
            ),
            "notes": "Standard in M&A NDAs; duration typically 12-18 months",
        },
    },
}


def list_all_clauses():
    """List all available clauses."""
    result = {}
    for category, clauses in CLAUSE_LIBRARY.items():
        result[category] = [{"id": cid, "name": c["name"]} for cid, c in clauses.items()]
    return result


def get_clauses(category, clause=None):
    """Get clauses by category and optionally by specific clause ID."""
    if category not in CLAUSE_LIBRARY:
        return {"error": f"Unknown category: {category}. Available: {list(CLAUSE_LIBRARY.keys())}"}

    if clause:
        clause_key = clause.replace("-", "_")
        if clause_key in CLAUSE_LIBRARY[category]:
            return CLAUSE_LIBRARY[category][clause_key]
        return {"error": f"Clause '{clause}' not found in category '{category}'. Available: {list(CLAUSE_LIBRARY[category].keys())}"}

    return CLAUSE_LIBRARY[category]


def main():
    parser = argparse.ArgumentParser(description="Browse and retrieve NDA clauses from the clause library.")
    parser.add_argument("--list-all", action="store_true", help="List all available clauses")
    parser.add_argument("--category", help="Clause category: standard, employee, investor, vendor, ma")
    parser.add_argument("--clause", help="Specific clause identifier within the category")
    parser.add_argument("--output", help="Output file path (default: stdout)")

    args = parser.parse_args()

    if args.list_all:
        result = list_all_clauses()
    elif args.category:
        result = get_clauses(args.category, args.clause)
    else:
        parser.print_help()
        sys.exit(1)

    output = json.dumps(result, indent=2)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Clauses written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
