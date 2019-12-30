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

class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    
    state: dp[i][j] whether backpack size of j can be filled by first i items 
    function: dp[i][j] = dp[i - 1][j] or dp[i - 1][j - A[i - 1]]
    initialize: dp[0][0] = True, dp[0][:] = False
    """
    def backPack(self, m, A):
        # write your code here
        n = len(A)
        
        dp = [[False]*(m + 1) for _ in range(n + 1)]
        dp[0][0] = True
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if j == A[i - 1]:
                    dp[i][j] = True
                elif j > A[i - 1]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - A[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        for j in range(m, -1, -1):
            if dp[n][j] == True:
                return j
