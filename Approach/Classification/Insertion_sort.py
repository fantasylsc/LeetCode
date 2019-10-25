'''

Insertion Sort

Worst case performance: O(n^2)
Best case performance: Ω(n)
Average performance: Θ(n^2)
Worst case space complexity: O(1)

'''

import unittest
from typing import List

class Solution:
    def insertionSort(self, nums: List[int]):
    	n = len(nums)

    	for i in range(1， n):
    		insert_val = nums[i]
    		j = i - 1
    		while j >= 0 and insert_val < nums[j]:
    			nums[j + 1] = nums[j]
    			j -= 1
    		nums[j + 1] = insert_val



class Test(unittest.TestCase):
	def test(self):
		nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
		s = Solution()
		s.insertionSort(nums)
		expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		self.assertEqual(nums, expected)

	def test_scond(self):
		nums = [1, 0, 1, 0, 1]
		s = Solution()
		s.insertionSort(nums)
		expected = [0, 0, 1, 1, 1]
		self.assertEqual(nums, expected)

unittest.main(verbosity = 2)

