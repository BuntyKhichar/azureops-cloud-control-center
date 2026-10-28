
import ipaddress


def validate_network(network_cidr, subnet_cidrs):
    """Validate that subnets are valid and contained in the VNet."""
    try:
        vnet = ipaddress.ip_network(network_cidr, strict=True)
    except ValueError as error:
        return [f"Invalid VNet CIDR: {error}"]

    errors = []
    subnets = []

    for cidr in subnet_cidrs:
        try:
            subnet = ipaddress.ip_network(cidr, strict=True)
        except ValueError as error:
            errors.append(f"Invalid subnet CIDR '{cidr}': {error}")
            continue

        if subnet.version != vnet.version or not subnet.subnet_of(vnet):
            errors.append(f"Subnet {subnet} is outside VNet {vnet}")
        else:
            subnets.append(subnet)

    for index, subnet in enumerate(subnets):
        for other in subnets[index + 1:]:
            if subnet.overlaps(other):
                errors.append(f"Overlapping subnets: {subnet} and {other}")

    return errors


if __name__ == "__main__":
    vnet_cidr = "10.10.0.0/16"
    subnet_cidrs = [
        "10.10.1.0/24",
        "10.10.1.128/25",
    ]

    problems = validate_network(vnet_cidr, subnet_cidrs)

    if problems:
        print("VALIDATION FAILED")
        for problem in problems:
            print(f"- {problem}")
    else:
        print("VALIDATION PASSED")
        print(f"VNet: {vnet_cidr}")
        print(f"Subnets: {len(subnet_cidrs)}")

