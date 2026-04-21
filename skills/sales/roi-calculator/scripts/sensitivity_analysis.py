#!/usr/bin/env python3
"""Run sensitivity analysis across ROI model assumptions.

Tests how changes in key variables affect ROI outcomes. Produces conservative,
moderate, and aggressive scenarios with break-even analysis.

Usage:
    python sensitivity_analysis.py --model roi_model.json --scenarios 3
    python sensitivity_analysis.py --demo --format markdown
    python sensitivity_analysis.py --demo --variables adoption_rate,license_cost
"""

import argparse
import json
from datetime import datetime


# Demo ROI model for sensitivity testing
DEMO_MODEL = {
    "name": "Cloud Platform Investment",
    "investment": 150000,
    "annual_gains": {
        "cost_savings": 120000,
        "productivity": 60000,
        "revenue_impact": 45000,
        "risk_reduction": 25000,
    },
    "annual_cost": 48000,
    "years": 3,
    "discount_rate": 10,
    "variables": {
        "adoption_rate": {
            "description": "Percentage of team actively using the platform",
            "base_value": 100,
            "unit": "%",
            "affects": ["cost_savings", "productivity"],
        },
        "license_cost": {
            "description": "Annual software license fee",
            "base_value": 48000,
            "unit": "$",
            "affects": ["annual_cost"],
        },
        "headcount": {
            "description": "Number of users impacted",
            "base_value": 50,
            "unit": "users",
            "affects": ["productivity", "cost_savings"],
        },
        "productivity_improvement": {
            "description": "Productivity gain per person",
            "base_value": 100,
            "unit": "%",
            "affects": ["productivity"],
        },
        "implementation_timeline": {
            "description": "Months to full deployment",
            "base_value": 4,
            "unit": "months",
            "affects": ["ramp_time"],
        },
        "revenue_growth": {
            "description": "Revenue improvement from solution",
            "base_value": 100,
            "unit": "%",
            "affects": ["revenue_impact"],
        },
    },
}


def calculate_roi(investment, total_annual_gains, annual_cost, years, discount_rate):
    """Calculate ROI metrics for a given set of parameters."""
    net_annual = total_annual_gains - annual_cost
    total_net_benefit = (net_annual * years) - investment
    roi_pct = round((total_net_benefit / investment) * 100, 1) if investment > 0 else 0
    payback_months = round(investment / (net_annual / 12), 1) if net_annual > 0 else None

    # NPV
    cash_flows = [-investment]
    for year in range(1, years + 1):
        if year == 1:
            # Apply ramp (average 62.5% in year 1)
            cash_flows.append(round(total_annual_gains * 0.625 - annual_cost))
        else:
            cash_flows.append(round(net_annual))

    npv = sum(cf / ((1 + discount_rate / 100) ** t) for t, cf in enumerate(cash_flows))

    return {
        "roi_pct": roi_pct,
        "net_benefit": round(total_net_benefit),
        "payback_months": payback_months,
        "npv": round(npv),
        "net_annual_benefit": round(net_annual),
    }


def run_sensitivity(model, variables_to_test=None):
    """Run sensitivity analysis on specified variables."""
    base_gains = sum(model["annual_gains"].values())
    investment = model["investment"]
    annual_cost = model["annual_cost"]
    years = model["years"]
    discount_rate = model["discount_rate"]

    if variables_to_test is None:
        variables_to_test = list(model["variables"].keys())

    # Base case
    base_case = calculate_roi(investment, base_gains, annual_cost, years, discount_rate)

    # Scenario analysis (overall)
    scenarios = {}
    for scenario_name, multiplier in [("conservative", 0.75), ("moderate", 1.0), ("aggressive", 1.25)]:
        adj_gains = base_gains * multiplier
        adj_cost = annual_cost * (1.1 if scenario_name == "conservative" else 0.9 if scenario_name == "aggressive" else 1.0)
        result = calculate_roi(investment, adj_gains, adj_cost, years, discount_rate)
        scenarios[scenario_name] = {
            "gains_multiplier": multiplier,
            "annual_gains": round(adj_gains),
            "annual_cost": round(adj_cost),
            **result,
        }

    # Individual variable sensitivity
    test_points = [-0.25, -0.10, 0, 0.10, 0.25]
    variable_sensitivity = {}

    for var_name in variables_to_test:
        if var_name not in model["variables"]:
            continue

        var_info = model["variables"][var_name]
        results = []

        for delta in test_points:
            # Calculate adjusted gains based on which categories this variable affects
            adj_gains = 0
            for category, amount in model["annual_gains"].items():
                if category in var_info["affects"]:
                    adj_gains += amount * (1 + delta)
                else:
                    adj_gains += amount

            # If variable affects annual_cost
            adj_cost = annual_cost
            if "annual_cost" in var_info["affects"]:
                adj_cost = annual_cost * (1 + delta)

            result = calculate_roi(investment, adj_gains, adj_cost, years, discount_rate)
            results.append({
                "change_pct": int(delta * 100),
                "roi_pct": result["roi_pct"],
                "npv": result["npv"],
                "payback_months": result["payback_months"],
            })

        # Calculate sensitivity score (ROI swing for 25% change)
        roi_range = results[-1]["roi_pct"] - results[0]["roi_pct"]
        sensitivity_level = "High" if abs(roi_range) > 100 else "Medium" if abs(roi_range) > 50 else "Low"

        variable_sensitivity[var_name] = {
            "description": var_info["description"],
            "base_value": var_info["base_value"],
            "unit": var_info["unit"],
            "affects": var_info["affects"],
            "results": results,
            "roi_range": round(roi_range, 1),
            "sensitivity_level": sensitivity_level,
        }

    # Sort by sensitivity
    sorted_variables = sorted(
        variable_sensitivity.items(),
        key=lambda x: abs(x[1]["roi_range"]),
        reverse=True,
    )

    # Break-even analysis
    breakeven_gains = (investment / years) + annual_cost
    breakeven_adoption = round((breakeven_gains / base_gains) * 100, 1) if base_gains > 0 else None
    max_acceptable_cost = base_gains - (investment / years)
    margin_of_safety = round(((base_gains - breakeven_gains) / base_gains) * 100, 1)

    # Risk adjustments
    risk_factors = [
        {"risk": "Implementation delay (30 days)", "probability": 30, "impact_on_roi": -15},
        {"risk": "Lower adoption (50% in Year 1)", "probability": 25, "impact_on_roi": -35},
        {"risk": "Price increase (10% Year 2)", "probability": 20, "impact_on_roi": -8},
        {"risk": "Staff turnover during rollout", "probability": 15, "impact_on_roi": -12},
        {"risk": "Integration complexity", "probability": 20, "impact_on_roi": -10},
    ]

    expected_risk_impact = sum(r["probability"] / 100 * r["impact_on_roi"] for r in risk_factors)
    risk_adjusted_roi = round(base_case["roi_pct"] + expected_risk_impact, 1)

    return {
        "base_case": base_case,
        "scenarios": scenarios,
        "variable_sensitivity": dict(sorted_variables),
        "breakeven": {
            "minimum_annual_gains": round(breakeven_gains),
            "minimum_adoption_rate_pct": breakeven_adoption,
            "maximum_acceptable_annual_cost": round(max_acceptable_cost),
            "margin_of_safety_pct": margin_of_safety,
        },
        "risk_analysis": {
            "risk_factors": risk_factors,
            "expected_risk_impact_on_roi": round(expected_risk_impact, 1),
            "unadjusted_roi": base_case["roi_pct"],
            "risk_adjusted_roi": risk_adjusted_roi,
        },
    }


def format_markdown(analysis):
    """Format sensitivity analysis as markdown."""
    lines = []
    lines.append("# Sensitivity Analysis")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d')}")
    lines.append("")

    bc = analysis["base_case"]
    lines.append("## Base Case")
    lines.append(f"- **ROI:** {bc['roi_pct']}%")
    lines.append(f"- **Net Benefit:** ${bc['net_benefit']:,}")
    lines.append(f"- **Payback:** {bc['payback_months']} months")
    lines.append(f"- **NPV:** ${bc['npv']:,}")
    lines.append("")

    lines.append("## Scenario Analysis")
    lines.append("| Scenario | Annual Gains | ROI | Payback | NPV |")
    lines.append("|----------|-------------|-----|---------|-----|")
    for name, s in analysis["scenarios"].items():
        lines.append(f"| {name.title()} | ${s['annual_gains']:,} | {s['roi_pct']}% | {s['payback_months']} mo | ${s['npv']:,} |")
    lines.append("")

    lines.append("## Variable Sensitivity (Ranked by Impact)")
    lines.append("| Variable | Sensitivity | ROI Range | -25% | Base | +25% |")
    lines.append("|----------|-----------|-----------|------|------|------|")
    for var_name, data in analysis["variable_sensitivity"].items():
        results = data["results"]
        low = results[0]["roi_pct"]
        base = results[2]["roi_pct"]
        high = results[4]["roi_pct"]
        lines.append(f"| {var_name.replace('_', ' ').title()} | {data['sensitivity_level']} | {data['roi_range']}% | {low}% | {base}% | {high}% |")
    lines.append("")

    be = analysis["breakeven"]
    lines.append("## Break-Even Analysis")
    lines.append(f"- **Minimum annual gains for positive ROI:** ${be['minimum_annual_gains']:,}")
    lines.append(f"- **Minimum adoption rate:** {be['minimum_adoption_rate_pct']}%")
    lines.append(f"- **Maximum acceptable annual cost:** ${be['maximum_acceptable_annual_cost']:,}")
    lines.append(f"- **Margin of safety:** {be['margin_of_safety_pct']}%")
    lines.append("")

    ra = analysis["risk_analysis"]
    lines.append("## Risk-Adjusted ROI")
    lines.append(f"- **Unadjusted ROI:** {ra['unadjusted_roi']}%")
    lines.append(f"- **Risk-Adjusted ROI:** {ra['risk_adjusted_roi']}%")
    lines.append(f"- **Expected Risk Impact:** {ra['expected_risk_impact_on_roi']}%")
    lines.append("")
    lines.append("| Risk Factor | Probability | Impact on ROI |")
    lines.append("|-------------|-------------|---------------|")
    for r in ra["risk_factors"]:
        lines.append(f"| {r['risk']} | {r['probability']}% | {r['impact_on_roi']}% |")
    lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Run sensitivity analysis across ROI model assumptions.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python sensitivity_analysis.py --demo --format markdown
  python sensitivity_analysis.py --demo --variables adoption_rate,license_cost
  python sensitivity_analysis.py --model roi_model.json --scenarios 3
        """,
    )
    parser.add_argument("--model", type=str, help="Path to JSON file with ROI model")
    parser.add_argument("--demo", action="store_true", help="Use built-in demo model")
    parser.add_argument("--variables", type=str, help="Comma-separated variables to test (default: all)")
    parser.add_argument("--scenarios", type=int, default=3, help="Number of scenarios (default: 3)")
    parser.add_argument("--format", type=str, choices=["json", "markdown"], default="json", help="Output format (default: json)")

    args = parser.parse_args()

    if args.demo:
        model = DEMO_MODEL
    elif args.model:
        with open(args.model) as f:
            model = json.load(f)
    else:
        parser.error("Either --demo or --model is required")
        return

    variables = None
    if args.variables:
        variables = [v.strip() for v in args.variables.split(",")]

    analysis = run_sensitivity(model, variables)
    analysis["metadata"] = {
        "generated": datetime.now().isoformat(),
        "model_name": model.get("name", "Unknown"),
        "variables_tested": variables or list(model["variables"].keys()),
        "data_source": "demo" if args.demo else "user-provided",
    }

    if args.format == "json":
        print(json.dumps(analysis, indent=2))
    else:
        print(format_markdown(analysis))


if __name__ == "__main__":
    main()
