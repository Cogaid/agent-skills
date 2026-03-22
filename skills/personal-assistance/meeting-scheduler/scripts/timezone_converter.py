#!/usr/bin/env python3
"""
Convert times across multiple time zones.

Usage:
    python timezone_converter.py --time "10:00 AM" --from-tz "America/New_York" --to-tz "Europe/London"
    python timezone_converter.py --time "14:00" --from-tz "PT" --to-tz "ET,CET,IST,JST"
    python timezone_converter.py --interactive

Output: JSON with converted times
"""

import argparse
import json
import sys
from datetime import datetime, timedelta

# Common timezone abbreviations and their UTC offsets (standard time)
# Note: Real implementation should use pytz for DST handling
TIMEZONE_OFFSETS = {
    # US
    "PT": -8, "PST": -8, "PDT": -7,
    "MT": -7, "MST": -7, "MDT": -6,
    "CT": -6, "CST": -6, "CDT": -5,
    "ET": -5, "EST": -5, "EDT": -4,
    # Europe
    "GMT": 0, "UTC": 0,
    "WET": 0, "WEST": 1,
    "CET": 1, "CEST": 2,
    "EET": 2, "EEST": 3,
    # Asia
    "IST": 5.5,  # India
    "ICT": 7,    # Indochina
    "CST_CHINA": 8, "HKT": 8, "SGT": 8,
    "JST": 9,
    "KST": 9,
    # Australia
    "AWST": 8,
    "ACST": 9.5,
    "AEST": 10, "AEDT": 11,
    # Full names
    "America/Los_Angeles": -8,
    "America/Denver": -7,
    "America/Chicago": -6,
    "America/New_York": -5,
    "Europe/London": 0,
    "Europe/Paris": 1,
    "Europe/Berlin": 1,
    "Asia/Kolkata": 5.5,
    "Asia/Singapore": 8,
    "Asia/Tokyo": 9,
    "Australia/Sydney": 10,
}


def parse_time(time_str):
    """Parse time string in various formats."""
    time_str = time_str.strip().upper()

    # Try different formats
    formats = [
        "%I:%M %p",  # 10:00 AM
        "%I:%M%p",   # 10:00AM
        "%I %p",     # 10 AM
        "%H:%M",     # 14:00
        "%H%M",      # 1400
    ]

    for fmt in formats:
        try:
            return datetime.strptime(time_str, fmt)
        except ValueError:
            continue

    raise ValueError(f"Could not parse time: {time_str}")


def get_offset(tz_name):
    """Get UTC offset for timezone."""
    tz_upper = tz_name.upper().strip()

    # Check direct match
    if tz_upper in TIMEZONE_OFFSETS:
        return TIMEZONE_OFFSETS[tz_upper]

    # Check with underscores/slashes
    normalized = tz_name.replace("-", "_").replace(" ", "_")
    if normalized in TIMEZONE_OFFSETS:
        return TIMEZONE_OFFSETS[normalized]

    # Try as full timezone name
    if tz_name in TIMEZONE_OFFSETS:
        return TIMEZONE_OFFSETS[tz_name]

    raise ValueError(f"Unknown timezone: {tz_name}")


def convert_time(time_obj, from_tz, to_tz):
    """Convert time from one timezone to another."""
    from_offset = get_offset(from_tz)
    to_offset = get_offset(to_tz)

    # Calculate difference
    diff = to_offset - from_offset

    # Apply difference
    converted = time_obj + timedelta(hours=diff)

    return converted


def format_time(dt, include_24h=True):
    """Format datetime as readable time."""
    time_12h = dt.strftime("%I:%M %p").lstrip("0")
    if include_24h:
        time_24h = dt.strftime("%H:%M")
        return f"{time_12h} ({time_24h})"
    return time_12h


def convert_to_multiple(time_str, from_tz, to_tzs):
    """Convert time to multiple timezones."""
    time_obj = parse_time(time_str)

    results = {
        "input": {
            "time": time_str,
            "timezone": from_tz
        },
        "conversions": []
    }

    for tz in to_tzs:
        tz = tz.strip()
        try:
            converted = convert_time(time_obj, from_tz, tz)
            day_diff = ""

            # Check if it's a different day
            if converted.day != time_obj.day:
                if converted.day > time_obj.day:
                    day_diff = " (+1 day)"
                else:
                    day_diff = " (-1 day)"

            results["conversions"].append({
                "timezone": tz,
                "time": format_time(converted),
                "day_change": day_diff.strip() if day_diff else None
            })
        except ValueError as e:
            results["conversions"].append({
                "timezone": tz,
                "error": str(e)
            })

    return results


def interactive_mode():
    """Interactive time conversion."""
    print("=== Timezone Converter ===\n")

    time_str = input("Enter time (e.g., 10:00 AM or 14:00): ").strip()
    from_tz = input("From timezone (e.g., ET, PT, CET): ").strip()
    to_tzs = input("To timezone(s) (comma-separated): ").strip()

    return time_str, from_tz, [t.strip() for t in to_tzs.split(",")]


def main():
    parser = argparse.ArgumentParser(description="Convert times across timezones")
    parser.add_argument("--time", "-t", help="Time to convert (e.g., '10:00 AM')")
    parser.add_argument("--from-tz", "-f", help="Source timezone")
    parser.add_argument("--to-tz", "-z", help="Target timezone(s), comma-separated")
    parser.add_argument("--interactive", "-i", action="store_true",
                        help="Interactive mode")
    parser.add_argument("--list-zones", action="store_true",
                        help="List available timezone abbreviations")

    args = parser.parse_args()

    if args.list_zones:
        zones = sorted(set(TIMEZONE_OFFSETS.keys()))
        print("Available timezone abbreviations:")
        for z in zones:
            print(f"  {z}: UTC{TIMEZONE_OFFSETS[z]:+.1f}")
        return

    if args.interactive:
        time_str, from_tz, to_tzs = interactive_mode()
    elif args.time and args.from_tz and args.to_tz:
        time_str = args.time
        from_tz = args.from_tz
        to_tzs = [t.strip() for t in args.to_tz.split(",")]
    else:
        parser.print_help()
        sys.exit(1)

    result = convert_to_multiple(time_str, from_tz, to_tzs)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
