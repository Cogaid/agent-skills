#!/usr/bin/env python3
"""
Generate professional invoices from parameters.

Usage:
    python generate_invoice.py --client "Acme Corp" --items items.json --terms net30
    python generate_invoice.py --client "Acme Corp" --items '[{"desc":"Consulting","qty":10,"rate":150}]' --terms net15 --currency USD
    python generate_invoice.py --client "Acme Corp" --items items.json --terms net30 --tax-rate 8.5 --discount 5
"""

import argparse
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path

PAYMENT_TERMS = {
    "due_on_receipt": 0,
    "net15": 15,
    "net30": 30,
    "net45": 45,
    "net60": 60,
    "net90": 90,
}

SAMPLE_ITEMS = [
    {"description": "Web Design Services", "quantity": 40, "rate": 150.00},
    {"description": "Hosting (Monthly)", "quantity": 1, "rate": 99.00},
    {"description": "Domain Registration", "quantity": 1, "rate": 15.00},
]

CURRENCY_SYMBOLS = {
    "USD": "$",
    "EUR": "\u20ac",
    "GBP": "\u00a3",
    "JPY": "\u00a5",
    "INR": "\u20b9",
    "CAD": "CA$",
    "AUD": "A$",
}


def format_currency(amount, currency="USD"):
    symbol = CURRENCY_SYMBOLS.get(currency, currency + " ")
    if currency == "JPY":
        return f"{symbol}{amount:,.0f}"
    return f"{symbol}{amount:,.2f}"


def parse_items(items_arg):
    """Parse items from JSON file path or inline JSON string."""
    if items_arg is None:
        return SAMPLE_ITEMS

    path = Path(items_arg)
    if path.exists():
        with open(path) as f:
            raw = json.load(f)
    else:
        try:
            raw = json.loads(items_arg)
        except json.JSONDecodeError:
            print(f"Error: Could not parse items. Provide a valid JSON file or JSON string.", file=sys.stderr)
            sys.exit(1)

    items = []
    for item in raw:
        items.append({
            "description": item.get("description", item.get("desc", "Service")),
            "quantity": item.get("quantity", item.get("qty", 1)),
            "rate": float(item.get("rate", item.get("price", 0))),
        })
    return items


def generate_invoice_number(prefix="INV"):
    now = datetime.now()
    return f"{prefix}-{now.year}-{now.strftime('%m%d')}-{now.strftime('%H%M')}"


def build_invoice(client, items, terms, tax_rate, discount_pct, currency, invoice_number=None):
    if invoice_number is None:
        invoice_number = generate_invoice_number()

    issue_date = datetime.now()
    days = PAYMENT_TERMS.get(terms, 30)
    due_date = issue_date + timedelta(days=days)

    line_items = []
    subtotal = 0.0
    for i, item in enumerate(items, 1):
        amount = item["quantity"] * item["rate"]
        subtotal += amount
        line_items.append({
            "number": i,
            "description": item["description"],
            "quantity": item["quantity"],
            "rate": item["rate"],
            "amount": amount,
        })

    tax_amount = subtotal * (tax_rate / 100) if tax_rate else 0.0
    discount_amount = subtotal * (discount_pct / 100) if discount_pct else 0.0
    total_due = subtotal + tax_amount - discount_amount

    invoice = {
        "invoice_number": invoice_number,
        "issue_date": issue_date.strftime("%Y-%m-%d"),
        "due_date": due_date.strftime("%Y-%m-%d"),
        "payment_terms": terms,
        "payment_days": days,
        "currency": currency,
        "client": client,
        "line_items": [
            {
                **item,
                "rate_formatted": format_currency(item["rate"], currency),
                "amount_formatted": format_currency(item["amount"], currency),
            }
            for item in line_items
        ],
        "subtotal": subtotal,
        "subtotal_formatted": format_currency(subtotal, currency),
        "tax_rate": tax_rate,
        "tax_amount": tax_amount,
        "tax_amount_formatted": format_currency(tax_amount, currency),
        "discount_pct": discount_pct,
        "discount_amount": discount_amount,
        "discount_amount_formatted": format_currency(discount_amount, currency),
        "total_due": total_due,
        "total_due_formatted": format_currency(total_due, currency),
        "status": "draft",
    }
    return invoice


def print_invoice_text(invoice):
    """Print a human-readable text representation of the invoice."""
    c = invoice["currency"]
    print("=" * 60)
    print(f"  INVOICE: {invoice['invoice_number']}")
    print("=" * 60)
    print(f"  Client:         {invoice['client']}")
    print(f"  Date Issued:    {invoice['issue_date']}")
    print(f"  Due Date:       {invoice['due_date']}")
    print(f"  Terms:          {invoice['payment_terms']} ({invoice['payment_days']} days)")
    print(f"  Currency:       {c}")
    print("-" * 60)
    print(f"  {'#':<4} {'Description':<28} {'Qty':>5} {'Rate':>10} {'Amount':>10}")
    print(f"  {'─'*4} {'─'*28} {'─'*5} {'─'*10} {'─'*10}")
    for item in invoice["line_items"]:
        print(f"  {item['number']:<4} {item['description']:<28} {item['quantity']:>5} {item['rate_formatted']:>10} {item['amount_formatted']:>10}")
    print("-" * 60)
    print(f"  {'Subtotal:':>48} {invoice['subtotal_formatted']:>10}")
    if invoice["tax_rate"]:
        print(f"  {f'Tax ({invoice['tax_rate']}%):':>48} {invoice['tax_amount_formatted']:>10}")
    if invoice["discount_pct"]:
        print(f"  {f'Discount ({invoice['discount_pct']}%):':>48} -{invoice['discount_amount_formatted']:>9}")
    print(f"  {'─'*10:>58}")
    print(f"  {'TOTAL DUE:':>48} {invoice['total_due_formatted']:>10}")
    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(
        description="Generate professional invoices with tax and discount calculations.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --client "Acme Corp" --terms net30
  %(prog)s --client "Acme Corp" --items items.json --tax-rate 8.5
  %(prog)s --client "Acme Corp" --items '[{"desc":"Design","qty":40,"rate":150}]' --discount 5
        """,
    )
    parser.add_argument("--client", required=True, help="Client company name")
    parser.add_argument("--items", default=None, help="Line items as JSON file path or inline JSON string")
    parser.add_argument("--terms", default="net30", choices=list(PAYMENT_TERMS.keys()),
                        help="Payment terms (default: net30)")
    parser.add_argument("--tax-rate", type=float, default=0.0, help="Tax rate percentage (default: 0)")
    parser.add_argument("--discount", type=float, default=0.0, help="Discount percentage (default: 0)")
    parser.add_argument("--currency", default="USD", choices=list(CURRENCY_SYMBOLS.keys()),
                        help="Currency code (default: USD)")
    parser.add_argument("--invoice-number", default=None, help="Custom invoice number")
    parser.add_argument("--format", choices=["json", "text"], default="text",
                        help="Output format (default: text)")

    args = parser.parse_args()
    items = parse_items(args.items)
    invoice = build_invoice(
        client=args.client,
        items=items,
        terms=args.terms,
        tax_rate=args.tax_rate,
        discount_pct=args.discount,
        currency=args.currency,
        invoice_number=args.invoice_number,
    )

    if args.format == "json":
        print(json.dumps(invoice, indent=2))
    else:
        print_invoice_text(invoice)


if __name__ == "__main__":
    main()
