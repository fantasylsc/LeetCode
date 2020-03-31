'''

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4


'''



# DP approach 1
# dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
# dp[i][j] represents the side length of the maximum square whose bottom right corner is the cell with index (i,j) in the original matrix.

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        if rows:
            cols = len(matrix[0])
        else:
            cols = 0
        
        dp = [[0]* cols for _ in range(rows)]
        maxsqlen = 0
        
        for i in range(rows):
            dp[i][0] = int(matrix[i][0])
            if dp[i][0] == 1:
                maxsqlen = 1
            
        for j in range(cols):
            dp[0][j] = int(matrix[0][j])
            if dp[0][j] == 1:
                maxsqlen = 1
        
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                    if dp[i][j] > maxsqlen:
                        maxsqlen = dp[i][j]
        return maxsqlen * maxsqlen

        
# Brute force

# class Solution:
#     def maximalSquare(self, matrix: List[List[str]]) -> int:
#         rows = len(matrix)
#         if rows:
#             cols = len(matrix[0])
#         else:
#             cols = 0
#         max_sqlen = 0
        
#         for i in range(rows):
#             for j in range(cols):
#                 if matrix[i][j] == '1':
#                     sqlen = 1
#                     flag = True
#                     while sqlen + i < rows and sqlen + j < cols and flag:
#                         for k in range(j, j + sqlen + 1):
#                             if matrix[i + sqlen][k] == '0':
#                                 flag = False
#                                 break
#                         for k in range(i, i + sqlen + 1):
#                             if matrix[k][j + sqlen] == '0':
#                                 flag = False
#                                 break
#                         if flag:
#                             sqlen += 1
#                     if max_sqlen < sqlen:
#                         max_sqlen = sqlen
#         return max_sqlen * max_sqlen       
        