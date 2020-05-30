import unittest

from bipartite import bipartite


class TestBFS(unittest.TestCase):
    def test_1(self):
        self.assertEqual(bipartite([[1, 3], [0, 2], [0, 1], [0]]), 0)

    def test_2(self):
        self.assertEqual(bipartite([[3], [3, 4], [3], [0, 1], [1]]), 1)

    if __name__ == '__main__':
        unittest.main()
