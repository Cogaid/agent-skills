#!/usr/bin/env python3
"""Build an ROI model from investment and savings inputs.

Calculates ROI percentage, payback period, NPV, IRR, and sensitivity ranges
for a proposed investment.

Usage:
    python calculate_roi.py --investment 150000 --annual-savings 200000 --years 3
    python calculate_roi.py --investment 150000 --annual-savings 200000 --years 3 --discount-rate 10
    python calculate_roi.py --investment 150000 --annual-savings 200000 --annual-cost 50000 --years 3
"""

import argparse
import json
from datetime import datetime


def calculate_npv(cash_flows, discount_rate):
    """Calculate Net Present Value of a series of cash flows."""
    npv = 0
    for t, cf in enumerate(cash_flows):
        npv += cf / ((1 + discount_rate / 100) ** t)
    return round(npv, 2)


def calculate_irr(cash_flows, tolerance=0.0001, max_iterations=1000):
    """Calculate Internal Rate of Return using bisection method."""
    low = -0.99
    high = 10.0

    for _ in range(max_iterations):
        mid = (low + high) / 2
        npv = sum(cf / ((1 + mid) ** t) for t, cf in enumerate(cash_flows))

        if abs(npv) < tolerance:
            return round(mid * 100, 2)
        elif npv > 0:
            low = mid
        else:
            high = mid

    return round(mid * 100, 2)


def calculate_payback_period(investment, monthly_net_benefit):
    """Calculate payback period in months."""
    if monthly_net_benefit <= 0:
        return None  # Never pays back
    return round(investment / monthly_net_benefit, 1)


def build_roi_model(investment, annual_savings, annual_cost=0, years=3, discount_rate=10,
                    ramp_schedule=None, revenue_gain=0, productivity_gain=0, risk_reduction=0):
    """Build a complete ROI model."""

    # Default ramp: 25%, 50%, 75%, 100% over first 4 quarters
    if ramp_schedule is None:
        ramp_schedule = [0.25, 0.50, 0.75, 1.0]

    # Total annual gains
    total_annual_gains = annual_savings + revenue_gain + productivity_gain + risk_reduction

    # Year-by-year cash flows
    yearly_data = []
    cash_flows = [-investment]  # Year 0

    for year in range(1, years + 1):
        # Apply ramp in year 1
        if year == 1:
            # Average of quarterly ramp
            avg_ramp = sum(ramp_schedule) / len(ramp_schedule)
            gains = round(total_annual_gains * avg_ramp)
        else:
            gains = total_annual_gains

        net = gains - annual_cost
        cash_flows.append(net)

        cumulative = sum(cash_flows)
        yearly_data.append({
            "year": year,
            "gains": gains,
            "costs": annual_cost,
            "net_benefit": net,
            "cumulative": cumulative,
        })

    # Core calculations
    total_gains = sum(yd["gains"] for yd in yearly_data)
    total_costs = investment + sum(yd["costs"] for yd in yearly_data)
    net_benefit = total_gains - total_costs
    roi_pct = round((net_benefit / investment) * 100, 1)

    # Monthly net benefit (at full ramp)
    monthly_net = (total_annual_gains - annual_cost) / 12
    payback_months = calculate_payback_period(investment, monthly_net)

    # NPV
    npv = calculate_npv(cash_flows, discount_rate)

    # IRR
    irr = calculate_irr(cash_flows)

    # Sensitivity analysis
    scenarios = {
        "conservative": {
            "gains_multiplier": 0.75,
            "cost_multiplier": 1.10,
        },
        "moderate": {
            "gains_multiplier": 1.0,
            "cost_multiplier": 1.0,
        },
        "aggressive": {
            "gains_multiplier": 1.25,
            "cost_multiplier": 0.90,
        },
    }

    sensitivity = {}
    for scenario_name, multipliers in scenarios.items():
        adj_gains = total_annual_gains * multipliers["gains_multiplier"]
        adj_cost = annual_cost * multipliers["cost_multiplier"]
        adj_net_annual = adj_gains - adj_cost
        adj_total_net = (adj_net_annual * years) - investment
        adj_roi = round((adj_total_net / investment) * 100, 1)
        adj_monthly = adj_net_annual / 12
        adj_payback = calculate_payback_period(investment, adj_monthly)

        adj_cash_flows = [-investment]
        for year in range(1, years + 1):
            if year == 1:
                avg_ramp = sum(ramp_schedule) / len(ramp_schedule)
                adj_cash_flows.append(round(adj_gains * avg_ramp - adj_cost))
            else:
                adj_cash_flows.append(round(adj_net_annual))

        adj_npv = calculate_npv(adj_cash_flows, discount_rate)

        sensitivity[scenario_name] = {
            "annual_gains": round(adj_gains),
            "annual_cost": round(adj_cost),
            "net_annual_benefit": round(adj_net_annual),
            "roi_pct": adj_roi,
            "payback_months": adj_payback,
            "npv": adj_npv,
        }

    # Break-even analysis
    breakeven_gains = investment / years + annual_cost
    breakeven_adoption = round((breakeven_gains / total_annual_gains) * 100, 1) if total_annual_gains > 0 else None

    return {
        "investment_summary": {
            "total_investment": investment,
            "annual_ongoing_cost": annual_cost,
            "total_cost_over_period": total_costs,
        },
        "gains_summary": {
            "annual_savings": annual_savings,
            "revenue_gain": revenue_gain,
            "productivity_gain": productivity_gain,
            "risk_reduction": risk_reduction,
            "total_annual_gains": total_annual_gains,
            "total_gains_over_period": total_gains,
        },
        "roi_metrics": {
            "roi_pct": roi_pct,
            "net_benefit": net_benefit,
            "payback_months": payback_months,
            "npv": npv,
            "irr_pct": irr,
            "discount_rate_used": discount_rate,
        },
        "yearly_breakdown": yearly_data,
        "cash_flows": cash_flows,
        "sensitivity_analysis": sensitivity,
        "breakeven": {
            "minimum_annual_gains_for_positive_roi": round(breakeven_gains),
            "minimum_adoption_rate_pct": breakeven_adoption,
        },
        "ramp_schedule": ramp_schedule,
    }


def format_markdown(model):
    """Format ROI model as markdown."""
    lines = []
    lines.append("# ROI Analysis")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d')}")
    lines.append("")

    roi = model["roi_metrics"]
    lines.append("## Key Metrics")
    lines.append(f"- **ROI:** {roi['roi_pct']}%")
    lines.append(f"- **Net Benefit:** ${roi['net_benefit']:,}")
    lines.append(f"- **Payback Period:** {roi['payback_months']} months")
    lines.append(f"- **NPV:** ${roi['npv']:,} (at {roi['discount_rate_used']}% discount rate)")
    lines.append(f"- **IRR:** {roi['irr_pct']}%")
    lines.append("")

    inv = model["investment_summary"]
    lines.append("## Investment")
    lines.append(f"- **Upfront Investment:** ${inv['total_investment']:,}")
    lines.append(f"- **Annual Ongoing Cost:** ${inv['annual_ongoing_cost']:,}")
    lines.append(f"- **Total Cost:** ${inv['total_cost_over_period']:,}")
    lines.append("")

    gains = model["gains_summary"]
    lines.append("## Annual Gains")
    lines.append(f"- **Cost Savings:** ${gains['annual_savings']:,}")
    if gains["revenue_gain"]:
        lines.append(f"- **Revenue Gain:** ${gains['revenue_gain']:,}")
    if gains["productivity_gain"]:
        lines.append(f"- **Productivity Gain:** ${gains['productivity_gain']:,}")
    if gains["risk_reduction"]:
        lines.append(f"- **Risk Reduction:** ${gains['risk_reduction']:,}")
    lines.append(f"- **Total Annual Gains:** ${gains['total_annual_gains']:,}")
    lines.append("")

    lines.append("## Year-by-Year Cash Flow")
    lines.append("| Year | Gains | Costs | Net | Cumulative |")
    lines.append("|------|-------|-------|-----|-----------|")
    lines.append(f"| 0 | -- | ${inv['total_investment']:,} | -${inv['total_investment']:,} | -${inv['total_investment']:,} |")
    for yd in model["yearly_breakdown"]:
        cum_str = f"${yd['cumulative']:,}" if yd["cumulative"] >= 0 else f"-${abs(yd['cumulative']):,}"
        lines.append(f"| {yd['year']} | ${yd['gains']:,} | ${yd['costs']:,} | ${yd['net_benefit']:,} | {cum_str} |")
    lines.append("")

    lines.append("## Sensitivity Analysis")
    lines.append("| Scenario | ROI | Payback | NPV |")
    lines.append("|----------|-----|---------|-----|")
    for name, s in model["sensitivity_analysis"].items():
        lines.append(f"| {name.title()} | {s['roi_pct']}% | {s['payback_months']} mo | ${s['npv']:,} |")
    lines.append("")

    be = model["breakeven"]
    lines.append("## Break-Even")
    lines.append(f"- **Minimum annual gains for positive ROI:** ${be['minimum_annual_gains_for_positive_roi']:,}")
    lines.append(f"- **Minimum adoption rate:** {be['minimum_adoption_rate_pct']}%")
    lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Build an ROI model from investment and savings inputs.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python calculate_roi.py --investment 150000 --annual-savings 200000 --years 3
  python calculate_roi.py --investment 150000 --annual-savings 200000 --annual-cost 50000 --years 3
  python calculate_roi.py --investment 150000 --annual-savings 100000 --revenue-gain 80000 --productivity-gain 50000 --years 3
        """,
    )
    parser.add_argument("--investment", type=float, required=True, help="Total upfront investment amount")
    parser.add_argument("--annual-savings", type=float, default=0, help="Annual cost savings")
    parser.add_argument("--revenue-gain", type=float, default=0, help="Annual revenue gain")
    parser.add_argument("--productivity-gain", type=float, default=0, help="Annual productivity gain value")
    parser.add_argument("--risk-reduction", type=float, default=0, help="Annual risk reduction value")
    parser.add_argument("--annual-cost", type=float, default=0, help="Annual ongoing cost of the solution")
    parser.add_argument("--years", type=int, default=3, choices=[1, 2, 3, 4, 5], help="Analysis period in years (default: 3)")
    parser.add_argument("--discount-rate", type=float, default=10, help="Discount rate for NPV calculation (default: 10%%)")
    parser.add_argument("--format", type=str, choices=["json", "markdown"], default="json", help="Output format (default: json)")

    args = parser.parse_args()

    total_gains = args.annual_savings + args.revenue_gain + args.productivity_gain + args.risk_reduction
    if total_gains <= 0:
        print(json.dumps({"error": "At least one gain type must be positive (--annual-savings, --revenue-gain, --productivity-gain, or --risk-reduction)"}, indent=2))
        return

    model = build_roi_model(
        investment=args.investment,
        annual_savings=args.annual_savings,
        annual_cost=args.annual_cost,
        years=args.years,
        discount_rate=args.discount_rate,
        revenue_gain=args.revenue_gain,
        productivity_gain=args.productivity_gain,
        risk_reduction=args.risk_reduction,
    )

    model["metadata"] = {
        "generated": datetime.now().isoformat(),
        "inputs": {
            "investment": args.investment,
            "annual_savings": args.annual_savings,
            "revenue_gain": args.revenue_gain,
            "productivity_gain": args.productivity_gain,
            "risk_reduction": args.risk_reduction,
            "annual_cost": args.annual_cost,
            "years": args.years,
            "discount_rate": args.discount_rate,
        },
    }

    if args.format == "json":
        print(json.dumps(model, indent=2))
    else:
        print(format_markdown(model))


if __name__ == "__main__":
    main()
