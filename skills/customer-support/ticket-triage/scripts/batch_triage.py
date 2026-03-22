#!/usr/bin/env python3
"""
Process multiple tickets from CSV and output triage results.

Usage:
    python batch_triage.py tickets.csv
    python batch_triage.py tickets.csv --output triaged.csv
    python batch_triage.py tickets.csv --format json

Input CSV format:
    id,subject,body,customer_email,customer_tier

Output includes: priority, category, red_flags, routing suggestion
"""

import argparse
import csv
import json
import sys
from collections import Counter

# Import from sibling scripts
from analyze_ticket import analyze_ticket
from check_red_flags import detect_red_flags


def determine_routing(category: str, priority: str, tier: str, has_red_flags: bool) -> str:
    """Determine routing based on triage results."""
    # Critical red flags override everything
    if has_red_flags:
        return "escalation_team"

    # Enterprise customers get special routing
    if tier and tier.lower() == "enterprise":
        return "enterprise_support"

    # Route by category
    routing_map = {
        "billing": "billing_team",
        "bug": "tier2_support" if priority in ["p1_critical", "p2_high"] else "tier1_support",
        "performance": "tier2_support",
        "access": "tier1_support",
        "howto": "tier1_support",
        "feature_request": "product_team",
        "integration": "tier2_support"
    }

    return routing_map.get(category, "tier1_support")


def process_ticket(ticket: dict) -> dict:
    """Process a single ticket and return triage results."""
    # Combine subject and body for analysis
    full_text = f"{ticket.get('subject', '')} {ticket.get('body', '')}"

    # Analyze
    analysis = analyze_ticket(full_text)
    red_flags = detect_red_flags(full_text)

    # Determine priority (may be adjusted by tier)
    priority = analysis["priority"]["suggested"]
    tier = ticket.get("customer_tier", "")

    # Enterprise customers get priority boost
    if tier and tier.lower() == "enterprise" and priority in ["p3_normal", "p4_low"]:
        priority = "p2_high"

    # Determine routing
    category = analysis["category"]["primary"]
    routing = determine_routing(
        category,
        priority,
        tier,
        red_flags["has_red_flags"]
    )

    return {
        "id": ticket.get("id", ""),
        "priority": priority,
        "category": category,
        "category_secondary": analysis["category"].get("secondary", ""),
        "sentiment": analysis["sentiment"]["overall"],
        "has_red_flags": red_flags["has_red_flags"],
        "red_flag_severity": red_flags["overall_severity"],
        "routing": routing,
        "keywords": ",".join(analysis["keywords"][:5]),
        "requires_escalation": red_flags["immediate_escalation_required"]
    }


def generate_summary(results: list) -> dict:
    """Generate summary statistics from results."""
    total = len(results)

    priority_counts = Counter(r["priority"] for r in results)
    category_counts = Counter(r["category"] for r in results)
    routing_counts = Counter(r["routing"] for r in results)

    escalations = sum(1 for r in results if r["requires_escalation"])
    red_flags = sum(1 for r in results if r["has_red_flags"])

    return {
        "total_tickets": total,
        "priority_breakdown": dict(priority_counts),
        "category_breakdown": dict(category_counts),
        "routing_breakdown": dict(routing_counts),
        "tickets_with_red_flags": red_flags,
        "immediate_escalations_required": escalations,
        "critical_tickets": priority_counts.get("p1_critical", 0)
    }


def main():
    parser = argparse.ArgumentParser(description="Batch triage support tickets")
    parser.add_argument("input", help="Input CSV file")
    parser.add_argument("--output", "-o", help="Output file (default: stdout)")
    parser.add_argument("--format", "-f", choices=["csv", "json"],
                        default="csv", help="Output format")
    parser.add_argument("--summary", "-s", action="store_true",
                        help="Include summary statistics")

    args = parser.parse_args()

    # Read input CSV
    tickets = []
    with open(args.input, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        tickets = list(reader)

    if not tickets:
        print("No tickets found in input file", file=sys.stderr)
        sys.exit(1)

    # Process each ticket
    results = [process_ticket(t) for t in tickets]

    # Generate output
    if args.format == "json":
        output_data = {"results": results}
        if args.summary:
            output_data["summary"] = generate_summary(results)
        output = json.dumps(output_data, indent=2)
    else:
        # CSV output
        import io
        string_buffer = io.StringIO()
        fieldnames = [
            "id", "priority", "category", "category_secondary",
            "sentiment", "has_red_flags", "red_flag_severity",
            "routing", "keywords", "requires_escalation"
        ]
        writer = csv.DictWriter(string_buffer, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)
        output = string_buffer.getvalue()

    # Write output
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(output)
    else:
        print(output)

    # Print summary to stderr if requested
    if args.summary:
        summary = generate_summary(results)
        print("\n--- TRIAGE SUMMARY ---", file=sys.stderr)
        print(f"Total tickets: {summary['total_tickets']}", file=sys.stderr)
        print(f"P1 Critical: {summary['critical_tickets']}", file=sys.stderr)
        print(f"Red flags detected: {summary['tickets_with_red_flags']}", file=sys.stderr)
        print(f"Immediate escalations: {summary['immediate_escalations_required']}",
              file=sys.stderr)


if __name__ == "__main__":
    main()
