'''

There are some processes that need to be executed. Amount of a load that process causes on a server that runs it, is being represented by a single integer. Total load caused on a server is the sum of the loads of all the processes that run on that server. You have at your disposal two servers, on which mentioned processes can be run. Your goal is to distribute given processes between those two servers in the way that, absolute difference of their loads will be minimized.

Given an array of n integers, of which represents loads caused by successive processes, return the minimum absolute difference of server loads.

Example 1:

Input: [1, 2, 3, 4, 5]
Output: 1
Explanation:
We can distribute the processes with loads [1, 2, 4] to the first server and [3, 5] to the second one,
so that their total loads will be 7 and 8, respectively, and the difference of their loads will be equal to 1.


'''

# be careful about dp initialization and boundary of index

import unittest

class Solution:
    def minAbs(self, s):
        '''
        : type s: List[int]
        : rtype : int 

        '''
        m = len(s)
        n = sum(s) // 2
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] <= j:
                    dp[i][j] = max(dp[i - 1][j], s[i - 1] + dp[i - 1][j - s[i - 1]])
                else:
                    dp[i][j] = dp[i - 1][j]

        return abs(sum(s) - dp[-1][-1] - dp[-1][-1])


class Test(unittest.TestCase):
    def test1(self):
        s = [1, 2, 3, 4, 5]
        expected = 1
        sol = Solution()
        actual = sol.minAbs(s)
        self.assertEqual(actual, expected)
    def test2(self):
        s = [10, 10, 9, 11]
        expected = 0
        sol = Solution()
        actual = sol.minAbs(s)
        self.assertEqual(actual, expected)
    def test3(self):
        s = [5, 5, 4, 10, 11]
        expected = 3
        sol = Solution()
        actual = sol.minAbs(s)
        self.assertEqual(actual, expected)
    def test4(self):
        s = [10, 10, 9, 9, 2]
        expected = 0
        sol = Solution()
        actual = sol.minAbs(s)
        self.assertEqual(actual, expected)

unittest.main(verbosity = 2)

