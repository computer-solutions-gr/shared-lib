from unittest import TestCase

from cssalib.probabilities import convert_dec_to_prob, exact_binomial_probability, cumulative_binomial_probabilities


class TestBasic(TestCase):
    def test_dec_to_prob(self):
        self.assertEqual(convert_dec_to_prob(0.2), 5.0)

    def test_exact_binomial(self):
        self.assertAlmostEqual(
            exact_binomial_probability(10, 1, 0.33), 0.08978, 5)

    def test_cumulative_binomial(self):
        self.assertAlmostEqual(
            cumulative_binomial_probabilities(10, 1, 0.1)[0], 0.3486784, 7)