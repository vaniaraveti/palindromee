import unittest
from lab import is_palindrome  # Adjust the import based on your file structure

class TestPalindrome(unittest.TestCase):

    def test_palindrome(self):
        # Test case where input is a known palindrome
        test_string = "A man, a plan, a canal, Panama"
        self.assertTrue(is_palindrome(test_string))  # Should return True
        
        # Test case where input is NOT a palindrome
        test_string = "Hello"
        self.assertFalse(is_palindrome(test_string))  # Should return False

if __name__ == "__main__":
    unittest.main()
