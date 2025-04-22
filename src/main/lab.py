def is_palindrome(s):
    """
    Check if a string is a palindrome and return True or False accordingly.
    
    :param s: The string to check.
    :return: True if the string is a palindrome, False otherwise.
    """
    # Ensure input is a string, and handle None or invalid input
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    
    # Convert the string to lowercase and remove non-alphanumeric characters
    s = ''.join(char.lower() for char in s if char.isalnum())
    
    # Compare the string with its reverse
    return s == s[::-1]


if __name__ == "__main__":
    # Example test case
    test_string = "A man, a plan, a canal, Panama"
    print(f"Is the string a palindrome? {is_palindrome(test_string)}")
