'''

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        
        m = len(matrix)
        n = len(matrix[0])
        res = []
        up = 0
        down = m - 1
        left = 0
        right = n - 1
        while True:
            for j in range(left, right + 1):
                res.append(matrix[up][j])
            up += 1
            if up > down:
                break
                
            for i in range(up, down + 1):
                res.append(matrix[i][right])
            right -= 1
            if right < left:
                break
                
            for j in range(right, left - 1, -1):
                res.append(matrix[down][j])
            down -= 1
            if down < up:
                break
                
            for i in range(down, up - 1, -1):
                res.append(matrix[i][left])
            left += 1
            if left > right:
                break
                
        return res

        

