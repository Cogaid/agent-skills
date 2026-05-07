#!/usr/bin/env python3
"""Generate a compliance gap analysis by comparing current controls against framework requirements.

Usage:
    python gap_analysis.py --framework gdpr
    python gap_analysis.py --framework soc2 --output gaps.json
"""

import argparse
import json
import sys
from datetime import datetime

SAMPLE_GAPS = {
    "gdpr": [
        {
            "id": "GAP-001",
            "control": "Record of processing activities (Art. 30)",
            "status": "Partial",
            "gap": "Processing inventory exists but is incomplete - missing 3 departments",
            "severity": "High",
            "remediation": "Complete data mapping for Marketing, HR, and Finance departments",
            "effort": "2 weeks",
            "owner": "[ASSIGN]",
        },
        {
            "id": "GAP-002",
            "control": "Data subject access request process",
            "status": "Missing",
            "gap": "No formal DSAR process exists",
            "severity": "Critical",
            "remediation": "Implement DSAR workflow with intake form, tracking, and 30-day SLA",
            "effort": "4 weeks",
            "owner": "[ASSIGN]",
        },
        {
            "id": "GAP-003",
            "control": "DPAs signed with all processors",
            "status": "Partial",
            "gap": "DPAs missing for 5 of 12 data processors",
            "severity": "Critical",
            "remediation": "Execute DPAs with remaining 5 processors using standard template",
            "effort": "3 weeks",
            "owner": "[ASSIGN]",
        },
        {
            "id": "GAP-004",
            "control": "Staff privacy training",
            "status": "Missing",
            "gap": "No formal privacy training program",
            "severity": "Medium",
            "remediation": "Develop and deploy annual privacy training for all staff",
            "effort": "6 weeks",
            "owner": "[ASSIGN]",
        },
    ],
    "soc2": [
        {
            "id": "GAP-001",
            "control": "CC6: Logical access controls",
            "status": "Partial",
            "gap": "MFA not enforced for all production systems",
            "severity": "Critical",
            "remediation": "Enable MFA for all production access via SSO provider",
            "effort": "2 weeks",
            "owner": "[ASSIGN]",
        },
        {
            "id": "GAP-002",
            "control": "CC7: System monitoring",
            "status": "Partial",
            "gap": "SIEM deployed but alert rules incomplete",
            "severity": "High",
            "remediation": "Define and implement alert rules for key security events",
            "effort": "3 weeks",
            "owner": "[ASSIGN]",
        },
        {
            "id": "GAP-003",
            "control": "CC8: Change management",
            "status": "Missing",
            "gap": "No formal change management process documented",
            "severity": "High",
            "remediation": "Document change management policy with approval workflows",
            "effort": "4 weeks",
            "owner": "[ASSIGN]",
        },
    ],
    "hipaa": [
        {
            "id": "GAP-001",
            "control": "Risk analysis",
            "status": "Outdated",
            "gap": "Last risk analysis completed 2 years ago",
            "severity": "Critical",
            "remediation": "Conduct comprehensive risk analysis covering all ePHI systems",
            "effort": "6 weeks",
            "owner": "[ASSIGN]",
        },
        {
            "id": "GAP-002",
            "control": "Encryption of ePHI at rest",
            "status": "Partial",
            "gap": "Database encrypted but backup storage is not",
            "severity": "Critical",
            "remediation": "Enable encryption for backup storage and verify key management",
            "effort": "2 weeks",
            "owner": "[ASSIGN]",
        },
    ],
}


def generate_gap_analysis(framework):
    """Generate a gap analysis for the specified framework."""
    gaps = SAMPLE_GAPS.get(framework, [])

    severity_counts = {}
    for g in gaps:
        sev = g["severity"]
        severity_counts[sev] = severity_counts.get(sev, 0) + 1

    report = {
        "metadata": {
            "framework": framework.upper(),
            "analysis_date": datetime.now().strftime("%Y-%m-%d"),
            "total_gaps": len(gaps),
            "status": "SAMPLE_DATA - Replace with actual assessment results",
        },
        "summary": {
            "gaps_by_severity": severity_counts,
            "highest_priority": gaps[0]["id"] if gaps else "None",
        },
        "gaps": gaps,
        "remediation_timeline": {
            "immediate_0_30_days": [g["id"] for g in gaps if g["severity"] == "Critical"],
            "short_term_30_90_days": [g["id"] for g in gaps if g["severity"] == "High"],
            "long_term_90_plus_days": [g["id"] for g in gaps if g["severity"] in ("Medium", "Low")],
        },
    }

    return report


def main():
    parser = argparse.ArgumentParser(
        description="Generate a compliance gap analysis for a specified framework."
    )
    parser.add_argument(
        "--framework",
        choices=["gdpr", "soc2", "hipaa", "pci-dss"],
        required=True,
        help="Framework to analyze gaps against",
    )
    parser.add_argument(
        "--output",
        help="Output file path (default: stdout)",
    )

    args = parser.parse_args()

    report = generate_gap_analysis(args.framework)
    output = json.dumps(report, indent=2)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Gap analysis written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
