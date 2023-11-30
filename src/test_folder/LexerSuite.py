import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_lowercase_identifier(self):
        """test_folder identifiers"""
        self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 101))
