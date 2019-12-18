'''

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.

'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[0] = True
        
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if nums[j] >= i - j:
                    dp[i] = True
                    break
            if dp[i] == False:
                return False
        return dp[-1]

# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         if len(nums) == 0:
#             return True
        
#         cur = 0
#         i = 0
#         n = len(nums)
        
#         while cur < n - 1:
#             pre = cur
#             while i <= pre:
#                 cur = max(cur, i + nums[i])
#                 i += 1
#             if pre == cur:
#                 return False
            
#         return True    


        

