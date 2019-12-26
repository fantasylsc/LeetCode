'''

Given two strings, find the longest common substring.

Return the length of it.

Example
Example 1:
    Input:  "ABCD" and "CBCE"
    Output:  2
    
    Explanation:
    Longest common substring is "BC"


Example 2:
    Input: "ABCD" and "EACB"
    Output:  1
    
    Explanation: 
    Longest common substring is 'A' or 'C' or 'B'
Challenge
O(n x m) time and memory.

Notice
The characters in substring should occur continuously in original string. This is different with subsequence.

'''

class Solution:
    """
    @param A: A string
    @param B: A string
    @return: the length of the longest common substring.
    """
    def longestCommonSubstring(self, A, B):
        # write your code here
        m = len(A)
        n = len(B)
        
        if m == 0 or n == 0:
            return 0
        
        res = 0
        dp = [[0]*(n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    res = max(res, dp[i][j])
                else:
                    dp[i][j] = 0
        
        return res
    
if __name__ == "__main__" : 
  
    X = "abcdxyz"
    Y = "xyzabcd"

    s = Solution()

    print(s.longestCommonSubstring(X, Y)) 

