
import unittest

from scripts.validate_nsg import validate_nsg_rule


class TestNsgValidation(unittest.TestCase):

    def test_public_ssh_is_flagged(self):
        rule = {
            "direction": "Inbound",
            "source": "0.0.0.0/0",
            "access": "Allow",
            "destination_port": "22",
        }
        self.assertTrue(validate_nsg_rule(rule))

    def test_public_all_ports_is_flagged(self):
        rule = {
            "direction": "Inbound",
            "source": "*",
            "access": "Allow",
            "destination_port": "*",
        }
        self.assertTrue(validate_nsg_rule(rule))

    def test_private_https_rule_is_not_flagged(self):
        rule = {
            "direction": "Inbound",
            "source": "10.10.0.0/16",
            "access": "Allow",
            "destination_port": "443",
        }
        self.assertEqual(validate_nsg_rule(rule), [])


if __name__ == "__main__":
    unittest.main()
