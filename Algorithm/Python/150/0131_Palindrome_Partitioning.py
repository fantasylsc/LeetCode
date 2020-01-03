'''

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]

'''


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        curr = []
        self.helper(s, 0, curr)
        return self.res
    
    def helper(self, s, start, curr):
        if start == len(s):
            self.res.append(curr[:])
        for i in range(start, len(s)):
            if not self.isPalindrome(s, start, i):
                continue
            curr.append(s[start: i + 1])
            self.helper(s, i + 1, curr)
            curr.pop()
        
    def isPalindrome(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
        

# optimized check palindrome substring

# class Solution:
#     def partition(self, s: str) -> List[List[str]]:
#         self.res = []
#         curr = []
#         n = len(s)
#         self.dp = [[False]*n for _ in range(n)]
        
#         for i in range(n):
#             for j in range(i + 1):
#                 if s[i] == s[j] and (i - j <= 2 or self.dp[j + 1][i - 1]):
#                     self.dp[j][i] = True
        
#         self.helper(s, 0, curr)
#         return self.res
    
#     def helper(self, s, start, curr):
#         if start == len(s):
#             self.res.append(curr[:])
#         for i in range(start, len(s)):
#             if not self.dp[start][i]:
#                 continue
#             curr.append(s[start: i + 1])
#             self.helper(s, i + 1, curr)
#             curr.pop()
        
#     def isPalindrome(self, s, start, end):
#         while start < end:
#             if s[start] != s[end]:
#                 return False
#             start += 1
#             end -= 1
#         return True


   
        