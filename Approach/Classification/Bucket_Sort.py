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

    
# Bucket sort for numbers
# having integer part
def bucketSort(arr, noOfBuckets):
    max_ele = max(arr)
    min_ele = min(arr)
 
    # range(for buckets)
    rnge = (max_ele - min_ele) / noOfBuckets
 
    temp = []
 
    # create empty buckets
    for i in range(noOfBuckets):
        temp.append([])
 
    # scatter the array elements
    # into the correct bucket
    for i in range(len(arr)):
        diff = (arr[i] - min_ele) / rnge -
              int((arr[i] - min_ele) / rnge)
 
        # append the boundary elements to the lower array
        if(diff == 0 and arr[i] != min_ele):
            temp[int((arr[i] - min_ele) / rnge) - 1].append(arr[i])
 
        else:
            temp[int((arr[i] - min_ele) / rnge)].append(arr[i])
 
    # Sort each bucket individually
    for i in range(len(temp)):
        if len(temp[i]) != 0:
            temp[i].sort()
 
    # Gather sorted elements
    # to the original array
    k = 0
    for lst in temp:
        if lst:
            for i in lst:
                arr[k] = i
                k = k+1

class Test(unittest.TestCase):
    def test(self):
        nums = x = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
        s = Solution()
        s.bucketSort(nums)
        expected = [0.1234, 0.3434, 0.565, 0.656, 0.665, 0.897]
        self.assertEqual(nums, expected)


unittest.main(verbosity = 2)

