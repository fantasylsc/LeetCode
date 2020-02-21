'''

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

'''
# Expand from middle
# DP



# O(n^2) solution
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        
        self.start = 0
        self.maxLen = 0
        
        for i in range(len(s)):
            self.searchPalindrome(s, i, i)
            self.searchPalindrome(s, i, i + 1)
            
        return s[self.start: self.start + self.maxLen]
    
    def searchPalindrome(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        if self.maxLen < j - i - 1:
            self.start = i + 1
            self.maxLen = j - i - 1


# O(n^3) solution
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            for j in range(len(s), i, -1):
                if len(res) >= j - i:
                    break
                if s[i:j] == s[i:j][::-1]:
                    res = s[i:j]
                    break
                    
        return res

# DP
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return s
        
        n = len(s) # get length of input string 

        dp = [[0]*n for _ in range(n)]  

        # All substrings of length 1 are 
        # palindromes 
        maxLength = 1
        for i in range(n):
            dp[i][i] = True

        # check for sub-string of length 2. 
        start = 0
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                maxLength = 2

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j] and dp[i + 1][j - 1] == True:
                    dp[i][j] = True
                    if j - i + 1 > maxLength:
                        maxLength = j - i + 1
                        start = i
        return s[start: start + maxLength]
        
# using for loop 
# Check for lengths greater than 2.  
# k is length of substring 
#         k = 3
#         while k <= n : 
#             # Fix the starting index 
#             i = 0
#             while i < (n - k + 1) : 
#                 if (dp[i + 1][j - 1] and 
#                           s[i] == s[j]) : 
#                     dp[i][j] = True

#                     if (k > maxLength) : 
#                         start = i 
#                         maxLength = k 
#                 i = i + 1
#             k = k + 1
