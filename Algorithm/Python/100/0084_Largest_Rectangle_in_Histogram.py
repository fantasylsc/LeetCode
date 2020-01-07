'''

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

Example:

Input: [2,1,5,6,2,3]
Output: 10

'''

# using stack

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        res = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[i] < heights[stack[-1]]:
                res = max(res, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)
        while stack[-1] != -1:
            res = max(res, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
        return res

    
# Divide and conquer TLE

'''

max(height[minindex] * (end - start + 1),\
                   self.helper(height, start, minindex - 1),\
                   self.helper(height, minindex + 1, end))

O(nlogn), worst case O(n^2)

'''


# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         return self.helper(heights, 0, len(heights) - 1)
        
#     def helper(self, heights, start, end):
#         if start > end:
#             return 0
#         minindex = start
#         for i in range(start, end + 1):
#             if heights[i] < heights[minindex]:
#                 minindex = i
#         return max(heights[minindex] * (end - start + 1),\
#                    self.helper(heights, start, minindex - 1),\
#                    self.helper(heights, minindex + 1, end))
        
            
        
# Brute force O(n^2) TLE 
# iterate all cases and find min height, calculate area

# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         res = 0
#         for i in range(len(heights)):
#             minheight = heights[i]
#             for j in range(i, len(heights)):
#                 minheight = min(minheight, heights[j])
#                 res = max(res, minheight * (j - i + 1))
#         return res
        
        
        
        



