'''

Backpack

Given n items with size Ai, an integer m denotes the size of a backpack. How full you can fill this backpack?

Example
Example 1:
    Input:  [3,4,8,5], backpack size=10
    Output:  9

Example 2:
    Input:  [2,3,5,7], backpack size=12
    Output:  12
    
Challenge
O(n x m) time and O(m) memory.

O(n x m) memory is also acceptable if you do not know how to optimize memory.

Notice
You can not divide any item into small pieces.

'''

# Approach 1
# More direct approach than approach 2.
# dp[i][j] represents the maximum size we can put for first i items in backpack size of j

import unittest

class Solution:
    def backPack(self, m, A):
        # write your code here
        n = len(A)
        
        dp = [[0]*(m + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if A[i - 1] <= j:
                    dp[i][j] = max(dp[i - 1][j], A[i - 1] + dp[i - 1][j - A[i - 1]])
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]

# Approach 2

# class Solution:
#     """
#     @param m: An integer m denotes the size of a backpack
#     @param A: Given n items with size A[i]
#     @return: The maximum size
    
#     state: dp[i][j] whether backpack size of j can be exactly filled by first i items 
#     function: dp[i][j] = dp[i - 1][j] or dp[i - 1][j - A[i - 1]]
#     initialize: dp[0][0] = True, dp[0][:] = False
#     """
#     def backPack(self, m, A):
#         # write your code here
#         n = len(A)
        
#         dp = [[False]*(m + 1) for _ in range(n + 1)]
#         dp[0][0] = True
        
#         for i in range(1, n + 1):
#             for j in range(1, m + 1):
#                 if j == A[i - 1]: # ith item size = size j
#                     dp[i][j] = True
#                 elif j > A[i - 1]: # item size < size j
#                     # not put ith item in backpack or put in backpack
#                     dp[i][j] = dp[i - 1][j] or dp[i - 1][j - A[i - 1]]
#                 else: # item size > size j, can't put in
#                     dp[i][j] = dp[i - 1][j]
        
#         for j in range(m, -1, -1):
#             if dp[n][j] == True:
#                 return j

class Test(unittest.TestCase):
    def test1(self):
        A = [3,4,8,5]
        m = 10
        expected = 9
        sol = Solution()
        actual = sol.backPack(m, A)
        self.assertEqual(expected, actual)

    def test2(self):
        A = [2,3,5,7]
        m = 12
        expected = 12
        sol = Solution()
        actual = sol.backPack(m, A)
        self.assertEqual(expected, actual)

unittest.main(verbosity = 2)
