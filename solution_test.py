# -*- coding: utf-8 -*-

import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(1, Solution.sub(3, 2))
        self.assertEqual(-1, Solution.sub(2, 3))


if __name__ == '__main__':
    unittest.main()
