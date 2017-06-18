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
