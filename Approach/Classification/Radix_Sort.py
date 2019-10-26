'''

Radix Sort

Worst case performance: O(nk)
Best case performance: Ω(nk)
Average performance: Θ(nk)
Worst case space complexity: O(n + k)

'''

import unittest
from typing import List

class Solution:
	def radixSort(self, nums: List[int]):
		# Find the maximum number to know number of digits 
		max_num = max(nums) 
  
		# Do counting sort for every digit. Note that instead 
		# of passing digit number, exp is passed. exp is 10^i 
		# where i is current digit number 
		exp = 1
		while max_num/exp > 0: 
			self.countingSort(nums, exp) 
			exp *= 10

	def countingSort(self, nums, exp1): 
  
		n = len(nums) 
  
		# The output array elements that will have sorted nums 
		output = [0] * (n) 
  
		# initialize count array as 0 
		count = [0] * (10) 
  
		# Store count of occurrences in count[] 
		for i in range(0, n): 
			index = (nums[i] // exp1) 
			count[(index) % 10] += 1
  
		# Change count[i] so that count[i] now contains actual 
		#  position of this digit in output array 
		for i in range(1, 10): 
			count[i] += count[i - 1] 
  
		# Build the output array 
		i = n - 1
		while i >= 0: 
			index = (nums[i] // exp1) 
			output[ count[(index) % 10] - 1] = nums[i] 
			count[(index) % 10] -= 1
			i -= 1
  
		# Copying the output array to nums[], 
		# so that nums now contains sorted numbers 
		i = 0
		for i in range(0, len(nums)): 
			nums[i] = output[i] 





class Test(unittest.TestCase):
	def test(self):
		nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
		s = Solution()
		s.radixSort(nums)
		expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		self.assertEqual(nums, expected)

	def test_scond(self):
		nums = [1, 0, 1, 0, 1]
		s = Solution()
		s.radixSort(nums)
		expected = [0, 0, 1, 1, 1]
		self.assertEqual(nums, expected)

unittest.main(verbosity = 2)

