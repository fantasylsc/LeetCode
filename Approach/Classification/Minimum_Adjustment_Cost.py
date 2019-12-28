'''

Given an integer array, adjust each integers so that the difference of every adjacent integers are not greater than a given number target.

If the array before adjustment is A, the array after adjustment is B, you should minimize the sum of |A[i]-B[i]|

Example
Example 1:
    Input:  [1,4,2,3], target=1
    Output:  2

Example 2:
    Input:  [3,5,4,7], target=2
    Output:  1
    
Notice
You can assume each number in the array is a positive integer and not greater than 100.

'''

class Solution:
    """
    @param: A: An integer array
    @param: target: An integer
    @return: An integer
    """
    
    '''
    state: dp[i][j] represents min ajustmentcost for first ith items of A and the ith item is j 
    function: dp[i][j] = min(dp[i][j], dp[i - 1][k] + abs(A[i - 1] - j))
              when abs(j - k) <= target
    initialize: dp[1][j] = abs(A[0] - j)
    
    '''
    
    
    def MinAdjustmentCost(self, A, target):
        # write your code here
        if A == None or len(A) == 0:
            return 0
            
        m = len(A)
        
        dp = [[float('inf')]*101 for _ in range(m + 1)]
        for j in range(101):
            dp[0][j] = 0
        
        for i in range(1, m + 1):
            for j in range(1, 101):
                for k in range(1, 101):
                    if abs(k - j) <= target:
                        dp[i][j] = min(dp[i][j], dp[i - 1][k] + abs(A[i - 1] - j))
        
        res = float('inf')
        for j in range(1, 101):
            res = min(res, dp[m][j])
        
        return res
        
        
        