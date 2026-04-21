#!/usr/bin/env python3
"""Track inbox management metrics over time.

Usage:
    python inbox_metrics.py --period this-week
    python inbox_metrics.py --period last-month --format json
"""

import argparse
import json
import sys
from datetime import datetime, timedelta

SAMPLE_DAILY_METRICS = [
    {"date": "Mon", "inbox_start": 23, "inbox_end": 2, "processed": 45, "avg_response_h": 3.2, "unsubscribes": 1, "filters_created": 0},
    {"date": "Tue", "inbox_start": 2, "inbox_end": 0, "processed": 38, "avg_response_h": 2.8, "unsubscribes": 0, "filters_created": 1},
    {"date": "Wed", "inbox_start": 0, "inbox_end": 3, "processed": 52, "avg_response_h": 4.1, "unsubscribes": 2, "filters_created": 0},
    {"date": "Thu", "inbox_start": 3, "inbox_end": 1, "processed": 41, "avg_response_h": 2.5, "unsubscribes": 0, "filters_created": 1},
    {"date": "Fri", "inbox_start": 1, "inbox_end": 0, "processed": 35, "avg_response_h": 3.0, "unsubscribes": 1, "filters_created": 0},
]

SAMPLE_CATEGORY_BREAKDOWN = {
    "Action Required": 42,
    "Waiting For": 18,
    "Delegated": 12,
    "FYI/Read": 35,
    "Archived": 68,
    "Deleted/Unsubscribed": 36,
}


def compute_weekly_metrics(daily: list) -> dict:
    """Compute aggregate weekly metrics."""
    total_processed = sum(d["processed"] for d in daily)
    avg_inbox_eod = sum(d["inbox_end"] for d in daily) / len(daily)
    avg_response = sum(d["avg_response_h"] for d in daily) / len(daily)
    total_unsubs = sum(d["unsubscribes"] for d in daily)
    total_filters = sum(d["filters_created"] for d in daily)
    inbox_zero_days = sum(1 for d in daily if d["inbox_end"] <= 5)
    inbox_zero_rate = (inbox_zero_days / len(daily)) * 100

    return {
        "period": "this-week",
        "days_tracked": len(daily),
        "total_emails_processed": total_processed,
        "avg_daily_volume": round(total_processed / len(daily), 1),
        "avg_inbox_count_eod": round(avg_inbox_eod, 1),
        "inbox_zero_days": inbox_zero_days,
        "inbox_zero_rate": f"{inbox_zero_rate:.0f}%",
        "avg_response_time_hours": round(avg_response, 1),
        "unsubscribes_this_week": total_unsubs,
        "filters_created_this_week": total_filters,
        "category_breakdown": SAMPLE_CATEGORY_BREAKDOWN,
        "targets": {
            "inbox_zero_rate": ">80%",
            "avg_response_time": "<24h",
            "processing_time_per_email": "<30s",
        },
    }


def main():
    parser = argparse.ArgumentParser(description="Track inbox management metrics.")
    parser.add_argument("--period", default="this-week", choices=["today", "this-week", "last-week", "this-month", "last-month"], help="Reporting period")
    parser.add_argument("--format", choices=["text", "json"], default="text", help="Output format")

    args = parser.parse_args()

    metrics = compute_weekly_metrics(SAMPLE_DAILY_METRICS)
    metrics["period"] = args.period
    metrics["generated_at"] = datetime.now().isoformat()

    if args.format == "json":
        print(json.dumps(metrics, indent=2))
    else:
        print("Inbox Management Metrics")
        print(f"Period: {args.period}")
        print("=" * 50)
        print(f"\n  Emails Processed:      {metrics['total_emails_processed']}")
        print(f"  Avg Daily Volume:      {metrics['avg_daily_volume']}")
        print(f"  Avg Inbox Count (EOD): {metrics['avg_inbox_count_eod']}")
        print(f"  Inbox Zero Days:       {metrics['inbox_zero_days']}/{metrics['days_tracked']}")
        print(f"  Inbox Zero Rate:       {metrics['inbox_zero_rate']}")
        print(f"  Avg Response Time:     {metrics['avg_response_time_hours']}h")
        print(f"  Unsubscribes:          {metrics['unsubscribes_this_week']}")
        print(f"  Filters Created:       {metrics['filters_created_this_week']}")
        print(f"\n  Category Breakdown:")
        for cat, count in SAMPLE_CATEGORY_BREAKDOWN.items():
            bar = "#" * (count // 3)
            print(f"    {cat:25s} {count:3d} {bar}")
        print(f"\n  Daily Detail:")
        for d in SAMPLE_DAILY_METRICS:
            status = "ZERO" if d["inbox_end"] == 0 else f"{d['inbox_end']} remaining"
            print(f"    {d['date']}: {d['processed']} processed, EOD: {status}")
        print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
