import numpy as np
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt


def mean_adjusted_exponent_error(
    y_true, y_pred, center=125, critical_range=55, slope=100, verbose=False
):
    """Calculates the mean adjusted exponent error between two arrays.

    This error metric penalizes large errors more than small errors by raising
    the absolute difference to an exponent. The exponent is calculated for each
    data point based on how far the prediction is from the true value and a
    configurable center, critical range, and slope.

    Args:
        y_true: Array of true target values.
        y_pred: Array of predicted target values.
        center: Center point to calculate exponent. Default 125.
        critical_range: Range to transition exponent. Default 55.
        slope: Slope of exponent transition. Default 100.
        verbose: Print exponent for each data point if True. Default False.

    Returns:
        The mean adjusted exponent error between y_true and y_pred.
    """

    def exponent(
        y_hat: float, y_i: float, a=center, b=critical_range, c=slope
    ) -> float:
        return 2 - np.tanh(((y_i - a) / b)) * ((y_hat - y_i) / c)

    sum_ = 0
    for i in range(len(y_true)):
        exp = exponent(y_pred[i], y_true[i])
        if verbose:
            print(exp)
        sum_ += abs((y_pred[i] - y_true[i])) ** exp
    return sum_ / len(y_true)


def graph_vs_mse(value, value_range, action=None, save_folder="."):
    """Plots mean adjusted exponent error and mean squared error vs a range of
    predictions around a reference value.

    Args:
        value: The reference value to center the predictions around.
        value_range: The range above and below the reference value to plot.
        action: 'save' to save the plot instead of displaying.
        save_folder: Folder to save plot if action='save'.

    Returns:
        The matplotlib plot object if action is not 'save'.
    """
    prediction = np.arange(value - value_range, value + value_range)
    errors = []
    mse = []
    for pred in prediction:
        errors.append(mean_adjusted_exponent_error([value], [pred]))
        mse.append(mean_squared_error([value], [pred]))
    plt.plot(prediction, errors, label="madex")
    plt.plot(prediction, mse, label="mse", ls="dotted")
    plt.axvline(value, label="Reference Value", color="k", ls="--")
    plt.xlabel("Predicted Value")
    plt.ylabel("Error")
    plt.title(f"{value} +- {value_range}")
    plt.legend()
    if action == "save":
        plt.savefig(f"{save_folder}/compare_vs_mse({value}+-{value_range}).png")
        plt.clf()
    else:
        return plt
