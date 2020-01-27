
'''

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

'''
# 1) use list or dic to record status; 2) transform i,j into box_index 

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[0]*9 for _ in range(9)]
        col = [[0]*9 for _ in range(9)]
        box = [[0]*9 for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    box_index = (i // 3)*3 + j//3
                    row[i][num - 1] += 1
                    col[j][num - 1] += 1
                    box[box_index][num - 1] += 1
                    if row[i][num - 1] > 1 or col[j][num - 1] > 1 or box[box_index][num - 1] > 1:
                        return False
        return True
        

# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         # init data
#         rows = [{} for i in range(9)]
#         columns = [{} for i in range(9)]
#         boxes = [{} for i in range(9)]

#         # validate a board
#         for i in range(9):
#             for j in range(9):
#                 num = board[i][j]
#                 if num != '.':
#                     num = int(num)
#                     box_index = (i // 3 ) * 3 + j // 3
                    
#                     # keep the current cell value
#                     rows[i][num] = rows[i].get(num, 0) + 1
#                     columns[j][num] = columns[j].get(num, 0) + 1
#                     boxes[box_index][num] = boxes[box_index].get(num, 0) + 1
                    
#                     # check if this value has been already seen before
#                     if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
#                         return False         
#         return True
        



