#!/usr/bin/env python3
"""Sprint capacity calculator for agile teams.

Calculates effective team capacity based on team size, availability,
and focus factors. Outputs capacity analysis as JSON or formatted text.

Usage:
    python capacity_calc.py --team-size 5 --sprint-days 10 --focus 0.7
    python capacity_calc.py --members "Alice:10:0:0:0.7,Bob:10:2:0:0.7,Carol:10:0:2:0.5"
    python capacity_calc.py --members "Alice:10:0:0:0.7" --velocity "30,36,38,35" --json
"""

import argparse
import json
import sys


def calculate_individual_capacity(name, sprint_days, pto_days, oncall_days, focus_factor):
    """Calculate effective capacity for one team member."""
    available_days = sprint_days - pto_days - oncall_days
    effective_days = available_days * focus_factor
    return {
        "name": name,
        "sprint_days": sprint_days,
        "pto_days": pto_days,
        "oncall_days": oncall_days,
        "available_days": available_days,
        "focus_factor": focus_factor,
        "effective_days": round(effective_days, 1),
    }


def calculate_team_capacity(members):
    """Calculate total team capacity from individual capacities."""
    total_effective = sum(m["effective_days"] for m in members)
    total_available = sum(m["available_days"] for m in members)
    return {
        "members": members,
        "total_effective_days": round(total_effective, 1),
        "total_available_days": total_available,
        "team_size": len(members),
        "avg_focus_factor": round(
            sum(m["focus_factor"] for m in members) / len(members), 2
        ),
    }


def calculate_velocity_stats(velocity_values):
    """Calculate velocity statistics from historical data."""
    if not velocity_values:
        return None
    avg = sum(velocity_values) / len(velocity_values)
    sorted_vals = sorted(velocity_values)
    return {
        "sprints_analyzed": len(velocity_values),
        "values": velocity_values,
        "average": round(avg, 1),
        "minimum": min(velocity_values),
        "maximum": max(velocity_values),
        "median": sorted_vals[len(sorted_vals) // 2],
        "recommended_commitment": {
            "conservative": round(avg * 0.85),
            "moderate": round(avg * 0.90),
            "aggressive": round(avg),
        },
    }


def recommend_commitment(capacity, velocity_stats):
    """Generate sprint commitment recommendation."""
    recommendation = {
        "effective_days": capacity["total_effective_days"],
        "team_size": capacity["team_size"],
    }
    if velocity_stats:
        recommendation["velocity_based"] = velocity_stats["recommended_commitment"]
        recommendation["recommended"] = velocity_stats["recommended_commitment"]["moderate"]
        recommendation["method"] = "velocity-based (moderate)"
    else:
        # Rough heuristic: ~3-4 story points per effective day
        points_per_day = 3.5
        estimated = round(capacity["total_effective_days"] * points_per_day)
        recommendation["capacity_based"] = {
            "conservative": round(estimated * 0.85),
            "moderate": estimated,
            "aggressive": round(estimated * 1.1),
        }
        recommendation["recommended"] = estimated
        recommendation["method"] = "capacity-based (no velocity history)"
    return recommendation


def parse_members(members_str):
    """Parse members string format: 'Name:days:pto:oncall:focus,...'"""
    members = []
    for entry in members_str.split(","):
        parts = entry.strip().split(":")
        if len(parts) != 5:
            print(f"Error: Invalid member format '{entry}'. Expected 'Name:days:pto:oncall:focus'", file=sys.stderr)
            sys.exit(1)
        members.append(
            calculate_individual_capacity(
                name=parts[0].strip(),
                sprint_days=int(parts[1]),
                pto_days=int(parts[2]),
                oncall_days=int(parts[3]),
                focus_factor=float(parts[4]),
            )
        )
    return members


def main():
    parser = argparse.ArgumentParser(
        description="Sprint capacity calculator for agile teams",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Simple team capacity
  %(prog)s --team-size 5 --sprint-days 10 --focus 0.7

  # Detailed per-member capacity
  %(prog)s --members "Alice:10:0:0:0.7,Bob:10:2:0:0.7,Carol:10:0:2:0.5"

  # With velocity history
  %(prog)s --members "Alice:10:0:0:0.7,Bob:10:2:0:0.7" --velocity "30,36,38,35"

  # JSON output
  %(prog)s --team-size 5 --sprint-days 10 --focus 0.7 --json
        """,
    )
    parser.add_argument("--team-size", type=int, help="Number of developers (for simple mode)")
    parser.add_argument("--sprint-days", type=int, default=10, help="Working days in the sprint (default: 10)")
    parser.add_argument("--focus", type=float, default=0.7, help="Focus factor 0.0-1.0 (default: 0.7)")
    parser.add_argument(
        "--members",
        type=str,
        help="Detailed members: 'Name:days:pto:oncall:focus,...'",
    )
    parser.add_argument(
        "--velocity",
        type=str,
        help="Historical velocity CSV: '30,36,38,35'",
    )
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    if not args.members and not args.team_size:
        # Use sample data
        members = [
            calculate_individual_capacity("Dev 1", 10, 0, 0, 0.7),
            calculate_individual_capacity("Dev 2", 10, 2, 0, 0.7),
            calculate_individual_capacity("Dev 3", 10, 0, 2, 0.5),
            calculate_individual_capacity("Dev 4", 10, 0, 0, 0.7),
            calculate_individual_capacity("Dev 5", 10, 1, 0, 0.7),
        ]
    elif args.members:
        members = parse_members(args.members)
    else:
        members = [
            calculate_individual_capacity(f"Dev {i+1}", args.sprint_days, 0, 0, args.focus)
            for i in range(args.team_size)
        ]

    velocity_values = None
    if args.velocity:
        velocity_values = [int(v.strip()) for v in args.velocity.split(",")]

    capacity = calculate_team_capacity(members)
    velocity_stats = calculate_velocity_stats(velocity_values)
    recommendation = recommend_commitment(capacity, velocity_stats)

    result = {
        "capacity": capacity,
        "velocity": velocity_stats,
        "recommendation": recommendation,
    }

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print("=" * 60)
        print("SPRINT CAPACITY ANALYSIS")
        print("=" * 60)
        print()
        print(f"{'Member':<15} {'Days':>6} {'PTO':>5} {'OnCall':>7} {'Avail':>6} {'Focus':>6} {'Effective':>10}")
        print("-" * 60)
        for m in capacity["members"]:
            print(
                f"{m['name']:<15} {m['sprint_days']:>6} {m['pto_days']:>5} "
                f"{m['oncall_days']:>7} {m['available_days']:>6} {m['focus_factor']:>6.2f} "
                f"{m['effective_days']:>10.1f}"
            )
        print("-" * 60)
        print(f"{'TOTAL':<15} {'':>6} {'':>5} {'':>7} {capacity['total_available_days']:>6} "
              f"{capacity['avg_focus_factor']:>6.2f} {capacity['total_effective_days']:>10.1f}")
        print()

        if velocity_stats:
            print("VELOCITY HISTORY")
            print("-" * 40)
            print(f"  Sprints analyzed: {velocity_stats['sprints_analyzed']}")
            print(f"  Average: {velocity_stats['average']} points")
            print(f"  Range: {velocity_stats['minimum']} - {velocity_stats['maximum']}")
            print()

        print("RECOMMENDATION")
        print("-" * 40)
        print(f"  Method: {recommendation['method']}")
        print(f"  Recommended commitment: {recommendation['recommended']} points")
        print()


if __name__ == "__main__":
    main()
