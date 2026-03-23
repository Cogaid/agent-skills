#!/usr/bin/env python3
"""
Delivery estimation utility.

Usage:
    python delivery_estimator.py --origin "90210" --dest "10001" --method "standard"
    python delivery_estimator.py --carrier "ups" --service "ground"
    python delivery_estimator.py --international --country "CA"

Output: Estimated delivery window and confidence level
"""

import argparse
import json
from datetime import datetime, timedelta


# Transit time estimates (business days)
DOMESTIC_TRANSIT = {
    "economy": {"min": 5, "max": 8, "description": "Economy/Ground"},
    "standard": {"min": 3, "max": 5, "description": "Standard Shipping"},
    "express": {"min": 2, "max": 3, "description": "Express Shipping"},
    "overnight": {"min": 1, "max": 1, "description": "Overnight/Next Day"},
    "same_day": {"min": 0, "max": 0, "description": "Same Day Delivery"}
}

# Carrier-specific transit times
CARRIER_SERVICES = {
    "usps": {
        "first_class": {"min": 2, "max": 5, "name": "First Class Mail"},
        "priority": {"min": 1, "max": 3, "name": "Priority Mail"},
        "priority_express": {"min": 1, "max": 2, "name": "Priority Mail Express"},
        "ground_advantage": {"min": 2, "max": 5, "name": "Ground Advantage"}
    },
    "ups": {
        "ground": {"min": 1, "max": 5, "name": "UPS Ground"},
        "3_day": {"min": 3, "max": 3, "name": "3 Day Select"},
        "2_day": {"min": 2, "max": 2, "name": "2nd Day Air"},
        "next_day": {"min": 1, "max": 1, "name": "Next Day Air"},
        "next_day_early": {"min": 1, "max": 1, "name": "Next Day Air Early"}
    },
    "fedex": {
        "ground": {"min": 1, "max": 5, "name": "FedEx Ground"},
        "express_saver": {"min": 3, "max": 3, "name": "Express Saver"},
        "2_day": {"min": 2, "max": 2, "name": "2Day"},
        "overnight": {"min": 1, "max": 1, "name": "Priority Overnight"},
        "first_overnight": {"min": 1, "max": 1, "name": "First Overnight"}
    }
}

# International transit times by region
INTERNATIONAL_TRANSIT = {
    "CA": {"economy": (7, 14), "express": (3, 5), "region": "Canada"},
    "MX": {"economy": (10, 21), "express": (4, 7), "region": "Mexico"},
    "GB": {"economy": (10, 21), "express": (3, 5), "region": "United Kingdom"},
    "DE": {"economy": (10, 21), "express": (3, 5), "region": "Germany"},
    "FR": {"economy": (10, 21), "express": (3, 5), "region": "France"},
    "AU": {"economy": (14, 28), "express": (5, 10), "region": "Australia"},
    "JP": {"economy": (10, 21), "express": (4, 7), "region": "Japan"},
    "CN": {"economy": (14, 28), "express": (5, 10), "region": "China"},
    "default": {"economy": (14, 28), "express": (5, 10), "region": "International"}
}

# Zone-based transit (simplified US zones)
US_ZONES = {
    "same_region": {"ground": (1, 3), "description": "Same region"},
    "adjacent": {"ground": (2, 4), "description": "Adjacent region"},
    "cross_country": {"ground": (4, 6), "description": "Cross-country"}
}

# Processing time factors
PROCESSING_TIMES = {
    "in_stock": {"min": 0, "max": 1, "description": "In stock items"},
    "warehouse": {"min": 1, "max": 2, "description": "Ships from warehouse"},
    "dropship": {"min": 2, "max": 4, "description": "Drop shipped"},
    "custom": {"min": 3, "max": 7, "description": "Custom/personalized"},
    "backorder": {"min": 7, "max": 14, "description": "Backordered"}
}


def calculate_business_days(start_date, num_days):
    """Calculate end date excluding weekends."""

    current = start_date
    days_added = 0

    while days_added < num_days:
        current += timedelta(days=1)
        if current.weekday() < 5:  # Monday = 0, Friday = 4
            days_added += 1

    return current


def estimate_delivery(
    method="standard",
    carrier=None,
    service=None,
    origin_zip=None,
    dest_zip=None,
    country=None,
    processing="in_stock",
    order_date=None
):
    """Calculate delivery estimate."""

    order_date = order_date or datetime.now()

    # Get processing time
    proc = PROCESSING_TIMES.get(processing, PROCESSING_TIMES["in_stock"])
    proc_min = proc["min"]
    proc_max = proc["max"]

    # Get transit time
    if country and country != "US":
        # International
        intl = INTERNATIONAL_TRANSIT.get(country, INTERNATIONAL_TRANSIT["default"])
        if method == "express":
            transit_min, transit_max = intl["express"]
        else:
            transit_min, transit_max = intl["economy"]
        region = intl["region"]
    elif carrier and service:
        # Carrier-specific
        carrier_services = CARRIER_SERVICES.get(carrier.lower(), {})
        svc = carrier_services.get(service.lower(), {"min": 3, "max": 5, "name": service})
        transit_min = svc["min"]
        transit_max = svc["max"]
        region = "Domestic"
    else:
        # Standard method
        transit = DOMESTIC_TRANSIT.get(method, DOMESTIC_TRANSIT["standard"])
        transit_min = transit["min"]
        transit_max = transit["max"]
        region = "Domestic"

    # Calculate total days
    total_min = proc_min + transit_min
    total_max = proc_max + transit_max

    # Calculate dates
    earliest = calculate_business_days(order_date, total_min)
    latest = calculate_business_days(order_date, total_max)

    # Determine confidence
    date_range = (latest - earliest).days
    if date_range <= 1:
        confidence = "high"
    elif date_range <= 3:
        confidence = "medium"
    else:
        confidence = "low"

    # Check for cutoff time (2 PM for same-day processing)
    cutoff_warning = None
    if order_date.hour >= 14 and proc_min == 0:
        cutoff_warning = "Order placed after 2 PM cutoff. Add 1 business day."
        earliest = calculate_business_days(earliest, 1)
        latest = calculate_business_days(latest, 1)

    return {
        "estimate": {
            "earliest": earliest.strftime("%Y-%m-%d"),
            "latest": latest.strftime("%Y-%m-%d"),
            "business_days": f"{total_min}-{total_max}"
        },
        "breakdown": {
            "processing": f"{proc_min}-{proc_max} days",
            "transit": f"{transit_min}-{transit_max} days"
        },
        "confidence": confidence,
        "region": region,
        "method": method if not service else f"{carrier.upper()} {service}",
        "cutoff_warning": cutoff_warning,
        "order_date": order_date.strftime("%Y-%m-%d %H:%M")
    }


def estimate_zone(origin_zip, dest_zip):
    """Estimate shipping zone based on ZIP codes."""

    if not origin_zip or not dest_zip:
        return {"zone": "unknown", "description": "ZIP codes required"}

    # Simplified zone calculation based on first digit of ZIP
    try:
        origin_region = int(origin_zip[0])
        dest_region = int(dest_zip[0])

        diff = abs(origin_region - dest_region)

        if diff == 0:
            zone = "same_region"
        elif diff <= 2:
            zone = "adjacent"
        else:
            zone = "cross_country"

        zone_info = US_ZONES[zone]

        return {
            "zone": zone,
            "description": zone_info["description"],
            "ground_transit": f"{zone_info['ground'][0]}-{zone_info['ground'][1]} days"
        }
    except (ValueError, IndexError):
        return {"zone": "unknown", "description": "Invalid ZIP format"}


def list_services(carrier=None):
    """List available shipping services."""

    if carrier:
        carrier = carrier.lower()
        if carrier in CARRIER_SERVICES:
            return {
                "carrier": carrier.upper(),
                "services": CARRIER_SERVICES[carrier]
            }
        else:
            return {"error": f"Unknown carrier: {carrier}"}

    return {
        "carriers": {
            k.upper(): list(v.keys())
            for k, v in CARRIER_SERVICES.items()
        }
    }


def format_estimate(estimate):
    """Format estimate for display."""

    lines = []
    lines.append("\n" + "=" * 50)
    lines.append("DELIVERY ESTIMATE")
    lines.append("=" * 50)

    lines.append(f"\nOrder Date: {estimate['order_date']}")
    lines.append(f"Shipping Method: {estimate['method']}")
    lines.append(f"Region: {estimate['region']}")

    lines.append(f"\n--- ESTIMATE ---")
    lines.append(f"Earliest: {estimate['estimate']['earliest']}")
    lines.append(f"Latest: {estimate['estimate']['latest']}")
    lines.append(f"Business Days: {estimate['estimate']['business_days']}")

    lines.append(f"\n--- BREAKDOWN ---")
    lines.append(f"Processing: {estimate['breakdown']['processing']}")
    lines.append(f"Transit: {estimate['breakdown']['transit']}")

    lines.append(f"\nConfidence: {estimate['confidence'].upper()}")

    if estimate.get('cutoff_warning'):
        lines.append(f"\n⚠️  {estimate['cutoff_warning']}")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description='Delivery estimation utility')
    parser.add_argument('--method', '-m',
                        choices=['economy', 'standard', 'express', 'overnight', 'same_day'],
                        default='standard', help='Shipping method')
    parser.add_argument('--carrier', '-c', help='Carrier (usps, ups, fedex)')
    parser.add_argument('--service', '-s', help='Carrier service code')
    parser.add_argument('--origin', help='Origin ZIP code')
    parser.add_argument('--dest', help='Destination ZIP code')
    parser.add_argument('--country', help='Destination country code (for international)')
    parser.add_argument('--processing', '-p',
                        choices=['in_stock', 'warehouse', 'dropship', 'custom', 'backorder'],
                        default='in_stock', help='Processing type')
    parser.add_argument('--international', '-i', action='store_true',
                        help='International shipment')
    parser.add_argument('--zone', '-z', action='store_true',
                        help='Calculate shipping zone')
    parser.add_argument('--list-services', '-l', action='store_true',
                        help='List available services')
    parser.add_argument('--format', '-f', choices=['json', 'text'],
                        default='text', help='Output format')

    args = parser.parse_args()

    if args.list_services:
        result = list_services(args.carrier)
        if args.format == "json":
            print(json.dumps(result, indent=2))
        else:
            print("\nAvailable Services:")
            if "carriers" in result:
                for carrier, services in result["carriers"].items():
                    print(f"\n  {carrier}:")
                    for svc in services:
                        print(f"    - {svc}")
            else:
                print(f"\n  {result['carrier']}:")
                for code, info in result["services"].items():
                    print(f"    {code}: {info['name']} ({info['min']}-{info['max']} days)")
        return

    if args.zone:
        result = estimate_zone(args.origin, args.dest)
        if args.format == "json":
            print(json.dumps(result, indent=2))
        else:
            print(f"\nZone: {result['zone']}")
            print(f"Description: {result['description']}")
            if "ground_transit" in result:
                print(f"Ground Transit: {result['ground_transit']}")
        return

    # Calculate estimate
    estimate = estimate_delivery(
        method=args.method,
        carrier=args.carrier,
        service=args.service,
        origin_zip=args.origin,
        dest_zip=args.dest,
        country=args.country if args.international else None,
        processing=args.processing
    )

    if args.format == "json":
        print(json.dumps(estimate, indent=2))
    else:
        print(format_estimate(estimate))


if __name__ == '__main__':
    main()
