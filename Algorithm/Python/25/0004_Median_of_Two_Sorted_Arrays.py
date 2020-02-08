'''

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

'''
# for a sorted list with k numbers, the median is the average of the (k + 1)//2 th number and (k + 2)//2 the number. 
# So the question is converted to find the (k + 1)//2 th number and (k + 2)//2 the number.
# Find kth: findKth(self, nums1, i, nums2, j, k)
# Base case for recursion: i, len(nums1), j, len(nums2), k == 1
# See if k/2th item exists, midVal1, midVal2, if not exist, set midVal = float('int')
# Eliminate the smaller k/2th number

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        
        left = (m + n + 1) // 2
        right = (m + n + 2) // 2
        
        return (self.findKth(nums1, 0, nums2, 0, left) + self.findKth(nums1, 0, nums2, 0, right)) / 2
    
    # find kth number in nums1 starts from ith item and nums2 starts from jth item
    def findKth(self, nums1, i, nums2, j, k):
        
        # i exceed lenth of nums1, nums1 = [], so find kth number in nums2
        if i >= len(nums1):
            return nums2[j + k - 1]
        if j >= len(nums2):
            return nums1[i + k - 1]
        if k == 1:
            return min(nums1[i], nums2[j])
        
        
        # nums1 = {1, 3}，nums2 = {2, 4, 5}，K=4, eliminate {1, 3} in nums1

        if i + k/2 - 1 < len(nums1): # if k/2th item exists, choose this item
            midVal1 = nums1[i + k//2 - 1]
        else: # Example: nums1 = {3}，nums2 = {2, 4, 5, 6, 7}，K=4. Should keep nums1 (set midVla1 = float('inf')), eliminate {2, 4} in nums2
            midVal1 = float('inf')
        if j + k/2 - 1 < len(nums2):
            midVal2 = nums2[j + k//2 - 1]
        else:
            midVal2 = float('inf')
        
        # Eliminate the k//2 values
        if midVal1 < midVal2:
            return self.findKth(nums1, i + k//2, nums2, j, k - k//2)
        else:
            return self.findKth(nums1, i , nums2, j + k//2, k - k//2)



