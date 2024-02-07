"""
This script is a Python program that checks if a given password has been breached
using the Pwned Passwords API. The user is prompted to enter a password, which is
then hashed using the SHA-1 algorithm.

The hashed password is split into two parts: a prefix (the first 5 characters) and
a suffix (the remaining characters). A GET request is sent to the Pwned Passwords
API with the prefix, and the response is checked for the suffix.

If the suffix is found in the response, the password has been breached and the
number of times it has been breached is returned. If the suffix is not found, the
password has not been breached. The result is then printed to the console.
"""

import requests
import hashlib
import getpass


def check_password_breach(password) -> int:
    """
    Check if the password has been breached using the Pwned Passwords API.
    :param password:
    :return: int: The number of times the password has been breached.
    """
    # Hash the password using SHA-1 algorithm
    sha1_password = hashlib.sha1(password.encode()).hexdigest().upper()

    # Split the first 5 characters and the remaining characters of the hashed password
    prefix, suffix = sha1_password[:5], sha1_password[5:]

    # Send a GET request to the Pwned Passwords API and search for the suffix
    response = requests.get(
        f"https://api.pwnedpasswords.com/range/{prefix}", {"Add-Padding": "true"}
    )

    # Check if the password is found in the response
    for line in response.text.splitlines():
        hash_suffix, count = line.split(":")
        if hash_suffix == suffix:
            return int(count)

    # Password not found
    return 0


def main(password: str = None):
    """
    Main function to check if a password has been breached.
    :return: str: The result of the password breach check.
    """
    # Prompt the user for a password
    password = getpass.getpass("Enter a password to check: ")

    # Check if the password has been breached
    breach_count = check_password_breach(password)

    if breach_count > 0:
        print(f"The password has been breached in {breach_count} datasets.")
    else:
        print("The password has not been breached.")


if __name__ == "__main__":
    main()
