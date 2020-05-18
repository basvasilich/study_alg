import unittest

from toposort import toposort


class TestReachability(unittest.TestCase):
    def test_1(self):
        self.assertEqual(toposort([[1], [], [0], [0]]), [3, 2, 0, 1])

    def test_2(self):
        self.assertEqual(toposort([[], [], [0], []]), [1, 2, 0, 3])

    def test_2(self):
        self.assertEqual(toposort([[], [0], [1, 0], [2, 0], [2, 1]]), [4, 3, 2, 1, 0])

    if __name__ == '__main__':
        unittest.main()
