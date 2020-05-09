import unittest
from random import randrange

from reachability import reach


class TestReachability(unittest.TestCase):
    def test_1(self):
        self.assertEqual(reach({1: [2, 4], 2: [1, 3], 3: [2, 4], 4: [1, 3]}, 1, 4), 1)

    def test_2(self):
        self.assertEqual(reach({1: [2], 2: [1, 3], 3: [2], 4: []}, 1, 4), 0)

    def test_3(self):
        self.assertEqual(reach({1: [], 4: []}, 1, 4), 0)


if __name__ == '__main__':
    unittest.main()
