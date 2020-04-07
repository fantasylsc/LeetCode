'''

You are given a string that represents time in the format hh:mm. Some of the digits are blank (represented by ?). 
Fill in ? such that the time represented by this string is the maximum possible. Maximum time: 23:59, minimum time: 00:00. You can assume that input string is always valid.

Example 1:

Input: "?4:5?"
Output: "14:59"

Example 2:

Input: "23:5?"
Output: "23:59"

Example 3:

Input: "2?:22"
Output: "23:22"

Example 4:

Input: "0?:??"
Output: "09:59"

Example 5:

Input: "??:??"
Output: "23:59"


'''

# hout: 0-23, minute: 0-59, 
# hour[0]

import unittest

class Solution:
    def maxTime(self, s):
        '''
        : type s: str
        : rtype : str 

        '''
        res = ''
        if s[0] == '?':
            if s[1] == '?' or int(s[1]) < 3:
                res += '2'
            else:
                res += '1'
        else:
            res += s[0]

        if s[1] == '?':
            if res[0] == '2':
                res += '3'
            else:
                res += '9'
        else:
            res += s[1]

        res += ':'

        if s[3] == '?':
            res += '5'
        else:
            res += s[3]

        if s[4] == '?':
            res += '9'
        else:
            res += s[4]

        return res


class Test(unittest.TestCase):
    def test1(self):
        s = "?4:5?"
        expected = "14:59"
        sol = Solution()
        actual = sol.maxTime(s)
        self.assertEqual(actual, expected)
    def test2(self):
        s = "23:5?"
        expected = "23:59"
        sol = Solution()
        actual = sol.maxTime(s)
        self.assertEqual(actual, expected)
    def test3(self):
        s = "2?:22"
        expected = "23:22"
        sol = Solution()
        actual = sol.maxTime(s)
        self.assertEqual(actual, expected)
    def test4(self):
        s = "0?:??"
        expected = "09:59"
        sol = Solution()
        actual = sol.maxTime(s)
        self.assertEqual(actual, expected)
    def test5(self):
        s = "??:??"
        expected = "23:59"
        sol = Solution()
        actual = sol.maxTime(s)
        self.assertEqual(actual, expected)

unittest.main(verbosity = 2)

