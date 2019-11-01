'''

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5

'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        i = len(s) - 1
        
        while i > 0:
            if s[i] != ' ':
                break
            i -= 1
            
        if ' ' in s[:i + 1]:
            last_word = s[:i + 1].rsplit(' ', 1)[1]
            return len(last_word)
        else:
            return len(s[:i + 1])
        


        

