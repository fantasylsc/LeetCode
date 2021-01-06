'''

The gray code is a binary numeral system where two successive values differ in only one bit.

Given an integer n representing the total number of bits in the code, return any sequence of gray code.

A gray code sequence must begin with 0.

 

Example 1:

Input: n = 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2
[0,2,3,1] is also a valid gray code sequence.
00 - 0
10 - 2
11 - 3
01 - 1
Example 2:

Input: n = 1
Output: [0,1]
 

Constraints:

0 <= n <= 15
Accepted

'''


# gray code follows the sequence 0, 1, 3, 2, 6, 7, 5, 4
# +1, +2, +4, +8...

class Solution:
    def grayCode(self, n: int) -> List[int]:
        dp = [0]
        
        for i in range(n):
            dp = dp + [x | 1<<i for x in reversed(dp)]
            
        return dp
        
        
        



