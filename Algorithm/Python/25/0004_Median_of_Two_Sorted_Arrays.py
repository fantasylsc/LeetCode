'''

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

'''


# find (m + n + 1)//2 and (m + n + 2)//2
# findkth(nums1, i, nums2, j, k)
# base case for recursion i >=len(nums1), j >= len(nums2), k == 1
# 1) if i >= len(nums1) 2) if i + k//2 - 1 < len(nums1) 3) if midVal1 < midVal2


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        left = (m + n + 1)//2
        right = (m + n + 2)//2
        
        return (self.findkth(nums1, 0, nums2, 0, left) + self.findkth(nums1, 0, nums2, 0, right)) / 2
        
    def findkth(self, nums1, i, nums2, j, k):
        if i >= len(nums1):
            return nums2[j + k - 1]
        if j >= len(nums2):
            return nums1[i + k - 1]
        if k == 1:
            return min(nums1[i], nums2[j])
        
        if i + k//2 - 1 < len(nums1):
            midVal1 = nums1[i + k//2 - 1]
        else:
            midVal1 =  float('inf')
        if j + k//2 - 1 < len(nums2):
            midVal2 = nums2[j + k//2 - 1]
        else:
            midVal2 = float('inf')
            
        if midVal1 < midVal2:
            return self.findkth(nums1, i + k//2, nums2, j, k - k//2)
        else:
            return self.findkth(nums1, i, nums2, j + k//2, k - k//2)
        
# huahua's solution

# find m1 nums in nums1, find m2 nums in nums2, so that m1 + m2 = k

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        
        # choose shorter num list
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        
        k = (n1 + n2 + 1)//2
        
        l = 0
        r = n1
        
        while l < r:
            m1 = l + (r - l)//2
            m2 = k - m1
            # if nums1 is smaller, need to include more nums
            if nums1[m1] < nums2[m2 - 1]:
                l = m1 + 1
            else:
                r = m1
        
        m1 = l
        m2 = k - l
        
        c1 = max(float('-inf') if m1 <= 0 else nums1[m1 - 1],\
                float('-inf') if m2 <= 0 else nums2[m2 - 1])
        
        if (n1 + n2) % 2 == 1:
            return c1
        
        c2 = min(float('inf') if m1 >= n1 else nums1[m1],\
                float('inf') if m2 >= n2 else nums2[m2])
        
        return (c1 + c2)/2        
