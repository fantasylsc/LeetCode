'''

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

'''

import sys

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        left = (m + n + 1) // 2
        right = (m + n + 2) // 2
        
        return (self.findKth(nums1, 0, nums2, 0, left) + self.findKth(nums1, 0, nums2, 0, right)) / 2
    
    def findKth(self, nums1, i, nums2, j, k):
        if i >= len(nums1):
            return nums2[j + k - 1]
        if j >= len(nums2):
            return nums1[i + k - 1]
        if k == 1:
            return min(nums1[i], nums2[j])
        
        if i + k/2 - 1 < len(nums1):
            midVal1 = nums1[i + k//2 - 1]
        else:
            midVal1 = sys.maxsize
        if j + k/2 - 1 < len(nums2):
            midVal2 = nums2[j + k//2 - 1]
        else:
            midVal2 = sys.maxsize
            
        if midVal1 < midVal2:
            return self.findKth(nums1, i + k//2, nums2, j, k - k//2)
        else:
            return self.findKth(nums1, i , nums2, j + k//2, k - k//2)



