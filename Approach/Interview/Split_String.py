'''

Given a string S, we can split S into 2 strings: S1 and S2. Return the number of ways S can be split such that the number of unique characters between S1 and S2 are the same.

Example 1:

Input: "aaaa"
Output: 3
Explanation: we can get a - aaa, aa - aa, aaa- a

Example 2:

Input: "bac"
Output: 0

Example 3:

Input: "ababa"
Output: 2
Explanation: ab - aba, aba - ba


'''

import unittest

class Solution:
    def spliString(self, s):
        '''
        : type s: str
        : rtype : int 

        '''
        
        left = []
        right = []
        set1 = set()
        set2 = set()
        res = 0

        # care for index
        for i in range(len(s) - 1):
            set1.add(s[i])
            left.append(set1.copy()) # set is mutable type, so create a copy then append

        for i in range(len(s) - 1, 0, -1):
            set2.add(s[i])
            right.insert(0, set2.copy())

        for i in range(len(s) - 1):
            if left[i] == right[i]:
                res += 1

        return res


class Test(unittest.TestCase):
    def test1(self):
        s = "aaaa"
        expected = 3
        sol = Solution()
        actual = sol.spliString(s)
        self.assertEqual(actual, expected)

    def test2(self):
        s = "bac"
        expected = 0
        sol = Solution()
        actual = sol.spliString(s)
        self.assertEqual(actual, expected)

    def test3(self):
        s = "ababa"
        expected = 2
        sol = Solution()
        actual = sol.spliString(s)
        self.assertEqual(actual, expected)

unittest.main(verbosity = 2)

