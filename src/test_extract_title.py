import unittest
from functions.extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        res = extract_title("# Hello")
        self.assertEqual("Hello", res)
