import math
from typing import Tuple


def convert_dec_to_prob(dec: float) -> float:
    """Converts a decimal probability to a probability value between 0 and 1.

    Args:
        dec (float): The decimal probability value to convert.

    Returns:
        float: The probability value between 0 and 1.
    """
    return round(1 / dec, 4)


def convert_prob_to_dec(prob: float) -> float:
    """Converts a probability value between 0 and 1 to a decimal probability.

    Args:
        prob (float): The probability value between 0 and 1 to convert.

    Returns:
        float: The decimal probability value.
    """
    return round(1 / prob, 4)


def convert_frac_to_prob(nom: int, denom: int) -> float:
    """Converts a fraction to a probability value between 0 and 1.

    Args:
        nom (int): The numerator of the fraction.
        denom (int): The denominator of the fraction.

    Returns:
        float: The probability value between 0 and 1.
    """
    return round(1 - (nom / (nom + denom)), 4)


def convert_frac_to_dec(nom: int, denom: int) -> float:
    """Converts a fraction to a decimal probability value.

    Args:
        nom (int): The numerator of the fraction.
        denom (int): The denominator of the fraction.

    Returns:
        float: The decimal probability value.
    """
    return round(1 / (1 - (nom / (nom + denom))), 4)


def exact_binomial_probability(
    number_of_trials: int, number_of_successes: int, success_probability: float
) -> float:
    """
    Calculates the exact binomial probability for the given number of trials,
    number of successes, and success probability.

    Args:
        number_of_trials (int): The number of trials.
        number_of_successes (int): The number of successes.
        success_probability (float): The probability of success on each trial.

    Returns:
        float: The exact binomial probability.
    """
    n_choose_k = math.factorial(number_of_trials) / (
        math.factorial(number_of_successes)
        * math.factorial(number_of_trials - number_of_successes)
    )
    return (
        n_choose_k
        * (success_probability**number_of_successes)
        * ((1 - success_probability) ** (number_of_trials - number_of_successes))
    )


def cumulative_binomial_probabilities(
    number_of_trials: int, number_of_successes: int, success_probability: float
) -> Tuple[float, float, float, float]:
    """
    Calculates the cumulative binomial probability distribution for the given
    number of trials, number of successes, and success probability.

    Returns the probabilities for X < x, X <= x, X > x, and X >= x, where x is
    the provided number of successes.
    """
    X_lt_x = 0
    X_lt_eq_x = 0
    X_gt_x = 0
    X_gt_eq_x = 0
    for i in range(number_of_trials + 1):
        exact = exact_binomial_probability(number_of_trials, i, success_probability)
        if i < number_of_successes:
            X_lt_x += exact
            X_lt_eq_x += exact
        elif i == number_of_successes:
            X_lt_eq_x += exact
            X_gt_eq_x += exact
        elif i > number_of_successes:
            X_gt_x += exact
            X_gt_eq_x += exact

    return X_lt_x, X_lt_eq_x, X_gt_x, X_gt_eq_x


if __name__ == "__main__":
    print(exact_binomial_probability(10, 1, 0.33))
    print(cumulative_binomial_probabilities(10, 1, 0.1))
