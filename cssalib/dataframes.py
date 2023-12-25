import pandas as pd
from loguru import logger


def save_df(dataframe, filename="test.pkl"):
    logger.info(f"Attempting to save file {filename}")
    dataframe.to_pickle(filename)


def read_df(filename="test.pkl"):
    logger.info(f"Attempting to read from pickle file {filename}")
    return pd.read_pickle(filename)


def slice_df(self, dataframe, index, number):
    """
    The function `slice_df` takes a dataframe, an index, and a number as input and returns a sliced
    portion of the dataframe starting from the given index and containing the specified number of
    rows.

    :param dataframe: The dataframe parameter is the pandas DataFrame that you want to slice
    :param index: The starting index of the slice. It specifies the position of the first element to
    include in the slice
    :param number: The number of rows to slice from the dataframe starting from the specified index
    :return: a slice of the dataframe starting from the specified index and containing the specified
    number of rows.
    """
    return dataframe[index : index + number]
