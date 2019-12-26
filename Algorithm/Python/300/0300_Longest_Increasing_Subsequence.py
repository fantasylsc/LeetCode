'''

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?

'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # wrong: dp[i] represents LIS length of first i num
        # right: dp[i] represents LIS length end with the ith num
        n = len(nums)
        if n == 0:
            return 0
        
        dp = [1] * n
        res = 1
        
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])
        return res
     
# samll optimization
        
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         # wrong: dp[i] represents LIS length of first i num
#         # right: dp[i] represents LIS length end with the ith num
#         n = len(nums)
#         if n == 0:
#             return 0
        
#         dp = [0] * n
#         dp[0] = 1
#         res = 1
        
#         for i in range(1, n):
#             temp_max = 0
#             for j in range(i):
#                 if nums[i] > nums[j]:
#                     temp_max = max(temp_max, dp[j])
#             dp[i] = temp_max + 1
#             res = max(res, dp[i])
#         return res
        


