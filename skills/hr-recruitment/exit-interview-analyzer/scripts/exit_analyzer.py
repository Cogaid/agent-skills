#!/usr/bin/env python3
"""
Exit Interview Analyzer

Analyzes exit interview data to identify attrition drivers, calculate
trends, segment by team/level/tenure, and generate executive reports
with actionable recommendations.

Usage:
    python exit_analyzer.py --demo
    python exit_analyzer.py --data exit_data.json
    python exit_analyzer.py --data exit_data.json --format summary
"""

import argparse
import json
import sys
from collections import defaultdict, Counter

# --- Category Codes ---

CATEGORY_NAMES = {
    "MGT": "Management Issues",
    "CMP": "Compensation",
    "CDV": "Career Development",
    "CUL": "Culture",
    "WLB": "Work-Life Balance",
    "ROL": "Role Misalignment",
    "REC": "Recognition",
    "REL": "Personal / Relocation",
    "OPP": "External Opportunity",
    "RES": "Resources / Tools",
}

SALARY_REPLACEMENT_COST = {
    "junior": 0.5,
    "mid": 1.0,
    "senior": 1.5,
    "leadership": 2.0,
}

# --- Sample Data ---

SAMPLE_DATA = {
    "period": "Q1 2026",
    "prior_period": "Q4 2025",
    "company_headcount": 500,
    "exits": [
        {
            "id": "E001",
            "department": "Engineering",
            "level": "mid",
            "tenure_months": 22,
            "manager": "Manager_A",
            "performance_rating": 4,
            "annual_salary": 140000,
            "categories": [
                {"code": "CDV", "intensity": 3, "push_pull": "push"},
                {"code": "CMP", "intensity": 2, "push_pull": "push"},
            ],
            "ratings": {"manager": 3, "career_dev": 2, "compensation": 2, "culture": 4, "wlb": 4, "resources": 3},
            "boomerang": "conditional",
            "regrettable": True,
            "preventable": "yes",
            "quote": "I loved the team but saw no path to promotion. After 2 years at the same level, I had to look elsewhere.",
        },
        {
            "id": "E002",
            "department": "Engineering",
            "level": "senior",
            "tenure_months": 36,
            "manager": "Manager_A",
            "performance_rating": 5,
            "annual_salary": 210000,
            "categories": [
                {"code": "MGT", "intensity": 3, "push_pull": "push"},
                {"code": "CDV", "intensity": 2, "push_pull": "push"},
            ],
            "ratings": {"manager": 1, "career_dev": 2, "compensation": 3, "culture": 3, "wlb": 3, "resources": 4},
            "boomerang": "unlikely",
            "regrettable": True,
            "preventable": "yes",
            "quote": "My manager never provided feedback and took credit for my work in leadership meetings.",
        },
        {
            "id": "E003",
            "department": "Sales",
            "level": "mid",
            "tenure_months": 14,
            "manager": "Manager_B",
            "performance_rating": 3,
            "annual_salary": 120000,
            "categories": [
                {"code": "CMP", "intensity": 3, "push_pull": "push"},
                {"code": "OPP", "intensity": 2, "push_pull": "pull"},
            ],
            "ratings": {"manager": 4, "career_dev": 3, "compensation": 1, "culture": 3, "wlb": 3, "resources": 3},
            "boomerang": "yes",
            "regrettable": False,
            "preventable": "possibly",
            "quote": "I received a 35% raise to move. I liked it here but the comp gap was too large to ignore.",
        },
        {
            "id": "E004",
            "department": "Product",
            "level": "senior",
            "tenure_months": 8,
            "manager": "Manager_C",
            "performance_rating": 4,
            "annual_salary": 175000,
            "categories": [
                {"code": "ROL", "intensity": 3, "push_pull": "push"},
                {"code": "CUL", "intensity": 2, "push_pull": "push"},
            ],
            "ratings": {"manager": 3, "career_dev": 3, "compensation": 4, "culture": 2, "wlb": 2, "resources": 3},
            "boomerang": "unlikely",
            "regrettable": True,
            "preventable": "yes",
            "quote": "The role was completely different from what was described in interviews. I was doing project management, not product strategy.",
        },
        {
            "id": "E005",
            "department": "Engineering",
            "level": "junior",
            "tenure_months": 6,
            "manager": "Manager_D",
            "performance_rating": 3,
            "annual_salary": 85000,
            "categories": [
                {"code": "WLB", "intensity": 3, "push_pull": "push"},
                {"code": "MGT", "intensity": 1, "push_pull": "push"},
            ],
            "ratings": {"manager": 2, "career_dev": 3, "compensation": 3, "culture": 2, "wlb": 1, "resources": 3},
            "boomerang": "unlikely",
            "regrettable": False,
            "preventable": "possibly",
            "quote": "The on-call rotation was brutal for a junior. I was woken up 3-4 times a week.",
        },
        {
            "id": "E006",
            "department": "Marketing",
            "level": "mid",
            "tenure_months": 30,
            "manager": "Manager_E",
            "performance_rating": 3,
            "annual_salary": 110000,
            "categories": [
                {"code": "REL", "intensity": 3, "push_pull": "push"},
            ],
            "ratings": {"manager": 4, "career_dev": 3, "compensation": 3, "culture": 4, "wlb": 4, "resources": 4},
            "boomerang": "yes",
            "regrettable": False,
            "preventable": "no",
            "quote": "My spouse got a job in another city. I would have stayed otherwise.",
        },
        {
            "id": "E007",
            "department": "Engineering",
            "level": "mid",
            "tenure_months": 18,
            "manager": "Manager_A",
            "performance_rating": 3,
            "annual_salary": 135000,
            "categories": [
                {"code": "MGT", "intensity": 2, "push_pull": "push"},
                {"code": "REC", "intensity": 2, "push_pull": "push"},
            ],
            "ratings": {"manager": 2, "career_dev": 3, "compensation": 3, "culture": 3, "wlb": 3, "resources": 3},
            "boomerang": "conditional",
            "regrettable": False,
            "preventable": "possibly",
            "quote": "Hard work goes unnoticed here. My manager did not even acknowledge our team's successful launch.",
        },
        {
            "id": "E008",
            "department": "Sales",
            "level": "senior",
            "tenure_months": 42,
            "manager": "Manager_B",
            "performance_rating": 4,
            "annual_salary": 180000,
            "categories": [
                {"code": "OPP", "intensity": 3, "push_pull": "pull"},
                {"code": "CDV", "intensity": 1, "push_pull": "push"},
            ],
            "ratings": {"manager": 4, "career_dev": 3, "compensation": 3, "culture": 4, "wlb": 4, "resources": 3},
            "boomerang": "yes",
            "regrettable": True,
            "preventable": "no",
            "quote": "I got my dream offer to lead sales at a company I have admired for years. Nothing you could have done.",
        },
    ],
    "prior_period_data": {
        "total_exits": 6,
        "attrition_rate": 4.8,
        "category_frequencies": {
            "MGT": 33,
            "CMP": 50,
            "CDV": 17,
            "CUL": 17,
            "WLB": 17,
            "ROL": 0,
            "REC": 0,
            "REL": 17,
            "OPP": 33,
            "RES": 0,
        },
    },
}


def analyze_exits(data):
    """Run full exit interview analysis."""
    exits = data["exits"]
    total_exits = len(exits)
    headcount = data["company_headcount"]
    attrition_rate = round(total_exits / headcount * 100, 1) if headcount > 0 else 0

    results = {
        "period": data["period"],
        "headline_metrics": {
            "total_departures": total_exits,
            "headcount": headcount,
            "attrition_rate": attrition_rate,
            "regrettable_count": sum(1 for e in exits if e.get("regrettable")),
            "regrettable_rate": round(sum(1 for e in exits if e.get("regrettable")) / total_exits * 100, 1) if total_exits > 0 else 0,
            "preventable_count": sum(1 for e in exits if e.get("preventable") == "yes"),
            "boomerang_willing": round(sum(1 for e in exits if e.get("boomerang") in ("yes", "conditional")) / total_exits * 100, 1) if total_exits > 0 else 0,
        },
        "category_analysis": {},
        "segmentation": {},
        "push_pull_analysis": {},
        "manager_analysis": {},
        "cost_analysis": {},
        "hotspots": [],
        "trends": {},
        "top_drivers": [],
        "recommendations": [],
        "representative_quotes": [],
    }

    # Category frequency analysis
    category_counts = Counter()
    category_intensity = defaultdict(list)
    for exit_record in exits:
        for cat in exit_record.get("categories", []):
            category_counts[cat["code"]] += 1
            category_intensity[cat["code"]].append(cat["intensity"])

    for code in CATEGORY_NAMES:
        count = category_counts.get(code, 0)
        freq_pct = round(count / total_exits * 100, 1) if total_exits > 0 else 0
        intensities = category_intensity.get(code, [])
        avg_intensity = round(sum(intensities) / len(intensities), 1) if intensities else 0

        prior_freq = data.get("prior_period_data", {}).get("category_frequencies", {}).get(code, 0)
        if freq_pct > prior_freq + 5:
            trend = "up"
        elif freq_pct < prior_freq - 5:
            trend = "down"
        else:
            trend = "flat"

        results["category_analysis"][code] = {
            "name": CATEGORY_NAMES[code],
            "count": count,
            "frequency_pct": freq_pct,
            "avg_intensity": avg_intensity,
            "prior_period_pct": prior_freq,
            "trend": trend,
            "alert": freq_pct >= 30 or (trend == "up" and freq_pct >= 20),
        }

    # Sort by frequency for top drivers
    sorted_categories = sorted(
        results["category_analysis"].items(),
        key=lambda x: x[1]["frequency_pct"],
        reverse=True,
    )
    results["top_drivers"] = [
        {"rank": i + 1, "code": code, **data_item}
        for i, (code, data_item) in enumerate(sorted_categories)
        if data_item["count"] > 0
    ][:5]

    # Push vs Pull analysis
    push_count = sum(1 for e in exits for c in e.get("categories", []) if c["push_pull"] == "push")
    pull_count = sum(1 for e in exits for c in e.get("categories", []) if c["push_pull"] == "pull")
    both_count = sum(1 for e in exits if
                     any(c["push_pull"] == "push" for c in e.get("categories", [])) and
                     any(c["push_pull"] == "pull" for c in e.get("categories", [])))

    total_factors = push_count + pull_count
    results["push_pull_analysis"] = {
        "push_pct": round(push_count / total_factors * 100, 1) if total_factors > 0 else 0,
        "pull_pct": round(pull_count / total_factors * 100, 1) if total_factors > 0 else 0,
        "exits_with_both": both_count,
    }

    # Segmentation: by department
    dept_exits = defaultdict(list)
    for e in exits:
        dept_exits[e["department"]].append(e)

    results["segmentation"]["by_department"] = {}
    for dept, dept_exit_list in dept_exits.items():
        cats = Counter()
        for e in dept_exit_list:
            for c in e.get("categories", []):
                cats[c["code"]] += 1
        top_reason = cats.most_common(1)[0][0] if cats else "N/A"
        results["segmentation"]["by_department"][dept] = {
            "departures": len(dept_exit_list),
            "top_reason": f"{top_reason} ({CATEGORY_NAMES.get(top_reason, top_reason)})",
            "regrettable": sum(1 for e in dept_exit_list if e.get("regrettable")),
        }

    # Segmentation: by tenure band
    tenure_bands = {"0-6 months": [], "6-18 months": [], "18-36 months": [], "36+ months": []}
    for e in exits:
        months = e["tenure_months"]
        if months <= 6:
            tenure_bands["0-6 months"].append(e)
        elif months <= 18:
            tenure_bands["6-18 months"].append(e)
        elif months <= 36:
            tenure_bands["18-36 months"].append(e)
        else:
            tenure_bands["36+ months"].append(e)

    results["segmentation"]["by_tenure"] = {}
    for band, band_exits in tenure_bands.items():
        pct = round(len(band_exits) / total_exits * 100, 1) if total_exits > 0 else 0
        cats = Counter()
        for e in band_exits:
            for c in e.get("categories", []):
                cats[c["code"]] += 1
        top = cats.most_common(1)[0] if cats else ("N/A", 0)
        results["segmentation"]["by_tenure"][band] = {
            "count": len(band_exits),
            "pct_of_exits": pct,
            "top_reason": CATEGORY_NAMES.get(top[0], top[0]) if top[0] != "N/A" else "N/A",
        }

    # Segmentation: by level
    level_exits = defaultdict(list)
    for e in exits:
        level_exits[e["level"]].append(e)

    results["segmentation"]["by_level"] = {}
    for level, level_exit_list in level_exits.items():
        total_salary = sum(e["annual_salary"] for e in level_exit_list)
        replacement_cost = sum(
            e["annual_salary"] * SALARY_REPLACEMENT_COST.get(e["level"], 1.0)
            for e in level_exit_list
        )
        results["segmentation"]["by_level"][level] = {
            "departures": len(level_exit_list),
            "regrettable": sum(1 for e in level_exit_list if e.get("regrettable")),
            "estimated_replacement_cost": round(replacement_cost),
        }

    # Manager analysis
    manager_exits = defaultdict(list)
    for e in exits:
        manager_exits[e["manager"]].append(e)

    results["manager_analysis"] = {}
    for mgr, mgr_exits in manager_exits.items():
        avg_mgr_rating = sum(e["ratings"]["manager"] for e in mgr_exits) / len(mgr_exits)
        results["manager_analysis"][mgr] = {
            "departures": len(mgr_exits),
            "avg_manager_rating": round(avg_mgr_rating, 1),
            "regrettable": sum(1 for e in mgr_exits if e.get("regrettable")),
            "alert": len(mgr_exits) >= 3 or avg_mgr_rating < 2.5,
        }

    # Cost analysis
    total_replacement_cost = sum(
        e["annual_salary"] * SALARY_REPLACEMENT_COST.get(e["level"], 1.0)
        for e in exits
    )
    results["cost_analysis"] = {
        "total_estimated_replacement_cost": round(total_replacement_cost),
        "average_per_departure": round(total_replacement_cost / total_exits) if total_exits > 0 else 0,
        "regrettable_cost": round(sum(
            e["annual_salary"] * SALARY_REPLACEMENT_COST.get(e["level"], 1.0)
            for e in exits if e.get("regrettable")
        )),
    }

    # Hotspots
    for mgr, mgr_data in results["manager_analysis"].items():
        if mgr_data["alert"]:
            results["hotspots"].append({
                "type": "manager",
                "entity": mgr,
                "departures": mgr_data["departures"],
                "avg_rating": mgr_data["avg_manager_rating"],
                "action": "Immediate review: skip-level conversations, management training assessment",
            })

    for dept, dept_data in results["segmentation"]["by_department"].items():
        if dept_data["departures"] >= 3:
            results["hotspots"].append({
                "type": "department",
                "entity": dept,
                "departures": dept_data["departures"],
                "action": f"Department review required. Top driver: {dept_data['top_reason']}",
            })

    # Recommendations
    for driver in results["top_drivers"][:3]:
        code = driver["code"]
        if code == "MGT":
            results["recommendations"].append({
                "priority": "high",
                "category": "Management Quality",
                "action": "Implement management training program for flagged managers. Launch skip-level conversations for at-risk teams.",
                "estimated_impact": "15-25% reduction in manager-driven attrition",
            })
        elif code == "CMP":
            results["recommendations"].append({
                "priority": "high",
                "category": "Compensation",
                "action": "Conduct market compensation study for affected roles. Adjust salaries to 50th-75th percentile.",
                "estimated_impact": "20-40% reduction in comp-driven attrition",
            })
        elif code == "CDV":
            results["recommendations"].append({
                "priority": "high",
                "category": "Career Development",
                "action": "Define career ladders for all major roles. Mandate quarterly career development conversations.",
                "estimated_impact": "15-30% reduction in growth-driven attrition",
            })
        elif code == "WLB":
            results["recommendations"].append({
                "priority": "medium",
                "category": "Work-Life Balance",
                "action": "Review on-call rotation policies. Assess team workload distribution.",
                "estimated_impact": "10-15% reduction in burnout-driven attrition",
            })
        elif code == "ROL":
            results["recommendations"].append({
                "priority": "medium",
                "category": "Role Alignment",
                "action": "Audit job descriptions vs actual responsibilities. Improve hiring process role clarity.",
                "estimated_impact": "Reduce early attrition (0-12 months) by 20%",
            })
        elif code == "REC":
            results["recommendations"].append({
                "priority": "medium",
                "category": "Recognition",
                "action": "Launch team recognition program. Train managers on timely acknowledgment of contributions.",
                "estimated_impact": "10-15% reduction in recognition-driven attrition",
            })

    # Representative quotes
    for e in exits:
        if e.get("quote"):
            results["representative_quotes"].append({
                "quote": e["quote"],
                "context": f"{e['level']} level, {e['department']}, {e['tenure_months']} months tenure",
                "primary_driver": e["categories"][0]["code"] if e.get("categories") else "N/A",
            })

    return results


def print_summary(results):
    """Print a human-readable executive summary."""
    h = results["headline_metrics"]
    print(f"=== EXIT INTERVIEW ANALYSIS ===")
    print(f"Period: {results['period']}")
    print(f"")
    print(f"HEADLINE METRICS")
    print(f"  Total Departures: {h['total_departures']}")
    print(f"  Attrition Rate: {h['attrition_rate']}%")
    print(f"  Regrettable: {h['regrettable_count']} ({h['regrettable_rate']}%)")
    print(f"  Preventable: {h['preventable_count']}")
    print(f"  Boomerang Willing: {h['boomerang_willing']}%")
    print(f"  Est. Replacement Cost: ${results['cost_analysis']['total_estimated_replacement_cost']:,}")
    print(f"")

    print(f"TOP ATTRITION DRIVERS")
    for d in results["top_drivers"]:
        alert = " ** ALERT **" if d.get("alert") else ""
        trend_arrow = {"up": "^", "down": "v", "flat": "-"}.get(d["trend"], "?")
        print(f"  {d['rank']}. {d['name']}: {d['frequency_pct']}% of exits (trend: {trend_arrow}){alert}")

    pp = results["push_pull_analysis"]
    print(f"\nPUSH vs PULL")
    print(f"  Push (internal): {pp['push_pct']}%")
    print(f"  Pull (external): {pp['pull_pct']}%")

    if results["hotspots"]:
        print(f"\nHOTSPOTS")
        for hs in results["hotspots"]:
            print(f"  [{hs['type'].upper()}] {hs['entity']}: {hs['departures']} departures - {hs['action']}")

    print(f"\nDEPARTMENT BREAKDOWN")
    for dept, data in results["segmentation"]["by_department"].items():
        print(f"  {dept}: {data['departures']} exits (regrettable: {data['regrettable']}) - Top: {data['top_reason']}")

    print(f"\nTENURE BREAKDOWN")
    for band, data in results["segmentation"]["by_tenure"].items():
        print(f"  {band}: {data['count']} ({data['pct_of_exits']}%) - Top: {data['top_reason']}")

    print(f"\nRECOMMENDATIONS")
    for i, rec in enumerate(results["recommendations"], 1):
        print(f"  {i}. [{rec['priority'].upper()}] {rec['category']}: {rec['action']}")
        print(f"     Expected Impact: {rec['estimated_impact']}")

    if results["representative_quotes"]:
        print(f"\nREPRESENTATIVE QUOTES")
        for q in results["representative_quotes"][:3]:
            print(f'  "{q["quote"]}"')
            print(f"  -- {q['context']}")
            print()


def main():
    parser = argparse.ArgumentParser(
        description="Analyze exit interview data to identify attrition drivers and generate insights."
    )
    parser.add_argument("--data", help="Path to JSON file with exit interview data")
    parser.add_argument("--demo", action="store_true", help="Run with sample data")
    parser.add_argument("--format", choices=["json", "summary"], default="json", help="Output format")

    args = parser.parse_args()

    if args.demo:
        data = SAMPLE_DATA
    elif args.data:
        try:
            with open(args.data, "r") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(json.dumps({"error": str(e)}))
            sys.exit(1)
    else:
        parser.error("Either --demo or --data is required")
        sys.exit(1)

    results = analyze_exits(data)

    if args.format == "summary":
        print_summary(results)
    else:
        print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
