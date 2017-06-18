# -*- coding: utf-8 -*-

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
