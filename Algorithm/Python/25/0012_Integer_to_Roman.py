'''

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: 3
Output: "III"
Example 2:

Input: 4
Output: "IV"

'''

class Solution:
    def intToRoman(self, num: int) -> str:
        res = ''
        sym = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        val = [1000, 500, 100, 50, 10, 5, 1]
        
        n = 0
        while n < 7:
            x = num // val[n]
            if x < 4:
                for _ in range(1, x + 1):
                    res += sym[n]
            elif x == 4:
                res = res + sym[n] + sym[n - 1]
            elif x > 4 and x < 9:
                res += sym[n - 1]
                for _ in range(6, x + 1):
                    res += sym[n]
            elif x == 9:
                res = res + sym[n] + sym[n - 2]
            
            num %= val[n]
            n += 2
            
        return res

    
# Another approach
class Solution:
    def intToRoman(self, num: int) -> str:
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        dic = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
              50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
              }
        res = ''
        
        for n in nums:
            while num >= n:
                num -= n
                res += dic[n]
                
        return res


