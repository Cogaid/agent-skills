#!/usr/bin/env python3
"""
Generate customized packing list based on trip type.

Usage:
    python packing_list.py --type business --days 3
    python packing_list.py --type vacation --days 7 --international
    python packing_list.py --interactive

Output: JSON with categorized packing checklist
"""

import argparse
import json
import sys


PACKING_ITEMS = {
    "documents": {
        "essential": [
            "ID/Driver's license",
            "Flight confirmations (printed + digital)",
            "Hotel confirmations",
            "Phone + charger",
            "Wallet/credit cards"
        ],
        "international": [
            "Passport (check 6+ month validity)",
            "Visa (if required)",
            "Travel insurance documents",
            "Vaccination records",
            "Local currency (small amount)",
            "Copies of documents (separate from originals)",
            "Embassy contact info"
        ],
        "business": [
            "Business cards",
            "Meeting materials/presentations",
            "Laptop + charger",
            "Notebook/pen"
        ]
    },
    "tech": {
        "essential": [
            "Phone charger",
            "Portable battery",
            "Headphones"
        ],
        "business": [
            "Laptop + charger",
            "Presentation clicker (if needed)",
            "USB drive (backup)"
        ],
        "international": [
            "Power adapter for destination",
            "Universal adapter"
        ]
    },
    "clothing": {
        "business": [
            "Business attire ({meeting_days} outfits)",
            "Dress shoes",
            "Belt",
            "Casual outfit (travel/evening)"
        ],
        "casual": [
            "T-shirts/casual tops ({days})",
            "Pants/shorts ({pants_count})",
            "Comfortable shoes"
        ],
        "always": [
            "Undergarments ({underwear_count})",
            "Socks ({socks_count})",
            "Sleepwear",
            "Light jacket/layers"
        ],
        "optional": [
            "Workout clothes",
            "Swimwear",
            "Rain jacket"
        ]
    },
    "toiletries": {
        "essential": [
            "Toothbrush + toothpaste",
            "Deodorant",
            "Razor/grooming kit",
            "Medications (in original containers)"
        ],
        "optional": [
            "Skincare products",
            "Contact lens supplies",
            "Glasses (backup)",
            "Sunscreen"
        ]
    },
    "misc": {
        "essential": [
            "Empty water bottle",
            "Snacks",
            "Entertainment (book/Kindle)"
        ],
        "optional": [
            "Umbrella (compact)",
            "Earplugs/eye mask",
            "Travel pillow"
        ],
        "international": [
            "Translation app downloaded",
            "Offline maps downloaded"
        ]
    }
}


def calculate_quantities(days):
    """Calculate clothing quantities based on trip length."""
    return {
        "underwear_count": days + 1,
        "socks_count": days + 1,
        "pants_count": max(2, (days + 1) // 2),
        "meeting_days": days,
        "days": days
    }


def generate_packing_list(trip_type, days, international=False, carry_on=False):
    """Generate customized packing list."""

    quantities = calculate_quantities(days)

    categories = {}

    # Documents
    docs = list(PACKING_ITEMS["documents"]["essential"])
    if trip_type == "business":
        docs.extend(PACKING_ITEMS["documents"]["business"])
    if international:
        docs.extend(PACKING_ITEMS["documents"]["international"])
    categories["Documents & ID"] = docs

    # Tech
    tech = list(PACKING_ITEMS["tech"]["essential"])
    if trip_type == "business":
        tech.extend(PACKING_ITEMS["tech"]["business"])
    if international:
        tech.extend(PACKING_ITEMS["tech"]["international"])
    categories["Tech & Electronics"] = tech

    # Clothing
    clothing = []
    if trip_type == "business":
        clothing.extend(PACKING_ITEMS["clothing"]["business"])
    else:
        clothing.extend(PACKING_ITEMS["clothing"]["casual"])
    clothing.extend(PACKING_ITEMS["clothing"]["always"])

    # Apply quantities
    clothing = [
        item.format(**quantities)
        for item in clothing
    ]
    categories["Clothing"] = clothing

    # Toiletries
    toiletries = list(PACKING_ITEMS["toiletries"]["essential"])
    if not carry_on:
        toiletries.extend(PACKING_ITEMS["toiletries"]["optional"])
    categories["Toiletries"] = toiletries

    # Misc
    misc = list(PACKING_ITEMS["misc"]["essential"])
    if international:
        misc.extend(PACKING_ITEMS["misc"]["international"])
    categories["Miscellaneous"] = misc

    # Recommendations
    recommendations = []
    if days <= 4:
        recommendations.append("This trip is short enough for carry-on only")
    if days > 5:
        recommendations.append("Consider doing laundry mid-trip to pack lighter")
    if international:
        recommendations.append("Check visa requirements and passport validity (6+ months)")
        recommendations.append("Notify bank of international travel")

    return {
        "trip_info": {
            "type": trip_type,
            "days": days,
            "international": international,
            "carry_on_recommended": days <= 4
        },
        "packing_list": categories,
        "recommendations": recommendations
    }


def interactive_mode():
    """Interactive packing list generation."""
    print("=== Packing List Generator ===\n")

    print("Trip types: business, vacation, conference")
    trip_type = input("Trip type: ").strip().lower() or "business"

    days = int(input("Number of days: ").strip() or 3)
    international = input("International? (y/n): ").strip().lower() == 'y'

    return trip_type, days, international


def main():
    parser = argparse.ArgumentParser(description="Generate packing list")
    parser.add_argument("--type", "-t", default="business",
                        choices=["business", "vacation", "conference"],
                        help="Trip type")
    parser.add_argument("--days", "-d", type=int, default=3,
                        help="Number of days")
    parser.add_argument("--international", "-i", action="store_true",
                        help="International travel")
    parser.add_argument("--carry-on", "-c", action="store_true",
                        help="Carry-on only")
    parser.add_argument("--interactive", action="store_true",
                        help="Interactive mode")

    args = parser.parse_args()

    if args.interactive:
        trip_type, days, international = interactive_mode()
        carry_on = days <= 4
    else:
        trip_type = args.type
        days = args.days
        international = args.international
        carry_on = args.carry_on

    result = generate_packing_list(trip_type, days, international, carry_on)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
