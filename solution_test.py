# -*- coding: utf-8 -*-

import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(1, Solution.sub(3, 2))
        self.assertEqual(-1, Solution.sub(2, 3))

    def test_sum(self):
        self.assertEqual([0, 1], Solution.twoSum([2, 7, 11, 15], 9))
        self.assertEqual([1, 2], Solution.twoSum([3, 2, 4], 6))


if __name__ == '__main__':
    unittest.main()
