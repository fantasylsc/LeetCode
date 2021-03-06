'''

Given a sorted array of n integers, find the starting and ending position of a given target value.

If the target is not found in the array, return [-1, -1].


Example

Example 1:

Input:
nums = []
target = 9
Output:
[-1,-1]

Example 2:

Input:
nums = [5, 7, 7, 8, 8, 10]
target = 8
Output:
[3, 4]

Challenge

O(log n) time


'''

import unittest
from typing import List

class Solution:
    def searchRange(self, nums, target):
        left = self.searchFirstTarget(nums, target)
        right = self.searchLastTarget(nums, target)
        return [left, right]


    def searchFirstTarget(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        
        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                end = mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end

        return -1

    def searchLastTarget(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        
        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
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
        actual = s.searchRange(nums, target)
        expected = [2, 3]
        self.assertEqual(actual, expected)

    def test2(self):
        nums = [1, 2, 3, 4, 4, 6, 7, 8, 9]
        target = 4
        s = Solution()
        actual = s.searchRange(nums, target)
        expected = [3, 4]
        self.assertEqual(actual, expected)

    def test3(self):
        nums = [1, 2, 2, 2, 2, 7, 8, 9]
        target = 2
        s = Solution()
        actual = s.searchRange(nums, target)
        expected = [1, 4]
        self.assertEqual(actual, expected)

    def test4(self):
        nums = [1, 7, 8, 9]
        target = 2
        s = Solution()
        actual = s.searchRange(nums, target)
        expected = [-1, -1]
        self.assertEqual(actual, expected)

    def test5(self):
        nums = []
        target = 2
        s = Solution()
        actual = s.searchRange(nums, target)
        expected = [-1, -1]
        self.assertEqual(actual, expected)

unittest.main(verbosity = 2)

