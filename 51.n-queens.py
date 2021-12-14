# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#


# @lc tags=backtracking

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
# 
# 
# 
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def isValid(row, col, chessBoard, n):
            # column has no Queen
            for i in range(row):
                if chessBoard[i][col] == 'Q':
                    return False
            # upper left corner
            new_row = row - 1
            new_col = col - 1
            while new_row >= 0 and new_col >= 0:
                if chessBoard[new_row][new_col] == 'Q':
                    return False
                new_row -= 1
                new_col -= 1
            # check upper right corner
            new_row = row - 1
            new_col = col + 1
            while new_row >= 0 and new_col < n:
                if chessBoard[new_row][new_col] == 'Q':
                    return False
                new_row -= 1
                new_col += 1
            return True
        def backtrack(row, chessBoard, n):
            # when the row is out of bound, meaning we have processed all
            # the rows
            if row == n:
                temp_res = []
                for temp in chessBoard:
                    temp_str = ''.join(temp)
                    temp_res.append(temp_str)
                result.append(temp_res)
            for col in range(n):
                if isValid(row, col, chessBoard, n):
                    chessBoard[row][col] = 'Q'
                    backtrack(row+1, chessBoard, n)
                    chessBoard[row][col] = '.'
        chessBoard = [['.' for _ in range(n)] for _ in range(n)]
        result = []
        backtrack(0, chessBoard, n)
        
        return result
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 4')
    print('Exception :')
    print('[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]')
    print('Output :')
    print(str(Solution().solveNQueens(4)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('n = 1')
    print('Exception :')
    print('[["Q"]]')
    print('Output :')
    print(str(Solution().solveNQueens(1)))
    print()
    
    pass
# @lc main=end
