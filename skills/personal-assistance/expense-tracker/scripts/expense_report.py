#!/usr/bin/env python3
"""
Generate formatted expense reports.

Usage:
    python expense_report.py expenses.json
    python expense_report.py expenses.json --type travel
    python expense_report.py expenses.json --month 01 --year 2025

Output: Formatted expense reports for reimbursement
"""

import argparse
import json
from datetime import datetime
from collections import defaultdict


def load_expenses(file_path):
    """Load expenses from JSON file."""
    with open(file_path, 'r') as f:
        return json.load(f)


def filter_expenses(expenses, month=None, year=None, category=None, status=None):
    """Filter expenses by criteria."""

    result = expenses.copy()

    if year:
        result = [e for e in result if e.get("date", "").startswith(str(year))]

    if month:
        result = [e for e in result if e.get("date", "")[5:7] == month.zfill(2)]

    if category:
        result = [e for e in result if e.get("category") == category]

    if status:
        result = [e for e in result if e.get("status") == status]

    return result


def generate_standard_report(expenses, user_info=None):
    """Generate standard expense report."""

    if not expenses:
        return {"error": "No expenses to report"}

    user = user_info or {"name": "[Employee Name]", "department": "[Department]"}

    # Calculate totals
    total = sum(e.get("amount", 0) for e in expenses)
    reimbursable = sum(e.get("amount", 0) for e in expenses if e.get("reimbursable", True))

    # Group by category
    by_category = defaultdict(list)
    for e in expenses:
        by_category[e.get("category", "other")].append(e)

    # Date range
    dates = [e.get("date") for e in expenses if e.get("date")]
    date_range = (min(dates), max(dates)) if dates else (None, None)

    report = {
        "header": {
            "report_number": f"EXP-{datetime.now().strftime('%Y%m%d-%H%M')}",
            "employee": user.get("name"),
            "department": user.get("department"),
            "period_start": date_range[0],
            "period_end": date_range[1],
            "submission_date": datetime.now().strftime("%Y-%m-%d"),
            "total_amount": round(total, 2),
            "reimbursable_amount": round(reimbursable, 2)
        },
        "category_summary": {},
        "expenses_by_category": {},
        "documentation_checklist": [],
        "certification": {
            "text": "I certify that the above expenses were incurred for legitimate business purposes and that I have not been reimbursed for these expenses from any other source.",
            "signed": False,
            "date": None
        }
    }

    # Build category sections
    for cat, cat_expenses in by_category.items():
        cat_total = sum(e.get("amount", 0) for e in cat_expenses)
        report["category_summary"][cat] = round(cat_total, 2)
        report["expenses_by_category"][cat] = sorted(
            cat_expenses,
            key=lambda x: x.get("date", "")
        )

    # Check documentation
    missing_receipts = [e for e in expenses if not e.get("receipt_attached", False)]
    if missing_receipts:
        report["documentation_checklist"].append({
            "item": "Missing receipts",
            "count": len(missing_receipts),
            "expense_ids": [e["id"] for e in missing_receipts]
        })

    # Check for meals without attendees
    meals_no_attendees = [
        e for e in expenses
        if e.get("category") == "meals" and not e.get("attendees")
    ]
    if meals_no_attendees:
        report["documentation_checklist"].append({
            "item": "Meals missing attendees",
            "count": len(meals_no_attendees),
            "expense_ids": [e["id"] for e in meals_no_attendees]
        })

    return report


def generate_travel_report(expenses, trip_info=None):
    """Generate travel expense report."""

    travel_expenses = [e for e in expenses if e.get("category") in ["travel", "meals", "other"]]

    if not travel_expenses:
        return {"error": "No travel expenses found"}

    trip = trip_info or {
        "destination": "[Destination]",
        "purpose": "[Business Purpose]",
        "departure": None,
        "return": None
    }

    # Categorize travel expenses
    categories = {
        "airfare": [],
        "lodging": [],
        "ground_transport": [],
        "meals": [],
        "other": []
    }

    for e in travel_expenses:
        desc_lower = e.get("description", "").lower()
        if any(word in desc_lower for word in ["flight", "airfare", "airline"]):
            categories["airfare"].append(e)
        elif any(word in desc_lower for word in ["hotel", "lodging", "accommodation"]):
            categories["lodging"].append(e)
        elif any(word in desc_lower for word in ["taxi", "uber", "lyft", "rental", "parking", "train"]):
            categories["ground_transport"].append(e)
        elif e.get("category") == "meals":
            categories["meals"].append(e)
        else:
            categories["other"].append(e)

    # Calculate totals
    totals = {}
    for cat, items in categories.items():
        totals[cat] = round(sum(e.get("amount", 0) for e in items), 2)

    grand_total = sum(totals.values())

    report = {
        "type": "travel",
        "header": {
            "report_number": f"TRV-{datetime.now().strftime('%Y%m%d-%H%M')}",
            "destination": trip.get("destination"),
            "purpose": trip.get("purpose"),
            "departure_date": trip.get("departure"),
            "return_date": trip.get("return"),
            "submission_date": datetime.now().strftime("%Y-%m-%d")
        },
        "summary": {
            "airfare": totals["airfare"],
            "lodging": totals["lodging"],
            "ground_transport": totals["ground_transport"],
            "meals": totals["meals"],
            "other": totals["other"],
            "total": round(grand_total, 2)
        },
        "details": categories
    }

    return report


def generate_monthly_report(expenses, month, year):
    """Generate monthly expense summary."""

    filtered = filter_expenses(expenses, month=month, year=year)

    if not filtered:
        return {"error": f"No expenses found for {month}/{year}"}

    # Daily breakdown
    by_day = defaultdict(lambda: {"expenses": [], "total": 0})
    for e in filtered:
        day = e.get("date")
        by_day[day]["expenses"].append(e)
        by_day[day]["total"] += e.get("amount", 0)

    # Category breakdown
    by_category = defaultdict(float)
    for e in filtered:
        by_category[e.get("category", "other")] += e.get("amount", 0)

    # Payment method breakdown
    by_payment = defaultdict(float)
    for e in filtered:
        by_payment[e.get("payment_method", "other")] += e.get("amount", 0)

    total = sum(e.get("amount", 0) for e in filtered)

    return {
        "type": "monthly",
        "month": f"{year}-{month.zfill(2)}",
        "total_expenses": len(filtered),
        "total_amount": round(total, 2),
        "by_category": {k: round(v, 2) for k, v in by_category.items()},
        "by_payment_method": {k: round(v, 2) for k, v in by_payment.items()},
        "daily_summary": {
            k: {"count": len(v["expenses"]), "total": round(v["total"], 2)}
            for k, v in sorted(by_day.items())
        }
    }


def format_report(report, output_format="text"):
    """Format report for output."""

    if output_format == "json":
        return json.dumps(report, indent=2)

    elif output_format == "text":
        lines = []

        if report.get("type") == "travel":
            lines.append("\n" + "=" * 70)
            lines.append("TRAVEL EXPENSE REPORT")
            lines.append("=" * 70)

            h = report["header"]
            lines.append(f"\nReport #: {h['report_number']}")
            lines.append(f"Destination: {h['destination']}")
            lines.append(f"Purpose: {h['purpose']}")
            lines.append(f"Travel Dates: {h['departure_date']} to {h['return_date']}")

            lines.append("\n--- EXPENSE SUMMARY ---")
            s = report["summary"]
            lines.append(f"  Airfare:          ${s['airfare']:>10,.2f}")
            lines.append(f"  Lodging:          ${s['lodging']:>10,.2f}")
            lines.append(f"  Ground Transport: ${s['ground_transport']:>10,.2f}")
            lines.append(f"  Meals:            ${s['meals']:>10,.2f}")
            lines.append(f"  Other:            ${s['other']:>10,.2f}")
            lines.append(f"  {'─' * 30}")
            lines.append(f"  TOTAL:            ${s['total']:>10,.2f}")

        elif report.get("type") == "monthly":
            lines.append("\n" + "=" * 70)
            lines.append(f"MONTHLY EXPENSE REPORT - {report['month']}")
            lines.append("=" * 70)

            lines.append(f"\nTotal Expenses: {report['total_expenses']}")
            lines.append(f"Total Amount: ${report['total_amount']:,.2f}")

            lines.append("\n--- BY CATEGORY ---")
            for cat, amount in sorted(report["by_category"].items(), key=lambda x: -x[1]):
                lines.append(f"  {cat}: ${amount:,.2f}")

            lines.append("\n--- BY PAYMENT METHOD ---")
            for method, amount in report["by_payment_method"].items():
                lines.append(f"  {method}: ${amount:,.2f}")

        else:  # Standard report
            lines.append("\n" + "=" * 70)
            lines.append("EXPENSE REPORT")
            lines.append("=" * 70)

            h = report.get("header", {})
            lines.append(f"\nReport #: {h.get('report_number', 'N/A')}")
            lines.append(f"Employee: {h.get('employee', 'N/A')}")
            lines.append(f"Department: {h.get('department', 'N/A')}")
            lines.append(f"Period: {h.get('period_start')} to {h.get('period_end')}")
            lines.append(f"\nTotal Amount: ${h.get('total_amount', 0):,.2f}")
            lines.append(f"Reimbursable: ${h.get('reimbursable_amount', 0):,.2f}")

            lines.append("\n--- CATEGORY SUMMARY ---")
            for cat, amount in sorted(report.get("category_summary", {}).items(), key=lambda x: -x[1]):
                lines.append(f"  {cat}: ${amount:,.2f}")

            lines.append("\n--- EXPENSE DETAILS ---")
            for cat, expenses in report.get("expenses_by_category", {}).items():
                lines.append(f"\n{cat.upper()}:")
                for e in expenses:
                    receipt = "✓" if e.get("receipt_attached") else "✗"
                    lines.append(f"  [{receipt}] {e['date']} | ${e['amount']:.2f} | {e['description']}")

            if report.get("documentation_checklist"):
                lines.append("\n--- DOCUMENTATION ISSUES ---")
                for issue in report["documentation_checklist"]:
                    lines.append(f"  ⚠ {issue['item']}: {issue['count']} items")

        lines.append("\n" + "=" * 70)
        return "\n".join(lines)

    elif output_format == "markdown":
        lines = []

        if report.get("type") == "monthly":
            lines.append(f"# Monthly Expense Report - {report['month']}")
            lines.append(f"\n**Total Expenses:** {report['total_expenses']}")
            lines.append(f"**Total Amount:** ${report['total_amount']:,.2f}")

            lines.append("\n## By Category")
            lines.append("| Category | Amount |")
            lines.append("|----------|--------|")
            for cat, amount in sorted(report["by_category"].items(), key=lambda x: -x[1]):
                lines.append(f"| {cat} | ${amount:,.2f} |")

        else:
            h = report.get("header", {})
            lines.append(f"# Expense Report: {h.get('report_number', 'N/A')}")
            lines.append(f"\n**Employee:** {h.get('employee', 'N/A')}")
            lines.append(f"**Period:** {h.get('period_start')} to {h.get('period_end')}")
            lines.append(f"**Total:** ${h.get('total_amount', 0):,.2f}")

            lines.append("\n## Summary")
            lines.append("| Category | Amount |")
            lines.append("|----------|--------|")
            for cat, amount in report.get("category_summary", {}).items():
                lines.append(f"| {cat} | ${amount:,.2f} |")

            lines.append("\n## Details")
            for cat, expenses in report.get("expenses_by_category", {}).items():
                lines.append(f"\n### {cat.title()}")
                lines.append("| Date | Amount | Description | Receipt |")
                lines.append("|------|--------|-------------|---------|")
                for e in expenses:
                    receipt = "Yes" if e.get("receipt_attached") else "No"
                    lines.append(f"| {e['date']} | ${e['amount']:.2f} | {e['description']} | {receipt} |")

        return "\n".join(lines)

    return json.dumps(report, indent=2)


def main():
    parser = argparse.ArgumentParser(description='Generate expense reports')
    parser.add_argument('file', help='Expense data file (JSON)')
    parser.add_argument('--type', '-t', choices=['standard', 'travel', 'monthly'],
                        default='standard', help='Report type')
    parser.add_argument('--month', '-m', help='Month (01-12)')
    parser.add_argument('--year', '-y', default=str(datetime.now().year),
                        help='Year')
    parser.add_argument('--category', '-c', help='Filter by category')
    parser.add_argument('--format', '-f', choices=['json', 'text', 'markdown'],
                        default='text', help='Output format')
    parser.add_argument('--destination', '-d', help='Trip destination (for travel reports)')
    parser.add_argument('--purpose', '-p', help='Trip purpose (for travel reports)')

    args = parser.parse_args()

    try:
        data = load_expenses(args.file)
    except FileNotFoundError:
        print(f"Error: File not found: {args.file}")
        return

    expenses = data.get("expenses", [])
    user_info = {"name": data.get("user", "[Employee]"), "department": "[Department]"}

    # Apply filters
    if args.category:
        expenses = filter_expenses(expenses, category=args.category)

    # Generate appropriate report
    if args.type == "travel":
        trip_info = {
            "destination": args.destination or "[Destination]",
            "purpose": args.purpose or "[Business Purpose]"
        }
        report = generate_travel_report(expenses, trip_info)

    elif args.type == "monthly":
        month = args.month or datetime.now().strftime("%m")
        report = generate_monthly_report(expenses, month, args.year)

    else:
        report = generate_standard_report(expenses, user_info)

    print(format_report(report, args.format))


if __name__ == '__main__':
    main()
