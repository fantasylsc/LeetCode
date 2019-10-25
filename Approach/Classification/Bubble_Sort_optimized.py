'''

Bubble Sort

Worst case performance: O(n^2)
Best case performance: Ω(n)
Average performance: Θ(n^2)
Worst case space complexity: O(1)

Optimized version, if no two elements were swapped, then break

'''

import unittest
from typing import List

class Solution:
    def bubbleSort_Opt(self, nums: List[int]):
    	n = len(nums)

    	for i in range(n):
    		swapped = False
    		for j in range(n - i - 1):
    			if nums[j] > nums[j + 1]:
    				nums[j], nums[j + 1] = nums[j + 1], nums[j]
    				swapped = True

    		if swapped == False:
    			break



class Test(unittest.TestCase):
	def test(self):
		nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
		s = Solution()
		s.bubbleSort_Opt(nums)
		expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		self.assertEqual(nums, expected)

	def test_second(self):
		nums = [1, 0, 1, 0, 1]
		s = Solution()
		s.bubbleSort_Opt(nums)
		expected = [0, 0, 1, 1, 1]
		self.assertEqual(nums, expected)

unittest.main(verbosity = 2)

