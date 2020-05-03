'''

Search for the last target in a sorted list.
Return the index of the target that last appeared in the list.
If the target is not in the list, return -1.

Example 1: nums = [1,2,2,2,2,3,3,4], target = 2
return 4

Example 2: nums = [1,2,3,3,3,4], target = 3
return 4


'''

import unittest
from typing import List

class Solution:
    def searchFirstTarget(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        
        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target: # sqeeze the interval to the right side
                start = mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[end] == target:
            return end
        if nums[start] == target:
            return start

        return -1


class Test(unittest.TestCase):
    def test1(self):
        nums = [1, 2, 3, 3, 8, 9]
        target = 3
        s = Solution()
        actual = s.searchFirstTarget(nums, target)
        expected = 3
        self.assertEqual(actual, expected)

    def test2(self):
        nums = [1, 2, 3, 4, 4, 6, 7, 8, 9]
        target = 4
        s = Solution()
        actual = s.searchFirstTarget(nums, target)
        expected = 4
        self.assertEqual(actual, expected)

    def test3(self):
        nums = [1, 2, 2, 2, 2, 7, 8, 9]
        target = 2
        s = Solution()
        actual = s.searchFirstTarget(nums, target)
        expected = 4
        self.assertEqual(actual, expected)

    def test4(self):
        nums = [1, 7, 8, 9]
        target = 2
        s = Solution()
        actual = s.searchFirstTarget(nums, target)
        expected = -1
        self.assertEqual(actual, expected)
        
    def test5(self):
        nums = [1, 2]
        target = 1
        s = Solution()
        actual = s.searchFirstTarget(nums, target)
        expected = 0
        self.assertEqual(actual, expected)

unittest.main(verbosity = 2)
