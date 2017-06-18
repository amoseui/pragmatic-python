# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode:
	
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	
	def sub(a, b):
		return a - b

	def twoSum(nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		cache = {}
		for idx, num in enumerate(nums):
			if target - num in cache.keys():
				return [cache[target - num], idx]
			cache[num] = idx

	def reverse(x):
		"""
		:type x: int
		:rtype: int
		"""
		answer = 0
		pos = 1 if x > 0 else -1
		num = pos * x
		while num > 0:	
			answer = answer * 10 + num % 10
			num = int(num / 10)
		answer = answer if answer < 2**31 else 0
		return pos * answer

	def addTwoNumbers(l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		n1 = l1
		first = 0
		i = 0
		while n1:
			first = n1.val * (10**i) + first
			n1 = n1.next
			i += 1
		n2 = l2
		second = 0
		i = 0
		while n2:
			second = n2.val * (10**i) + second
			n2 = n2.next
			i += 1
		third = first + second

		num = third
		l3 = None if num > 0 else ListNode(0)
		while num > 0:
			if l3:
				n3.next = ListNode(num % 10)
				n3 = n3.next
			else:
				l3 = ListNode(num % 10)
				n3 = l3
			num = int(num / 10)
		return l3

