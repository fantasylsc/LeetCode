
'''

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

'''


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right_end = mid
                left_end = mid
                while right_end < len(nums) - 1 and nums[right_end] == nums[right_end + 1]:
                    right_end += 1
                while left_end > 0 and nums[left_end] == nums[left_end - 1]:
                    left_end -= 1                
                return [left_end, right_end]
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if nums[left] == target:
            return [left, left]
        else:
            return [-1, -1]
        



