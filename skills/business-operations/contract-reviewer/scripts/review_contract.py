#!/usr/bin/env python3
"""
Automated contract clause extraction and risk flagging.

Usage:
    python review_contract.py --file contract.pdf --type msa
    python review_contract.py --type nda --demo
    python review_contract.py --type saas --demo --format json
"""

import argparse
import json
from datetime import datetime

# Sample contract clause data for demonstration
SAMPLE_CONTRACTS = {
    "msa": {
        "title": "Master Services Agreement",
        "parties": ["Your Company, Inc.", "Acme Corporation"],
        "effective_date": "2026-04-01",
        "term": "2 years with auto-renewal",
        "clauses": [
            {"section": "Liability Cap", "risk": 4, "finding": "Liability capped at fees paid in prior 3 months. Industry standard is 12 months.", "recommendation": "Negotiate to 12 months of fees paid"},
            {"section": "Indemnification", "risk": 3, "finding": "Mutual indemnification but broad scope includes 'related to' language.", "recommendation": "Narrow to 'arising from breach of this Agreement'"},
            {"section": "IP Ownership", "risk": 5, "finding": "'All work product' assigned to client including pre-existing IP and tools.", "recommendation": "Carve out pre-existing IP, tools, and general know-how"},
            {"section": "Termination", "risk": 3, "finding": "60-day notice for convenience, 30-day cure for cause. Reasonable.", "recommendation": "Reduce convenience notice to 30 days"},
            {"section": "Confidentiality", "risk": 2, "finding": "Mutual NDA with 3-year term. Standard exclusions present.", "recommendation": "Acceptable as-is"},
            {"section": "Data Privacy", "risk": 3, "finding": "References GDPR but no DPA attached. No data deletion timeline.", "recommendation": "Attach DPA, add 30-day deletion requirement"},
            {"section": "Non-Compete", "risk": 4, "finding": "12-month non-compete with no geographic limitation.", "recommendation": "Limit to specific client accounts for 6 months"},
            {"section": "Auto-Renewal", "risk": 3, "finding": "Auto-renews for successive 1-year terms with 90-day cancellation notice.", "recommendation": "Reduce notice to 30 days, calendar the deadline"},
            {"section": "Payment Terms", "risk": 2, "finding": "Net 30 with 1.5% monthly late fee. Standard.", "recommendation": "Acceptable"},
            {"section": "Governing Law", "risk": 2, "finding": "Delaware law, Delaware courts. Neutral jurisdiction.", "recommendation": "Acceptable"},
            {"section": "Force Majeure", "risk": 1, "finding": "Standard force majeure with pandemic included. Mutual.", "recommendation": "Acceptable"},
            {"section": "Insurance", "risk": 2, "finding": "$2M general liability, $1M professional liability required.", "recommendation": "Verify current coverage meets requirements"},
        ],
    },
    "nda": {
        "title": "Non-Disclosure Agreement",
        "parties": ["Your Company, Inc.", "Partner Corp"],
        "effective_date": "2026-04-15",
        "term": "3 years",
        "clauses": [
            {"section": "Scope", "risk": 3, "finding": "Unilateral - only protects discloser's information.", "recommendation": "Make mutual if both parties sharing info"},
            {"section": "Definition", "risk": 2, "finding": "Broad definition but includes standard exclusions.", "recommendation": "Acceptable"},
            {"section": "Permitted Use", "risk": 2, "finding": "Limited to evaluating potential business relationship.", "recommendation": "Acceptable"},
            {"section": "Duration", "risk": 2, "finding": "3-year obligation. Trade secrets protected indefinitely.", "recommendation": "Acceptable"},
            {"section": "Return/Destruction", "risk": 3, "finding": "Must return or destroy on request, but no certification required.", "recommendation": "Add written certification of destruction"},
            {"section": "Remedies", "risk": 2, "finding": "Injunctive relief available. Standard.", "recommendation": "Acceptable"},
        ],
    },
    "saas": {
        "title": "SaaS Subscription Agreement",
        "parties": ["Your Company, Inc.", "CloudTool Inc."],
        "effective_date": "2026-05-01",
        "term": "1 year with auto-renewal",
        "clauses": [
            {"section": "License Grant", "risk": 2, "finding": "Non-exclusive, non-transferable SaaS license. Standard.", "recommendation": "Acceptable"},
            {"section": "Usage Limits", "risk": 3, "finding": "50 seats, overage billed at 150% of per-seat rate.", "recommendation": "Negotiate overage to 100% or add buffer seats"},
            {"section": "Data Ownership", "risk": 4, "finding": "Ambiguous: vendor claims right to use 'service data' for improvements.", "recommendation": "Clarify that customer data remains customer's; limit to anonymized/aggregated"},
            {"section": "SLA", "risk": 3, "finding": "99.5% uptime SLA with service credits only (max 10% of monthly fees).", "recommendation": "Push for 99.9% with meaningful credits or termination right"},
            {"section": "Data Portability", "risk": 4, "finding": "No data export provision. API access is read-only.", "recommendation": "Add right to full data export in standard format within 30 days of termination"},
            {"section": "Price Escalation", "risk": 3, "finding": "Vendor may increase price up to 10% on renewal with 30 days notice.", "recommendation": "Cap at CPI or 5%, with 60 days notice"},
            {"section": "Termination", "risk": 4, "finding": "No termination for convenience. Locked in for full term.", "recommendation": "Add 30-day termination for convenience with prorated refund"},
            {"section": "Security", "risk": 2, "finding": "SOC 2 Type II certified. Encryption at rest and in transit.", "recommendation": "Acceptable. Request annual audit report."},
        ],
    },
}


def compute_risk_score(clauses):
    """Compute weighted risk score."""
    weights = {
        "Liability Cap": 3, "Indemnification": 3, "IP Ownership": 3,
        "Termination": 2, "Confidentiality": 2, "Data Privacy": 2,
        "Data Ownership": 3, "Data Portability": 2, "SLA": 2,
        "Payment Terms": 1, "Non-Compete": 2, "Governing Law": 1,
        "Auto-Renewal": 1, "Price Escalation": 1, "Security": 2,
        "Usage Limits": 1, "License Grant": 1, "Force Majeure": 1,
        "Insurance": 1, "Scope": 2, "Definition": 1, "Permitted Use": 1,
        "Duration": 1, "Return/Destruction": 1, "Remedies": 1,
    }

    total_weighted = 0
    total_max = 0
    for clause in clauses:
        w = weights.get(clause["section"], 1)
        total_weighted += clause["risk"] * w
        total_max += 5 * w

    score = round((total_weighted / total_max) * 100) if total_max else 0
    return score


def get_recommendation(score):
    if score <= 35:
        return "Sign - Low risk, proceed with minor edits"
    elif score <= 55:
        return "Sign with Changes - Moderate risk, negotiate flagged items"
    elif score <= 75:
        return "Renegotiate - High risk, significant changes needed"
    else:
        return "Walk Away - Critical risk, terms are unacceptable"


def print_review(contract):
    """Print formatted contract review."""
    score = compute_risk_score(contract["clauses"])
    rec = get_recommendation(score)

    print("=" * 75)
    print(f"  CONTRACT REVIEW REPORT")
    print(f"  Generated: {datetime.now().strftime('%Y-%m-%d')}")
    print("=" * 75)
    print(f"  Contract:       {contract['title']}")
    print(f"  Parties:        {' and '.join(contract['parties'])}")
    print(f"  Effective Date: {contract['effective_date']}")
    print(f"  Term:           {contract['term']}")
    print(f"\n  RISK SCORE:     {score}/100")
    print(f"  RECOMMENDATION: {rec}")
    print("=" * 75)

    print(f"\n  {'Section':<22} {'Risk':>6} {'Finding'}")
    print(f"  {'─'*22} {'─'*6} {'─'*45}")

    for clause in sorted(contract["clauses"], key=lambda c: c["risk"], reverse=True):
        risk_label = {1: "Low", 2: "Low", 3: "Med", 4: "High", 5: "CRIT"}[clause["risk"]]
        print(f"  {clause['section']:<22} {risk_label:>6} {clause['finding'][:50]}")

    # High risk items detail
    high_risk = [c for c in contract["clauses"] if c["risk"] >= 4]
    if high_risk:
        print(f"\n  CRITICAL / HIGH RISK ITEMS:")
        print(f"  {'─'*70}")
        for c in high_risk:
            print(f"\n  {c['section']} (Risk: {c['risk']}/5)")
            print(f"    Finding:        {c['finding']}")
            print(f"    Recommendation: {c['recommendation']}")

    # Action items
    actionable = [c for c in contract["clauses"] if c["risk"] >= 3]
    if actionable:
        print(f"\n  REQUIRED CHANGES BEFORE SIGNING:")
        print(f"  {'─'*70}")
        for i, c in enumerate(actionable, 1):
            print(f"  {i}. {c['section']}: {c['recommendation']}")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Contract clause extraction and risk flagging.",
    )
    parser.add_argument("--file", default=None, help="Contract file path (PDF, DOCX)")
    parser.add_argument("--type", required=True, choices=["msa", "nda", "saas", "sow", "vendor"],
                        help="Contract type")
    parser.add_argument("--demo", action="store_true", help="Use sample data for demonstration")
    parser.add_argument("--format", choices=["text", "json"], default="text")

    args = parser.parse_args()

    if not args.demo and not args.file:
        parser.error("Provide --file with a contract path, or use --demo for sample data")

    contract_type = args.type if args.type in SAMPLE_CONTRACTS else "msa"
    contract = SAMPLE_CONTRACTS[contract_type]

    if args.format == "json":
        score = compute_risk_score(contract["clauses"])
        result = {
            **contract,
            "risk_score": score,
            "recommendation": get_recommendation(score),
            "high_risk_count": sum(1 for c in contract["clauses"] if c["risk"] >= 4),
            "review_date": datetime.now().strftime("%Y-%m-%d"),
        }
        print(json.dumps(result, indent=2))
    else:
        print_review(contract)


if __name__ == "__main__":
    main()
