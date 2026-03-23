#!/usr/bin/env python3
"""
Process refund calculations and generate documentation.

Usage:
    python process_refund.py --amount 99.99 --reason defective
    python process_refund.py --amount 199.99 --category electronics --opened
    python process_refund.py --interactive

Output: Refund calculation details and documentation template
"""

import argparse
import json
import sys
from datetime import datetime, timedelta


# Refund configuration
RESTOCKING_FEES = {
    "electronics": 0.15,
    "furniture": 0.20,
    "software": 0.50,
    "standard": 0.0,
    "apparel": 0.0,
    "accessories": 0.0
}

RETURN_WINDOWS = {
    "electronics": 15,
    "perishables": 2,
    "standard": 30,
    "furniture": 30,
    "apparel": 30,
    "software": 0,  # non-refundable
    "digital": 0    # non-refundable
}

REASON_CODES = {
    "preference": {"code": "RET01", "full_refund": False, "customer_pays_shipping": True},
    "defective": {"code": "RET02", "full_refund": True, "customer_pays_shipping": False},
    "wrong_item": {"code": "RET03", "full_refund": True, "customer_pays_shipping": False},
    "not_received": {"code": "RET04", "full_refund": True, "customer_pays_shipping": False},
    "damaged": {"code": "RET05", "full_refund": True, "customer_pays_shipping": False},
    "quality": {"code": "RET06", "full_refund": False, "customer_pays_shipping": True},
    "late": {"code": "RET07", "full_refund": False, "customer_pays_shipping": True},
    "duplicate": {"code": "RET08", "full_refund": True, "customer_pays_shipping": False},
    "pricing_error": {"code": "RET09", "full_refund": True, "customer_pays_shipping": False},
    "goodwill": {"code": "RET10", "full_refund": True, "customer_pays_shipping": False}
}


def calculate_refund(
    amount,
    category="standard",
    reason="preference",
    is_opened=False,
    shipping_cost=0,
    days_since_purchase=None,
    tax_rate=0.0
):
    """Calculate refund amount based on various factors."""

    result = {
        "original_amount": amount,
        "category": category,
        "reason": reason,
        "reason_code": REASON_CODES.get(reason, REASON_CODES["preference"])["code"],
        "calculations": {},
        "deductions": [],
        "eligible": True,
        "notes": []
    }

    # Check return window
    return_window = RETURN_WINDOWS.get(category, RETURN_WINDOWS["standard"])

    if return_window == 0:
        result["eligible"] = False
        result["notes"].append(f"Category '{category}' is non-refundable")
        result["refund_amount"] = 0
        return result

    if days_since_purchase is not None and days_since_purchase > return_window:
        result["eligible"] = False
        result["notes"].append(f"Outside {return_window}-day return window (day {days_since_purchase})")
        result["refund_amount"] = 0
        return result

    # Base amount with tax
    tax_amount = amount * tax_rate
    base_total = amount + tax_amount
    result["calculations"]["item_price"] = amount
    result["calculations"]["tax"] = round(tax_amount, 2)

    # Calculate deductions
    total_deductions = 0

    # Restocking fee
    reason_info = REASON_CODES.get(reason, REASON_CODES["preference"])

    if not reason_info["full_refund"] and is_opened:
        restocking_rate = RESTOCKING_FEES.get(category, 0)
        restocking_fee = amount * restocking_rate
        if restocking_fee > 0:
            total_deductions += restocking_fee
            result["deductions"].append({
                "type": "restocking_fee",
                "rate": f"{restocking_rate * 100}%",
                "amount": round(restocking_fee, 2)
            })

    # Shipping cost handling
    if reason_info["customer_pays_shipping"] and shipping_cost > 0:
        total_deductions += shipping_cost
        result["deductions"].append({
            "type": "original_shipping",
            "amount": round(shipping_cost, 2)
        })
        result["notes"].append("Original shipping not refunded (customer preference return)")
    elif shipping_cost > 0 and not reason_info["customer_pays_shipping"]:
        result["calculations"]["shipping_refunded"] = shipping_cost
        base_total += shipping_cost
        result["notes"].append("Shipping refunded (company error)")

    # Final calculation
    refund_amount = base_total - total_deductions
    result["refund_amount"] = round(max(0, refund_amount), 2)
    result["total_deductions"] = round(total_deductions, 2)

    # Refund type determination
    if result["refund_amount"] == base_total:
        result["refund_type"] = "full"
    elif result["refund_amount"] > 0:
        result["refund_type"] = "partial"
    else:
        result["refund_type"] = "none"

    return result


def check_eligibility(days_since_purchase, category="standard"):
    """Check if return is within eligibility window."""
    window = RETURN_WINDOWS.get(category, RETURN_WINDOWS["standard"])

    return {
        "eligible": days_since_purchase <= window,
        "return_window": window,
        "days_since_purchase": days_since_purchase,
        "days_remaining": max(0, window - days_since_purchase)
    }


def generate_documentation(refund_data, customer_info=None):
    """Generate refund documentation template."""

    customer = customer_info or {
        "name": "[CUSTOMER_NAME]",
        "email": "[EMAIL]",
        "account_id": "[ACCOUNT_ID]"
    }

    doc = {
        "timestamp": datetime.now().isoformat(),
        "customer": customer,
        "refund_details": {
            "original_amount": refund_data["original_amount"],
            "refund_amount": refund_data["refund_amount"],
            "refund_type": refund_data.get("refund_type", "unknown"),
            "reason_code": refund_data["reason_code"],
            "category": refund_data["category"]
        },
        "calculations": refund_data.get("calculations", {}),
        "deductions": refund_data.get("deductions", []),
        "notes": refund_data.get("notes", []),
        "processing": {
            "method": "[TO BE SELECTED]",
            "timeline": "3-5 business days",
            "requires_return": refund_data.get("reason") not in ["not_received", "duplicate"]
        }
    }

    return doc


def estimate_processing_time(refund_method):
    """Estimate processing time by refund method."""

    times = {
        "credit_card": {
            "processing": "24 hours",
            "customer_visible": "3-5 business days",
            "total_estimate": "5-7 days"
        },
        "debit_card": {
            "processing": "24 hours",
            "customer_visible": "3-5 business days",
            "total_estimate": "5-7 days"
        },
        "paypal": {
            "processing": "Immediate",
            "customer_visible": "24-48 hours",
            "total_estimate": "1-2 days"
        },
        "store_credit": {
            "processing": "Immediate",
            "customer_visible": "Immediate",
            "total_estimate": "Same day"
        },
        "gift_card": {
            "processing": "1 business day",
            "customer_visible": "Email delivery",
            "total_estimate": "1-2 days"
        },
        "check": {
            "processing": "1-2 business days",
            "customer_visible": "7-10 business days (mail)",
            "total_estimate": "2-3 weeks"
        }
    }

    return times.get(refund_method, {
        "processing": "Unknown",
        "customer_visible": "Contact support",
        "total_estimate": "Varies"
    })


def interactive_mode():
    """Interactive refund processing mode."""

    print("\n=== Refund Calculator ===\n")

    # Gather information
    try:
        amount = float(input("Original purchase amount ($): "))
    except ValueError:
        print("Invalid amount")
        return

    print("\nCategories: standard, electronics, furniture, apparel, software")
    category = input("Product category [standard]: ").strip().lower() or "standard"

    print("\nReasons: preference, defective, wrong_item, not_received, damaged, quality")
    reason = input("Refund reason [preference]: ").strip().lower() or "preference"

    is_opened = input("Product opened? (y/n) [n]: ").strip().lower() == "y"

    try:
        shipping = float(input("Original shipping cost ($) [0]: ").strip() or "0")
    except ValueError:
        shipping = 0

    try:
        days = int(input("Days since purchase [0]: ").strip() or "0")
    except ValueError:
        days = 0

    try:
        tax_rate = float(input("Tax rate (decimal, e.g., 0.08) [0]: ").strip() or "0")
    except ValueError:
        tax_rate = 0

    # Calculate
    result = calculate_refund(
        amount=amount,
        category=category,
        reason=reason,
        is_opened=is_opened,
        shipping_cost=shipping,
        days_since_purchase=days,
        tax_rate=tax_rate
    )

    # Display results
    print("\n" + "=" * 40)
    print("REFUND CALCULATION RESULTS")
    print("=" * 40)

    print(f"\nOriginal Amount: ${result['original_amount']:.2f}")

    if result['calculations'].get('tax', 0) > 0:
        print(f"Tax: ${result['calculations']['tax']:.2f}")

    if result['calculations'].get('shipping_refunded', 0) > 0:
        print(f"Shipping Refunded: ${result['calculations']['shipping_refunded']:.2f}")

    if result['deductions']:
        print("\nDeductions:")
        for d in result['deductions']:
            if 'rate' in d:
                print(f"  {d['type']}: ${d['amount']:.2f} ({d['rate']})")
            else:
                print(f"  {d['type']}: ${d['amount']:.2f}")

    print("\n" + "-" * 40)

    if result['eligible']:
        print(f"REFUND AMOUNT: ${result['refund_amount']:.2f}")
        print(f"Refund Type: {result['refund_type'].upper()}")
        print(f"Reason Code: {result['reason_code']}")
    else:
        print("REFUND: NOT ELIGIBLE")

    if result['notes']:
        print("\nNotes:")
        for note in result['notes']:
            print(f"  • {note}")

    # Ask about documentation
    if result['eligible'] and input("\nGenerate documentation? (y/n) [n]: ").strip().lower() == "y":
        doc = generate_documentation(result)
        print("\n" + json.dumps(doc, indent=2))


def main():
    parser = argparse.ArgumentParser(description='Process refund calculations')
    parser.add_argument('--amount', '-a', type=float, help='Original purchase amount')
    parser.add_argument('--category', '-c', default='standard',
                        help='Product category (electronics, furniture, apparel, etc.)')
    parser.add_argument('--reason', '-r', default='preference',
                        help='Refund reason (defective, wrong_item, preference, etc.)')
    parser.add_argument('--opened', action='store_true', help='Product has been opened')
    parser.add_argument('--shipping', '-s', type=float, default=0,
                        help='Original shipping cost')
    parser.add_argument('--days', '-d', type=int, help='Days since purchase')
    parser.add_argument('--tax', '-t', type=float, default=0,
                        help='Tax rate (decimal)')
    parser.add_argument('--interactive', '-i', action='store_true',
                        help='Interactive mode')
    parser.add_argument('--format', '-f', choices=['json', 'text'],
                        default='json', help='Output format')
    parser.add_argument('--document', action='store_true',
                        help='Generate full documentation')

    args = parser.parse_args()

    if args.interactive:
        interactive_mode()
        return

    if not args.amount:
        parser.print_help()
        return

    result = calculate_refund(
        amount=args.amount,
        category=args.category,
        reason=args.reason,
        is_opened=args.opened,
        shipping_cost=args.shipping,
        days_since_purchase=args.days,
        tax_rate=args.tax
    )

    if args.document:
        result = generate_documentation(result)

    if args.format == 'json':
        print(json.dumps(result, indent=2))
    else:
        print(f"\nRefund Calculation for ${args.amount:.2f}")
        print("-" * 40)
        print(f"Category: {result.get('category', args.category)}")
        print(f"Reason: {args.reason} ({result.get('reason_code', 'N/A')})")
        print(f"Eligible: {'Yes' if result.get('eligible', False) else 'No'}")

        if result.get('eligible', False):
            print(f"Refund Amount: ${result['refund_amount']:.2f}")
            print(f"Type: {result.get('refund_type', 'N/A').upper()}")

            if result.get('deductions'):
                print("\nDeductions:")
                for d in result['deductions']:
                    print(f"  - {d['type']}: ${d['amount']:.2f}")

        if result.get('notes'):
            print("\nNotes:")
            for note in result['notes']:
                print(f"  • {note}")


if __name__ == '__main__':
    main()
