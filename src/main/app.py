import unittest
from lab import is_palindrome  # Ensure the import path is correct based on your project structure

class TestPalindrome(unittest.TestCase):

    def test_palindrome(self):
        
        test_string = "A man, a plan, a canal, Panama"
        self.assertTrue(is_palindrome(test_string))

    def test_non_palindrome(self):
        
        test_string = "Hello"
        self.assertFalse(is_palindrome(test_string))

    def test_empty_string(self):
        
        test_string = ""
        self.assertTrue(is_palindrome(test_string))

if __name__ == "__main__":
    unittest.main()
