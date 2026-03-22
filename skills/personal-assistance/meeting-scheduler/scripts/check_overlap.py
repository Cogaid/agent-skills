#!/usr/bin/env python3
"""
Find overlap windows for meetings across multiple time zones.

Usage:
    python check_overlap.py --zones "PT,ET,CET,IST"
    python check_overlap.py --zones "America/New_York,Europe/London,Asia/Tokyo"

Output: JSON with best meeting overlap windows
"""

import argparse
import json
import sys

# Timezone UTC offsets (standard time)
TIMEZONE_OFFSETS = {
    "PT": -8, "PST": -8, "PDT": -7,
    "MT": -7, "MST": -7, "MDT": -6,
    "CT": -6, "CST": -6, "CDT": -5,
    "ET": -5, "EST": -5, "EDT": -4,
    "GMT": 0, "UTC": 0,
    "CET": 1, "CEST": 2,
    "IST": 5.5,
    "SGT": 8, "HKT": 8,
    "JST": 9,
    "AEST": 10, "AEDT": 11,
    "America/Los_Angeles": -8,
    "America/New_York": -5,
    "Europe/London": 0,
    "Europe/Paris": 1,
    "Asia/Kolkata": 5.5,
    "Asia/Singapore": 8,
    "Asia/Tokyo": 9,
    "Australia/Sydney": 10,
}

# Default working hours (local time)
DEFAULT_WORK_START = 9
DEFAULT_WORK_END = 18


def get_offset(tz_name):
    """Get UTC offset for timezone."""
    tz_upper = tz_name.upper().strip()
    if tz_upper in TIMEZONE_OFFSETS:
        return TIMEZONE_OFFSETS[tz_upper]
    if tz_name in TIMEZONE_OFFSETS:
        return TIMEZONE_OFFSETS[tz_name]
    raise ValueError(f"Unknown timezone: {tz_name}")


def format_hour(hour):
    """Format hour as readable time."""
    hour = hour % 24
    if hour == 0:
        return "12:00 AM"
    elif hour < 12:
        return f"{hour}:00 AM"
    elif hour == 12:
        return "12:00 PM"
    else:
        return f"{hour-12}:00 PM"


def utc_to_local(utc_hour, tz_offset):
    """Convert UTC hour to local hour."""
    return (utc_hour + tz_offset) % 24


def local_to_utc(local_hour, tz_offset):
    """Convert local hour to UTC hour."""
    return (local_hour - tz_offset) % 24


def find_overlap(zones, work_start=DEFAULT_WORK_START, work_end=DEFAULT_WORK_END):
    """Find overlapping work hours across timezones."""

    offsets = {}
    for tz in zones:
        try:
            offsets[tz] = get_offset(tz)
        except ValueError as e:
            return {"error": str(e)}

    # For each timezone, calculate work hours in UTC
    utc_ranges = {}
    for tz, offset in offsets.items():
        utc_start = local_to_utc(work_start, offset)
        utc_end = local_to_utc(work_end, offset)
        utc_ranges[tz] = (utc_start, utc_end)

    # Find overlapping hours
    overlap_hours = []

    for utc_hour in range(24):
        all_working = True
        local_times = {}

        for tz, (utc_start, utc_end) in utc_ranges.items():
            local_hour = utc_to_local(utc_hour, offsets[tz])
            local_times[tz] = local_hour

            # Check if within working hours (handling day wrap)
            if utc_start <= utc_end:
                in_range = utc_start <= utc_hour < utc_end
            else:
                # Wraps around midnight
                in_range = utc_hour >= utc_start or utc_hour < utc_end

            if not in_range:
                all_working = False

        if all_working:
            overlap_hours.append({
                "utc_hour": utc_hour,
                "local_times": {tz: format_hour(h) for tz, h in local_times.items()}
            })

    # Build result
    if overlap_hours:
        # Find best window (most reasonable local times)
        best_window = overlap_hours[0]
        for window in overlap_hours:
            # Prefer hours closer to mid-day for all
            avg_deviation = sum(
                abs(h - 12) for h in
                [utc_to_local(window["utc_hour"], offsets[tz]) for tz in zones]
            )
            best_avg = sum(
                abs(h - 12) for h in
                [utc_to_local(best_window["utc_hour"], offsets[tz]) for tz in zones]
            )
            if avg_deviation < best_avg:
                best_window = window

        result = {
            "timezones": list(zones),
            "work_hours": f"{work_start}:00 - {work_end}:00",
            "overlap_count": len(overlap_hours),
            "recommended": best_window,
            "all_overlap_hours": overlap_hours
        }
    else:
        # No overlap - find least bad options
        least_bad = []
        for utc_hour in range(24):
            local_times = {tz: utc_to_local(utc_hour, offsets[tz]) for tz in zones}
            # Count how many are outside work hours
            bad_count = sum(
                1 for h in local_times.values()
                if h < work_start or h >= work_end
            )
            least_bad.append({
                "utc_hour": utc_hour,
                "outside_work_count": bad_count,
                "local_times": {tz: format_hour(h) for tz, h in local_times.items()}
            })

        least_bad.sort(key=lambda x: x["outside_work_count"])

        result = {
            "timezones": list(zones),
            "work_hours": f"{work_start}:00 - {work_end}:00",
            "overlap_count": 0,
            "message": "No perfect overlap exists",
            "least_bad_options": least_bad[:5]
        }

    return result


def main():
    parser = argparse.ArgumentParser(description="Find meeting overlap windows")
    parser.add_argument("--zones", "-z", required=True,
                        help="Comma-separated timezones")
    parser.add_argument("--work-start", type=int, default=9,
                        help="Work start hour (default 9)")
    parser.add_argument("--work-end", type=int, default=18,
                        help="Work end hour (default 18)")

    args = parser.parse_args()

    zones = [z.strip() for z in args.zones.split(",")]
    result = find_overlap(zones, args.work_start, args.work_end)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
