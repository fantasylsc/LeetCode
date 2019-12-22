'''

Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
 

Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.

'''

'''
dp[i] represents the nums of solutions when target is i

dp[i] += dp[i - num]

Example: 
[1,2,3] 4
4 = 1 + 3 or 2 + 2 or 3 + 1
dp[4] = dp[4] + dp[3] when 4 = 1 + 3
        dp[4] + dp[2] when 4 = 2 + 2
        dp[4] + dp[1] when 4 = 3 + 1

'''

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i - num]
        return dp[-1]
        
        
        
        




