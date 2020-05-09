import unittest
from random import randrange

from connected_components import number_of_components


class TestReachability(unittest.TestCase):
    def test_1(self):
        self.assertEqual(number_of_components({1: [2], 2: [1, 3], 3: [2]}), 1)

    def test_2(self):
        self.assertEqual(number_of_components({1: [2], 2: [1, 3], 3: [2], 4: [5], 5: [4]}), 2)

    def test_3(self):
        self.assertEqual(number_of_components({1: [2], 2: [1, 3], 3: [2], 4: []}), 2)

    def test_4(self):
        self.assertEqual(number_of_components({1: []}), 1)


    def test_5(self):
        self.assertEqual(number_of_components({1: [2], 3: [2], 4: [], 2: [1, 3]}), 2)


if __name__ == '__main__':
    unittest.main()
