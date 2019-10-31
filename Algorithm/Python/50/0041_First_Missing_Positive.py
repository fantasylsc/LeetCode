'''

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1

'''

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while nums[i] > 0 and nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                p1 = i
                p2 = nums[i] - 1
                nums[p1], nums[p2] = nums[p2], nums[p1]
        
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1




