'''

Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.

'''

# TLE
# dp f[i][j] split i nums into j parts
# formula f[i][j] = min(f[i][j], max(f[k][j - 1], nums[k + 1] + ... + nums[i])) 
# O(n^2 * m)
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        f = [[float('inf')] * (m + 1) for _ in range(n + 1)]
        sums = [0] * (n + 1)
        for i in range(n):
            sums[i + 1] = sums[i] + nums[i]
        
        f[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                for k in range(i):
                    f[i][j] = min(f[i][j], max(f[k][j - 1], sums[i] - sums[k]))
        return f[n][m]





# TLE
# Brute force O(n^m), totally choose m - 1 from n - 1 cases  
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        self.ans = float('inf')
        n = len(nums)
        
        def dfs(nums, i, cntSubarrays, curSum, curMax):
            if i == n and cntSubarrays == m:
                self.ans = min(self.ans, curMax)
                return
            if i == n:
                return
            if i > 0:
                # include nums[i] into previous subarray, cntSubarrays will not change, curSum + nums[i]
                dfs(nums, i + 1, cntSubarrays, curSum + nums[i], max(curMax, curSum + nums[i]))
            if cntSubarrays < m:
                # take nums[i] as a new start for a subarray
                dfs(nums, i + 1, cntSubarrays + 1, nums[i], max(curMax, nums[i]))

        dfs(nums, 0, 0, 0, 0)
        return self.ans




