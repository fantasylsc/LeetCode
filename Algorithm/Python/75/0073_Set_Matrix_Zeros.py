'''

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        rowZero = False
        colZero = False
        
        if row == 0 and col == 0:
            return
        
        # record zero col and zero row status
        for i in range(row):
            if matrix[i][0] == 0:
                colZero = True
        for j in range(col):
            if matrix[0][j] == 0:
                rowZero = True
        
        # save matrix status into the zero col and zero row
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
                    
        # update matrix status according to zero col and zero row
        for i in range(1, row):
            for j in range(1, col):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
                    
        # update zero col and zero row according to colZero and rowZero
        if rowZero:
            for j in range(col):
                matrix[0][j] = 0
        if colZero:
            for i in range(row):
                matrix[i][0] = 0    
            
        

