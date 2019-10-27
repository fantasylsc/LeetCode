'''

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3

'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])
        island = 0
        
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == '1':
                    island += 1
                    self.dfs(grid, i, j)
                    
        return island
    
    def dfs(self, grid, r, c):
        nr = len(grid)
        nc = len(grid[0])
        
        grid[r][c] = '0'
        if r - 1 >= 0 and grid[r - 1][c] == '1':
            self.dfs(grid, r - 1, c)
        if r + 1 <= nr - 1 and grid[r + 1][c] == '1':
            self.dfs(grid, r + 1, c)
        if c - 1 >= 0 and grid[r][c - 1] == '1':
            self.dfs(grid, r, c - 1)
        if c + 1 <= nc - 1 and grid[r][c + 1] == '1':
            self.dfs(grid, r, c + 1)




