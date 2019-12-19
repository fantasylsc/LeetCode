'''

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.

'''

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        n = len(nums)
        i = 0
        reach = 0
        
        while reach < n - 1:
            jumps += 1
            pre = reach
            while i <= pre: # iterate through i to reach, find next reach range
                reach = max(reach, i + nums[i])
                i += 1
        return jumps




