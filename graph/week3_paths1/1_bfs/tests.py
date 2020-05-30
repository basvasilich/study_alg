import unittest

from bfs import distance


class TestBFS(unittest.TestCase):
    def test_1(self):
        self.assertEqual(distance([[1, 3], [0, 2], [0, 1], [0]], 2, 3), 2)

    def test_2(self):
        self.assertEqual(distance([[2, 3], [4], [0, 3], [0, 2], [1]], 2, 4), -1)

    if __name__ == '__main__':
        unittest.main()
