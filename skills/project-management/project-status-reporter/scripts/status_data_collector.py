#!/usr/bin/env python3
"""Project status data collector.

Collects sprint metrics, milestone status, and generates structured
data for status reports. Can pull from sample data or integrate with
GitHub via subprocess calls.

Usage:
    python status_data_collector.py --demo
    python status_data_collector.py --repo org/repo --sprint "Sprint 14"
    python status_data_collector.py --demo --json
"""

import argparse
import json
import subprocess
import sys
from datetime import date, timedelta


DEMO_SPRINT_DATA = {
    "sprint_name": "Sprint 14",
    "sprint_number": 14,
    "start_date": (date.today() - timedelta(days=7)).isoformat(),
    "end_date": (date.today() + timedelta(days=3)).isoformat(),
    "day_of_sprint": 8,
    "total_days": 10,
    "stories": {
        "total": 14,
        "completed": 10,
        "in_progress": 3,
        "todo": 1,
    },
    "points": {
        "planned": 38,
        "completed": 28,
        "remaining": 10,
    },
    "bugs": {
        "opened": 3,
        "fixed": 5,
        "open": 7,
        "critical": 1,
    },
    "prs": {
        "merged": 18,
        "open": 4,
        "avg_review_hours": 4.2,
    },
    "tests": {
        "coverage_pct": 82,
        "passing": 347,
        "failing": 2,
        "build_success_rate": 97,
    },
}

DEMO_MILESTONES = [
    {"name": "Requirements Complete", "planned": "2026-03-01", "actual": "2026-03-01", "status": "DONE"},
    {"name": "Design Complete", "planned": "2026-04-01", "actual": "2026-04-03", "status": "DONE"},
    {"name": "Development Complete", "planned": "2026-06-01", "forecast": "2026-06-01", "status": "GREEN"},
    {"name": "UAT Start", "planned": "2026-06-15", "forecast": "2026-06-15", "status": "GREEN"},
    {"name": "Go-Live", "planned": "2026-07-01", "forecast": "2026-07-01", "status": "GREEN"},
]

DEMO_BUDGET = {
    "categories": [
        {"name": "Personnel", "budget": 200000, "actual": 180000, "forecast": 205000},
        {"name": "Infrastructure", "budget": 50000, "actual": 48000, "forecast": 58000},
        {"name": "Licenses", "budget": 20000, "actual": 20000, "forecast": 20000},
    ],
}


def collect_github_metrics(repo):
    """Attempt to collect metrics from GitHub CLI."""
    metrics = {}
    try:
        result = subprocess.run(
            ["gh", "pr", "list", "--repo", repo, "--state", "merged", "--json", "number", "--jq", "length"],
            capture_output=True, text=True, timeout=10,
        )
        metrics["prs_merged"] = int(result.stdout.strip()) if result.returncode == 0 else "N/A"
    except (subprocess.TimeoutExpired, FileNotFoundError, ValueError):
        metrics["prs_merged"] = "N/A"

    try:
        result = subprocess.run(
            ["gh", "pr", "list", "--repo", repo, "--state", "open", "--json", "number", "--jq", "length"],
            capture_output=True, text=True, timeout=10,
        )
        metrics["prs_open"] = int(result.stdout.strip()) if result.returncode == 0 else "N/A"
    except (subprocess.TimeoutExpired, FileNotFoundError, ValueError):
        metrics["prs_open"] = "N/A"

    try:
        result = subprocess.run(
            ["gh", "issue", "list", "--repo", repo, "--state", "open", "--json", "number", "--jq", "length"],
            capture_output=True, text=True, timeout=10,
        )
        metrics["issues_open"] = int(result.stdout.strip()) if result.returncode == 0 else "N/A"
    except (subprocess.TimeoutExpired, FileNotFoundError, ValueError):
        metrics["issues_open"] = "N/A"

    return metrics


def calculate_health_score(sprint_data):
    """Calculate a simple project health score (0-100)."""
    scores = []

    # Sprint progress (are we on track for points?)
    expected_pct = sprint_data["day_of_sprint"] / sprint_data["total_days"]
    actual_pct = sprint_data["points"]["completed"] / sprint_data["points"]["planned"]
    progress_score = min(100, (actual_pct / expected_pct) * 100) if expected_pct > 0 else 100
    scores.append(("Sprint Progress", round(progress_score)))

    # Quality (build success + test coverage)
    quality_score = (sprint_data["tests"]["build_success_rate"] + sprint_data["tests"]["coverage_pct"]) / 2
    scores.append(("Quality", round(quality_score)))

    # Bug health
    bug_score = max(0, 100 - (sprint_data["bugs"]["critical"] * 20) - (sprint_data["bugs"]["open"] * 5))
    scores.append(("Bug Health", round(bug_score)))

    # PR throughput
    pr_score = min(100, sprint_data["prs"]["merged"] * 5)
    scores.append(("PR Throughput", round(pr_score)))

    overall = round(sum(s[1] for s in scores) / len(scores))

    return {
        "overall": overall,
        "components": {name: val for name, val in scores},
        "rating": "GREEN" if overall >= 80 else "AMBER" if overall >= 60 else "RED",
    }


def format_budget(budget_data):
    """Format budget data with variance calculations."""
    total_budget = sum(c["budget"] for c in budget_data["categories"])
    total_actual = sum(c["actual"] for c in budget_data["categories"])
    total_forecast = sum(c["forecast"] for c in budget_data["categories"])

    categories = []
    for cat in budget_data["categories"]:
        variance_pct = ((cat["forecast"] - cat["budget"]) / cat["budget"]) * 100 if cat["budget"] > 0 else 0
        categories.append({
            **cat,
            "variance_pct": round(variance_pct, 1),
        })

    return {
        "categories": categories,
        "totals": {
            "budget": total_budget,
            "actual": total_actual,
            "forecast": total_forecast,
            "variance_pct": round(((total_forecast - total_budget) / total_budget) * 100, 1),
        },
    }


def main():
    parser = argparse.ArgumentParser(
        description="Collect project status data for reporting",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Demo with sample data
  %(prog)s --demo

  # Collect from GitHub repo
  %(prog)s --repo org/repo --sprint "Sprint 14"

  # JSON output
  %(prog)s --demo --json
        """,
    )
    parser.add_argument("--demo", action="store_true", help="Use sample project data")
    parser.add_argument("--repo", type=str, help="GitHub repo (org/repo)")
    parser.add_argument("--sprint", type=str, help="Sprint name")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    if args.demo:
        sprint_data = DEMO_SPRINT_DATA
        milestones = DEMO_MILESTONES
        budget = format_budget(DEMO_BUDGET)
        github_metrics = None
    elif args.repo:
        github_metrics = collect_github_metrics(args.repo)
        sprint_data = DEMO_SPRINT_DATA  # Would be replaced with real data source
        milestones = DEMO_MILESTONES
        budget = format_budget(DEMO_BUDGET)
    else:
        print("Use --demo for sample data or --repo for GitHub metrics.")
        sys.exit(1)

    health = calculate_health_score(sprint_data)

    result = {
        "report_date": date.today().isoformat(),
        "sprint": sprint_data,
        "milestones": milestones,
        "budget": budget,
        "health_score": health,
    }
    if github_metrics:
        result["github_metrics"] = github_metrics

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print("=" * 60)
        print(f"PROJECT STATUS DATA - {result['report_date']}")
        print("=" * 60)
        print()
        s = sprint_data
        print(f"Sprint: {s['sprint_name']} (Day {s['day_of_sprint']} of {s['total_days']})")
        print(f"Stories: {s['stories']['completed']}/{s['stories']['total']} complete")
        print(f"Points:  {s['points']['completed']}/{s['points']['planned']} delivered")
        print(f"Bugs:    {s['bugs']['open']} open ({s['bugs']['critical']} critical)")
        print(f"PRs:     {s['prs']['merged']} merged, {s['prs']['open']} open")
        print(f"Tests:   {s['tests']['coverage_pct']}% coverage, {s['tests']['build_success_rate']}% build success")
        print()
        print(f"HEALTH SCORE: {health['overall']}/100 ({health['rating']})")
        for comp, val in health["components"].items():
            bar = "#" * (val // 5) + "." * (20 - val // 5)
            print(f"  {comp:<20} [{bar}] {val}%")
        print()
        print("BUDGET")
        print("-" * 60)
        for cat in budget["categories"]:
            print(f"  {cat['name']:<15} Budget: ${cat['budget']:>10,} | "
                  f"Forecast: ${cat['forecast']:>10,} | Var: {cat['variance_pct']:+.1f}%")
        t = budget["totals"]
        print(f"  {'TOTAL':<15} Budget: ${t['budget']:>10,} | "
              f"Forecast: ${t['forecast']:>10,} | Var: {t['variance_pct']:+.1f}%")
        print()


if __name__ == "__main__":
    main()
