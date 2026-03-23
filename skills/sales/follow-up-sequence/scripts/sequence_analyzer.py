#!/usr/bin/env python3
"""
Analyze follow-up sequence performance metrics.

Usage:
    python sequence_analyzer.py sequence_data.json
    python sequence_analyzer.py --report summary sequence_data.json
    python sequence_analyzer.py --compare seq1.json seq2.json

Output: Performance analysis and optimization recommendations
"""

import argparse
import json
import sys
from collections import defaultdict


# Industry benchmarks
BENCHMARKS = {
    "cold_outreach": {
        "open_rate": {"good": 0.25, "great": 0.40},
        "reply_rate": {"good": 0.05, "great": 0.10},
        "meeting_rate": {"good": 0.02, "great": 0.05},
        "conversion_rate": {"good": 0.01, "great": 0.03}
    },
    "post_meeting": {
        "open_rate": {"good": 0.60, "great": 0.80},
        "reply_rate": {"good": 0.30, "great": 0.50},
        "next_stage_rate": {"good": 0.40, "great": 0.60}
    },
    "re_engagement": {
        "open_rate": {"good": 0.20, "great": 0.35},
        "reply_rate": {"good": 0.03, "great": 0.08},
        "meeting_rate": {"good": 0.01, "great": 0.03}
    }
}


def load_data(file_path):
    """Load sequence performance data."""
    with open(file_path, 'r') as f:
        return json.load(f)


def calculate_metrics(data):
    """Calculate key performance metrics."""

    total_sequences = len(data.get("sequences", [data]))
    total_sent = sum(s.get("emails_sent", 0) for s in data.get("sequences", [data]))
    total_opened = sum(s.get("emails_opened", 0) for s in data.get("sequences", [data]))
    total_replied = sum(s.get("replies", 0) for s in data.get("sequences", [data]))
    total_meetings = sum(s.get("meetings_booked", 0) for s in data.get("sequences", [data]))

    metrics = {
        "total_sequences": total_sequences,
        "total_emails_sent": total_sent,
        "total_opened": total_opened,
        "total_replies": total_replied,
        "total_meetings": total_meetings,
        "open_rate": round(total_opened / total_sent, 4) if total_sent else 0,
        "reply_rate": round(total_replied / total_sent, 4) if total_sent else 0,
        "meeting_rate": round(total_meetings / total_sent, 4) if total_sent else 0,
        "reply_to_meeting": round(total_meetings / total_replied, 4) if total_replied else 0
    }

    return metrics


def analyze_by_touch(data):
    """Analyze performance by touch number."""

    touch_data = defaultdict(lambda: {
        "sent": 0, "opened": 0, "replied": 0, "meetings": 0
    })

    for seq in data.get("sequences", [data]):
        for touch in seq.get("touches", []):
            num = touch.get("touch_number", 0)
            touch_data[num]["sent"] += touch.get("sent", 0)
            touch_data[num]["opened"] += touch.get("opened", 0)
            touch_data[num]["replied"] += touch.get("replied", 0)
            touch_data[num]["meetings"] += touch.get("meetings", 0)

    # Calculate rates
    results = {}
    for num, data in sorted(touch_data.items()):
        sent = data["sent"]
        results[f"touch_{num}"] = {
            "sent": sent,
            "opened": data["opened"],
            "replied": data["replied"],
            "open_rate": round(data["opened"] / sent, 4) if sent else 0,
            "reply_rate": round(data["replied"] / sent, 4) if sent else 0,
            "meetings": data["meetings"]
        }

    return results


def analyze_by_subject(data):
    """Analyze performance by subject line."""

    subject_data = defaultdict(lambda: {
        "sent": 0, "opened": 0, "replied": 0
    })

    for seq in data.get("sequences", [data]):
        for touch in seq.get("touches", []):
            subject = touch.get("subject", "Unknown")
            subject_data[subject]["sent"] += touch.get("sent", 0)
            subject_data[subject]["opened"] += touch.get("opened", 0)
            subject_data[subject]["replied"] += touch.get("replied", 0)

    # Sort by open rate
    results = []
    for subject, data in subject_data.items():
        sent = data["sent"]
        if sent >= 10:  # Minimum sample size
            results.append({
                "subject": subject,
                "sent": sent,
                "open_rate": round(data["opened"] / sent, 4),
                "reply_rate": round(data["replied"] / sent, 4)
            })

    return sorted(results, key=lambda x: -x["open_rate"])


def compare_to_benchmarks(metrics, sequence_type="cold_outreach"):
    """Compare metrics to industry benchmarks."""

    benchmarks = BENCHMARKS.get(sequence_type, BENCHMARKS["cold_outreach"])
    comparison = {}

    for metric, thresholds in benchmarks.items():
        if metric in metrics:
            value = metrics[metric]
            if value >= thresholds["great"]:
                status = "great"
                icon = "🟢"
            elif value >= thresholds["good"]:
                status = "good"
                icon = "🟡"
            else:
                status = "below_target"
                icon = "🔴"

            comparison[metric] = {
                "value": value,
                "status": status,
                "icon": icon,
                "good_threshold": thresholds["good"],
                "great_threshold": thresholds["great"]
            }

    return comparison


def identify_drop_offs(touch_analysis):
    """Identify where prospects are dropping off."""

    drop_offs = []
    prev_rate = 1.0

    for touch_key in sorted(touch_analysis.keys()):
        data = touch_analysis[touch_key]
        current_rate = data.get("reply_rate", 0)

        if prev_rate > 0:
            drop_rate = (prev_rate - current_rate) / prev_rate
            if drop_rate > 0.5:  # More than 50% drop
                drop_offs.append({
                    "touch": touch_key,
                    "drop_percentage": round(drop_rate * 100, 1),
                    "current_reply_rate": current_rate
                })

        prev_rate = current_rate

    return drop_offs


def generate_recommendations(metrics, touch_analysis, benchmark_comparison):
    """Generate optimization recommendations."""

    recommendations = []

    # Check open rates
    if metrics.get("open_rate", 0) < 0.25:
        recommendations.append({
            "priority": "high",
            "area": "Subject Lines",
            "issue": f"Open rate ({metrics['open_rate']:.1%}) is below 25%",
            "suggestions": [
                "Test shorter subject lines (4-7 words)",
                "Add personalization (name, company)",
                "Try question format subject lines",
                "A/B test urgency vs. curiosity approaches"
            ]
        })

    # Check reply rates
    if metrics.get("reply_rate", 0) < 0.05:
        recommendations.append({
            "priority": "high",
            "area": "Email Copy",
            "issue": f"Reply rate ({metrics['reply_rate']:.1%}) is below 5%",
            "suggestions": [
                "Shorten emails to under 100 words",
                "Add a clear, single CTA",
                "Include more personalization",
                "Lead with value, not pitch"
            ]
        })

    # Check meeting conversion
    if metrics.get("reply_to_meeting", 0) < 0.30:
        recommendations.append({
            "priority": "medium",
            "area": "Follow-Through",
            "issue": f"Reply-to-meeting rate ({metrics['reply_to_meeting']:.1%}) is low",
            "suggestions": [
                "Respond faster to replies (under 1 hour)",
                "Include calendar link in responses",
                "Be more specific with meeting ask",
                "Provide 2-3 time options"
            ]
        })

    # Check specific touch performance
    for touch_key, data in touch_analysis.items():
        if data.get("reply_rate", 0) == 0 and data.get("sent", 0) >= 50:
            recommendations.append({
                "priority": "medium",
                "area": f"Touch {touch_key.replace('touch_', '')}",
                "issue": f"No replies from {touch_key} ({data['sent']} sent)",
                "suggestions": [
                    "Completely rewrite this touch",
                    "Try different value proposition",
                    "Change the channel for this touch",
                    "Consider removing or replacing"
                ]
            })

    # Add benchmark-based recommendations
    for metric, comparison in benchmark_comparison.items():
        if comparison["status"] == "below_target":
            recommendations.append({
                "priority": "medium",
                "area": metric.replace("_", " ").title(),
                "issue": f"{metric} at {comparison['value']:.1%}, target is {comparison['good_threshold']:.1%}+",
                "suggestions": [
                    f"Focus on improving {metric} as priority",
                    "Study high-performing sequences in your space",
                    "Test new approaches for 2 weeks before evaluating"
                ]
            })

    return recommendations


def generate_report(analysis, format_type="text"):
    """Generate formatted analysis report."""

    if format_type == "json":
        return json.dumps(analysis, indent=2)

    lines = []
    lines.append("\n" + "=" * 60)
    lines.append("SEQUENCE PERFORMANCE ANALYSIS")
    lines.append("=" * 60)

    # Overall metrics
    if "metrics" in analysis:
        metrics = analysis["metrics"]
        lines.append("\n--- OVERALL METRICS ---")
        lines.append(f"Sequences Analyzed: {metrics.get('total_sequences', 0)}")
        lines.append(f"Emails Sent: {metrics.get('total_emails_sent', 0)}")
        lines.append(f"Open Rate: {metrics.get('open_rate', 0):.1%}")
        lines.append(f"Reply Rate: {metrics.get('reply_rate', 0):.1%}")
        lines.append(f"Meeting Rate: {metrics.get('meeting_rate', 0):.1%}")

    # Benchmark comparison
    if "benchmark_comparison" in analysis:
        lines.append("\n--- VS BENCHMARKS ---")
        for metric, data in analysis["benchmark_comparison"].items():
            lines.append(f"{data['icon']} {metric}: {data['value']:.1%} ({data['status']})")

    # Touch analysis
    if "touch_analysis" in analysis:
        lines.append("\n--- PERFORMANCE BY TOUCH ---")
        for touch, data in analysis["touch_analysis"].items():
            lines.append(f"  {touch}: Open {data['open_rate']:.1%} | Reply {data['reply_rate']:.1%}")

    # Top subjects
    if "subject_analysis" in analysis and analysis["subject_analysis"]:
        lines.append("\n--- TOP SUBJECT LINES ---")
        for i, subject in enumerate(analysis["subject_analysis"][:5], 1):
            lines.append(f"  {i}. \"{subject['subject'][:40]}...\"")
            lines.append(f"     Open: {subject['open_rate']:.1%} | Reply: {subject['reply_rate']:.1%}")

    # Recommendations
    if "recommendations" in analysis:
        lines.append("\n--- RECOMMENDATIONS ---")
        for rec in sorted(analysis["recommendations"], key=lambda x: x["priority"]):
            lines.append(f"\n[{rec['priority'].upper()}] {rec['area']}")
            lines.append(f"  Issue: {rec['issue']}")
            lines.append("  Suggestions:")
            for suggestion in rec["suggestions"][:3]:
                lines.append(f"    • {suggestion}")

    lines.append("\n" + "=" * 60)
    return "\n".join(lines)


def compare_sequences(data1, data2):
    """Compare two sequences side by side."""

    metrics1 = calculate_metrics(data1)
    metrics2 = calculate_metrics(data2)

    comparison = {
        "sequence_a": {
            "name": data1.get("name", "Sequence A"),
            "metrics": metrics1
        },
        "sequence_b": {
            "name": data2.get("name", "Sequence B"),
            "metrics": metrics2
        },
        "winner": {},
        "improvements": {}
    }

    # Determine winners
    for key in ["open_rate", "reply_rate", "meeting_rate"]:
        if metrics1.get(key, 0) > metrics2.get(key, 0):
            comparison["winner"][key] = "sequence_a"
            diff = metrics1[key] - metrics2[key]
        else:
            comparison["winner"][key] = "sequence_b"
            diff = metrics2[key] - metrics1[key]
        comparison["improvements"][key] = round(diff, 4)

    return comparison


def main():
    parser = argparse.ArgumentParser(description='Analyze sequence performance')
    parser.add_argument('file', nargs='?', help='Sequence data file (JSON)')
    parser.add_argument('--report', '-r', choices=['summary', 'detailed', 'touch'],
                        default='summary', help='Report type')
    parser.add_argument('--compare', '-c', nargs=2, metavar='FILE',
                        help='Compare two sequence files')
    parser.add_argument('--format', '-f', choices=['json', 'text'],
                        default='text', help='Output format')
    parser.add_argument('--benchmark', '-b', choices=['cold_outreach', 'post_meeting', 're_engagement'],
                        default='cold_outreach', help='Benchmark type')
    parser.add_argument('--sample', '-s', action='store_true',
                        help='Generate sample data')

    args = parser.parse_args()

    if args.sample:
        sample_data = {
            "name": "Cold Outreach Q1",
            "sequences": [
                {
                    "emails_sent": 500,
                    "emails_opened": 175,
                    "replies": 35,
                    "meetings_booked": 12,
                    "touches": [
                        {"touch_number": 1, "subject": "Quick question about growth", "sent": 500, "opened": 150, "replied": 20, "meetings": 8},
                        {"touch_number": 2, "subject": "Re: Quick question", "sent": 480, "opened": 100, "replied": 8, "meetings": 2},
                        {"touch_number": 3, "subject": "Worth 10 minutes?", "sent": 472, "opened": 80, "replied": 5, "meetings": 1},
                        {"touch_number": 4, "subject": "Case study inside", "sent": 467, "opened": 70, "replied": 2, "meetings": 1}
                    ]
                }
            ]
        }
        print(json.dumps(sample_data, indent=2))
        return

    if args.compare:
        try:
            data1 = load_data(args.compare[0])
            data2 = load_data(args.compare[1])
            result = compare_sequences(data1, data2)
            print(json.dumps(result, indent=2) if args.format == "json" else generate_report({"comparison": result}))
        except Exception as e:
            print(json.dumps({"error": str(e)}))
        return

    if not args.file:
        parser.print_help()
        return

    try:
        data = load_data(args.file)
    except FileNotFoundError:
        print(json.dumps({"error": f"File not found: {args.file}"}))
        sys.exit(1)

    # Run analysis
    metrics = calculate_metrics(data)
    touch_analysis = analyze_by_touch(data)
    subject_analysis = analyze_by_subject(data)
    benchmark_comparison = compare_to_benchmarks(metrics, args.benchmark)
    recommendations = generate_recommendations(metrics, touch_analysis, benchmark_comparison)

    analysis = {
        "metrics": metrics,
        "touch_analysis": touch_analysis,
        "subject_analysis": subject_analysis[:10],  # Top 10
        "benchmark_comparison": benchmark_comparison,
        "recommendations": recommendations
    }

    print(generate_report(analysis, args.format))


if __name__ == '__main__':
    main()
