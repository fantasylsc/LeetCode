'''

Quick Sort

Worst case performance: O(n^2)
Best case performance: Ω(nlogn)
Average performance: Θ(nlogn)
Worst case space complexity: O(nlogn)

Take last element in nums as pivot.

'''

'''
idea:
Put smaller nums left and larger nums right accordint to pivot
Loop through nums, if current num is samller than pivot:
swap current num with larger num
If current num is larger than pivot:
Do nothing, continue.
i + 1 points to larger num, so we do i + 1 before swap
j points to the num we are looping through
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
        
    def better_partition(self, nums, low, high): 
        #partition
        r = randint(low, high)
        nums[r], nums[high] = nums[high], nums[r]

        p = high  # set pivot to rightmost element
        i, j = low, high - 1

        while i <= j:
            if nums[i] < nums[p]: 
                i += 1
            else:
                if nums[j] > nums[p]:
                    j -= 1
                else:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
        
        nums[i], nums[p] = nums[p], nums[i]

        return i
    
        
    # other partition function implementation
    def partition1(self, nums, left, right): 
        # if choose pivot as the last item
        pivot = nums[right]
        # 1. move pivot to end
        # nums[pivot_index], nums[right] = nums[right], nums[pivot_index]  

        # 2. move all smaller elements to the left
        store_index = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1

        # 3. move pivot to its final place
        nums[right], nums[store_index] = nums[store_index], nums[right]  

        return store_index



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


class Solution():
    def quickSort(self, l, left, right):
        if left < right:
            pivot = self.partition(l, left, right)
            self.quickSort(l, left, pivot - 1)
            self.quickSort(l, pivot + 1, right)
            
    def partition(self, l, left, right):
        pivot = l[right]
        store_index = left
        
        for i in range(left, right):
            if l[i] < pivot:
                l[store_index], l[i] = l[i], l[store_index]
                store_index += 1
        
        l[store_index], l[right] = l[right], l[store_index]
        
        return store_index

    
class Solution1():
    # select item in kth index in sorted order
    def quickSelect(self, l, left, right, k):
        if left == right:
            return l[left]
        pivot_index = self.partition(l, left, right)
        if pivot_index == k:
            return l[pivot_index]
        elif pivot_index < k:
            return self.quickSelect(l, pivot_index + 1, right, k)
        else:
            return self.quickSelect(l, left, pivot_index - 1, k)
        
    def partition(self, l, left, right):
        random_index = randint(left, right)
        l[random_index], l[right] = l[right], l[random_index]
        
        i, j = left, right - 1
        
        while i <= j:
            if l[i] < l[right]:
                i += 1
            else:
                if l[j] > l[right]:
                    j -= 1
                else:
                    l[i], l[j] = l[j], l[i]
                    i += 1
                    j -= 1
        
        l[i], l[right] = l[right], l[i]
        
        return i
