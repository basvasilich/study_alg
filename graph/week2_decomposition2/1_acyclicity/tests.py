import unittest

from acyclicity import acyclic


class TestReachability(unittest.TestCase):
    def test_1(self):
        self.assertEqual(acyclic([[2], [2], [0], [0]]), 1)

    def test_2(self):
        self.assertEqual(acyclic([[1, 2, 3], [2, 4], [3, 4], [], []]), 0)

    if __name__ == '__main__':
        unittest.main()
