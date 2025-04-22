import unittest
from lab import is_palindrome  # Ensure the import path is correct based on your project structure

class TestPalindrome(unittest.TestCase):

    def test_palindrome(self):
        # Test with a known palindrome string
        test_string = "A man, a plan, a canal, Panama"
        self.assertTrue(is_palindrome(test_string))

    def test_non_palindrome(self):
        # Test with a string that is not a palindrome
        test_string = "Hello"
        self.assertFalse(is_palindrome(test_string))

    def test_empty_string(self):
        # Test with an empty string (should be a palindrome)
        test_string = ""
        self.assertTrue(is_palindrome(test_string))

if __name__ == "__main__":
    unittest.main()
