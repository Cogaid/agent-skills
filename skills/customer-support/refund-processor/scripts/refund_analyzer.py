#!/usr/bin/env python3
"""
Analyze refund patterns and identify trends.

Usage:
    python refund_analyzer.py refunds.json
    python refund_analyzer.py refunds.csv --format summary
    python refund_analyzer.py --customer customer_id refunds.json

Output: Refund pattern analysis and recommendations
"""

import argparse
import json
import csv
import sys
from datetime import datetime, timedelta
from collections import defaultdict


# Risk thresholds
RISK_THRESHOLDS = {
    "refund_rate": 0.30,  # 30% refund rate is concerning
    "refunds_per_90_days": 3,  # 3+ refunds in 90 days
    "high_value_threshold": 500,  # Refunds over $500
    "velocity_threshold": 2  # 2+ refunds in 7 days
}


def load_data(file_path):
    """Load refund data from JSON or CSV file."""

    if file_path.endswith('.json'):
        with open(file_path, 'r') as f:
            return json.load(f)
    elif file_path.endswith('.csv'):
        data = []
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert numeric fields
                if 'amount' in row:
                    row['amount'] = float(row['amount'])
                if 'date' in row:
                    row['date'] = row['date']
                data.append(row)
        return data
    else:
        raise ValueError("Unsupported file format. Use .json or .csv")


def analyze_overall(refunds):
    """Analyze overall refund statistics."""

    if not refunds:
        return {"error": "No refund data provided"}

    total_refunds = len(refunds)
    total_amount = sum(r.get('amount', 0) for r in refunds)

    # Reason breakdown
    reasons = defaultdict(lambda: {"count": 0, "amount": 0})
    for r in refunds:
        reason = r.get('reason', 'unknown')
        reasons[reason]['count'] += 1
        reasons[reason]['amount'] += r.get('amount', 0)

    # Category breakdown
    categories = defaultdict(lambda: {"count": 0, "amount": 0})
    for r in refunds:
        category = r.get('category', 'unknown')
        categories[category]['count'] += 1
        categories[category]['amount'] += r.get('amount', 0)

    # Time analysis
    dates = []
    for r in refunds:
        if 'date' in r:
            try:
                dates.append(datetime.fromisoformat(r['date'].replace('Z', '+00:00')))
            except (ValueError, AttributeError):
                pass

    date_analysis = {}
    if dates:
        date_analysis = {
            "earliest": min(dates).isoformat(),
            "latest": max(dates).isoformat(),
            "date_range_days": (max(dates) - min(dates)).days
        }

    return {
        "summary": {
            "total_refunds": total_refunds,
            "total_amount": round(total_amount, 2),
            "average_amount": round(total_amount / total_refunds, 2) if total_refunds else 0
        },
        "by_reason": dict(reasons),
        "by_category": dict(categories),
        "date_analysis": date_analysis
    }


def analyze_customer(refunds, customer_id):
    """Analyze refund patterns for a specific customer."""

    customer_refunds = [r for r in refunds if r.get('customer_id') == customer_id]

    if not customer_refunds:
        return {"error": f"No refunds found for customer: {customer_id}"}

    total = len(customer_refunds)
    total_amount = sum(r.get('amount', 0) for r in customer_refunds)

    # Calculate velocity (refunds in last 90 days)
    now = datetime.now()
    recent_refunds = []
    for r in customer_refunds:
        if 'date' in r:
            try:
                date = datetime.fromisoformat(r['date'].replace('Z', '+00:00'))
                if (now - date).days <= 90:
                    recent_refunds.append(r)
            except (ValueError, AttributeError):
                pass

    # Risk assessment
    risk_factors = []
    risk_score = 0

    if len(recent_refunds) >= RISK_THRESHOLDS["refunds_per_90_days"]:
        risk_factors.append(f"{len(recent_refunds)} refunds in last 90 days")
        risk_score += 30

    # Check for high-value refunds
    high_value = [r for r in customer_refunds if r.get('amount', 0) > RISK_THRESHOLDS["high_value_threshold"]]
    if high_value:
        risk_factors.append(f"{len(high_value)} high-value refunds (>${RISK_THRESHOLDS['high_value_threshold']})")
        risk_score += 20

    # Check for velocity (multiple refunds in short period)
    if len(recent_refunds) >= 2:
        recent_dates = []
        for r in recent_refunds:
            if 'date' in r:
                try:
                    recent_dates.append(datetime.fromisoformat(r['date'].replace('Z', '+00:00')))
                except (ValueError, AttributeError):
                    pass

        if len(recent_dates) >= 2:
            recent_dates.sort()
            for i in range(1, len(recent_dates)):
                if (recent_dates[i] - recent_dates[i-1]).days <= 7:
                    risk_factors.append("Multiple refunds within 7 days")
                    risk_score += 25
                    break

    # Determine risk level
    if risk_score >= 50:
        risk_level = "high"
    elif risk_score >= 25:
        risk_level = "medium"
    else:
        risk_level = "low"

    # Reason patterns
    reasons = defaultdict(int)
    for r in customer_refunds:
        reasons[r.get('reason', 'unknown')] += 1

    return {
        "customer_id": customer_id,
        "summary": {
            "total_refunds": total,
            "total_amount": round(total_amount, 2),
            "refunds_last_90_days": len(recent_refunds)
        },
        "risk_assessment": {
            "level": risk_level,
            "score": risk_score,
            "factors": risk_factors
        },
        "reason_breakdown": dict(reasons),
        "refund_history": customer_refunds
    }


def identify_patterns(refunds):
    """Identify patterns and anomalies in refund data."""

    patterns = {
        "high_frequency_customers": [],
        "high_value_refunds": [],
        "common_reasons": [],
        "problematic_categories": [],
        "recommendations": []
    }

    # Customer frequency analysis
    customer_counts = defaultdict(lambda: {"count": 0, "amount": 0})
    for r in refunds:
        cid = r.get('customer_id', 'unknown')
        customer_counts[cid]['count'] += 1
        customer_counts[cid]['amount'] += r.get('amount', 0)

    # Find high-frequency customers
    for cid, data in customer_counts.items():
        if data['count'] >= 3:
            patterns["high_frequency_customers"].append({
                "customer_id": cid,
                "refund_count": data['count'],
                "total_amount": round(data['amount'], 2)
            })

    # High-value refunds
    for r in refunds:
        if r.get('amount', 0) > RISK_THRESHOLDS["high_value_threshold"]:
            patterns["high_value_refunds"].append({
                "customer_id": r.get('customer_id'),
                "amount": r.get('amount'),
                "reason": r.get('reason'),
                "date": r.get('date')
            })

    # Reason analysis
    reason_counts = defaultdict(int)
    for r in refunds:
        reason_counts[r.get('reason', 'unknown')] += 1

    total = len(refunds)
    for reason, count in sorted(reason_counts.items(), key=lambda x: -x[1]):
        percentage = (count / total * 100) if total else 0
        patterns["common_reasons"].append({
            "reason": reason,
            "count": count,
            "percentage": round(percentage, 1)
        })

    # Category issues
    category_rates = defaultdict(lambda: {"refunds": 0, "amount": 0})
    for r in refunds:
        cat = r.get('category', 'unknown')
        category_rates[cat]['refunds'] += 1
        category_rates[cat]['amount'] += r.get('amount', 0)

    for cat, data in category_rates.items():
        if data['refunds'] >= 5:  # Minimum sample size
            patterns["problematic_categories"].append({
                "category": cat,
                "refund_count": data['refunds'],
                "total_amount": round(data['amount'], 2)
            })

    # Generate recommendations
    if patterns["high_frequency_customers"]:
        patterns["recommendations"].append({
            "type": "fraud_review",
            "message": f"Review {len(patterns['high_frequency_customers'])} high-frequency customers for potential abuse"
        })

    if len(patterns["common_reasons"]) > 0:
        top_reason = patterns["common_reasons"][0]
        if top_reason["percentage"] > 30:
            patterns["recommendations"].append({
                "type": "root_cause",
                "message": f"Investigate root cause of '{top_reason['reason']}' ({top_reason['percentage']}% of refunds)"
            })

    if patterns["problematic_categories"]:
        worst = max(patterns["problematic_categories"], key=lambda x: x["refund_count"])
        patterns["recommendations"].append({
            "type": "quality",
            "message": f"Review quality issues in '{worst['category']}' category ({worst['refund_count']} refunds)"
        })

    return patterns


def generate_report(analysis, output_format='text'):
    """Generate a formatted report from analysis."""

    if output_format == 'json':
        return json.dumps(analysis, indent=2)

    # Text format
    lines = []
    lines.append("\n" + "=" * 50)
    lines.append("REFUND ANALYSIS REPORT")
    lines.append("=" * 50)

    if "summary" in analysis:
        lines.append("\n--- SUMMARY ---")
        summary = analysis["summary"]
        lines.append(f"Total Refunds: {summary.get('total_refunds', 'N/A')}")
        lines.append(f"Total Amount: ${summary.get('total_amount', 0):,.2f}")
        lines.append(f"Average Amount: ${summary.get('average_amount', 0):,.2f}")

    if "risk_assessment" in analysis:
        lines.append("\n--- RISK ASSESSMENT ---")
        risk = analysis["risk_assessment"]
        lines.append(f"Risk Level: {risk.get('level', 'N/A').upper()}")
        lines.append(f"Risk Score: {risk.get('score', 0)}/100")
        if risk.get("factors"):
            lines.append("Risk Factors:")
            for factor in risk["factors"]:
                lines.append(f"  • {factor}")

    if "by_reason" in analysis:
        lines.append("\n--- BY REASON ---")
        for reason, data in sorted(analysis["by_reason"].items(),
                                   key=lambda x: -x[1]["count"]):
            lines.append(f"  {reason}: {data['count']} (${data['amount']:,.2f})")

    if "common_reasons" in analysis:
        lines.append("\n--- TOP REASONS ---")
        for item in analysis["common_reasons"][:5]:
            lines.append(f"  {item['reason']}: {item['count']} ({item['percentage']}%)")

    if "high_frequency_customers" in analysis and analysis["high_frequency_customers"]:
        lines.append("\n--- HIGH FREQUENCY CUSTOMERS ---")
        for cust in analysis["high_frequency_customers"][:10]:
            lines.append(f"  {cust['customer_id']}: {cust['refund_count']} refunds (${cust['total_amount']:,.2f})")

    if "recommendations" in analysis and analysis["recommendations"]:
        lines.append("\n--- RECOMMENDATIONS ---")
        for rec in analysis["recommendations"]:
            lines.append(f"  [{rec['type'].upper()}] {rec['message']}")

    lines.append("\n" + "=" * 50)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description='Analyze refund patterns')
    parser.add_argument('file', nargs='?', help='Refund data file (JSON or CSV)')
    parser.add_argument('--customer', '-c', help='Analyze specific customer')
    parser.add_argument('--patterns', '-p', action='store_true',
                        help='Identify patterns and anomalies')
    parser.add_argument('--format', '-f', choices=['json', 'text'],
                        default='text', help='Output format')
    parser.add_argument('--sample', '-s', action='store_true',
                        help='Generate sample data for testing')

    args = parser.parse_args()

    if args.sample:
        # Generate sample data
        sample_data = [
            {"customer_id": "C001", "amount": 99.99, "reason": "defective",
             "category": "electronics", "date": "2025-01-15T10:00:00Z"},
            {"customer_id": "C001", "amount": 49.99, "reason": "preference",
             "category": "apparel", "date": "2025-01-20T14:30:00Z"},
            {"customer_id": "C001", "amount": 199.99, "reason": "quality",
             "category": "electronics", "date": "2025-02-01T09:15:00Z"},
            {"customer_id": "C002", "amount": 599.99, "reason": "defective",
             "category": "electronics", "date": "2025-01-18T11:00:00Z"},
            {"customer_id": "C003", "amount": 29.99, "reason": "wrong_item",
             "category": "apparel", "date": "2025-01-22T16:45:00Z"},
            {"customer_id": "C004", "amount": 149.99, "reason": "preference",
             "category": "furniture", "date": "2025-01-25T13:00:00Z"},
            {"customer_id": "C002", "amount": 79.99, "reason": "damaged",
             "category": "apparel", "date": "2025-02-05T10:30:00Z"},
            {"customer_id": "C005", "amount": 399.99, "reason": "not_received",
             "category": "electronics", "date": "2025-02-08T15:00:00Z"},
        ]
        print(json.dumps(sample_data, indent=2))
        return

    if not args.file:
        parser.print_help()
        return

    try:
        refunds = load_data(args.file)
    except FileNotFoundError:
        print(json.dumps({"error": f"File not found: {args.file}"}))
        sys.exit(1)
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)

    if args.customer:
        analysis = analyze_customer(refunds, args.customer)
    elif args.patterns:
        analysis = identify_patterns(refunds)
    else:
        analysis = analyze_overall(refunds)

    print(generate_report(analysis, args.format))


if __name__ == '__main__':
    main()
