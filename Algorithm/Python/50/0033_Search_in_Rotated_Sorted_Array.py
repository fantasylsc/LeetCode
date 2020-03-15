
'''

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

'''

# Approach 1) take the original nums as a line, rotated nums as two line segments
# original line, [1,2,3,4,5,6]
        /6
       /5
      /4
     /3
    /2
   /1
# rotated two line segments, [4,5,6] [1,2,3]

#   /6
#  /5
# /4
#      /3
#     /2
#    /1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        start = 0
        end = len(nums) - 1
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            if nums[start] < nums[mid]: # nums[mid] in the left segment
                if nums[start] <= target and target <= nums[mid]: # target in the left segment
                    end = mid
                else: # target in the right side of nums[mid]
                    start = mid
            else: # nums[mid] in the right segment 
                if nums[mid] <= target and target <= nums[end]: # target in the right segment
                    start = mid
                else: # target in the left segment
                    end = mid
        
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

# Approach 2) find pivot, then use binary search two times
    
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         if len(nums) == 0:
#             return -1

#         # find pivot
#         left = 0
#         right = len(nums) - 1
#         while left < right:
#             mid = left + (right - left) // 2
#             if nums[mid] > nums[right]:
#                 left = mid + 1
#             else:
#                 right = mid
                
#         pivot = left
        
#         # find target, binary search in [0: pivot] and [pivot: len(nums)] respectively
#         res = self.binarySearch(nums, target, 0, pivot)
        
#         if res == -1:
#             return self.binarySearch(nums, target, pivot, len(nums))
#         else:
#             return res
        
        
#     def binarySearch(self, nums, target, left, right):
#         while left < right:
#             mid = left + (right - left) // 2
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid
                
#         return -1
        



