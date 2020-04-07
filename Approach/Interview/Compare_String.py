'''

One string is strictly smaller than another when the frequency of occurrence of the smallest character in the string is less than the frequency of occurrence of the smallest character 
in the comparision string.

For example: "abcs" is smaller than "aaa" Because the smallest character (in lexicographical order) in "abcd" is 'a', with a frequency of 1, the smallest character in "aaa" is also 'a', but with
a frequency of 3.

Given string A and B, returns an array C of N integers. For 0 <= J < N, values of C[J] specify the number of strings in A which are strictly smaller than the comparision Jth
string in B.

Example:

A = "abcd,aabc,bd"

B = "aaa,aa"

C = [3, 2]

'''

# Naive approach, 1) count smallest character for each string and save in lists listA and listB. 
#                 2) compare listA and listB, how many item in listA is smaller than each item of listB, O(mn)

# Improved approach: similar idea like counting sort, use a list to record frequency of smallest character in list A, 
#                    index represents the frequency, value represents how many times this frequency occured. 

import unittest

class Solution:
    def compareString(self, A, B):
        '''
        : type A, B: str
        : rtype : List[int] 

        '''
        freqconter = [0] * 11
        wordsA = A.split(',')
        wordsB = B.split(',')
        res = []

        for w in wordsA:
            freq = w.count(min(w))
            freqconter[freq] += 1

        for w in wordsB:
            freq = w.count(min(w))
            res.append(sum(freqconter[:freq]))

        return res


class Test(unittest.TestCase):
    def test1(self):
        A = "abcd,aabc,bd"
        B = "aaa,aa"
        expected = [3, 2]
        sol = Solution()
        actual = sol.compareString(A, B)
        self.assertEqual(actual, expected)
    def test2(self):
        A = "abaa,aadvsbc,bdsdsdb"
        B = "aaa,aa"
        expected = [2, 0]
        sol = Solution()
        actual = sol.compareString(A, B)
        self.assertEqual(actual, expected)

unittest.main(verbosity = 2)

