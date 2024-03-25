"""
Misc Module
"""

import requests


def leap_years(start_year: int, end_year: int) -> list:
    """
    The function `leap_years` returns a list of leap years within a specified range of years.

    Args:
      start_year (int): The `start_year` parameter is the beginning year from which you want to start
        checking for leap years.
      end_year (int): The `end_year` parameter represents the ending year for the range of years for
        which you want to find leap years. This function will return a list of leap years between
        `start_year` (inclusive) and `end_year` (exclusive).

    Returns:
        list: The function `leap_years` returns a list of leap years between the `start_year` (inclusive) and
        `end_year` (exclusive) provided as input arguments. The list comprehension checks each year in the
        range for leap year conditions (divisible by 4 but not by 100 unless also divisible by 400) and
        includes the year in the list if it meets these conditions.
    """
    return [
        year
        for year in range(start_year, end_year)
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    ]


def public_ip() -> str:
    """
    This Python function retrieves and returns the public IP address of the current machine using an
    external API.

    Returns:
        The `public_ip` function returns the public IP address of the current machine by making a request
        to the "https://api64.ipify.org?format=json" API and extracting the IP address from the JSON
        response.
    """
    return requests.get("https://api64.ipify.org?format=json").json()["ip"]


def most_common_element(_list: list):
    """
    Returns the most common element in the given list.

    Args:
        _list (list): A list of elements.

    Returns:
        The most common element in the list.

    Examples:
        >>> most_common_element([1, 2, 2, 3, 3, 3, 4])
        3
    """
    if _list:
        return max(set(_list), key=_list.count)
    else:
        return None


def extract_domain_from_email(email: str) -> str:
    """
    Extracts the domain name from the given email address.

    The email address is split on the '@' symbol, and the part after the '@'
    is taken as the domain. This is then split on '.' and the last 2 sections
    are joined back together with '.' to get the domain name.

    Args:
        email (str): The email address to extract the domain from.

    Returns:
        str: The domain name extracted from the email address.

    Raises:
        AttributeError: If no '@' symbol is found in the email.
    """

    return ".".join(email.split("@")[1].split(".")[-2:])


def test():
    """
    Prints 'Test' and returns 'Test'.

    Returns:
        str: 'Test'
    """
    print("Test")
    return "Test"
