import requests

"""Generates a list of leap years between 2000 and 2050.

Uses a list comprehension to check each year in the range 
2000-2050, and include it if it meets the leap year criteria.
"""
leap_years = [
    year
    for year in range(2000, 2051)
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
]

"""Makes a GET request to the ipify API to retrieve the public IP address.

The API endpoint is https://api64.ipify.org?format=json, and it returns the IP 
address in JSON format. The code extracts just the "ip" field from the JSON 
response and stores it in the public_ip variable.
"""
public_ip = requests.get("https://api64.ipify.org?format=json").json()["ip"]


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

    return max(set(_list), key=_list.count)


def extract_domain_from_email(email: str) -> str:
    """
    Extracts the domain from the given email address.

    Args:
        email (str): The email address from which to extract the domain.

    Returns:
        str: The domain extracted from the email address.

    Raises:
        AttributeError: If the domain pattern is not found in the email address.
    """

    import re

    return re.search(r"@(\w+\.\w+)", email).group(1)


def test():
    """
    Prints 'Test' and returns 'Test'.

    Returns:
        str: 'Test'
    """
    print("Test")
    return "Test"
