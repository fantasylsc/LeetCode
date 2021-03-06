'''

Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.

'''

class Solution:
    def myAtoi(self, str: str) -> int:
        if len(str) == 0:
            return 0
        
        sign = 1
        res = 0
        n = len(str)
        i = 0
        
        while i < n and str[i] == ' ':
            i += 1
            
        if i < n and str[i].isalpha():
            return 0
        
        if i < n and str[i] == '-':
            sign = -1
            i += 1
        elif i< n and str[i] == '+':
            sign = 1
            i += 1
            
        while i < n and str[i] >= '0' and str[i] <= '9':
            res = int(str[i]) + res * 10
            i += 1
            
        res = res * sign
        
        if res < - 2**31:
            return - 2**31
        if res > 2**31 - 1:
            return 2**31 - 1
        
        return res

# small optimization
class Solution:
    def myAtoi(self, str: str) -> int:
        n = len(str)
        if n == 0:
            return 0
        
        i = 0
        while i < n and str[i] == ' ': # pay attention to index range when using while loop
            i += 1
        
        Negative = False
        if i < n and (str[i] == '-' or str[i] == '+'):
            if str[i] == '-':
                Negative = True
            i += 1
        elif i < n and not str[i].isnumeric():
            return 0
        
        res = 0
        while i < n and str[i].isnumeric():
            res = 10 * res + int(str[i])
            i += 1
            
        if Negative:
            res = - res
        
        if res <= - 2 ** 31:
            return - 2 ** 31
        elif res >= 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return res


