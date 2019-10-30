
'''

Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.

'''


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == - 2 ** 31 and divisor == -1:
            return 2 ** 31 - 1
        sign = 1
        if dividend < 0:
            sign *= -1
        if divisor < 0:
            sign *= -1
            
        m = abs(dividend)
        n = abs(divisor)
        res = 0
        while m >= n:
            t = n
            p = 1
            while m >= (t << 1):
                t <<= 1
                p <<= 1
            res += p
            m -= t
        return res * sign
        



