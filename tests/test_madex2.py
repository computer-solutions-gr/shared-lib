import unittest
from projects.diabetes.madex import mean_adjusted_exponent_error


class TestMadex(unittest.TestCase):

    def test_perfect_match(self):
        y_true = [100, 200, 300]
        y_pred = [100, 200, 300]
        error = mean_adjusted_exponent_error(y_true, y_pred)
        self.assertEqual(error, 0)

    def test_large_error(self):
        y_true = [100]
        y_pred = [500]
        error = mean_adjusted_exponent_error(y_true, y_pred)
        expected = 400
        self.assertGreater(error, expected)

    def test_asymmetric(self):
        y_true = [100, 200]
        y_pred = [150, 250]
        error = mean_adjusted_exponent_error(y_true, y_pred)
        reverse_error = mean_adjusted_exponent_error(y_pred, y_true)
        self.assertNotEqual(error, reverse_error)


if __name__ == "__main__":
    unittest.main()
