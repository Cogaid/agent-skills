#!/usr/bin/env python3
"""
Order status lookup and tracking utility.

Usage:
    python order_lookup.py --order "ORD-12345"
    python order_lookup.py --tracking "1Z999AA10123456784"
    python order_lookup.py --customer "customer@email.com"

Output: Order status, tracking info, and timeline
"""

import argparse
import json
from datetime import datetime, timedelta
import random


# Sample order statuses
ORDER_STATUSES = {
    "ORD_RCV": {"label": "Order Received", "stage": 1},
    "PAY_CONF": {"label": "Payment Confirmed", "stage": 2},
    "PROC": {"label": "Processing", "stage": 3},
    "PICK": {"label": "Picking", "stage": 4},
    "PACK": {"label": "Packing", "stage": 5},
    "RTS": {"label": "Ready to Ship", "stage": 6},
    "SHIP": {"label": "Shipped", "stage": 7},
    "TRNS": {"label": "In Transit", "stage": 8},
    "OFD": {"label": "Out for Delivery", "stage": 9},
    "DEL": {"label": "Delivered", "stage": 10},
    "HOLD": {"label": "On Hold", "stage": 0},
    "CANC": {"label": "Cancelled", "stage": -1}
}

# Carrier information
CARRIERS = {
    "usps": {
        "name": "USPS",
        "tracking_url": "https://tools.usps.com/go/TrackConfirmAction?tLabels=",
        "phone": "1-800-275-8777"
    },
    "ups": {
        "name": "UPS",
        "tracking_url": "https://www.ups.com/track?tracknum=",
        "phone": "1-800-742-5877"
    },
    "fedex": {
        "name": "FedEx",
        "tracking_url": "https://www.fedex.com/fedextrack/?trknbr=",
        "phone": "1-800-463-3339"
    },
    "dhl": {
        "name": "DHL",
        "tracking_url": "https://www.dhl.com/en/express/tracking.html?AWB=",
        "phone": "1-800-225-5345"
    }
}


def generate_sample_order(order_id):
    """Generate sample order data for demonstration."""

    statuses = list(ORDER_STATUSES.keys())
    current_status = random.choice(statuses[:10])  # Exclude HOLD and CANC usually

    carriers = list(CARRIERS.keys())
    carrier = random.choice(carriers)

    order_date = datetime.now() - timedelta(days=random.randint(1, 14))

    # Generate tracking events based on status
    events = []
    status_info = ORDER_STATUSES[current_status]

    for code, info in ORDER_STATUSES.items():
        if info["stage"] > 0 and info["stage"] <= status_info["stage"]:
            event_date = order_date + timedelta(hours=info["stage"] * 8)
            events.append({
                "status": info["label"],
                "timestamp": event_date.isoformat(),
                "location": random.choice(["Warehouse", "Distribution Center", "Local Facility", ""])
            })

    return {
        "order_id": order_id,
        "status": current_status,
        "status_label": status_info["label"],
        "order_date": order_date.isoformat(),
        "customer": {
            "name": "Sample Customer",
            "email": "customer@example.com"
        },
        "shipping": {
            "carrier": CARRIERS[carrier]["name"],
            "carrier_code": carrier,
            "tracking_number": f"1Z{random.randint(100000000, 999999999)}",
            "method": random.choice(["Standard", "Express", "Overnight"]),
            "address": {
                "street": "123 Main St",
                "city": "Anytown",
                "state": "CA",
                "zip": "90210",
                "country": "US"
            }
        },
        "estimated_delivery": (order_date + timedelta(days=random.randint(3, 7))).strftime("%Y-%m-%d"),
        "items": [
            {"name": "Sample Product", "quantity": 1, "price": 49.99}
        ],
        "events": events
    }


def lookup_order(order_id):
    """Look up order by order ID."""

    # In a real implementation, this would query a database
    order = generate_sample_order(order_id)

    # Add tracking URL
    carrier_code = order["shipping"]["carrier_code"]
    tracking = order["shipping"]["tracking_number"]
    order["shipping"]["tracking_url"] = CARRIERS[carrier_code]["tracking_url"] + tracking

    return order


def lookup_by_tracking(tracking_number):
    """Look up order by tracking number."""

    # Detect carrier from tracking format
    carrier = detect_carrier(tracking_number)

    # Generate sample tracking data
    return {
        "tracking_number": tracking_number,
        "carrier": CARRIERS.get(carrier, {}).get("name", "Unknown"),
        "carrier_code": carrier,
        "tracking_url": CARRIERS.get(carrier, {}).get("tracking_url", "") + tracking_number,
        "status": "In Transit",
        "estimated_delivery": (datetime.now() + timedelta(days=2)).strftime("%Y-%m-%d"),
        "events": [
            {
                "status": "In Transit",
                "timestamp": datetime.now().isoformat(),
                "location": "Distribution Center"
            },
            {
                "status": "Shipped",
                "timestamp": (datetime.now() - timedelta(days=1)).isoformat(),
                "location": "Origin Facility"
            }
        ]
    }


def detect_carrier(tracking_number):
    """Detect carrier from tracking number format."""

    tracking = tracking_number.upper().replace(" ", "")

    # UPS: 1Z followed by 16 alphanumeric
    if tracking.startswith("1Z") and len(tracking) == 18:
        return "ups"

    # FedEx: 12, 15, or 20 digits
    if tracking.isdigit() and len(tracking) in [12, 15, 20]:
        return "fedex"

    # USPS: 20-22 digits or starts with specific prefixes
    if tracking.isdigit() and len(tracking) in [20, 22]:
        return "usps"

    # DHL: 10 digits or starts with specific patterns
    if tracking.isdigit() and len(tracking) == 10:
        return "dhl"

    return "unknown"


def estimate_delivery(order_data):
    """Estimate delivery window based on current status."""

    status = order_data.get("status", "PROC")
    estimated = order_data.get("estimated_delivery")

    status_info = ORDER_STATUSES.get(status, {"stage": 0})

    estimate = {
        "original_estimate": estimated,
        "current_status": ORDER_STATUSES.get(status, {}).get("label", "Unknown"),
        "on_track": True,
        "confidence": "high"
    }

    if status_info["stage"] < 7:  # Not yet shipped
        estimate["message"] = "Order is being prepared. Delivery estimate will be more accurate once shipped."
        estimate["confidence"] = "medium"
    elif status_info["stage"] == 10:  # Delivered
        estimate["message"] = "Order has been delivered."
        estimate["delivered"] = True
    else:
        estimate["message"] = f"On track for delivery by {estimated}"

    return estimate


def format_order_summary(order):
    """Format order for display."""

    lines = []
    lines.append("\n" + "=" * 60)
    lines.append("ORDER SUMMARY")
    lines.append("=" * 60)

    lines.append(f"\nOrder ID: {order['order_id']}")
    lines.append(f"Status: {order['status_label']}")
    lines.append(f"Order Date: {order['order_date'][:10]}")

    lines.append("\n--- SHIPPING ---")
    shipping = order["shipping"]
    lines.append(f"Carrier: {shipping['carrier']}")
    lines.append(f"Method: {shipping['method']}")
    lines.append(f"Tracking: {shipping['tracking_number']}")
    lines.append(f"Track here: {shipping.get('tracking_url', 'N/A')}")

    lines.append(f"\nShip to:")
    addr = shipping["address"]
    lines.append(f"  {addr['street']}")
    lines.append(f"  {addr['city']}, {addr['state']} {addr['zip']}")

    lines.append(f"\nEstimated Delivery: {order['estimated_delivery']}")

    lines.append("\n--- ITEMS ---")
    for item in order["items"]:
        lines.append(f"  {item['quantity']}x {item['name']} - ${item['price']:.2f}")

    if order.get("events"):
        lines.append("\n--- TRACKING HISTORY ---")
        for event in reversed(order["events"][-5:]):  # Last 5 events
            lines.append(f"  {event['timestamp'][:16]} - {event['status']}")
            if event.get("location"):
                lines.append(f"    Location: {event['location']}")

    return "\n".join(lines)


def format_tracking_summary(tracking_data):
    """Format tracking data for display."""

    lines = []
    lines.append("\n" + "=" * 60)
    lines.append("TRACKING INFORMATION")
    lines.append("=" * 60)

    lines.append(f"\nTracking Number: {tracking_data['tracking_number']}")
    lines.append(f"Carrier: {tracking_data['carrier']}")
    lines.append(f"Current Status: {tracking_data['status']}")
    lines.append(f"Estimated Delivery: {tracking_data['estimated_delivery']}")
    lines.append(f"\nTrack here: {tracking_data.get('tracking_url', 'N/A')}")

    if tracking_data.get("events"):
        lines.append("\n--- TRACKING EVENTS ---")
        for event in tracking_data["events"]:
            lines.append(f"  {event['timestamp'][:16]} - {event['status']}")
            if event.get("location"):
                lines.append(f"    Location: {event['location']}")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description='Order status lookup utility')
    parser.add_argument('--order', '-o', help='Order ID to look up')
    parser.add_argument('--tracking', '-t', help='Tracking number to look up')
    parser.add_argument('--customer', '-c', help='Customer email to look up orders')
    parser.add_argument('--estimate', '-e', action='store_true',
                        help='Show delivery estimate')
    parser.add_argument('--format', '-f', choices=['json', 'text'],
                        default='text', help='Output format')

    args = parser.parse_args()

    if args.order:
        order = lookup_order(args.order)

        if args.estimate:
            estimate = estimate_delivery(order)
            if args.format == "json":
                print(json.dumps(estimate, indent=2))
            else:
                print(f"\nDelivery Estimate: {estimate['message']}")
                print(f"Confidence: {estimate['confidence']}")
            return

        if args.format == "json":
            print(json.dumps(order, indent=2))
        else:
            print(format_order_summary(order))
        return

    if args.tracking:
        tracking_data = lookup_by_tracking(args.tracking)

        if args.format == "json":
            print(json.dumps(tracking_data, indent=2))
        else:
            print(format_tracking_summary(tracking_data))
        return

    if args.customer:
        # In real implementation, would look up all orders for customer
        print(f"\nLooking up orders for: {args.customer}")
        print("(Sample data - would query database in production)")

        # Generate sample orders
        orders = [generate_sample_order(f"ORD-{i}") for i in range(1, 4)]

        if args.format == "json":
            print(json.dumps({"orders": orders}, indent=2))
        else:
            for order in orders:
                print(f"\n  {order['order_id']} - {order['status_label']} - {order['order_date'][:10]}")
        return

    parser.print_help()


if __name__ == '__main__':
    main()
