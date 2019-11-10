'''

Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.


'''

'''
Newton's method
sqrt(S) equals to f(x) = x ** 2 - S = 0

x(n+1) = x(n) - f(x(n))/f'(x(n)) = x(n) - (x(n) ** 2 - S)/2x(n) = (x(n) + S/x(n))/2

'''

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        x0 = x
        x1 = (x0 + x / x0) / 2
        while abs(x0 - x1) >= 1:
            x0 = x1
            x1 = (x0 + x / x0) / 2        
            
        return int(x1)        
            
        

