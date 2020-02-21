'''

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

'''

class Solution:
    def reverse(self, x: int) -> int:
        Negative = False
        if x < 0:
            x = - x
            Negative = True
            
        res = 0
        while x != 0:
            digit = x % 10
            x = x //10
            res = res * 10 + digit
            
        if Negative:
            res = - res
            
        if res < - 2**31 or res > 2**31 - 1:
            return 0
        else:    
            return res

# Reverse list of string
class Solution:
    def reverse(self, x: int) -> int:
        s = list(str(x))
        flag = True
        if s[0] == '-':
            flag = False
            s = s[1:]
        
        i = 0
        j = len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        
        while s[0] == 0:
            s = s[1:]
        
        res = ''
        res = int(res.join(s))
        if flag == False:
            res = - res
            
        if res <= - 2**31 or res >= 2**31 - 1:
            return 0
        else:
            return res


