'''

X = [1, 2, 4, 3, 5]
Y = [1, 2, 3, 4, 5]

Array X is larger than array Y because X[2] > Y[2]. A contiguous subarray is defined as a subarray which has consecutive indexes.

Write a funtion that, given a zero-indexed array A consisting of N integers and an interger K, returns the largest contiguous subarray of length K from
all the contiguous subarrays of length K.

For example:

A = [1, 4, 3, 2, 5], K = 4

return [4, 3, 2, 5]

Because between two contiguous subarrays: [1, 4, 3, 2] and [4, 3, 2, 5], [4, 3, 2, 5] is larger.

Assume that:
    1 <= K <= N <= 100;
    1 <= A[J] <= 1000
given an array A contains N distinct integers.

'''


import unittest

class Solution:
    def compareString(self, A, K):
        '''
        : type A: List[int]
        : type K: int
        : rtype : List[int] 

        '''
        
        n = len(A)
        maxIndex = 0

        for i in range(1, n - K + 1):
            if A[i] > A[maxIndex]:
                maxIndex = i

        print('maxIndex:',maxIndex)

        return A[maxIndex: maxIndex + K]


class Test(unittest.TestCase):
    def test1(self):
        A = [1, 4, 3, 2, 5]
        K = 4
        expected = [4, 3, 2, 5]
        sol = Solution()
        actual = sol.compareString(A, K)
        self.assertEqual(actual, expected)
    def test2(self):
        A = [8, 5, 9, 3, 2, 4]
        K = 2
        expected = [9, 3]
        sol = Solution()
        actual = sol.compareString(A, K)
        self.assertEqual(actual, expected)

unittest.main(verbosity = 2)

