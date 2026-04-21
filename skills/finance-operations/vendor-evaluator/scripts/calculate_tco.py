#!/usr/bin/env python3
"""
Build Total Cost of Ownership model for vendor comparison.

Usage:
    python calculate_tco.py --vendor "Vendor A" --users 50 --years 3
    python calculate_tco.py --compare --users 50 --years 3
    python calculate_tco.py --compare --users 50 --years 3 --format json
"""

import argparse
import json
from datetime import datetime

VENDOR_COST_PROFILES = {
    "CloudPlatform Pro": {
        "per_user_monthly": 45,
        "annual_discount": 0.15,
        "setup_fee": 15000,
        "implementation_services": 25000,
        "training_initial": 5000,
        "training_ongoing": 1000,
        "migration_cost": 8000,
        "annual_price_increase": 0.05,
        "internal_impl_hours": 200,
        "internal_admin_hours_monthly": 10,
        "integration_hours": 80,
        "integration_maintenance_hours_monthly": 5,
        "ramp_up_productivity_loss_months": 2,
    },
    "AgileTools Inc": {
        "per_user_monthly": 35,
        "annual_discount": 0.20,
        "setup_fee": 5000,
        "implementation_services": 12000,
        "training_initial": 3000,
        "training_ongoing": 500,
        "migration_cost": 5000,
        "annual_price_increase": 0.07,
        "internal_impl_hours": 120,
        "internal_admin_hours_monthly": 8,
        "integration_hours": 40,
        "integration_maintenance_hours_monthly": 3,
        "ramp_up_productivity_loss_months": 1,
    },
    "BudgetSoft": {
        "per_user_monthly": 19,
        "annual_discount": 0.10,
        "setup_fee": 0,
        "implementation_services": 3000,
        "training_initial": 1500,
        "training_ongoing": 500,
        "migration_cost": 2000,
        "annual_price_increase": 0.10,
        "internal_impl_hours": 80,
        "internal_admin_hours_monthly": 15,
        "integration_hours": 60,
        "integration_maintenance_hours_monthly": 8,
        "ramp_up_productivity_loss_months": 3,
    },
}

INTERNAL_HOURLY_RATE = 75  # fully loaded internal cost


def calculate_tco(vendor_name, profile, users, years, user_growth_pct=10):
    """Calculate multi-year TCO for a vendor."""
    yearly = []
    total = 0
    current_users = users

    for year in range(1, years + 1):
        # License cost with annual increase
        price_multiplier = (1 + profile["annual_price_increase"]) ** (year - 1)
        monthly_per_user = profile["per_user_monthly"] * price_multiplier
        annual_license = monthly_per_user * current_users * 12 * (1 - profile["annual_discount"])

        # Year 1 one-time costs
        setup = profile["setup_fee"] if year == 1 else 0
        implementation = profile["implementation_services"] if year == 1 else 0
        training = profile["training_initial"] if year == 1 else profile["training_ongoing"]
        migration = profile["migration_cost"] if year == 1 else 0

        # Internal costs
        impl_hours = profile["internal_impl_hours"] if year == 1 else 0
        admin_hours = profile["internal_admin_hours_monthly"] * 12
        integration_hours = profile["integration_hours"] if year == 1 else 0
        integration_maint = profile["integration_maintenance_hours_monthly"] * 12
        ramp_loss = (profile["ramp_up_productivity_loss_months"] * current_users * 20 * INTERNAL_HOURLY_RATE * 0.1) if year == 1 else 0

        internal_cost = (impl_hours + admin_hours + integration_hours + integration_maint) * INTERNAL_HOURLY_RATE

        # Additional users in subsequent years
        additional_users_cost = 0
        if year > 1:
            new_users = round(users * user_growth_pct / 100)
            current_users += new_users
            additional_users_cost = monthly_per_user * new_users * 12 * (1 - profile["annual_discount"])

        year_total = (annual_license + setup + implementation + training +
                      migration + internal_cost + ramp_loss + additional_users_cost)
        total += year_total

        yearly.append({
            "year": year,
            "users": current_users,
            "license": round(annual_license),
            "setup": round(setup),
            "implementation": round(implementation),
            "training": round(training),
            "migration": round(migration),
            "internal": round(internal_cost),
            "ramp_loss": round(ramp_loss),
            "additional_users": round(additional_users_cost),
            "year_total": round(year_total),
        })

    return {
        "vendor": vendor_name,
        "initial_users": users,
        "years": years,
        "yearly": yearly,
        "total_tco": round(total),
        "avg_per_user_monthly": round(total / (sum(y["users"] for y in yearly) / len(yearly)) / (years * 12), 2),
    }


def print_tco(tco):
    """Print formatted TCO report."""
    print(f"\n  {tco['vendor']}")
    print(f"  {'─'*60}")
    header = f"  {'':24}"
    for y in tco["yearly"]:
        header += f"{'Year ' + str(y['year']):>12}"
    header += f"{'TOTAL':>12}"
    print(header)
    print(f"  {'─'*24}" + "─" * 12 * (len(tco["yearly"]) + 1))

    rows = [
        ("License/Subscription", "license"),
        ("Setup/Onboarding", "setup"),
        ("Implementation", "implementation"),
        ("Training", "training"),
        ("Data Migration", "migration"),
        ("Internal Team Cost", "internal"),
        ("Productivity Loss", "ramp_loss"),
        ("Additional Users", "additional_users"),
    ]

    for label, key in rows:
        values = [y[key] for y in tco["yearly"]]
        if sum(values) > 0:
            row = f"  {label:<24}"
            for v in values:
                row += f"${v:>11,}" if v > 0 else f"{'--':>12}"
            row += f"${sum(values):>11,}"
            print(row)

    print(f"  {'─'*24}" + "─" * 12 * (len(tco["yearly"]) + 1))
    total_row = f"  {'YEAR TOTAL':<24}"
    for y in tco["yearly"]:
        total_row += f"${y['year_total']:>11,}"
    total_row += f"${tco['total_tco']:>11,}"
    print(total_row)
    print(f"  Avg per user/month: ${tco['avg_per_user_monthly']:.2f}")


def main():
    parser = argparse.ArgumentParser(
        description="Build Total Cost of Ownership model for vendors.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --vendor "CloudPlatform Pro" --users 50 --years 3
  %(prog)s --compare --users 50 --years 3
        """,
    )
    parser.add_argument("--vendor", default=None, help="Vendor name to analyze")
    parser.add_argument("--compare", action="store_true", help="Compare all vendors")
    parser.add_argument("--users", type=int, required=True, help="Number of users")
    parser.add_argument("--years", type=int, default=3, help="TCO horizon in years (default: 3)")
    parser.add_argument("--growth", type=int, default=10, help="Annual user growth % (default: 10)")
    parser.add_argument("--format", choices=["text", "json"], default="text")

    args = parser.parse_args()

    if args.compare:
        vendors_to_analyze = list(VENDOR_COST_PROFILES.keys())
    elif args.vendor:
        match = None
        for k in VENDOR_COST_PROFILES:
            if args.vendor.lower() in k.lower():
                match = k
                break
        vendors_to_analyze = [match] if match else list(VENDOR_COST_PROFILES.keys())[:1]
    else:
        vendors_to_analyze = list(VENDOR_COST_PROFILES.keys())

    results = []
    for vendor in vendors_to_analyze:
        tco = calculate_tco(vendor, VENDOR_COST_PROFILES[vendor], args.users, args.years, args.growth)
        results.append(tco)

    if args.format == "json":
        print(json.dumps(results, indent=2))
    else:
        print("=" * 80)
        print(f"  TOTAL COST OF OWNERSHIP ANALYSIS ({args.years}-Year)")
        print(f"  Users: {args.users} (growing {args.growth}%/year)")
        print(f"  Generated: {datetime.now().strftime('%Y-%m-%d')}")
        print("=" * 80)

        for tco in results:
            print_tco(tco)

        if len(results) > 1:
            print(f"\n  COMPARISON SUMMARY:")
            print(f"  {'─'*60}")
            ranked = sorted(results, key=lambda r: r["total_tco"])
            for i, r in enumerate(ranked, 1):
                savings = r["total_tco"] - ranked[0]["total_tco"]
                extra = f" (+${savings:,})" if savings > 0 else " (lowest)"
                print(f"  #{i} {r['vendor']:<25} {args.years}-yr TCO: ${r['total_tco']:>10,}  Per user/mo: ${r['avg_per_user_monthly']:.2f}{extra}")
        print()


if __name__ == "__main__":
    main()
