'''

Bucket Sort

Worst case performance: O(n^2)
Best case performance: Ω(n + k)
Average performance: Θ(n + k)
Worst case space complexity: O(n)

'''

import unittest
from typing import List

class Solution:
    def bucketSort(self, nums: List[int]):
        arr = [] 
        slot_num = 10 # 10 means 10 slots, each 
                      # slot's size is 0.1 
        for i in range(slot_num): 
            arr.append([]) 
              
        # Put array elements in different buckets  
        for j in nums: 
            index_b = int(slot_num * j)  
            arr[index_b].append(j) 
          
        # Sort individual buckets  
        for i in range(slot_num): 
            arr[i] = self.insertionSort(arr[i]) 
              
        # concatenate the result 
        k = 0
        for i in range(slot_num): 
            for j in range(len(arr[i])): 
                nums[k] = arr[i][j] 
                k += 1
        return nums 


    def insertionSort(self, b): 
        for i in range(1, len(b)): 
            key = b[i] 
            j = i - 1
            while j >=0 and b[j] > key:  
                b[j + 1] = b[j] 
                j -= 1
            b[j + 1] = key      
        return b



class Test(unittest.TestCase):
    def test(self):
        nums = x = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
        s = Solution()
        s.bucketSort(nums)
        expected = [0.1234, 0.3434, 0.565, 0.656, 0.665, 0.897]
        self.assertEqual(nums, expected)


unittest.main(verbosity = 2)

