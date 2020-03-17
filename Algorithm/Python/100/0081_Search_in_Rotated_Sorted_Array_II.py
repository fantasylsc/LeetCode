'''

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?

'''

# consider conditions like:
# 1) nums[start] == nums[mid] and nums[end] == nums[mid],
#    can't decide, end -= 1
# 2) nums[start] == nums[mid],
#    [start, mid] are duplicates, start = mid
# 3) nums[end] == nums[mid], 
#    [mid, end] are duplicates, end = mid

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        
        start = 0
        end = len(nums) - 1
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return True
            if nums[start] == nums[mid] and nums[end] == nums[mid]:
                end -= 1
            elif nums[start] == nums[mid]:
                start = mid
            elif nums[end] == nums[mid]:
                end = mid
            elif nums[mid] > nums[start]:
                if nums[start] <= target and target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if nums[mid] <= target and target <= nums[end]:
                    start = mid
                else:
                    end = mid
        if nums[start] == target:
            return True
        if nums[end] == target:
            return True
        return False
        
        
