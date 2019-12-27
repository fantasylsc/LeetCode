'''

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

'''

'''

state: dp[i][j] represents whether s1[:i] and s2[:j] match s3[:i+j]
function: dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
initialize: dp[i][0] = dp[i - 1][0] and (s1[i - 1] == s3[i - 1]) # match s1 with s3
            dp[0][j] = dp[0][j - 1] and (s2[j - 1] == s3[j - 1]) # match s2 with s3

'''

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        r = len(s3)
        
        if m + n != r:
            return False
        
        dp = [[False]*(n + 1) for _ in range(m + 1)]
        dp[0][0] = True # 0 and 0 match 0
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
            
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or \
                           (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        return dp[-1][-1]
        
        


