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

