'''

Merge Sort

Worst case performance: O(nlogn)
Best case performance: Ω(nlogn)
Average performance: Θ(nlogn)
Worst case space complexity: O(n)

'''

import unittest
from typing import List

class Solution:
    def mergeSort(self, nums: List[int]):
        if len(nums) > 1:
            mid = len(nums) // 2
            L = nums[:mid]   
            R = nums[mid:] 
      
            self.mergeSort(L) 
            self.mergeSort(R) 
      
            i = j = k = 0
              
            while i < len(L) and j < len(R): 
                if L[i] < R[j]: 
                    nums[k] = L[i] 
                    i+=1
                else: 
                    nums[k] = R[j] 
                    j+=1
                k+=1
              
            while i < len(L): 
                nums[k] = L[i] 
                i+=1
                k+=1
              
            while j < len(R): 
                nums[k] = R[j] 
                j+=1
                k+=1




class Test(unittest.TestCase):
    def test(self):
        nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        s = Solution()
        s.mergeSort(nums)
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(nums, expected)

    def test_scond(self):
        nums = [1, 0, 1, 0, 1]
        s = Solution()
        s.mergeSort(nums)
        expected = [0, 0, 1, 1, 1]
        self.assertEqual(nums, expected)

unittest.main(verbosity = 2)

