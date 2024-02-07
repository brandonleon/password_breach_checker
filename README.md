"""
# Password Breach Checker

This is a Python program that checks if a given password has been breached using the Pwned Passwords API.

## Description

The user is prompted to enter a password, which is then hashed using the SHA-1 algorithm. The hashed password is split into two parts: a prefix (the first 5 characters) and a suffix (the remaining characters). A GET request is sent to the Pwned Passwords API with the prefix, and the response is checked for the suffix.

If the suffix is found in the response, the password has been breached and the number of times it has been breached is returned. If the suffix is not found, the password has not been breached. The result is then printed to the console.