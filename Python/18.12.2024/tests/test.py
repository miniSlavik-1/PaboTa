from summ_file import summ
import unittest


class Testmyfunc(unittest.TestCase):
    def test_my(self):
        self.assertEqual(summ(5, 7), 12)
        self.assertEqual(summ(5, 6), 11)
        self.assertEqual(summ(5, 8), 13)
        self.assertEqual(summ(5, 9), 14)


if __name__ == "__main__":
    unittest.main()