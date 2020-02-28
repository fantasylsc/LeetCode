'''

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49

'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0
        current_water = 0
        
        while left != right:
            current_water = (right - left) * min(height[right], height[left])
            if current_water > max_water:
                max_water = current_water
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
        return max_water




