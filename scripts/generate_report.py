
import json
from datetime import datetime, timezone
from pathlib import Path

from validate_network import validate_network
from validate_nsg import validate_nsg_rule


BASE_DIR = Path(__file__).resolve().parent.parent


def generate_report():
    vnet = "10.10.0.0/16"

    subnets = [
        "10.10.1.0/24",
        "10.10.2.0/24",
    ]

    nsg_rules = [
        {
            "name": "Allow-SSH-Public",
            "direction": "Inbound",
            "source": "0.0.0.0/0",
            "access": "Allow",
            "destination_port": "22",
        },
        {
            "name": "Allow-HTTPS-Private",
            "direction": "Inbound",
            "source": "10.10.0.0/16",
            "access": "Allow",
            "destination_port": "443",
        },
    ]

    findings = []

    for error in validate_network(vnet, subnets):
        findings.append({
            "category": "Networking",
            "severity": "High",
            "message": error,
        })

    for rule in nsg_rules:
        for warning in validate_nsg_rule(rule):
            findings.append({
                "category": "NSG Security",
                "severity": "High",
                "rule": rule["name"],
                "message": warning,
            })

    report = {
        "project": "AzureOps",
        "environment": "Local simulation",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_findings": len(findings),
        "findings": findings,
    }

    output_file = BASE_DIR / "data" / "security_report.json"
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with output_file.open("w", encoding="utf-8") as file:
        json.dump(report, file, indent=2)

    print("AzureOps Security Report Generated")
    print(f"Total findings: {len(findings)}")
    print(f"Saved to: {output_file}")


if __name__ == "__main__":
    generate_report()
