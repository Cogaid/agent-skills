#!/usr/bin/env python3
"""
Content Calendar Planner -- Generate content calendars from pillars and goals.

Usage:
    python plan_calendar.py --period Q2-2025 --pillars 4 --frequency weekly
    python plan_calendar.py --period 2025-05 --pillars 3 --frequency daily --output calendar.json
    python plan_calendar.py --period Q3-2025 --pillars 4 --frequency weekly --format markdown
"""

import argparse
import json
import sys
from datetime import datetime, timedelta

SAMPLE_PILLARS = [
    {
        "name": "Product & Features",
        "target_pct": 10,
        "topics": [
            "Product updates", "Feature deep-dives", "How-to guides",
            "Integration tutorials", "Use case showcases",
        ],
    },
    {
        "name": "Industry Insights",
        "target_pct": 30,
        "topics": [
            "Trend analysis", "Market reports", "Expert interviews",
            "Conference recaps", "Predictions",
        ],
    },
    {
        "name": "Educational Content",
        "target_pct": 40,
        "topics": [
            "Beginner guides", "Best practices", "Frameworks",
            "Tutorials", "Comparison guides", "Checklists",
        ],
    },
    {
        "name": "Thought Leadership",
        "target_pct": 20,
        "topics": [
            "Original research", "Opinion pieces", "Case studies",
            "Behind the scenes", "Founder stories",
        ],
    },
]

CONTENT_TYPES = [
    {"type": "Blog Post", "channel": "Website", "effort_hours": 5},
    {"type": "Newsletter", "channel": "Email", "effort_hours": 3},
    {"type": "Social Post", "channel": "LinkedIn", "effort_hours": 1},
    {"type": "Social Post", "channel": "Twitter", "effort_hours": 0.5},
    {"type": "Video", "channel": "YouTube", "effort_hours": 12},
]

FREQUENCY_CONFIGS = {
    "daily": {
        "blog_per_week": 5,
        "newsletter_per_week": 3,
        "social_per_week": 14,
        "video_per_month": 8,
    },
    "weekly": {
        "blog_per_week": 2,
        "newsletter_per_week": 1,
        "social_per_week": 7,
        "video_per_month": 2,
    },
    "biweekly": {
        "blog_per_week": 1,
        "newsletter_per_week": 0.5,
        "social_per_week": 5,
        "video_per_month": 1,
    },
}

SEASONAL_THEMES = {
    1: "New Year, Planning, Trends & Predictions",
    2: "Love & Partnerships, Industry Awards",
    3: "Spring Renewal, Women in Industry",
    4: "Tax Season, Earth Day, Spring Cleaning",
    5: "Midyear Check-in, Conference Season",
    6: "Pride, Summer Kickoff, Midyear Reviews",
    7: "Independence, Q3 Planning, Summer",
    8: "Back to School, Fall Planning",
    9: "Labor Day, Productivity, Q4 Prep",
    10: "Halloween, Cybersecurity, Open Enrollment",
    11: "Thanksgiving, Black Friday, Gratitude",
    12: "Holidays, Year in Review, Planning Ahead",
}


def parse_period(period_str):
    """Parse period string into start and end dates."""
    if period_str.startswith("Q"):
        parts = period_str.split("-")
        quarter = int(parts[0][1])
        year = int(parts[1])
        start_month = (quarter - 1) * 3 + 1
        start = datetime(year, start_month, 1)
        end_month = start_month + 2
        if end_month == 12:
            end = datetime(year, 12, 31)
        else:
            end = datetime(year, end_month + 1, 1) - timedelta(days=1)
        period_type = "quarter"
    else:
        parts = period_str.split("-")
        year = int(parts[0])
        month = int(parts[1])
        start = datetime(year, month, 1)
        if month == 12:
            end = datetime(year, 12, 31)
        else:
            end = datetime(year, month + 1, 1) - timedelta(days=1)
        period_type = "month"

    return start, end, period_type


def generate_weeks(start, end):
    """Generate week boundaries within a period."""
    weeks = []
    current = start
    while current <= end:
        week_end = min(current + timedelta(days=6), end)
        weeks.append({"start": current, "end": week_end, "number": len(weeks) + 1})
        current = week_end + timedelta(days=1)
    return weeks


def assign_pillar(week_num, pillars):
    """Assign a primary pillar focus for a week."""
    idx = (week_num - 1) % len(pillars)
    return pillars[idx]


def generate_calendar(start, end, pillars, frequency_config, num_pillars):
    """Generate a complete content calendar."""
    used_pillars = pillars[:num_pillars]
    weeks = generate_weeks(start, end)
    freq = FREQUENCY_CONFIGS[frequency_config]

    calendar = {
        "period": {
            "start": start.strftime("%Y-%m-%d"),
            "end": end.strftime("%Y-%m-%d"),
            "weeks": len(weeks),
        },
        "pillars": [
            {"name": p["name"], "target_pct": p["target_pct"]}
            for p in used_pillars
        ],
        "frequency": frequency_config,
        "targets": {
            "blog_posts_per_week": freq["blog_per_week"],
            "newsletters_per_week": freq["newsletter_per_week"],
            "social_posts_per_week": freq["social_per_week"],
            "videos_per_month": freq["video_per_month"],
        },
        "weeks": [],
        "monthly_themes": {},
    }

    # Add monthly themes
    current_month = start.month
    while current_month <= end.month or (end.year > start.year):
        month_key = current_month if current_month <= 12 else current_month - 12
        calendar["monthly_themes"][str(month_key)] = SEASONAL_THEMES.get(month_key, "")
        current_month += 1
        if current_month > end.month and end.year == start.year:
            break
        if current_month > 12:
            break

    # Generate weekly plans
    for week in weeks:
        pillar = assign_pillar(week["number"], used_pillars)
        topic_idx = (week["number"] - 1) % len(pillar["topics"])

        week_plan = {
            "week_number": week["number"],
            "start": week["start"].strftime("%Y-%m-%d"),
            "end": week["end"].strftime("%Y-%m-%d"),
            "primary_pillar": pillar["name"],
            "theme": pillar["topics"][topic_idx],
            "content": [],
        }

        # Blog posts
        for i in range(int(freq["blog_per_week"])):
            topic = pillar["topics"][(topic_idx + i) % len(pillar["topics"])]
            week_plan["content"].append({
                "type": "Blog Post",
                "channel": "Website",
                "pillar": pillar["name"],
                "suggested_topic": f"[{topic}] -- {pillar['name']}",
                "status": "backlog",
                "day": ["Monday", "Wednesday", "Friday"][i % 3],
            })

        # Newsletter
        if freq["newsletter_per_week"] >= 1:
            week_plan["content"].append({
                "type": "Newsletter",
                "channel": "Email",
                "pillar": pillar["name"],
                "suggested_topic": f"Weekly roundup: {pillar['topics'][topic_idx]}",
                "status": "backlog",
                "day": "Tuesday",
            })

        # Social posts
        social_count = min(int(freq["social_per_week"]), 7)
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        for i in range(social_count):
            platform = ["LinkedIn", "Twitter", "LinkedIn", "Twitter", "LinkedIn", "Instagram", "Twitter"][i % 7]
            week_plan["content"].append({
                "type": "Social Post",
                "channel": platform,
                "pillar": pillar["name"],
                "suggested_topic": f"Key insight from {pillar['topics'][(topic_idx + i) % len(pillar['topics'])]}",
                "status": "backlog",
                "day": days[i % 7],
            })

        # Video (first week of each month)
        if week["number"] % 4 == 1 and freq["video_per_month"] >= 1:
            week_plan["content"].append({
                "type": "Video",
                "channel": "YouTube",
                "pillar": pillar["name"],
                "suggested_topic": f"Deep dive: {pillar['topics'][topic_idx]}",
                "status": "backlog",
                "day": "Thursday",
            })

        calendar["weeks"].append(week_plan)

    # Calculate totals
    total_content = sum(len(w["content"]) for w in calendar["weeks"])
    calendar["summary"] = {
        "total_content_pieces": total_content,
        "total_weeks": len(weeks),
        "avg_pieces_per_week": round(total_content / max(len(weeks), 1), 1),
    }

    return calendar


def render_markdown(calendar):
    """Render calendar as markdown."""
    lines = [
        "# Content Calendar",
        "",
        f"**Period:** {calendar['period']['start']} to {calendar['period']['end']}",
        f"**Frequency:** {calendar['frequency']}",
        f"**Total Weeks:** {calendar['period']['weeks']}",
        f"**Total Pieces Planned:** {calendar['summary']['total_content_pieces']}",
        "",
        "## Pillars",
        "",
        "| Pillar | Target % |",
        "|--------|----------|",
    ]
    for p in calendar["pillars"]:
        lines.append(f"| {p['name']} | {p['target_pct']}% |")

    lines.extend(["", "## Weekly Targets", ""])
    for key, val in calendar["targets"].items():
        lines.append(f"- {key.replace('_', ' ').title()}: {val}")

    lines.extend(["", "---", ""])

    for week in calendar["weeks"]:
        lines.extend([
            f"## Week {week['week_number']}: {week['start']} to {week['end']}",
            f"**Pillar:** {week['primary_pillar']} | **Theme:** {week['theme']}",
            "",
            "| Day | Type | Channel | Topic | Status |",
            "|-----|------|---------|-------|--------|",
        ])
        for item in week["content"]:
            lines.append(
                f"| {item['day']} | {item['type']} | {item['channel']} | "
                f"{item['suggested_topic']} | {item['status']} |"
            )
        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Generate content calendars from pillars and goals",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --period Q2-2025 --pillars 4 --frequency weekly
  %(prog)s --period 2025-05 --pillars 3 --frequency daily --output calendar.json
  %(prog)s --period Q3-2025 --pillars 4 --frequency biweekly --format markdown
        """,
    )
    parser.add_argument(
        "--period", required=True,
        help="Time period (e.g., Q2-2025, 2025-05)",
    )
    parser.add_argument(
        "--pillars", type=int, default=4, choices=[2, 3, 4, 5],
        help="Number of content pillars (default: 4)",
    )
    parser.add_argument(
        "--frequency",
        choices=["daily", "weekly", "biweekly"],
        default="weekly",
        help="Publishing frequency (default: weekly)",
    )
    parser.add_argument(
        "--format",
        choices=["json", "markdown"],
        default="json",
        help="Output format (default: json)",
    )
    parser.add_argument("--output", help="Output file (default: stdout)")

    args = parser.parse_args()

    start, end, period_type = parse_period(args.period)
    calendar = generate_calendar(start, end, SAMPLE_PILLARS, args.frequency, args.pillars)

    result = {
        "generated_at": datetime.now().isoformat(),
        "calendar": calendar,
    }

    if args.format == "markdown":
        output = render_markdown(calendar)
    else:
        output = json.dumps(result, indent=2, default=str)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Calendar written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
