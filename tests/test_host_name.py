import unittest
from cssalib.system_funcs import host_name


class TestHostName(unittest.TestCase):

    def test_returns_string(self):
        result = host_name()
        self.assertIsInstance(result, str)

    def test_not_empty(self):
        result = host_name()
        self.assertTrue(len(result) > 0)

    def test_valid_hostname(self):
        result = host_name()
        # Check that hostname only contains valid characters
        self.assertRegex(result, r"^[a-zA-Z0-9-]+$")


if __name__ == "__main__":
    unittest.main()
