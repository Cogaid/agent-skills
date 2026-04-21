#!/usr/bin/env python3
"""
Compare two contract versions to identify changes and risk impact.

Usage:
    python compare_contracts.py --original v1.pdf --revised v2.pdf
    python compare_contracts.py --demo --format json
"""

import argparse
import json
from datetime import datetime

# Sample comparison data
SAMPLE_COMPARISON = {
    "original": {"version": "v1", "date": "2026-03-01"},
    "revised": {"version": "v2", "date": "2026-04-10"},
    "changes": [
        {
            "section": "Liability Cap",
            "original": "Total liability shall not exceed fees paid in the prior 3 months.",
            "revised": "Total liability shall not exceed fees paid in the prior 12 months.",
            "change_type": "improved",
            "risk_impact": -2,
            "notes": "Increased cap from 3 to 12 months. Now at industry standard.",
        },
        {
            "section": "IP Ownership",
            "original": "All work product and deliverables are assigned to Client.",
            "revised": "Deliverables are assigned to Client. Provider retains ownership of pre-existing IP and general tools/methods, with a license granted to Client for use in deliverables.",
            "change_type": "improved",
            "risk_impact": -3,
            "notes": "Pre-existing IP carve-out added. Critical improvement.",
        },
        {
            "section": "Termination",
            "original": "Either party may terminate for convenience with 60 days written notice.",
            "revised": "Either party may terminate for convenience with 30 days written notice.",
            "change_type": "improved",
            "risk_impact": -1,
            "notes": "Notice period reduced from 60 to 30 days.",
        },
        {
            "section": "Non-Compete",
            "original": "Provider shall not provide services to Client's competitors for 12 months.",
            "revised": "Provider shall not provide substantially similar services to the specific accounts listed in Exhibit B for 6 months.",
            "change_type": "improved",
            "risk_impact": -2,
            "notes": "Narrowed from all competitors to specific accounts, and reduced to 6 months.",
        },
        {
            "section": "Auto-Renewal",
            "original": "Agreement auto-renews for successive 1-year terms. 90 days notice to cancel.",
            "revised": "Agreement auto-renews for successive 1-year terms. 90 days notice to cancel.",
            "change_type": "unchanged",
            "risk_impact": 0,
            "notes": "No change. Still recommended to reduce to 30 days.",
        },
        {
            "section": "Data Privacy",
            "original": "Provider shall comply with applicable data protection laws.",
            "revised": "Provider shall comply with applicable data protection laws. DPA attached as Exhibit C. Provider shall delete all Customer data within 30 days of termination.",
            "change_type": "improved",
            "risk_impact": -2,
            "notes": "DPA added and deletion timeline specified. Good improvement.",
        },
        {
            "section": "Payment Terms",
            "original": "Net 30. Late fee of 1.5% monthly.",
            "revised": "Net 30. Late fee of 1.5% monthly. Early payment discount: 2% if paid within 10 days.",
            "change_type": "new_addition",
            "risk_impact": -1,
            "notes": "Early payment discount added. Favorable for cash flow management.",
        },
        {
            "section": "Insurance",
            "original": "$2M general liability, $1M professional liability.",
            "revised": "$2M general liability, $2M professional liability, $5M cyber liability.",
            "change_type": "changed",
            "risk_impact": -1,
            "notes": "Increased professional liability and added cyber coverage. More protection.",
        },
    ],
}


def print_comparison(comparison):
    """Print formatted contract comparison."""
    print("=" * 80)
    print(f"  CONTRACT COMPARISON REPORT")
    print(f"  Original: {comparison['original']['version']} ({comparison['original']['date']})")
    print(f"  Revised:  {comparison['revised']['version']} ({comparison['revised']['date']})")
    print(f"  Generated: {datetime.now().strftime('%Y-%m-%d')}")
    print("=" * 80)

    # Summary
    improved = sum(1 for c in comparison["changes"] if c["change_type"] == "improved")
    unchanged = sum(1 for c in comparison["changes"] if c["change_type"] == "unchanged")
    worsened = sum(1 for c in comparison["changes"] if c["change_type"] == "worsened")
    new_add = sum(1 for c in comparison["changes"] if c["change_type"] == "new_addition")
    total_impact = sum(c["risk_impact"] for c in comparison["changes"])

    print(f"\n  SUMMARY:")
    print(f"    Sections improved:   {improved}")
    print(f"    Sections unchanged:  {unchanged}")
    print(f"    Sections worsened:   {worsened}")
    print(f"    New additions:       {new_add}")
    print(f"    Net risk impact:     {total_impact:+d} ({'Lower risk' if total_impact < 0 else 'Higher risk' if total_impact > 0 else 'No change'})")

    # Detailed changes
    print(f"\n  DETAILED CHANGES:")
    print(f"  {'─'*76}")

    type_labels = {"improved": "IMPROVED", "worsened": "WORSENED", "unchanged": "UNCHANGED",
                   "new_addition": "NEW", "changed": "CHANGED"}

    for change in comparison["changes"]:
        label = type_labels.get(change["change_type"], "CHANGED")
        impact = f"Risk: {change['risk_impact']:+d}" if change["risk_impact"] != 0 else "No impact"
        print(f"\n  [{label}] {change['section']} ({impact})")
        if change["change_type"] != "unchanged":
            print(f"    Was: {change['original'][:70]}")
            print(f"    Now: {change['revised'][:70]}")
        print(f"    Note: {change['notes']}")

    # Remaining concerns
    still_open = [c for c in comparison["changes"] if c["change_type"] == "unchanged" and c["risk_impact"] == 0]
    if still_open:
        print(f"\n  STILL OPEN (no change in v2):")
        print(f"  {'─'*76}")
        for c in still_open:
            print(f"    - {c['section']}: {c['notes']}")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Compare two contract versions and assess risk impact.",
    )
    parser.add_argument("--original", default=None, help="Original contract file")
    parser.add_argument("--revised", default=None, help="Revised contract file")
    parser.add_argument("--demo", action="store_true", help="Use sample data")
    parser.add_argument("--format", choices=["text", "json"], default="text")

    args = parser.parse_args()
    if not args.demo and (not args.original or not args.revised):
        parser.error("Provide --original and --revised, or use --demo")

    comparison = SAMPLE_COMPARISON

    if args.format == "json":
        total_impact = sum(c["risk_impact"] for c in comparison["changes"])
        result = {
            **comparison,
            "net_risk_impact": total_impact,
            "changes_count": len(comparison["changes"]),
            "improved_count": sum(1 for c in comparison["changes"] if c["change_type"] == "improved"),
            "generated": datetime.now().strftime("%Y-%m-%d"),
        }
        print(json.dumps(result, indent=2))
    else:
        print_comparison(comparison)


if __name__ == "__main__":
    main()
