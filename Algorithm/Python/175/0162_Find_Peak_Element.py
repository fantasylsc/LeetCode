'''

A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.
Note:

Your solution should be in logarithmic complexity.

'''
# binary search 1

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] > nums[mid + 1]:
                end = mid
            else:
                start = mid
                
        if nums[start] > nums[end]:
            return start
        return end

# binary search 2

# class Solution:
#     def findPeakElement(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return 0
#         if nums[0] > nums[1]:
#             return 0
#         if nums[-1] > nums[-2]:
#             return len(nums) - 1
        
#         left = 0
#         right = len(nums) - 1
        
#         while left < right:
#             mid = left + (right - left)//2
#             if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
#                 return mid
#             elif nums[mid] > nums[mid - 1] and nums[mid + 1] > nums[mid]:
#                 left = mid + 1
#             else:
#                 right = mid
        
#         return left


