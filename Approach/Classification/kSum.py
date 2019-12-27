'''

k Sum

Given n distinct positive integers, integer k (k <= n) and a number target.

Find k numbers where sum is target. Calculate how many solutions there are?

Example
Example 1

Input:
List = [1,2,3,4]
k = 2
target = 5
Output: 2
Explanation: 1 + 4 = 2 + 3 = 5
Example 2

Input:
List = [1,2,3,4,5]
k = 3
target = 6
Output: 1
Explanation: There is only one method. 1 + 2 + 3 = 6

'''

class Solution:
    """
    @param A: An integer array
    @param k: A positive integer (k <= length(A))
    @param target: An integer
    @return: An integer
    """
    
    '''
    
    state: dp[i][j][t] represents num of solutions by picking j items from first ith items so the sum is t
    function: dp[i][j][t] = dp[i - 1][j - 1][t] + dp[i - 1][j - 1][j - A[i - 1]
    initialize: dp[0][0][0] = 1, 
                for i in range(m + 1):
                    dp[i][0][0] = 1 
    
    '''
    
    
    def kSum(self, A, k, target):
        # write your code here
        if (A == None or len(A) == 0) and k == 0 and target == 0:
            return 1
        if (A == None or len(A) == 0) or k <= 0 or target <= 0:
            return 0
        
        m = len(A)
        n = k
        r = target
        
        dp = [[[0]*(r + 1) for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0][0] = 1
        for i in range(m + 1):
            dp[i][0][0] = 1
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                for t in range(1, r + 1):
                    dp[i][j][t] = dp[i - 1][j][t]
                    if t >= A[i - 1]:
                        dp[i][j][t] += dp[i - 1][j - 1][t - A[i - 1]]
                    
        return dp[-1][-1][-1]
        
        
        


