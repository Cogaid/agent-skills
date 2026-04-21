#!/usr/bin/env python3
"""
Content Tracker -- Track content through workflow stages and identify bottlenecks.

Usage:
    python track_content.py --status all --period this-month
    python track_content.py --status in-review --format markdown
    python track_content.py --add --title "New Blog Post" --author "Jane" --due 2025-06-15
    python track_content.py --bottlenecks --period last-30-days
"""

import argparse
import json
import sys
from datetime import datetime, timedelta

WORKFLOW_STAGES = [
    "backlog",
    "assigned",
    "outline",
    "drafting",
    "in_review",
    "revisions",
    "approved",
    "scheduled",
    "published",
    "promoting",
]

STAGE_SLAS = {
    "backlog": None,
    "assigned": 3,
    "outline": 3,
    "drafting": 7,
    "in_review": 2,
    "revisions": 2,
    "approved": 1,
    "scheduled": None,
    "published": None,
    "promoting": 14,
}

SAMPLE_CONTENT = [
    {
        "id": "CONT-2025-001",
        "title": "Complete Guide to Content Marketing Strategy",
        "type": "Blog Post",
        "pillar": "Educational Content",
        "author": "Sarah Chen",
        "editor": "Mike Johnson",
        "status": "published",
        "keyword": "content marketing strategy",
        "word_count_target": 2500,
        "created": "2025-03-01",
        "due": "2025-03-20",
        "published": "2025-03-18",
        "days_in_pipeline": 17,
    },
    {
        "id": "CONT-2025-002",
        "title": "2025 State of AI in Marketing Report",
        "type": "Research Report",
        "pillar": "Thought Leadership",
        "author": "David Park",
        "editor": "Sarah Chen",
        "status": "in_review",
        "keyword": "AI marketing trends 2025",
        "word_count_target": 4000,
        "created": "2025-03-10",
        "due": "2025-04-05",
        "published": None,
        "days_in_pipeline": 28,
    },
    {
        "id": "CONT-2025-003",
        "title": "How to Build a Content Calendar (Template)",
        "type": "Blog Post",
        "pillar": "Educational Content",
        "author": "Lisa Wong",
        "editor": "Mike Johnson",
        "status": "drafting",
        "keyword": "content calendar template",
        "word_count_target": 1800,
        "created": "2025-03-25",
        "due": "2025-04-10",
        "published": None,
        "days_in_pipeline": 14,
    },
    {
        "id": "CONT-2025-004",
        "title": "Customer Story: How Acme Corp 3x'd Their Blog Traffic",
        "type": "Case Study",
        "pillar": "Product & Features",
        "author": "Sarah Chen",
        "editor": "David Park",
        "status": "revisions",
        "keyword": "content marketing case study",
        "word_count_target": 1200,
        "created": "2025-03-15",
        "due": "2025-04-01",
        "published": None,
        "days_in_pipeline": 24,
    },
    {
        "id": "CONT-2025-005",
        "title": "SEO vs. Paid: Where to Invest Your Marketing Budget",
        "type": "Blog Post",
        "pillar": "Industry Insights",
        "author": "Mike Johnson",
        "editor": "Lisa Wong",
        "status": "approved",
        "keyword": "SEO vs paid advertising",
        "word_count_target": 2000,
        "created": "2025-03-05",
        "due": "2025-03-25",
        "published": None,
        "days_in_pipeline": 33,
    },
    {
        "id": "CONT-2025-006",
        "title": "Content Pillars: The Foundation of Scalable Content",
        "type": "Blog Post",
        "pillar": "Educational Content",
        "author": "David Park",
        "editor": "Sarah Chen",
        "status": "backlog",
        "keyword": "content pillars strategy",
        "word_count_target": 1500,
        "created": "2025-04-01",
        "due": "2025-04-20",
        "published": None,
        "days_in_pipeline": 7,
    },
    {
        "id": "CONT-2025-007",
        "title": "Video: 5 Mistakes in Your Content Strategy",
        "type": "Video",
        "pillar": "Educational Content",
        "author": "Lisa Wong",
        "editor": "Mike Johnson",
        "status": "outline",
        "keyword": "content strategy mistakes",
        "word_count_target": 800,
        "created": "2025-04-02",
        "due": "2025-04-25",
        "published": None,
        "days_in_pipeline": 6,
    },
    {
        "id": "CONT-2025-008",
        "title": "The Rise of AI-Generated Content: What Marketers Need to Know",
        "type": "Blog Post",
        "pillar": "Thought Leadership",
        "author": "Sarah Chen",
        "editor": "David Park",
        "status": "scheduled",
        "keyword": "AI generated content",
        "word_count_target": 2200,
        "created": "2025-03-08",
        "due": "2025-04-01",
        "published": None,
        "days_in_pipeline": 30,
    },
]


def filter_by_status(content, status):
    """Filter content by status."""
    if status == "all":
        return content
    if status == "active":
        inactive = {"published", "backlog"}
        return [c for c in content if c["status"] not in inactive]
    return [c for c in content if c["status"] == status.replace("-", "_")]


def filter_by_period(content, period):
    """Filter content by time period."""
    today = datetime.now()
    if period == "this-month":
        start = today.replace(day=1)
    elif period == "last-30-days":
        start = today - timedelta(days=30)
    elif period == "this-quarter":
        quarter_start_month = ((today.month - 1) // 3) * 3 + 1
        start = today.replace(month=quarter_start_month, day=1)
    else:
        return content

    return [
        c for c in content
        if datetime.strptime(c["created"], "%Y-%m-%d") >= start
    ]


def identify_bottlenecks(content):
    """Identify pipeline bottlenecks."""
    stage_counts = {}
    stage_ages = {}
    overdue = []

    today = datetime.now()

    for item in content:
        status = item["status"]
        stage_counts[status] = stage_counts.get(status, 0) + 1

        if status not in stage_ages:
            stage_ages[status] = []
        stage_ages[status].append(item["days_in_pipeline"])

        if item.get("due"):
            due_date = datetime.strptime(item["due"], "%Y-%m-%d")
            if due_date < today and item["status"] != "published":
                overdue.append({
                    "id": item["id"],
                    "title": item["title"],
                    "status": item["status"],
                    "due": item["due"],
                    "days_overdue": (today - due_date).days,
                    "author": item["author"],
                })

    bottlenecks = []
    for stage, count in stage_counts.items():
        sla = STAGE_SLAS.get(stage)
        avg_days = sum(stage_ages.get(stage, [0])) / max(len(stage_ages.get(stage, [1])), 1)

        if count >= 3:
            bottlenecks.append({
                "stage": stage,
                "count": count,
                "avg_days_in_stage": round(avg_days, 1),
                "sla_days": sla,
                "severity": "high" if count >= 5 else "medium",
                "recommendation": f"Review items stuck in '{stage}' -- {count} items queued",
            })
        elif sla and avg_days > sla * 2:
            bottlenecks.append({
                "stage": stage,
                "count": count,
                "avg_days_in_stage": round(avg_days, 1),
                "sla_days": sla,
                "severity": "medium",
                "recommendation": f"Items in '{stage}' exceed SLA ({sla} days) by {round(avg_days - sla, 1)} days avg",
            })

    bottlenecks.sort(key=lambda x: 0 if x["severity"] == "high" else 1)

    return {
        "stage_distribution": stage_counts,
        "bottlenecks": bottlenecks,
        "overdue_items": sorted(overdue, key=lambda x: -x["days_overdue"]),
        "total_in_pipeline": sum(1 for c in content if c["status"] not in ("published", "backlog")),
    }


def generate_summary(content):
    """Generate pipeline summary."""
    status_counts = {}
    for item in content:
        status_counts[item["status"]] = status_counts.get(item["status"], 0) + 1

    by_author = {}
    for item in content:
        author = item["author"]
        if author not in by_author:
            by_author[author] = {"total": 0, "active": 0, "published": 0}
        by_author[author]["total"] += 1
        if item["status"] == "published":
            by_author[author]["published"] += 1
        elif item["status"] not in ("backlog",):
            by_author[author]["active"] += 1

    by_pillar = {}
    for item in content:
        pillar = item["pillar"]
        by_pillar[pillar] = by_pillar.get(pillar, 0) + 1

    return {
        "total_items": len(content),
        "by_status": status_counts,
        "by_author": by_author,
        "by_pillar": by_pillar,
        "workflow_stages": WORKFLOW_STAGES,
    }


def render_markdown(data, view="summary"):
    """Render tracker data as markdown."""
    lines = ["# Content Pipeline Status", "", f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}", ""]

    if "summary" in data:
        summary = data["summary"]
        lines.extend([
            "## Pipeline Overview",
            "",
            "| Status | Count |",
            "|--------|-------|",
        ])
        for stage in WORKFLOW_STAGES:
            count = summary["by_status"].get(stage, 0)
            if count > 0:
                lines.append(f"| {stage.replace('_', ' ').title()} | {count} |")
        lines.append("")

        lines.extend(["## By Author", "", "| Author | Active | Published | Total |", "|--------|--------|-----------|-------|"])
        for author, counts in summary["by_author"].items():
            lines.append(f"| {author} | {counts['active']} | {counts['published']} | {counts['total']} |")
        lines.append("")

    if "bottlenecks" in data:
        bn = data["bottlenecks"]
        if bn["bottlenecks"]:
            lines.extend(["## Bottlenecks", ""])
            for b in bn["bottlenecks"]:
                lines.append(f"- **[{b['severity'].upper()}]** {b['recommendation']}")
            lines.append("")

        if bn["overdue_items"]:
            lines.extend(["## Overdue Items", "", "| Title | Status | Due | Days Overdue | Author |", "|-------|--------|-----|-------------|--------|"])
            for item in bn["overdue_items"]:
                lines.append(f"| {item['title'][:40]}... | {item['status']} | {item['due']} | {item['days_overdue']} | {item['author']} |")
            lines.append("")

    if "items" in data:
        lines.extend(["## Content Items", "", "| ID | Title | Status | Author | Due |", "|-----|-------|--------|--------|-----|"])
        for item in data["items"]:
            title = item["title"][:45] + "..." if len(item["title"]) > 45 else item["title"]
            lines.append(f"| {item['id']} | {title} | {item['status']} | {item['author']} | {item.get('due', 'N/A')} |")
        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Track content through workflow stages",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --status all --period this-month
  %(prog)s --status in-review --format markdown
  %(prog)s --bottlenecks --period last-30-days
  %(prog)s --summary
        """,
    )
    parser.add_argument(
        "--status",
        choices=["all", "active", "backlog", "assigned", "outline", "drafting",
                 "in-review", "revisions", "approved", "scheduled", "published", "promoting"],
        help="Filter by content status",
    )
    parser.add_argument(
        "--period",
        choices=["this-month", "last-30-days", "this-quarter", "all"],
        default="all",
        help="Filter by time period",
    )
    parser.add_argument("--bottlenecks", action="store_true", help="Show bottleneck analysis")
    parser.add_argument("--summary", action="store_true", help="Show pipeline summary")
    parser.add_argument(
        "--format",
        choices=["json", "markdown"],
        default="json",
        help="Output format (default: json)",
    )
    parser.add_argument("--output", help="Output file (default: stdout)")

    args = parser.parse_args()

    content = SAMPLE_CONTENT.copy()

    if args.status:
        content = filter_by_status(content, args.status)

    content = filter_by_period(content, args.period)

    result = {"generated_at": datetime.now().isoformat(), "items": content}

    if args.summary or not (args.bottlenecks or args.status):
        result["summary"] = generate_summary(SAMPLE_CONTENT)

    if args.bottlenecks:
        result["bottlenecks"] = identify_bottlenecks(SAMPLE_CONTENT)

    if args.format == "markdown":
        output = render_markdown(result)
    else:
        output = json.dumps(result, indent=2)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Report written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
