'''

Heap Sort

Worst case performance: O(nlogn)
Best case performance: Ω(nlogn)
Average performance: Θ(nlogn)
Worst case space complexity: O(1)

Heap

       4
     /   \
    10    3
   /  \
  5    1

Note:
Root is at index 0 in array.
Left child of i-th node is at (2*i + 1)th index.
Right child of i-th node is at (2*i + 2)th index.
Parent of i-th node is at (i-1)/2 index.

'''

import unittest
from typing import List

class Solution:
	def heapSort(self, nums: List[int]):
		n = len(nums)
		start_index = (n // 2) - 1 # (i-1)/2 = ((n - 1) - 1) // 2 = n // 2 - 1
	  
		# Build a maxheap in reverse level order follow top-down approach. 
		for i in range(start_index, -1, -1): 
			self.heapify(nums, n, i) 
	  
		# One by one extract elements 
		for i in range(n-1, 0, -1): 
			nums[i], nums[0] = nums[0], nums[i] # swap 
			self.heapify(nums, i, 0) 
	
	# Heapify subtree rooted at index i
	def heapify(self, nums, n, i): 
		largest = i # Initialize largest as root 
		l = 2 * i + 1	# left = 2*i + 1 
		r = 2 * i + 2	# right = 2*i + 2 
	  
		# See if left child of root exists and is 
		# greater than root 
		if l < n and nums[i] < nums[l]: 
			largest = l 
	  
		# See if right child of root exists and is 
		# greater than root 
		if r < n and nums[largest] < nums[r]: 
			largest = r 
	  
		# Change root, if needed 
		if largest != i: 
			nums[i],nums[largest] = nums[largest],nums[i] # swap 
	  		# Heapify the subtree affected by the swap. 
			self.heapify(nums, n, largest) 
  



class Test(unittest.TestCase):
	def test(self):
		nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
		s = Solution()
		s.heapSort(nums)
		expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		self.assertEqual(nums, expected)

	def test_scond(self):
		nums = [1, 0, 1, 0, 1]
		s = Solution()
		s.heapSort(nums)
		expected = [0, 0, 1, 1, 1]
		self.assertEqual(nums, expected)

unittest.main(verbosity = 2)

