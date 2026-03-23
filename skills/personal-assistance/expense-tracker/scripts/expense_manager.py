#!/usr/bin/env python3
"""
Track and categorize expenses.

Usage:
    python expense_manager.py --add
    python expense_manager.py --list expenses.json
    python expense_manager.py --summary expenses.json --month 01

Output: Expense tracking and categorization
"""

import argparse
import json
from datetime import datetime
from collections import defaultdict


# Expense categories
CATEGORIES = [
    "travel",
    "meals",
    "office",
    "software",
    "professional",
    "equipment",
    "utilities",
    "marketing",
    "other"
]

# Payment methods
PAYMENT_METHODS = [
    "corporate_card",
    "personal_card",
    "cash",
    "bank_transfer",
    "other"
]


def create_expense(
    amount,
    category,
    description,
    date=None,
    vendor=None,
    payment_method="corporate_card",
    receipt=False,
    reimbursable=True,
    project=None,
    notes=None,
    attendees=None
):
    """Create a new expense entry."""

    return {
        "id": f"EXP{datetime.now().strftime('%Y%m%d%H%M%S')}",
        "date": date or datetime.now().strftime("%Y-%m-%d"),
        "amount": round(float(amount), 2),
        "category": category,
        "description": description,
        "vendor": vendor,
        "payment_method": payment_method,
        "receipt_attached": receipt,
        "reimbursable": reimbursable,
        "project": project,
        "notes": notes,
        "attendees": attendees,
        "status": "pending",
        "created": datetime.now().isoformat()
    }


def load_expenses(file_path):
    """Load expenses from JSON file."""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "user": "",
            "expenses": [],
            "created": datetime.now().isoformat()
        }


def save_expenses(data, file_path):
    """Save expenses to JSON file."""
    data["last_updated"] = datetime.now().isoformat()
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)


def add_expense(data, expense):
    """Add a new expense."""
    data["expenses"].append(expense)
    return data


def list_expenses(data, filters=None):
    """List expenses with optional filtering."""

    expenses = data.get("expenses", [])

    if filters:
        if filters.get("category"):
            expenses = [e for e in expenses if e.get("category") == filters["category"]]
        if filters.get("month"):
            expenses = [e for e in expenses if e.get("date", "").startswith(f"2025-{filters['month']}")]
        if filters.get("status"):
            expenses = [e for e in expenses if e.get("status") == filters["status"]]
        if filters.get("reimbursable") is not None:
            expenses = [e for e in expenses if e.get("reimbursable") == filters["reimbursable"]]

    return expenses


def calculate_summary(expenses, group_by="category"):
    """Calculate expense summary."""

    summary = defaultdict(lambda: {"count": 0, "total": 0})

    for expense in expenses:
        key = expense.get(group_by, "other")
        summary[key]["count"] += 1
        summary[key]["total"] += expense.get("amount", 0)

    # Round totals
    for key in summary:
        summary[key]["total"] = round(summary[key]["total"], 2)

    return dict(summary)


def generate_report(expenses, title="Expense Report"):
    """Generate expense report."""

    if not expenses:
        return {"error": "No expenses to report"}

    total = sum(e.get("amount", 0) for e in expenses)
    reimbursable = sum(e.get("amount", 0) for e in expenses if e.get("reimbursable", True))

    # Group by category
    by_category = calculate_summary(expenses, "category")

    # Group by status
    by_status = calculate_summary(expenses, "status")

    # Date range
    dates = [e.get("date", "") for e in expenses if e.get("date")]
    date_range = {
        "earliest": min(dates) if dates else None,
        "latest": max(dates) if dates else None
    }

    # Missing receipts
    missing_receipts = [
        {"id": e["id"], "description": e["description"], "amount": e["amount"]}
        for e in expenses if not e.get("receipt_attached", False)
    ]

    return {
        "title": title,
        "generated": datetime.now().isoformat(),
        "summary": {
            "total_expenses": len(expenses),
            "total_amount": round(total, 2),
            "reimbursable_amount": round(reimbursable, 2),
            "date_range": date_range
        },
        "by_category": by_category,
        "by_status": by_status,
        "missing_receipts": missing_receipts,
        "expenses": expenses
    }


def export_report(report, format_type="text"):
    """Export report in specified format."""

    if format_type == "json":
        return json.dumps(report, indent=2)

    elif format_type == "text":
        lines = []
        lines.append("\n" + "=" * 60)
        lines.append(report.get("title", "EXPENSE REPORT"))
        lines.append("=" * 60)

        summary = report.get("summary", {})
        lines.append(f"\n--- SUMMARY ---")
        lines.append(f"Total Expenses: {summary.get('total_expenses', 0)}")
        lines.append(f"Total Amount: ${summary.get('total_amount', 0):,.2f}")
        lines.append(f"Reimbursable: ${summary.get('reimbursable_amount', 0):,.2f}")

        if summary.get("date_range"):
            lines.append(f"Period: {summary['date_range']['earliest']} to {summary['date_range']['latest']}")

        lines.append(f"\n--- BY CATEGORY ---")
        for cat, data in sorted(report.get("by_category", {}).items(), key=lambda x: -x[1]["total"]):
            lines.append(f"  {cat}: ${data['total']:,.2f} ({data['count']} items)")

        lines.append(f"\n--- BY STATUS ---")
        for status, data in report.get("by_status", {}).items():
            lines.append(f"  {status}: ${data['total']:,.2f} ({data['count']} items)")

        if report.get("missing_receipts"):
            lines.append(f"\n--- MISSING RECEIPTS ---")
            for item in report["missing_receipts"]:
                lines.append(f"  {item['id']}: {item['description']} (${item['amount']:.2f})")

        lines.append(f"\n--- EXPENSE DETAILS ---")
        for expense in report.get("expenses", []):
            lines.append(f"\n[{expense['id']}] {expense['date']}")
            lines.append(f"  ${expense['amount']:.2f} | {expense['category']} | {expense['description']}")
            if expense.get('vendor'):
                lines.append(f"  Vendor: {expense['vendor']}")

        return "\n".join(lines)

    elif format_type == "csv":
        lines = ["id,date,amount,category,description,vendor,reimbursable,receipt,status"]
        for e in report.get("expenses", []):
            line = f"{e['id']},{e['date']},{e['amount']},{e['category']},{e.get('description', '').replace(',', ';')},{e.get('vendor', '')},{e.get('reimbursable', True)},{e.get('receipt_attached', False)},{e.get('status', 'pending')}"
            lines.append(line)
        return "\n".join(lines)

    return json.dumps(report, indent=2)


def interactive_add():
    """Interactive expense addition."""

    print("\n=== Add Expense ===\n")

    # Required fields
    try:
        amount = float(input("Amount ($): ").strip().replace("$", ""))
    except ValueError:
        print("Invalid amount")
        return None

    print(f"\nCategories: {', '.join(CATEGORIES)}")
    category = input("Category [other]: ").strip().lower() or "other"

    description = input("Description: ").strip()
    if not description:
        print("Description required")
        return None

    # Optional fields
    date = input("Date (YYYY-MM-DD) [today]: ").strip()
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    vendor = input("Vendor (optional): ").strip() or None

    print(f"\nPayment methods: {', '.join(PAYMENT_METHODS)}")
    payment = input("Payment method [corporate_card]: ").strip().lower() or "corporate_card"

    receipt = input("Receipt attached? (y/n) [n]: ").strip().lower() == "y"
    reimbursable = input("Reimbursable? (y/n) [y]: ").strip().lower() != "n"

    project = input("Project/Client (optional): ").strip() or None

    # For meals, get attendees
    attendees = None
    if category == "meals":
        att_input = input("Attendees (comma-separated, optional): ").strip()
        if att_input:
            attendees = [a.strip() for a in att_input.split(",")]

    notes = input("Notes (optional): ").strip() or None

    expense = create_expense(
        amount=amount,
        category=category,
        description=description,
        date=date,
        vendor=vendor,
        payment_method=payment,
        receipt=receipt,
        reimbursable=reimbursable,
        project=project,
        notes=notes,
        attendees=attendees
    )

    return expense


def main():
    parser = argparse.ArgumentParser(description='Track expenses')
    parser.add_argument('file', nargs='?', default='expenses.json',
                        help='Expense file (JSON)')
    parser.add_argument('--add', '-a', action='store_true',
                        help='Add expense (interactive)')
    parser.add_argument('--list', '-l', action='store_true',
                        help='List expenses')
    parser.add_argument('--summary', '-s', action='store_true',
                        help='Show summary')
    parser.add_argument('--report', '-r', action='store_true',
                        help='Generate full report')
    parser.add_argument('--format', '-f', choices=['json', 'text', 'csv'],
                        default='text', help='Output format')
    parser.add_argument('--category', '-c', help='Filter by category')
    parser.add_argument('--month', '-m', help='Filter by month (01-12)')
    parser.add_argument('--new', '-n', help='Create new expense file with user name')
    parser.add_argument('--quick', '-q', nargs=3, metavar=('AMOUNT', 'CATEGORY', 'DESC'),
                        help='Quick add: amount category description')

    args = parser.parse_args()

    if args.new:
        data = {
            "user": args.new,
            "created": datetime.now().isoformat(),
            "expenses": []
        }
        save_expenses(data, args.file)
        print(f"Created new expense file: {args.file}")
        return

    if args.quick:
        data = load_expenses(args.file)
        expense = create_expense(
            amount=args.quick[0],
            category=args.quick[1],
            description=args.quick[2]
        )
        data = add_expense(data, expense)
        save_expenses(data, args.file)
        print(f"Added: {expense['id']} - ${expense['amount']:.2f} - {expense['description']}")
        return

    if args.add:
        data = load_expenses(args.file)
        expense = interactive_add()
        if expense:
            data = add_expense(data, expense)
            save_expenses(data, args.file)
            print(f"\nExpense added: {expense['id']}")
            print(f"Saved to: {args.file}")
        return

    if args.report or args.summary:
        data = load_expenses(args.file)
        filters = {}
        if args.category:
            filters["category"] = args.category
        if args.month:
            filters["month"] = args.month.zfill(2)

        expenses = list_expenses(data, filters)
        report = generate_report(expenses)
        print(export_report(report, args.format))
        return

    if args.list or True:  # Default action
        data = load_expenses(args.file)
        filters = {}
        if args.category:
            filters["category"] = args.category
        if args.month:
            filters["month"] = args.month.zfill(2)

        expenses = list_expenses(data, filters)

        if args.format == "json":
            print(json.dumps(expenses, indent=2))
        else:
            print(f"\n{'='*60}")
            print(f"EXPENSES ({len(expenses)} items)")
            print(f"{'='*60}")

            total = 0
            for e in sorted(expenses, key=lambda x: x.get("date", "")):
                print(f"\n[{e['id']}] {e['date']}")
                print(f"  ${e['amount']:.2f} | {e['category']} | {e['description']}")
                if e.get('vendor'):
                    print(f"  Vendor: {e['vendor']}")
                total += e.get("amount", 0)

            print(f"\n{'='*60}")
            print(f"TOTAL: ${total:,.2f}")


if __name__ == '__main__':
    main()
