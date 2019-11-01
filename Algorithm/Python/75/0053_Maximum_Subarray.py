'''

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        max_sum = current_sum = nums[0]
        
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i]) # local maximum
            max_sum = max(max_sum, current_sum) # global maximum
            
        return max_sum      


# Divide and Conquer

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         if len(nums) == 0:
#             return 0
#         return helper(nums, 0, len(nums) - 1)
    
    
# def helper(nums, left, right):
#     if (left >= right):
#         return nums[left]

#     mid = left + (right - left)//2
#     lmax = helper(nums, left, mid - 1)
#     rmax = helper(nums, mid + 1, right)
#     mmax = nums[mid]
#     t = mmax

#     for i in range(mid - 1, left - 1, -1):
#         t += nums[i]
#         mmax = max(mmax, t)

#     t = mmax

#     for i in range(mid + 1, right + 1):
#         t += nums[i]
#         mmax = max(mmax, t)

#     return max(mmax, max(lmax, rmax))
        

