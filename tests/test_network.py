
import unittest

from scripts.validate_network import validate_network


class TestNetworkValidation(unittest.TestCase):

    def test_valid_subnets_pass(self):
        errors = validate_network(
            "10.10.0.0/16",
            ["10.10.1.0/24", "10.10.2.0/24"],
        )
        self.assertEqual(errors, [])

    def test_overlapping_subnets_fail(self):
        errors = validate_network(
            "10.10.0.0/16",
            ["10.10.1.0/24", "10.10.1.128/25"],
        )
        self.assertTrue(any("Overlapping subnets" in e for e in errors))

    def test_subnet_outside_vnet_fails(self):
        errors = validate_network(
            "10.10.0.0/16",
            ["10.20.1.0/24"],
        )
        self.assertTrue(any("outside VNet" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
