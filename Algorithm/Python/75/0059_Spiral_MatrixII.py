'''

Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

'''

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
     
        matrix = [[0]*n for _ in range(n)]
        up = 0
        down = n - 1
        left = 0
        right = n - 1
        num = 1
        
        while True:
            for j in range(left, right + 1):
                matrix[up][j] = num
                num += 1
            up += 1
            if up > down:
                break
                
            for i in range(up, down + 1):
                matrix[i][right] = num
                num += 1
            right -= 1
            if right < left:
                break
                
            for j in range(right, left - 1, -1):
                matrix[down][j] = num
                num += 1
            down -= 1
            if down < up:
                break
                
            for i in range(down, up - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
            if left > right:
                break
                
        return matrix
        

