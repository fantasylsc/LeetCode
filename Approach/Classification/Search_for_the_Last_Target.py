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
    def SearchFirstTarget(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        
        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid

        if nums[end] == target:
            return end
        if nums[start] == target:
            return start

        return -1

# solution 2:
# class Solution:
# 	def SearchFirstTarget(self, nums, target):
# 		left = 0
# 		right = len(nums) - 1

# 		while left < right:
# 			mid = left + (right - left)//2
# 			if nums[mid] < target:
# 				left = mid + 1
# 			elif nums[mid] > target:
# 				right = mid
# 			else:
# 				if mid == len(nums) - 1:
# 					return mid
# 				elif nums[mid + 1] == target:
# 					left = mid + 1
# 				else:
# 					return mid

# 		if nums[left] == target:
# 			return left
# 		else:
# 			return -1


class Test(unittest.TestCase):
    def test1(self):
        nums = [1, 2, 3, 3, 8, 9]
        target = 3
        s = Solution()
        actual = s.SearchFirstTarget(nums, target)
        expected = 3
        self.assertEqual(actual, expected)

    def test2(self):
        nums = [1, 2, 3, 4, 4, 6, 7, 8, 9]
        target = 4
        s = Solution()
        actual = s.SearchFirstTarget(nums, target)
        expected = 4
        self.assertEqual(actual, expected)

    def test3(self):
        nums = [1, 2, 2, 2, 2, 7, 8, 9]
        target = 2
        s = Solution()
        actual = s.SearchFirstTarget(nums, target)
        expected = 4
        self.assertEqual(actual, expected)

    def test4(self):
        nums = [1, 7, 8, 9]
        target = 2
        s = Solution()
        actual = s.SearchFirstTarget(nums, target)
        expected = -1
        self.assertEqual(actual, expected)
    def test5(self):
        nums = [1, 2]
        target = 1
        s = Solution()
        actual = s.SearchFirstTarget(nums, target)
        expected = 0
        self.assertEqual(actual, expected)

unittest.main(verbosity = 2)

