'''

Binary Search Template

Search target in nums, return the index of the target in the list

Actually this method return the first value that larger or equal than the target

Explanation about binary search:
https://www.zhihu.com/question/36132386

'''

# This method return the first value that larger or equal than the target
# Difference with NineChapter template: 
# left < right vs. left + 1 < right
# if nums[mid] == target: left or right = mid
# when loop is finished, if nums[left] == target or if nums[right] == target, return left or right or -1


import unittest
from typing import List

class Solution:
    def binarySearch(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if nums[left] == target:
            return left
        else:
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

unittest.main(verbosity = 2)

