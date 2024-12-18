import unittest
from t9 import t9

class Test_function(unittest.TestCase):
    def test_my(self):
        self.assertEqual(
            t9("привет,мои друзья .меня зовут Владимир ."),
            "Привет, мои друзья. Меня зовут Владимир."
        )
        self.assertEqual(
            t9("  привет,мои   друзья . меня зовут Владимир ."),
            "Привет, мои друзья. Меня зовут Владимир."
        )