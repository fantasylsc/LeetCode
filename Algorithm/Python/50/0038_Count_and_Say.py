
'''

The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

 

Example 1:

Input: 1
Output: "1"

'''


class Solution:
    def countAndSay(self, n: int) -> str:
        if n <= 0:
            return ''
        
        if n == 1:
            return '1'
        
        n -= 1
        res = '1'
        
        while n:
            cur = ''
            i = 0
            while i < len(res):
                count = 1
                while i + 1 < len(res) and res[i] == res[i + 1]:
                    count += 1
                    i += 1
                cur += str(count) + res[i]
                i += 1
            res = cur
            n -= 1
                
        return res
        



