
def validate_nsg_rule(rule):
    """Flag potentially risky inbound NSG rules in sample configuration."""
    warnings = []

    if rule.get("direction", "").lower() != "inbound":
        return warnings

    source = str(rule.get("source", "")).strip().lower()
    access = str(rule.get("access", "")).strip().lower()
    port = str(rule.get("destination_port", "")).strip()

    if access != "allow":
        return warnings

    public_sources = {"*", "internet", "any", "0.0.0.0/0", "::/0"}

    if source in public_sources:
        if port == "*":
            warnings.append("Risk: all ports allowed from a public source")
        elif port in {"22", "3389"}:
            warnings.append(
                f"Risk: management port {port} allowed from a public source"
            )

    return warnings
