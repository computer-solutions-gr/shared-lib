import requests

leap_years = [
    year
    for year in range(2000, 2051)
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
]

public_ip = requests.get("https://api64.ipify.org?format=json").json()["ip"]


def most_common_element(_list: list):
    return max(set(_list), key=_list.count)


def extract_domain_from_email(email: str) -> str:
    import re

    return re.search(r"@(\w+\.\w+)", email).group(1)


def test():
    print("Test")
    return "Test"
