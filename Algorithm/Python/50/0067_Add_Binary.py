'''

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l1 = len(a)
        l2 = len(b)
        
        if l1 == 0:
            return b
        if l2 == 0:
            return a
        
        res = ''
        p1 = l1 - 1
        p2 = l2 - 1
        carry = 0
        d1 = 0
        d2 = 0
        
        while p1 >= 0 or p2 >= 0:
            if p1 < 0:
                d1 = 0
            else:
                d1 = int(a[p1])
            if p2 < 0:
                d2 = 0
            else:
                d2 = int(b[p2])
            Sum = d1 + d2 + carry
            current = Sum % 2
            carry = Sum // 2
            res = str(current) + res
            p1 -= 1
            p2 -= 1
            
        if carry == 1:
            res = '1' + res
            
        return res
            
        

