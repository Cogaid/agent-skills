#!/usr/bin/env python3
"""
Metrics Formatter -- Format case study results data into presentation-ready tables.

Usage:
    python metrics_formatter.py --metrics '{"response_time": {"before": 4.2, "after": 1.1, "unit": "hours"}}' --format markdown
    python metrics_formatter.py --input metrics.json --format html
    python metrics_formatter.py --input metrics.json --format json --calculate-roi --investment 50000
"""

import argparse
import json
import sys
from datetime import datetime


SAMPLE_METRICS = {
    "response_time": {
        "name": "Average Response Time",
        "before": 4.2,
        "after": 1.1,
        "unit": "hours",
        "direction": "decrease",
    },
    "customer_satisfaction": {
        "name": "Customer Satisfaction (CSAT)",
        "before": 3.2,
        "after": 4.7,
        "unit": "/5",
        "direction": "increase",
    },
    "monthly_revenue": {
        "name": "Monthly Revenue",
        "before": 180000,
        "after": 312000,
        "unit": "$",
        "direction": "increase",
        "is_currency": True,
    },
    "ticket_volume": {
        "name": "Tickets Resolved/Day",
        "before": 45,
        "after": 120,
        "unit": "tickets",
        "direction": "increase",
    },
    "onboarding_time": {
        "name": "Onboarding Time",
        "before": 21,
        "after": 3,
        "unit": "days",
        "direction": "decrease",
    },
}


def calculate_change(before, after, direction="auto"):
    """Calculate the percentage or absolute change between before and after."""
    if before == 0:
        return {"percent_change": None, "absolute_change": after, "direction": "increase"}

    abs_change = after - before
    pct_change = ((after - before) / abs(before)) * 100

    if direction == "auto":
        direction = "increase" if abs_change > 0 else "decrease"

    is_improvement = (direction == "decrease" and abs_change < 0) or (
        direction == "increase" and abs_change > 0
    )

    return {
        "percent_change": round(pct_change, 1),
        "absolute_change": round(abs_change, 2),
        "direction": direction,
        "is_improvement": is_improvement,
    }


def format_value(value, unit="", is_currency=False):
    """Format a value with its unit for display."""
    if is_currency:
        if abs(value) >= 1_000_000:
            return f"${value / 1_000_000:.1f}M"
        elif abs(value) >= 1_000:
            return f"${value / 1_000:.0f}K"
        else:
            return f"${value:,.0f}"
    elif unit.startswith("/"):
        return f"{value}{unit}"
    elif unit:
        return f"{value} {unit}"
    else:
        return str(value)


def format_change(change_data, unit="", is_currency=False):
    """Format a change value for display."""
    pct = change_data["percent_change"]
    abs_val = change_data["absolute_change"]

    if pct is not None:
        sign = "+" if pct > 0 else ""
        pct_str = f"{sign}{pct:.0f}%"
    else:
        pct_str = "N/A"

    if is_currency:
        abs_str = format_value(abs(abs_val), is_currency=True)
        sign = "+" if abs_val > 0 else "-"
        abs_str = f"{sign}{abs_str}"
    else:
        sign = "+" if abs_val > 0 else ""
        abs_str = f"{sign}{abs_val:.1f} {unit}".strip()

    return {"percent": pct_str, "absolute": abs_str}


def process_metrics(metrics_data):
    """Process raw metrics into formatted results."""
    processed = []

    for key, metric in metrics_data.items():
        before = metric["before"]
        after = metric["after"]
        unit = metric.get("unit", "")
        direction = metric.get("direction", "auto")
        is_currency = metric.get("is_currency", False)
        name = metric.get("name", key.replace("_", " ").title())

        change = calculate_change(before, after, direction)
        formatted_change = format_change(change, unit, is_currency)

        processed.append(
            {
                "key": key,
                "name": name,
                "before": format_value(before, unit, is_currency),
                "after": format_value(after, unit, is_currency),
                "change": formatted_change,
                "is_improvement": change["is_improvement"],
                "raw": {
                    "before": before,
                    "after": after,
                    "percent_change": change["percent_change"],
                    "absolute_change": change["absolute_change"],
                },
            }
        )

    return processed


def calculate_roi(metrics_data, investment, period_months=12):
    """Calculate ROI from metrics data."""
    total_savings = 0

    for key, metric in metrics_data.items():
        if metric.get("is_currency"):
            monthly_delta = metric["after"] - metric["before"]
            total_savings += monthly_delta * period_months

    annual_investment = investment * (12 / period_months)

    net_benefit = total_savings - annual_investment
    roi_pct = (net_benefit / annual_investment * 100) if annual_investment > 0 else 0
    payback_months = (
        (investment / (total_savings / period_months))
        if total_savings > 0
        else float("inf")
    )

    return {
        "investment": format_value(investment, is_currency=True),
        "annual_savings": format_value(total_savings, is_currency=True),
        "net_benefit": format_value(net_benefit, is_currency=True),
        "roi_percent": f"{roi_pct:.0f}%",
        "payback_months": f"{payback_months:.1f} months" if payback_months != float("inf") else "N/A",
        "raw": {
            "investment": investment,
            "total_savings": total_savings,
            "net_benefit": net_benefit,
            "roi_percent": round(roi_pct, 1),
            "payback_months": round(payback_months, 1) if payback_months != float("inf") else None,
        },
    }


def render_markdown(processed, roi=None):
    """Render metrics as a markdown table."""
    lines = ["## Results at a Glance", "", "| Metric | Before | After | Change |", "|--------|--------|-------|--------|"]

    for m in processed:
        status = "+" if m["is_improvement"] else "-"
        lines.append(
            f"| {m['name']} | {m['before']} | {m['after']} | {m['change']['percent']} |"
        )

    if roi:
        lines.extend([
            "",
            "## ROI Analysis",
            "",
            "| Item | Amount |",
            "|------|--------|",
            f"| Annual Investment | {roi['investment']} |",
            f"| Annual Savings | {roi['annual_savings']} |",
            f"| Net Annual Benefit | {roi['net_benefit']} |",
            f"| ROI | {roi['roi_percent']} |",
            f"| Payback Period | {roi['payback_months']} |",
        ])

    lines.extend([
        "",
        "## Headline Metrics",
        "",
    ])

    for m in processed:
        if m["is_improvement"]:
            lines.append(f"- **{m['change']['percent']}** {m['name'].lower()}")

    return "\n".join(lines)


def render_html(processed, roi=None):
    """Render metrics as an HTML table."""
    rows = ""
    for m in processed:
        color = "green" if m["is_improvement"] else "red"
        rows += (
            f"  <tr>\n"
            f"    <td>{m['name']}</td>\n"
            f"    <td>{m['before']}</td>\n"
            f"    <td>{m['after']}</td>\n"
            f'    <td style="color: {color}">{m["change"]["percent"]}</td>\n'
            f"  </tr>\n"
        )

    return (
        "<table>\n"
        "  <thead>\n"
        "    <tr><th>Metric</th><th>Before</th><th>After</th><th>Change</th></tr>\n"
        "  </thead>\n"
        f"  <tbody>\n{rows}  </tbody>\n"
        "</table>"
    )


def main():
    parser = argparse.ArgumentParser(
        description="Format case study metrics into presentation-ready tables",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --sample --format markdown
  %(prog)s --input metrics.json --format json
  %(prog)s --input metrics.json --format markdown --calculate-roi --investment 50000
        """,
    )
    parser.add_argument("--input", help="JSON file with metrics data")
    parser.add_argument(
        "--metrics", help="Inline JSON string with metrics data"
    )
    parser.add_argument(
        "--sample", action="store_true", help="Use sample metrics data for demonstration"
    )
    parser.add_argument(
        "--format",
        choices=["json", "markdown", "html"],
        default="json",
        help="Output format (default: json)",
    )
    parser.add_argument(
        "--calculate-roi", action="store_true", help="Include ROI calculation"
    )
    parser.add_argument(
        "--investment",
        type=float,
        default=0,
        help="Annual investment amount for ROI calculation",
    )
    parser.add_argument("--output", help="Output file (default: stdout)")

    args = parser.parse_args()

    if args.sample:
        metrics_data = SAMPLE_METRICS
    elif args.input:
        with open(args.input) as f:
            metrics_data = json.load(f)
    elif args.metrics:
        metrics_data = json.loads(args.metrics)
    else:
        parser.error("One of --input, --metrics, or --sample is required")
        return

    processed = process_metrics(metrics_data)

    roi = None
    if args.calculate_roi and args.investment > 0:
        roi = calculate_roi(metrics_data, args.investment)

    if args.format == "markdown":
        output = render_markdown(processed, roi)
    elif args.format == "html":
        output = render_html(processed, roi)
    else:
        result = {
            "generated_at": datetime.now().isoformat(),
            "metrics": processed,
        }
        if roi:
            result["roi"] = roi
        output = json.dumps(result, indent=2)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Formatted metrics written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
