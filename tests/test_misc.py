import unittest
from cssalib.misc import leap_years, most_common_element


class TestLeapYears(unittest.TestCase):

    def test_normal_range(self):
        result = leap_years(2000, 2010)
        expected = [2000, 2004, 2008]
        self.assertEqual(result, expected)

    def test_start_year_leap_year(self):
        result = leap_years(2004, 2010)
        expected = [2004, 2008]
        self.assertEqual(result, expected)

    def test_end_year_leap_year(self):
        result = leap_years(2000, 2008)
        expected = [2000, 2004]
        self.assertEqual(result, expected)

    def test_no_leap_years(self):
        result = leap_years(2001, 2002)
        expected = []
        self.assertEqual(result, expected)


class TestMostCommonElement(unittest.TestCase):

    def test_empty_list(self):
        result = most_common_element([])
        expected = None
        self.assertEqual(result, expected)

    def test_single_element_list(self):
        result = most_common_element([1])
        expected = 1
        self.assertEqual(result, expected)

    def test_multiple_max_elements(self):
        result = most_common_element([1, 2, 2, 3, 3])
        expected = 2
        self.assertEqual(result, expected)

    def test_string_elements(self):
        result = most_common_element(["a", "b", "b", "c", "c", "c"])
        expected = "c"
        self.assertEqual(result, expected)


from cssalib.misc import extract_domain_from_email


class TestExtractDomain(unittest.TestCase):

    def test_basic(self):
        email = "john@example.com"
        expected = "example.com"
        actual = extract_domain_from_email(email)
        self.assertEqual(actual, expected)

    def test_subdomain(self):
        email = "jane@mail.example.com"
        expected = "example.com"
        actual = extract_domain_from_email(email)
        self.assertEqual(actual, expected)

    def test_invalid_email(self):
        email = "notanemail"
        with self.assertRaises(Exception):
            extract_domain_from_email(email)

    def test_empty_string(self):
        email = ""
        with self.assertRaises(Exception):
            extract_domain_from_email(email)
