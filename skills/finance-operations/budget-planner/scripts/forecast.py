#!/usr/bin/env python3
"""
Generate rolling forecasts using various methodologies.

Usage:
    python forecast.py --method driver-based --horizon 12
    python forecast.py --method moving-average --horizon 6 --format json
    python forecast.py --method scenario --horizon 12
"""

import argparse
import json
from datetime import datetime

# Historical monthly data for forecasting
HISTORICAL = [
    {"month": "2025-07", "revenue": 165000, "expenses": 148000, "headcount": 38},
    {"month": "2025-08", "revenue": 170000, "expenses": 150000, "headcount": 39},
    {"month": "2025-09", "revenue": 172000, "expenses": 152000, "headcount": 39},
    {"month": "2025-10", "revenue": 178000, "expenses": 155000, "headcount": 40},
    {"month": "2025-11", "revenue": 180000, "expenses": 158000, "headcount": 42},
    {"month": "2025-12", "revenue": 188000, "expenses": 160000, "headcount": 44},
    {"month": "2026-01", "revenue": 198000, "expenses": 165000, "headcount": 45},
    {"month": "2026-02", "revenue": 205000, "expenses": 168000, "headcount": 46},
    {"month": "2026-03", "revenue": 215000, "expenses": 172000, "headcount": 47},
    {"month": "2026-04", "revenue": 228000, "expenses": 175000, "headcount": 48},
]

DRIVERS = {
    "revenue_per_customer": 750,
    "customers_current": 325,
    "monthly_customer_growth": 22,
    "avg_salary_monthly": 10000,
    "benefits_rate": 0.28,
    "non_people_ratio": 0.35,
    "monthly_churn_pct": 1.4,
}


def forecast_moving_average(historical, horizon, window=3):
    """Simple moving average forecast."""
    revenues = [h["revenue"] for h in historical]
    expenses = [h["expenses"] for h in historical]
    forecasts = []
    last_month = datetime.strptime(historical[-1]["month"], "%Y-%m")

    for i in range(horizon):
        month = last_month.replace(month=last_month.month + i + 1) if last_month.month + i + 1 <= 12 else \
            last_month.replace(year=last_month.year + (last_month.month + i) // 12, month=(last_month.month + i) % 12 + 1)
        rev_avg = sum(revenues[-window:]) / window
        exp_avg = sum(expenses[-window:]) / window
        revenues.append(rev_avg)
        expenses.append(exp_avg)
        forecasts.append({
            "month": month.strftime("%Y-%m"),
            "revenue": round(rev_avg),
            "expenses": round(exp_avg),
            "net": round(rev_avg - exp_avg),
            "method": "moving_average",
            "confidence": "medium",
        })
    return forecasts


def forecast_growth_rate(historical, horizon):
    """Growth rate based forecast."""
    recent = historical[-6:]
    rev_growth = (recent[-1]["revenue"] / recent[0]["revenue"]) ** (1 / len(recent)) - 1
    exp_growth = (recent[-1]["expenses"] / recent[0]["expenses"]) ** (1 / len(recent)) - 1

    forecasts = []
    last_rev = historical[-1]["revenue"]
    last_exp = historical[-1]["expenses"]
    last_month = datetime.strptime(historical[-1]["month"], "%Y-%m")

    for i in range(horizon):
        month_num = (last_month.month + i) % 12 + 1
        year = last_month.year + (last_month.month + i) // 12
        last_rev *= (1 + rev_growth)
        last_exp *= (1 + exp_growth)
        forecasts.append({
            "month": f"{year}-{month_num:02d}",
            "revenue": round(last_rev),
            "expenses": round(last_exp),
            "net": round(last_rev - last_exp),
            "method": "growth_rate",
            "monthly_rev_growth": round(rev_growth * 100, 2),
            "confidence": "medium",
        })
    return forecasts


def forecast_driver_based(historical, horizon):
    """Driver-based forecast using business inputs."""
    d = DRIVERS
    forecasts = []
    customers = d["customers_current"]
    headcount = historical[-1]["headcount"]
    last_month = datetime.strptime(historical[-1]["month"], "%Y-%m")

    for i in range(horizon):
        month_num = (last_month.month + i) % 12 + 1
        year = last_month.year + (last_month.month + i) // 12

        # Customer growth with churn
        new_customers = d["monthly_customer_growth"]
        churned = round(customers * d["monthly_churn_pct"] / 100)
        customers = customers + new_customers - churned

        revenue = customers * d["revenue_per_customer"]

        # Headcount grows every 3 months
        if i > 0 and i % 3 == 0:
            headcount += 1

        people_cost = headcount * d["avg_salary_monthly"] * (1 + d["benefits_rate"])
        non_people = people_cost * d["non_people_ratio"]
        expenses = round(people_cost + non_people)

        forecasts.append({
            "month": f"{year}-{month_num:02d}",
            "revenue": round(revenue),
            "expenses": expenses,
            "net": round(revenue - expenses),
            "customers": customers,
            "headcount": headcount,
            "method": "driver_based",
            "confidence": "high",
        })
    return forecasts


def forecast_scenario(historical, horizon):
    """Three-scenario forecast (conservative, base, optimistic)."""
    base = forecast_growth_rate(historical, horizon)
    scenarios = {"conservative": [], "base": base, "optimistic": []}

    for f in base:
        scenarios["conservative"].append({
            **f,
            "revenue": round(f["revenue"] * 0.85),
            "expenses": round(f["expenses"] * 1.05),
            "net": round(f["revenue"] * 0.85 - f["expenses"] * 1.05),
            "scenario": "conservative",
        })
        scenarios["optimistic"].append({
            **f,
            "revenue": round(f["revenue"] * 1.15),
            "expenses": round(f["expenses"] * 0.98),
            "net": round(f["revenue"] * 1.15 - f["expenses"] * 0.98),
            "scenario": "optimistic",
        })
    return scenarios


def print_forecast(forecasts, method, historical):
    """Print formatted forecast."""
    print("=" * 75)
    print(f"  ROLLING FORECAST ({method.replace('-', ' ').upper()})")
    print(f"  Generated: {datetime.now().strftime('%Y-%m-%d')}")
    print(f"  Horizon: {len(forecasts) if isinstance(forecasts, list) else len(forecasts.get('base', []))} months")
    print("=" * 75)

    if method == "scenario":
        print(f"\n  {'Month':<10} {'Conservative':>14} {'Base Case':>14} {'Optimistic':>14} {'Weighted Avg':>14}")
        print(f"  {'─'*10} {'─'*14} {'─'*14} {'─'*14} {'─'*14}")
        for i in range(len(forecasts["base"])):
            c = forecasts["conservative"][i]["net"]
            b = forecasts["base"][i]["net"]
            o = forecasts["optimistic"][i]["net"]
            w = round(c * 0.25 + b * 0.50 + o * 0.25)
            print(f"  {forecasts['base'][i]['month']:<10} ${c:>13,.0f} ${b:>13,.0f} ${o:>13,.0f} ${w:>13,.0f}")
    else:
        print(f"\n  HISTORICAL (last 3 months):")
        for h in historical[-3:]:
            net = h["revenue"] - h["expenses"]
            print(f"    {h['month']}   Rev: ${h['revenue']:>10,.0f}   Exp: ${h['expenses']:>10,.0f}   Net: ${net:>10,.0f}")

        print(f"\n  FORECAST:")
        print(f"  {'Month':<10} {'Revenue':>12} {'Expenses':>12} {'Net':>12} {'Confidence':>12}")
        print(f"  {'─'*10} {'─'*12} {'─'*12} {'─'*12} {'─'*12}")
        for f in forecasts:
            print(f"  {f['month']:<10} ${f['revenue']:>11,.0f} ${f['expenses']:>11,.0f} ${f['net']:>11,.0f} {f['confidence']:>12}")

        total_rev = sum(f["revenue"] for f in forecasts)
        total_exp = sum(f["expenses"] for f in forecasts)
        print(f"  {'─'*10} {'─'*12} {'─'*12} {'─'*12}")
        print(f"  {'TOTAL':<10} ${total_rev:>11,.0f} ${total_exp:>11,.0f} ${total_rev - total_exp:>11,.0f}")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Generate rolling forecasts with various methods.",
    )
    parser.add_argument("--method", required=True,
                        choices=["moving-average", "growth-rate", "driver-based", "scenario"],
                        help="Forecasting method")
    parser.add_argument("--horizon", type=int, default=12, help="Forecast horizon in months (default: 12)")
    parser.add_argument("--format", choices=["text", "json"], default="text")

    args = parser.parse_args()

    method_map = {
        "moving-average": forecast_moving_average,
        "growth-rate": forecast_growth_rate,
        "driver-based": forecast_driver_based,
        "scenario": forecast_scenario,
    }

    forecasts = method_map[args.method](HISTORICAL, args.horizon)

    if args.format == "json":
        print(json.dumps({"method": args.method, "horizon": args.horizon, "forecasts": forecasts}, indent=2))
    else:
        print_forecast(forecasts, args.method, HISTORICAL)


if __name__ == "__main__":
    main()
