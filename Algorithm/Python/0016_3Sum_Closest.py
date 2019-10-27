'''

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

'''

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return None
        
        nums.sort()
        closest_sum = 0
        min_diff = float('inf')
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum == target:
                    return current_sum
                elif current_sum < target:
                    if abs(current_sum - target) < min_diff:
                        min_diff = abs(current_sum - target)
                        closest_sum = current_sum
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                    left += 1
                else:
                    if abs(current_sum - target) < min_diff:
                        min_diff = abs(current_sum - target)
                        closest_sum = current_sum
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                    right -= 1
        
        return closest_sum




