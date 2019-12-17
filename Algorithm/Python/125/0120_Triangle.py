'''

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

'''

# O(n) space solution

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        n = len(triangle[m - 1])
        
        dp = triangle[-1][:]
        
        for i in range(m - 2, -1, -1):
            for j in range(0, i + 1):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
        return dp[0]
        

# Solution 2

# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         m = len(triangle)
#         n = len(triangle[m - 1])
        
#         dp = [[0] * n for _ in range(m)]
#         dp[0][0] = triangle[0][0]
        
#         for i in range(1, m):
#             for j in range(i + 1):
#                 if j == 0:
#                     dp[i][j] = dp[i - 1][j] + triangle[i][j]
#                 elif j == i:
#                     dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
#                 else:
#                     dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
#         return min(dp[m - 1])



