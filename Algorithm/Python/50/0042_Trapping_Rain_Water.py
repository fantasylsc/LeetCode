'''

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

'''

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0] * n
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i - 1])
        
        right_max = [0] * n
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i + 1])
        
        res = 0
        for i in range(n):
            min_rl = min(left_max[i], right_max[i])
            if min_rl > height[i]:
                res += min_rl - height[i]
                
        return res




