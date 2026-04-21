#!/usr/bin/env python3
"""Detect anomalies in metric data based on statistical thresholds.

Usage:
    python anomaly_detect.py --sensitivity 2
    python anomaly_detect.py --sensitivity 1.5 --output anomalies.json
"""

import argparse
import json
import math
import random
import sys
from datetime import datetime, timedelta

# Sample time series data with some anomalies injected
def generate_sample_data():
    """Generate sample time series data with injected anomalies."""
    metrics = {}
    base_date = datetime.now() - timedelta(days=180)

    for metric_name, base_val, noise in [
        ("Revenue", 1000000, 50000),
        ("Active Users", 40000, 2000),
        ("Error Rate", 0.5, 0.15),
        ("Response Time ms", 200, 30),
    ]:
        values = []
        for i in range(180):
            date = base_date + timedelta(days=i)
            val = base_val + random.gauss(0, noise)
            # Inject anomalies at specific points
            if i == 150:
                val = base_val + noise * 4  # High anomaly
            if i == 90:
                val = base_val - noise * 3.5  # Low anomaly
            values.append({"date": date.strftime("%Y-%m-%d"), "value": round(val, 2)})
        metrics[metric_name] = values

    return metrics


def detect_anomalies(values, sensitivity):
    """Detect anomalies using z-score method."""
    data_values = [v["value"] for v in values]
    n = len(data_values)
    if n < 10:
        return []

    mean = sum(data_values) / n
    variance = sum((x - mean) ** 2 for x in data_values) / n
    std_dev = math.sqrt(variance) if variance > 0 else 0.001

    anomalies = []
    for item in values:
        z_score = (item["value"] - mean) / std_dev
        if abs(z_score) >= sensitivity:
            severity = "Critical" if abs(z_score) >= 3 else "Warning" if abs(z_score) >= 2 else "Notable"
            direction = "above" if z_score > 0 else "below"
            anomalies.append({
                "date": item["date"],
                "value": item["value"],
                "z_score": round(z_score, 2),
                "severity": severity,
                "direction": direction,
                "deviation_pct": round(((item["value"] - mean) / mean) * 100, 1),
                "mean": round(mean, 2),
                "std_dev": round(std_dev, 2),
            })

    return anomalies


def main():
    parser = argparse.ArgumentParser(
        description="Detect anomalies in metric data based on statistical thresholds."
    )
    parser.add_argument(
        "--sensitivity",
        type=float,
        default=2.0,
        help="Z-score threshold for anomaly detection (default: 2.0)",
    )
    parser.add_argument(
        "--output",
        help="Output file path (default: stdout)",
    )

    args = parser.parse_args()

    sample_data = generate_sample_data()

    results = {
        "detection_date": datetime.now().strftime("%Y-%m-%d"),
        "sensitivity": args.sensitivity,
        "note": "Using sample data -- replace with actual metric time series",
        "anomalies_by_metric": {},
        "summary": {"total_anomalies": 0, "critical": 0, "warning": 0, "notable": 0},
    }

    for metric_name, values in sample_data.items():
        anomalies = detect_anomalies(values, args.sensitivity)
        results["anomalies_by_metric"][metric_name] = {
            "anomaly_count": len(anomalies),
            "anomalies": anomalies,
        }
        results["summary"]["total_anomalies"] += len(anomalies)
        for a in anomalies:
            sev = a["severity"].lower()
            results["summary"][sev] = results["summary"].get(sev, 0) + 1

    output = json.dumps(results, indent=2)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Anomaly detection results written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
