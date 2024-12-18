import unittest
from count_text import word, schifter


class Test_function(unittest.TestCase):
    def test_my(self):
        self.assertDictEqual(word("Hello"), {'H': 1, 'e': 1, 'l': 2, 'o': 1})
        self.assertDictEqual(word("AAAbbb"), {'A': 3, 'b': 3})

    def test_my_2(self):
        self.assertListEqual(schifter([1, 2, 3]), [3, 2, 1])