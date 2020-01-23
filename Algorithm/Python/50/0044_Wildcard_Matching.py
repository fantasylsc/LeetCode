'''

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false

'''

# 1) If the last characters are the same or pattern character is '?'
#     dp[i][j] = dp[i - 1][j - 1]
# 2) If the pattern character is '*' 
#    and there was a match on the previous step dp[i - 1][j - 1] = True 
#    dp[i - 1][k] = True, k >= j - 1  

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len = len(s)
        p_len = len(p)
        
        if p == s or p == '*':
            return True
        if p == '' or s == '':
            return False
        
        dp = [[False] * (s_len + 1) for _ in range(p_len + 1)]
        dp[0][0] = True
        
        for i in range(1, p_len + 1):
            if p[i - 1] == '*':
                j = 1
                while not dp[i - 1][j - 1] and j < (s_len + 1):
                    j += 1
                dp[i][j - 1] = dp[i - 1][j - 1]
                while j < s_len + 1:
                    dp[i][j] = True
                    j += 1
            elif p[i - 1] == '?':
                for j in range(1, s_len + 1):
                    dp[i][j] = dp[i - 1][j - 1]
            else:
                for j in range(1, s_len + 1):
                    dp[i][j] = dp[i - 1][j - 1] and p[i - 1] == s[j - 1]
        return dp[p_len][s_len]
                
        
        