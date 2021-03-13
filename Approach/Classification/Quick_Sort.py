'''

Quick Sort

Worst case performance: O(n^2)
Best case performance: Ω(nlogn)
Average performance: Θ(nlogn)
Worst case space complexity: O(nlogn)

Take last element in nums as pivot.

'''

import unittest
from typing import List

class Solution:
    def quickSort(self, nums: List[int], low: int, high: int):
        if low < high: 
            # pi is partitioning index 
            pi = self.partition(nums, low, high) 
  
            # Separately sort elements before 
            # partition and after partition 
            self.quickSort(nums, low, pi - 1) 
            self.quickSort(nums, pi + 1, high)

    def partition(self, nums, low, high): 
        i = (low - 1)         # i + 1 points to num larger than pivot 
        pivot = nums[high]     # pivot 
  
        for j in range(low , high): 
            # If current element is smaller than the pivot, i == j, no change sequence
            # If larger, i + 1 points to the larger item, next time change i + 1 and j
            if   nums[j] < pivot: # nums[j] is smaller
                i = i + 1 # i + 1 points to the larger item
                nums[i], nums[j] = nums[j], nums[i] # swap smaller num and larger num
  
        nums[i + 1], nums[high] = nums[high], nums[i + 1] 
        return (i + 1)  




class Test(unittest.TestCase):
    def test(self):
        nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        s = Solution()
        high = len(nums) - 1
        s.quickSort(nums, 0, high)
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(nums, expected)

    def test_scond(self):
        nums = [1, 0, 1, 0, 1]
        s = Solution()
        high = len(nums) - 1
        s.quickSort(nums, 0, high)
        expected = [0, 0, 1, 1, 1]
        self.assertEqual(nums, expected)

unittest.main(verbosity = 2)

