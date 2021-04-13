import unittest

from solution import Solution


class TestSolution(unittest.TestCase):

    def test_basic(self):
        solution: Solution = Solution(1)
        solution.solve()
        self.assertEqual(solution.n, 2)


if __name__ == '__main__':
    unittest.main()
