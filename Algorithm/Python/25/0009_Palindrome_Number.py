'''

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        original = x
        reverse = 0
        
        while x > 0:
            digit = x % 10
            x = x // 10
            reverse = reverse * 10 + digit
        
        return reverse == original

# Two pointers
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        n = len(s)
        if n == 0 or n == 1:
            return True
        
        i = 0
        j = n - 1
        while i < n and j >= 0:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
    
# Haha
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1] 


