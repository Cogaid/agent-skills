#!/usr/bin/env python3
"""Sprint velocity tracker and analyzer.

Tracks velocity across sprints, identifies trends, and recommends
commitment levels for upcoming sprints.

Usage:
    python velocity_tracker.py --sprints "30,36,38,35,40"
    python velocity_tracker.py --sprints "30,36,38,35" --planned "34,38,40,42"
    python velocity_tracker.py --sprints "30,36,38,35" --target 38 --json
"""

import argparse
import json
import sys


def analyze_velocity(completed, planned=None):
    """Analyze velocity data and produce statistics and trends."""
    n = len(completed)
    if n == 0:
        return {"error": "No velocity data provided"}

    avg = sum(completed) / n
    sorted_vals = sorted(completed)
    median = sorted_vals[n // 2]

    # Calculate trend (simple linear regression slope)
    if n >= 2:
        x_mean = (n - 1) / 2
        y_mean = avg
        numerator = sum((i - x_mean) * (completed[i] - y_mean) for i in range(n))
        denominator = sum((i - x_mean) ** 2 for i in range(n))
        slope = numerator / denominator if denominator != 0 else 0
        if slope > 0.5:
            trend = "increasing"
        elif slope < -0.5:
            trend = "decreasing"
        else:
            trend = "stable"
    else:
        slope = 0
        trend = "insufficient data"

    # Variability
    variance = sum((v - avg) ** 2 for v in completed) / n if n > 1 else 0
    std_dev = variance ** 0.5
    coefficient_of_variation = (std_dev / avg * 100) if avg > 0 else 0

    if coefficient_of_variation < 10:
        stability = "very stable"
    elif coefficient_of_variation < 20:
        stability = "stable"
    elif coefficient_of_variation < 30:
        stability = "moderate"
    else:
        stability = "volatile"

    result = {
        "summary": {
            "sprints_analyzed": n,
            "average": round(avg, 1),
            "median": median,
            "min": min(completed),
            "max": max(completed),
            "std_dev": round(std_dev, 1),
            "coefficient_of_variation": round(coefficient_of_variation, 1),
            "stability": stability,
            "trend": trend,
            "trend_slope": round(slope, 2),
        },
        "recommendation": {
            "conservative": round(avg * 0.85),
            "moderate": round(avg * 0.90),
            "aggressive": round(avg),
            "stretch": round(avg * 1.10),
        },
        "sprints": [],
    }

    for i, comp in enumerate(completed):
        sprint_data = {
            "sprint": i + 1,
            "completed": comp,
        }
        if planned and i < len(planned):
            sprint_data["planned"] = planned[i]
            sprint_data["carry_over"] = max(0, planned[i] - comp)
            sprint_data["accuracy"] = round((comp / planned[i]) * 100, 1) if planned[i] > 0 else 0
        result["sprints"].append(sprint_data)

    if planned:
        accuracies = [s["accuracy"] for s in result["sprints"] if "accuracy" in s]
        result["planning_accuracy"] = {
            "average": round(sum(accuracies) / len(accuracies), 1) if accuracies else 0,
            "total_carry_over": sum(s.get("carry_over", 0) for s in result["sprints"]),
        }

    return result


def check_target(analysis, target):
    """Check if a target velocity is achievable based on historical data."""
    avg = analysis["summary"]["average"]
    max_val = analysis["summary"]["max"]
    std_dev = analysis["summary"]["std_dev"]

    if target <= avg * 0.85:
        risk = "low"
        comment = "Target is below conservative recommendation"
    elif target <= avg:
        risk = "low"
        comment = "Target is at or below average velocity"
    elif target <= avg + std_dev:
        risk = "medium"
        comment = "Target is above average but within one standard deviation"
    elif target <= max_val:
        risk = "high"
        comment = "Target exceeds average; achieved only in best sprints"
    else:
        risk = "very high"
        comment = "Target exceeds historical maximum velocity"

    return {
        "target": target,
        "average": round(avg, 1),
        "difference_from_avg": round(target - avg, 1),
        "risk": risk,
        "comment": comment,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Sprint velocity tracker and trend analyzer",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Analyze completed velocity
  %(prog)s --sprints "30,36,38,35,40"

  # Compare planned vs completed
  %(prog)s --sprints "30,36,38,35" --planned "34,38,40,42"

  # Check if a target is realistic
  %(prog)s --sprints "30,36,38,35" --target 38

  # JSON output
  %(prog)s --sprints "30,36,38,35,40" --json
        """,
    )
    parser.add_argument(
        "--sprints",
        type=str,
        help="Completed points CSV: '30,36,38,35'",
    )
    parser.add_argument(
        "--planned",
        type=str,
        help="Planned points CSV: '34,38,40,42'",
    )
    parser.add_argument("--target", type=int, help="Target velocity to assess")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    if args.sprints:
        completed = [int(v.strip()) for v in args.sprints.split(",")]
    else:
        # Sample data
        completed = [30, 36, 38, 35, 40]

    planned = None
    if args.planned:
        planned = [int(v.strip()) for v in args.planned.split(",")]

    analysis = analyze_velocity(completed, planned)

    if args.target:
        analysis["target_assessment"] = check_target(analysis, args.target)

    if args.json:
        print(json.dumps(analysis, indent=2))
    else:
        s = analysis["summary"]
        print("=" * 55)
        print("VELOCITY ANALYSIS")
        print("=" * 55)
        print(f"  Sprints analyzed: {s['sprints_analyzed']}")
        print(f"  Average velocity: {s['average']} points")
        print(f"  Median: {s['median']} | Min: {s['min']} | Max: {s['max']}")
        print(f"  Std deviation: {s['std_dev']} | CV: {s['coefficient_of_variation']}%")
        print(f"  Stability: {s['stability']}")
        print(f"  Trend: {s['trend']} (slope: {s['trend_slope']})")
        print()

        print("SPRINT HISTORY")
        print("-" * 55)
        header = f"  {'Sprint':<10} {'Completed':>10}"
        if planned:
            header += f" {'Planned':>10} {'Accuracy':>10}"
        print(header)
        for sp in analysis["sprints"]:
            line = f"  Sprint {sp['sprint']:<4} {sp['completed']:>10}"
            if "planned" in sp:
                line += f" {sp['planned']:>10} {sp['accuracy']:>9.1f}%"
            print(line)
        print()

        r = analysis["recommendation"]
        print("COMMITMENT RECOMMENDATION")
        print("-" * 55)
        print(f"  Conservative (85%): {r['conservative']} points")
        print(f"  Moderate (90%):     {r['moderate']} points")
        print(f"  Aggressive (100%):  {r['aggressive']} points")
        print(f"  Stretch (110%):     {r['stretch']} points")

        if "target_assessment" in analysis:
            t = analysis["target_assessment"]
            print()
            print("TARGET ASSESSMENT")
            print("-" * 55)
            print(f"  Target: {t['target']} points")
            print(f"  vs Average: {t['difference_from_avg']:+.1f} points")
            print(f"  Risk: {t['risk'].upper()}")
            print(f"  Note: {t['comment']}")
        print()


if __name__ == "__main__":
    main()
