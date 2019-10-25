'''

Selection Sort

Worst case performance: O(n^2)
Best case performance: Ω(n^2)
Average performance: Θ(n^2)
Worst case space complexity: O(1)

'''

import unittest
from typing import List

class Solution:
    def selectionSort(self, nums: List[int]):
    	n = len(nums)

    	for i in range(n):
    		min_idx = i
    		for j in range(i + 1, n):
    			if nums[j] < nums[min_idx]:
    				min_idx = j
    		nums[i], nums[min_idx] = nums[min_idx], nums[i]



class Test(unittest.TestCase):
	def test(self):
		nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
		s = Solution()
		s.selectionSort(nums)
		expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		self.assertEqual(nums, expected)

	def test_second(self):
		nums = [1, 0, 1, 0, 1]
		s = Solution()
		s.selectionSort(nums)
		expected = [0, 0, 1, 1, 1]
		self.assertEqual(nums, expected)

unittest.main(verbosity = 2)

