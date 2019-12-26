'''

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

'''

'''

state: dp[i][j] represents the num of operations required to convert word1[:i + 1] to word2[:j + 1]
function: dp[i][j] = MIN(dp[i-1][j-1], dp[i-1][j]+1, dp[i][j-1]+1) // word1[i] == word2[j]
         = MIN(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1 // word1[i] != word2[j]
intialize: dp[i][0] = i, dp[0][j] = j

'''

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        
        if m == 0:
            return n
        if n == 0:
            return m
        
        dp = [[0]*(n + 1) for _ in range(m + 1)]
        
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(m + 1):
            dp[i][0] = i
            
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j] + 1, dp[i][j - 1] + 1)
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[-1][-1]
            
        

