'''

Question 1:
Given an Array A, find the minimum amplitude you can get after changing up to 3 elements. Amplitude is the range of the array (basically difference between largest and smallest element).

Example 1:

Input: [-1, 3, -1, 8, 5, 4]
Output: 2
Explanation: we can change -1, -1, 8 to 3, 4 or 5

Example 2:

Input: [10, 10, 3, 4, 10]
Output: 0
Explanation: change 3 and 4 to 10



'''

import unittest

class Solution:
    def minAmplitude(self, s):
        '''
        : type s: List
        : rtype : int 

        '''

        n = len(s)
        if n <= 4:
            return 0

        s1 = s[0: 4]
        s1.sort()
        max1, max2, max3, max4 = s1[3], s1[2], s1[1], s1[0]
        min1, min2, min3, min4 = s1[0], s1[1], s1[2], s1[3]

        for i in range(4, n):
            if s[i] > max1:
                max4 = max3
                max3 = max2
                max2 = max1
                max1 = s[i]
            elif s[i] > max2:
                max4 = max3
                max3 = max2
                max2 = s[i]
            elif s[i] > max3:
                max4 = max3
                max3 = s[i]
            elif s[i] > max4:
                max4 = s[i]

            if s[i] < min1:
                min4 = min3
                min3 = min2
                min2 = min1
                min1 = s[i]
            elif s[i] < min2:
                min4 = min3
                min3 = min2
                min2 = s[i]
            elif s[i] < min3:
                min4 = min3
                min3 = s[i]
            elif s[i] < min4:
                min4 = s[i]

        # res = float('inf')

        res = min(max4 - min1, max1 - min4, max3 - min2, max2 - min3)

        return res


class Test(unittest.TestCase):
    def test1(self):
        s = [-1, 3, -1, 8, 5, 4]
        expected = 2
        sol = Solution()
        actual = sol.minAmplitude(s)
        self.assertEqual(actual, expected)

    def test2(self):
        s = [10, 10, 3, 4, 10]
        expected = 0
        sol = Solution()
        actual = sol.minAmplitude(s)
        self.assertEqual(actual, expected)

unittest.main(verbosity = 2)

