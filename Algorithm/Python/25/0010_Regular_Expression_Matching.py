'''

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false

'''

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(p) == 0:
            return len(s) == 0
        
        if len(p) == 1:
            return len(s) == 1 and (s[0] == p[0] or p[0] == '.')
        
        if p[1] != '*':
            if len(s) == 0:
                return False
            return (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p[1:])
        
        while len(s) != 0 and (s[0] == p[0] or p[0] == '.'):
            if self.isMatch(s, p[2:]):
                return True
            s = s[1:]
            
        return self.isMatch(s, p[2:])

# Recursion

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: # p is empty
            return not s

        first_match = bool(s) and p[0] in {s[0], '.'} # whether first character matches

        if len(p) >= 2 and p[1] == '*': # p[1] == '*'
            return (self.isMatch(s, p[2:]) or # repeat 0 time means delete
                    first_match and self.isMatch(s[1:], p)) # first_match, repeat p[0]
        else: # p[1] != '*', match the rest string
            return first_match and self.isMatch(s[1:], p[1:])   
    
    
    
    


