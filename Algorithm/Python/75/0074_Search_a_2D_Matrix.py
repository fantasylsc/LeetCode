'''

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false

'''

# 1. using two binary search
# 2. regard the 2D Matrix as a list, row = idx // n , col = idx % n, n = len(matrix[0])

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if m == 1 and n == 0:
            return False
        
        start, end = 0, n * m - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            mid_val = matrix[mid // n][mid % n]
            if mid_val == target:
                return True
            if mid_val > target:
                end = mid
            else:
                start = mid
        if matrix[start // n][start % n] == target:
            return True
        if matrix[end // n][end % n] == target:
            return True
        return False
        

