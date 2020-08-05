'''

Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

Example 1:

Input: s1 = "great", s2 = "rgeat"
Output: true
Example 2:

Input: s1 = "abcde", s2 = "caebd"
Output: false

'''
# recursion
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        str1 = s1
        str2 = s2
        if sorted(str1) != sorted(str2):
            return False
        
        for i in range(1, len(s1)):
            s11 = s1[0:i]
            s12 = s1[i:]
            s21 = s2[0:i]
            s22 = s2[i:]
            if self.isScramble(s11, s21) and self.isScramble(s12, s22):
                return True
            
            s21 = s2[len(s1) - i:]
            s22 = s2[0:len(s1) - i]
            if self.isScramble(s11, s21) and self.isScramble(s12, s22):
                return True
            
        return False
            

# DP
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        n = len(s1)
        
        dp = [[[False] * n for _ in range(n)] for _ in range(n + 1)]
        
        # dp[k][i][j], 3,1,2 dimension
        # dp[k][i][j]: whether s1, s2 with length k and start with ith and jth string are scrable
        for l in range(1, n + 1):
            for i in range(0, n - l + 1):
                for j in range(0, n - l + 1):
                    if l == 1:
                        dp[l][i][j] = (s1[i] == s2[j])
                    else:
                        for k in range(1, l):
                            if (dp[k][i][j] and dp[l - k][i + k][j + k]) or \
                            (dp[l - k][i + k][j] and dp[k][i][j + l - k]):
                                dp[l][i][j] = True
        return dp[n][0][0]
        
    '''
    class Solution {
public:
    bool isScramble(string s1, string s2) {
        if (s1.size() != s2.size()) return false;
        if (s1 == s2) return true;
        int n = s1.size();
        vector<vector<vector<bool>>> dp (n, vector<vector<bool>>(n, vector<bool>(n + 1)));
        for (int len = 1; len <= n; ++len) {
            for (int i = 0; i <= n - len; ++i) {
                for (int j = 0; j <= n - len; ++j) {
                    if (len == 1) {
                        dp[i][j][1] = s1[i] == s2[j];
                    } else {
                        for (int k = 1; k < len; ++k) {
                            if ((dp[i][j][k] && dp[i + k][j + k][len - k]) || (dp[i + k][j][len - k] && dp[i][j + len - k][k])) {
                                dp[i][j][len] = true;
                            }
                        }
                    }                
                }
            }
        }
        return dp[0][0][n];
    }
};
    
    '''

        
        
