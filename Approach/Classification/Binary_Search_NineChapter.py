'''

Binary Search Template in NineChapter
Thie template can be widely used in a lot of cases.
This binary search template can be used in find the first or last target in the list. Example: [1,2,2,2,2,3,3,4]

'''

import unittest
from typing import List

class Solution:
    def binarySearch(self, nums: List[int], target: int) -> int:
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

    def test_get_first_target_in_list(self):
        nums = [1, 2, 2, 2, 2, 7, 8, 9]
        target = 2
        s = Solution()
        actual = s.binarySearch(nums, target)
        expected = 1
        self.assertEqual(actual, expected)

    # def test_get_last_target_in_list(self):
    #     nums = [1, 2, 2, 2, 2, 7, 8, 9]
    #     target = 2
    #     s = Solution()
    #     actual = s.binarySearch(nums, target)
    #     expected = 4
    #     self.assertEqual(actual, expected)

unittest.main(verbosity = 2)

