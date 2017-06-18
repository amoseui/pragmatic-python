# -*- coding: utf-8 -*-

import unittest

from solution import ListNode, Solution


class SolutionTest(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(1, Solution.sub(3, 2))
        self.assertEqual(-1, Solution.sub(2, 3))

    def test_twoSum(self):
        self.assertEqual([0, 1], Solution.twoSum([2, 7, 11, 15], 9))
        self.assertEqual([1, 2], Solution.twoSum([3, 2, 4], 6))
        self.assertEqual([0, 1], Solution.twoSum([3, 3], 6))
    
    def test_reverse(self):
        self.assertEqual(123, Solution.reverse(321))
        self.assertEqual(-123, Solution.reverse(-321))
        self.assertEqual(0, Solution.reverse(0))
        self.assertEqual(0, Solution.reverse(1534236469))

    def test_addTwoNumbers(self):
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)
        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)
        l3 = Solution.addTwoNumbers(l1, l2)
        self.assertEqual(7, l3.val)
        self.assertEqual(0, l3.next.val)
        self.assertEqual(8, l3.next.next.val)

        l1 = ListNode(0)
        l2 = ListNode(0)
        l3 = Solution.addTwoNumbers(l1, l2)
        self.assertEqual(0, l3.val)

        l1 = ListNode(1)
        l1.next = ListNode(8)
        l2 = ListNode(0)
        l3 = Solution.addTwoNumbers(l1, l2)
        self.assertEqual(1, l3.val)
        self.assertEqual(8, l3.next.val)

 
if __name__ == '__main__':
    unittest.main()
