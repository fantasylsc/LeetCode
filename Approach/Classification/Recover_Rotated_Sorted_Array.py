'''
Description
Given a rotated sorted array, recover it to sorted array in-place.（Ascending）


Clarification

What is rotated array?

    For example, the orginal array is [1,2,3,4], The rotated array of it can be [1,2,3,4], [2,3,4,1], [3,4,1,2], [4,1,2,3]

Example

Example1:
[4, 5, 1, 2, 3] -> [1, 2, 3, 4, 5]
Example2:
[6,8,9,1,2] -> [1,2,6,8,9]
Challenge

In-place, O(1) extra space and O(n) time.


'''

class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        n = len(nums)
        if n <= 1:
            return
        if n == 2:
            if nums[0] <= nums[1]:
                return
            else:
                nums[0], nums[1] = nums[1], nums[0]
                return
        
        pos = -1
        for i in range(1, n - 2):
            if nums[i] > nums[i + 1]:
                pos = i
                break
        
        if pos == -1:
            return 
        else:
            self.reverse(nums, 0, i)
            self.reverse(nums, i + 1, n - 1)
            self.reverse(nums, 0, n - 1)
            return
        
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

        
