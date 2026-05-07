#!/usr/bin/env python3
"""Generate an incident report skeleton based on severity and category.

Usage:
    python incident_report.py --severity p1 --category data-breach
    python incident_report.py --severity p0 --category system-outage --output report.json
"""

import argparse
import json
import sys
from datetime import datetime

CATEGORIES = {
    "data-breach": {
        "name": "Data Breach",
        "regulatory_triggers": ["GDPR Art. 33/34", "CCPA", "HIPAA", "PCI-DSS", "State notification laws"],
        "impact_areas": ["records_affected", "data_types_exposed", "data_subjects", "geographic_scope"],
        "immediate_actions": [
            "Isolate affected systems to prevent further exposure",
            "Preserve forensic evidence (logs, images, network captures)",
            "Determine scope of data accessed or exfiltrated",
            "Assess whether notification thresholds are met",
            "Engage legal counsel for regulatory notification assessment",
        ],
    },
    "system-outage": {
        "name": "System Outage",
        "regulatory_triggers": ["SLA obligations", "SOC 2 availability"],
        "impact_areas": ["downtime_duration", "affected_services", "customer_impact", "revenue_impact"],
        "immediate_actions": [
            "Activate incident response and assemble response team",
            "Update status page and notify affected customers",
            "Implement failover or rollback procedures",
            "Identify root cause of service disruption",
            "Estimate time to recovery and communicate ETA",
        ],
    },
    "unauthorized-access": {
        "name": "Unauthorized Access",
        "regulatory_triggers": ["SOC 2 CC6/CC7", "PCI-DSS Req 7-8", "HIPAA 164.312"],
        "impact_areas": ["accounts_compromised", "systems_accessed", "data_exposure", "privilege_level"],
        "immediate_actions": [
            "Disable compromised accounts and credentials",
            "Review access logs for scope of unauthorized activity",
            "Reset credentials for affected and related accounts",
            "Check for persistence mechanisms (backdoors, new accounts)",
            "Enable enhanced monitoring on affected systems",
        ],
    },
    "malware": {
        "name": "Malware / Ransomware",
        "regulatory_triggers": ["All frameworks", "Law enforcement reporting"],
        "impact_areas": ["systems_affected", "data_encrypted", "data_exfiltrated", "lateral_movement"],
        "immediate_actions": [
            "Isolate infected systems from the network immediately",
            "Preserve forensic images before any remediation",
            "Identify malware type and indicators of compromise",
            "Assess lateral movement and additional infections",
            "Engage incident response firm if needed",
        ],
    },
    "compliance-violation": {
        "name": "Compliance Violation",
        "regulatory_triggers": ["Framework-specific", "Internal policy"],
        "impact_areas": ["regulation_violated", "duration_of_violation", "data_subjects_affected", "remediation_complexity"],
        "immediate_actions": [
            "Document the violation with evidence and timeline",
            "Assess the scope and duration of non-compliance",
            "Identify root cause of the compliance gap",
            "Implement immediate corrective measures",
            "Determine self-reporting obligations",
        ],
    },
}

SEVERITIES = {
    "p0": {"name": "Critical", "response_time": "15 minutes", "commander_level": "VP/C-Level", "update_frequency": "Every 30 minutes"},
    "p1": {"name": "High", "response_time": "1 hour", "commander_level": "Director", "update_frequency": "Every 2 hours"},
    "p2": {"name": "Medium", "response_time": "4 hours", "commander_level": "Manager", "update_frequency": "Every 4 hours"},
    "p3": {"name": "Low", "response_time": "24 hours", "commander_level": "Team Lead", "update_frequency": "Daily"},
    "p4": {"name": "Info", "response_time": "48 hours", "commander_level": "Security Analyst", "update_frequency": "As needed"},
}


def generate_report(severity, category):
    """Generate an incident report skeleton."""
    sev = SEVERITIES.get(severity, SEVERITIES["p2"])
    cat = CATEGORIES.get(category, CATEGORIES["compliance-violation"])

    now = datetime.now()
    report_id = f"INC-{now.strftime('%Y-%m')}-[NNN]"

    report = {
        "metadata": {
            "report_id": report_id,
            "classification": cat["name"],
            "severity": f"{severity.upper()} - {sev['name']}",
            "status": "Active",
            "report_date": now.strftime("%Y-%m-%d %H:%M UTC"),
            "incident_date": "[TO BE DETERMINED]",
            "detection_date": "[TO BE DETERMINED]",
            "resolution_date": "Ongoing",
        },
        "response_requirements": {
            "response_time": sev["response_time"],
            "commander_level": sev["commander_level"],
            "update_frequency": sev["update_frequency"],
        },
        "regulatory_triggers": cat["regulatory_triggers"],
        "impact_areas_to_assess": cat["impact_areas"],
        "immediate_actions": cat["immediate_actions"],
        "report_sections": [
            "Executive Summary",
            "Timeline of Events",
            "Impact Assessment (Data, Business, Regulatory)",
            "Root Cause Analysis (5 Whys)",
            "Containment and Response",
            "Long-Term Remediation Plan",
            "Lessons Learned",
            "Appendices (Evidence, Communications, IOCs)",
        ],
        "notification_checklist": [
            {"entity": "Internal stakeholders", "deadline": sev["response_time"], "status": "PENDING"},
            {"entity": "Legal counsel", "deadline": "Immediately for P0/P1", "status": "PENDING"},
            {"entity": "Affected customers", "deadline": "Per SLA and regulation", "status": "PENDING"},
            {"entity": "Regulatory authorities", "deadline": "72h (GDPR) / 60d (HIPAA) / 4d (SEC)", "status": "PENDING"},
            {"entity": "Law enforcement", "deadline": "If criminal activity suspected", "status": "PENDING"},
        ],
    }

    return report


def main():
    parser = argparse.ArgumentParser(
        description="Generate an incident report skeleton based on severity and category."
    )
    parser.add_argument(
        "--severity",
        choices=list(SEVERITIES.keys()),
        default="p2",
        help="Incident severity level (default: p2)",
    )
    parser.add_argument(
        "--category",
        choices=list(CATEGORIES.keys()),
        default="data-breach",
        help="Incident category (default: data-breach)",
    )
    parser.add_argument(
        "--output",
        help="Output file path (default: stdout)",
    )

    args = parser.parse_args()

    report = generate_report(severity=args.severity, category=args.category)
    output = json.dumps(report, indent=2)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Incident report skeleton written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
