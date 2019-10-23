'''

A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) are the coordinates of its bottom-left corner, and (x2, y2) are the coordinates of its top-right corner.

Two rectangles overlap if the area of their intersection is positive.  To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two (axis-aligned) rectangles, return whether they overlap.

Example 1:

Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true
Example 2:

Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
Output: false

'''

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x_start_max = max(rec1[0], rec2[0])
        x_end_min = min(rec1[2], rec2[2])
        y_start_max = max(rec1[1], rec2[1])
        y_end_min = min(rec1[3], rec2[3])
        
        return (x_start_max < x_end_min) and (y_start_max < y_end_min)




