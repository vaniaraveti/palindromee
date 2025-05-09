def is_palindrome(s):
    """
    Check if a string is a palindrome and return True or False accordingly.
    
    :param s: The string to check.
    :return: True if the string is a palindrome, False otherwise.
    """
    if not isinstance(s, str):
        raise ValueError("Input must be a string")

    s = ''.join(char.lower() for char in s if char.isalnum())

    return s == s[::-1]


