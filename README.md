# AzureOps — Cloud Infrastructure & Security Control Center

A local cloud infrastructure validation and security monitoring project built to practice Azure administration, network configuration, and security best practices.

## Overview

AzureOps validates network configurations, identifies potentially risky Network Security Group (NSG) rules, generates a security report, and displays findings through a web dashboard.

The project also includes Azure Bicep infrastructure code that can be compiled locally into an ARM JSON template.

**Environment:** Local simulation. No Azure resources are deployed by this project.

## Features

- **Network validation:** Checks subnet CIDR configurations and identifies overlapping or out-of-range subnets.
- **NSG security checks:** Detects potentially risky inbound rules, including public SSH access.
- **Automated reporting:** Generates a JSON security report.
- **Security dashboard:** Displays finding counts and security issues in a browser.
- **Infrastructure as Code:** Defines an Azure Virtual Network and subnets using Bicep.
- **Local template compilation:** Compiles Bicep into an ARM JSON template without deploying resources.
- **Automated tests:** Includes tests for network validation and NSG security checks.

## Technology Stack

- Python
- Azure Bicep
- ARM JSON templates
- HTML, CSS and JavaScript
- Python `unittest`

## Project Structure

```text
azureops-cloud-control-center/
├── data/
│   └── security_report.json
├── docs/
├── infra/
│   ├── main.bicep
│   └── network.bicep
├── runbooks/
├── scripts/
│   ├── dashboard.html
│   ├── generate_report.py
│   ├── validate_network.py
│   └── validate_nsg.py
├── tests/
│   ├── test_network.py
│   └── test_nsg.py
└── README.md
```

## Run Locally

### 1. Generate the security report

From the project root, run:

```bash
python3 scripts/generate_report.py
```

### 2. Start the local dashboard

```bash
python3 -m http.server 8000
```

Open the following address in your browser:

```text
http://localhost:8000/scripts/dashboard.html
```

Keep the terminal running while viewing the dashboard.

### 3. Compile the Bicep template

```bash
bicep build infra/network.bicep --outfile /tmp/azureops-network.json
```

This command compiles the infrastructure template locally. It does not deploy resources to Azure.

### 4. Run automated tests

```bash
python3 -m unittest discover -s tests -v
```

## Learning Objectives

- Understand Azure virtual networks and subnet addressing.
- Practice network configuration validation.
- Identify common NSG inbound security risks.
- Work with infrastructure as code using Bicep.
- Generate security reports and present findings in a dashboard.
- Test Python validation logic.

## Project Status

**Current stage:** Local prototype and simulation.

Azure deployment, live Azure resource inventory, and integration with Azure security services are not implemented.

## Disclaimer

This project is intended for learning and portfolio demonstration. Findings are generated from local sample configuration and should not be interpreted as a live assessment of an Azure subscription.