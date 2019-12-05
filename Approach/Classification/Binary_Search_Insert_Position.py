'''

Binary Search insert position

'''

import unittest
from typing import List

class Solution:
    def binarySearch(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        
        start = 0
        end = len(nums) - 1

        if target <= nums[0]:
            return 0
        if target >= nums[-1]:
            return end
        
        # find the last number less than target
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[end] == target:
            return end
        if nums[end] < target:
            return end + 1
        if nums[start] == target:
            return start

        return start + 1


class Test(unittest.TestCase):
    def test(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        target = 5
        s = Solution()
        actual = s.binarySearch(nums, target)
        expected = 4
        self.assertEqual(actual, expected)

    def test_second(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        target = 9
        s = Solution()
        actual = s.binarySearch(nums, target)
        expected = 8
        self.assertEqual(actual, expected)

    def test_insert_middle(self):
        nums = [1, 3, 4, 8, 9]
        target = 2
        s = Solution()
        actual = s.binarySearch(nums, target)
        expected = 1
        self.assertEqual(actual, expected)

    def test_insert_2(self):
        nums = [1, 2, 3, 4, 7, 8, 9]
        target = 5
        s = Solution()
        actual = s.binarySearch(nums, target)
        expected = 4
        self.assertEqual(actual, expected)

unittest.main(verbosity = 2)

