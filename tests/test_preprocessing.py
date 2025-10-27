import unittest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from data.preprocessing import clean_text

class TestPreprocessing(unittest.TestCase):

    def test_lowercase(self):
        """Test that the text is converted to lowercase."""
        text = "This is a Test Sentence."
        expected_output = "this is a test sentence"
        self.assertEqual(clean_text(text), expected_output)

    def test_remove_punctuation(self):
        """Test that punctuation is removed."""
        text = "Hello, world! This is a test."
        expected_output = "hello world this is a test"
        self.assertEqual(clean_text(text), expected_output)

    def test_lowercase_and_remove_punctuation(self):
        """Test both lowercase and punctuation removal."""
        text = "Another Test, with Punctuation!"
        expected_output = "another test with punctuation"
        self.assertEqual(clean_text(text), expected_output)

if __name__ == '__main__':
    unittest.main()
