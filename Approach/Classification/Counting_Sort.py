'''

Counting Sort

Worst case performance: O(n + k)
Best case performance: Ω(n + k)
Average performance: Θ(n + k)
Worst case space complexity: O(k)

'''

import unittest
from typing import List

class Solution:
    def countingSort(self, nums: List[int]):
        max_val = max(nums)
        count = [0] * (max_val + 1)
        res = []

        for i in range(len(nums)):
            count[nums[i]] += 1

        for i in range(len(count)):
            for _ in range(count[i]):
                res.append(i)

        return res


class Test(unittest.TestCase):
    def test(self):
        nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        s = Solution()
        res = s.countingSort(nums)
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(res, expected)

    def test_scond(self):
        nums = [1, 0, 1, 0, 1]
        s = Solution()
        res = s.countingSort(nums)
        expected = [0, 0, 1, 1, 1]
        self.assertEqual(res, expected)

unittest.main(verbosity = 2)

