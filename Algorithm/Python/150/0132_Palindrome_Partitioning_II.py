'''

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:

Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

'''


class Solution:
    def minCut(self, s: str) -> int:
        if s == None or len(s) == 0:
            return 0
        n = len(s)
        isPalindrome = [[False]*n for _ in range(n)]
        dp = [0]*n
        
        for i in range(n):
            dp[i] = i
            for j in range(i + 1):
                if s[i] == s[j] and (i - j < 2 or isPalindrome[j + 1][i - 1]):
                    isPalindrome[j][i] = True
                    dp[i] = 0 if j == 0 else min(dp[i], dp[j - 1] + 1)
        return dp[n - 1]
        
        
        