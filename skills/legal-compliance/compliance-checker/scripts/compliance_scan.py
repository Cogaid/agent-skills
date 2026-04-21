#!/usr/bin/env python3
"""Run a compliance scan against a specified framework and generate a gap analysis.

Usage:
    python compliance_scan.py --framework gdpr
    python compliance_scan.py --framework soc2 --output report.json
    python compliance_scan.py --framework hipaa --format summary
"""

import argparse
import json
import sys
from datetime import datetime

FRAMEWORKS = {
    "gdpr": {
        "name": "GDPR",
        "controls": [
            {"id": "GDPR-001", "category": "Data Mapping", "control": "Record of processing activities (Art. 30)", "weight": 10},
            {"id": "GDPR-002", "category": "Lawful Basis", "control": "Lawful basis documented for each processing activity", "weight": 10},
            {"id": "GDPR-003", "category": "Consent", "control": "Consent mechanisms are freely given, specific, informed", "weight": 8},
            {"id": "GDPR-004", "category": "Rights", "control": "DSAR process operational (30-day response)", "weight": 10},
            {"id": "GDPR-005", "category": "Rights", "control": "Right to erasure with cascade to processors", "weight": 8},
            {"id": "GDPR-006", "category": "Rights", "control": "Data portability in machine-readable format", "weight": 6},
            {"id": "GDPR-007", "category": "Security", "control": "Encryption at rest and in transit (Art. 32)", "weight": 10},
            {"id": "GDPR-008", "category": "Security", "control": "Access controls and authentication", "weight": 8},
            {"id": "GDPR-009", "category": "Breach", "control": "Breach notification procedure (72h)", "weight": 10},
            {"id": "GDPR-010", "category": "Governance", "control": "DPO appointed (if required)", "weight": 6},
            {"id": "GDPR-011", "category": "Governance", "control": "DPIA for high-risk processing", "weight": 8},
            {"id": "GDPR-012", "category": "Third Party", "control": "DPAs signed with all processors", "weight": 10},
            {"id": "GDPR-013", "category": "Transfer", "control": "International transfer mechanisms (SCCs)", "weight": 8},
            {"id": "GDPR-014", "category": "Retention", "control": "Retention schedules per data category", "weight": 6},
            {"id": "GDPR-015", "category": "Training", "control": "Staff privacy training records", "weight": 6},
        ],
    },
    "soc2": {
        "name": "SOC 2",
        "controls": [
            {"id": "SOC2-CC1", "category": "Control Environment", "control": "CC1: Integrity and ethical values", "weight": 8},
            {"id": "SOC2-CC2", "category": "Communication", "control": "CC2: Internal and external communication", "weight": 6},
            {"id": "SOC2-CC3", "category": "Risk Assessment", "control": "CC3: Risk identification and analysis", "weight": 8},
            {"id": "SOC2-CC4", "category": "Monitoring", "control": "CC4: Monitoring of controls", "weight": 8},
            {"id": "SOC2-CC5", "category": "Control Activities", "control": "CC5: Selection and development of controls", "weight": 8},
            {"id": "SOC2-CC6", "category": "Access", "control": "CC6: Logical and physical access controls", "weight": 10},
            {"id": "SOC2-CC7", "category": "Operations", "control": "CC7: System operations and monitoring", "weight": 10},
            {"id": "SOC2-CC8", "category": "Change Mgmt", "control": "CC8: Change management processes", "weight": 8},
            {"id": "SOC2-CC9", "category": "Risk Mitigation", "control": "CC9: Risk mitigation activities", "weight": 8},
            {"id": "SOC2-A1", "category": "Availability", "control": "A1: System availability and DR", "weight": 8},
            {"id": "SOC2-PI1", "category": "Processing", "control": "PI1: Processing completeness and accuracy", "weight": 6},
            {"id": "SOC2-C1", "category": "Confidentiality", "control": "C1: Confidential information protection", "weight": 8},
        ],
    },
    "hipaa": {
        "name": "HIPAA",
        "controls": [
            {"id": "HIPAA-A01", "category": "Administrative", "control": "Security officer designated", "weight": 10},
            {"id": "HIPAA-A02", "category": "Administrative", "control": "Risk analysis completed", "weight": 10},
            {"id": "HIPAA-A03", "category": "Administrative", "control": "Workforce training on PHI", "weight": 8},
            {"id": "HIPAA-A04", "category": "Administrative", "control": "Sanction policy for violations", "weight": 6},
            {"id": "HIPAA-A05", "category": "Administrative", "control": "Contingency plan (backup, DR)", "weight": 8},
            {"id": "HIPAA-A06", "category": "Administrative", "control": "BAAs with all vendors", "weight": 10},
            {"id": "HIPAA-P01", "category": "Physical", "control": "Facility access controls", "weight": 8},
            {"id": "HIPAA-P02", "category": "Physical", "control": "Device and media controls", "weight": 8},
            {"id": "HIPAA-T01", "category": "Technical", "control": "Unique user identification", "weight": 8},
            {"id": "HIPAA-T02", "category": "Technical", "control": "Encryption of ePHI", "weight": 10},
            {"id": "HIPAA-T03", "category": "Technical", "control": "Audit controls and logging", "weight": 8},
            {"id": "HIPAA-T04", "category": "Technical", "control": "Transmission security (TLS)", "weight": 8},
            {"id": "HIPAA-B01", "category": "Breach", "control": "Breach risk assessment procedure", "weight": 10},
            {"id": "HIPAA-B02", "category": "Breach", "control": "Individual notification within 60 days", "weight": 10},
        ],
    },
    "pci-dss": {
        "name": "PCI-DSS v4.0",
        "controls": [
            {"id": "PCI-01", "category": "Network", "control": "Network security controls installed", "weight": 8},
            {"id": "PCI-02", "category": "Configuration", "control": "Secure configurations applied", "weight": 8},
            {"id": "PCI-03", "category": "Data Protection", "control": "Stored cardholder data protected", "weight": 10},
            {"id": "PCI-04", "category": "Encryption", "control": "Encrypted transmission of cardholder data", "weight": 10},
            {"id": "PCI-05", "category": "Anti-Malware", "control": "Anti-malware solutions deployed", "weight": 8},
            {"id": "PCI-06", "category": "Development", "control": "Secure development practices", "weight": 8},
            {"id": "PCI-07", "category": "Access", "control": "Access restricted by business need", "weight": 8},
            {"id": "PCI-08", "category": "Authentication", "control": "Strong authentication for users", "weight": 10},
            {"id": "PCI-09", "category": "Physical", "control": "Physical access restricted", "weight": 6},
            {"id": "PCI-10", "category": "Logging", "control": "Logging and monitoring active", "weight": 10},
            {"id": "PCI-11", "category": "Testing", "control": "Regular security testing", "weight": 8},
            {"id": "PCI-12", "category": "Policy", "control": "Information security policy maintained", "weight": 6},
        ],
    },
}


def run_scan(framework):
    """Run compliance scan for the specified framework."""
    if framework not in FRAMEWORKS:
        return {"error": f"Unknown framework: {framework}. Available: {list(FRAMEWORKS.keys())}"}

    fw = FRAMEWORKS[framework]
    total_weight = sum(c["weight"] for c in fw["controls"])

    # Generate assessment template (all controls start as NOT_ASSESSED)
    controls = []
    categories = {}
    for c in fw["controls"]:
        controls.append({
            "id": c["id"],
            "category": c["category"],
            "control": c["control"],
            "weight": c["weight"],
            "status": "NOT_ASSESSED",
            "evidence": "",
            "notes": "",
        })
        if c["category"] not in categories:
            categories[c["category"]] = {"total": 0, "count": 0}
        categories[c["category"]]["total"] += c["weight"]
        categories[c["category"]]["count"] += 1

    report = {
        "metadata": {
            "framework": fw["name"],
            "scan_date": datetime.now().strftime("%Y-%m-%d"),
            "total_controls": len(fw["controls"]),
            "total_weight": total_weight,
        },
        "summary": {
            "status": "ASSESSMENT_TEMPLATE_GENERATED",
            "categories": {
                k: {"controls": v["count"], "max_score": v["total"]}
                for k, v in categories.items()
            },
            "maturity_level": "N/A - Pending assessment",
            "compliance_score": "N/A - Pending assessment",
        },
        "controls": controls,
        "instructions": [
            "Review each control and set status to: PASS, FAIL, PARTIAL, or N/A",
            "Document evidence for each assessed control",
            "Add notes explaining any gaps or compensating controls",
            "Calculate compliance score: sum of passing control weights / total weight",
        ],
    }

    return report


def main():
    parser = argparse.ArgumentParser(
        description="Run a compliance scan and generate a gap analysis template."
    )
    parser.add_argument(
        "--framework",
        choices=list(FRAMEWORKS.keys()),
        required=True,
        help="Compliance framework to scan against",
    )
    parser.add_argument(
        "--format",
        choices=["full", "summary"],
        default="full",
        help="Output format (default: full)",
    )
    parser.add_argument(
        "--output",
        help="Output file path (default: stdout)",
    )

    args = parser.parse_args()

    report = run_scan(args.framework)

    if args.format == "summary" and "error" not in report:
        report = {
            "metadata": report["metadata"],
            "summary": report["summary"],
            "instructions": report["instructions"],
        }

    output = json.dumps(report, indent=2)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Compliance scan report written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
