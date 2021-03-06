# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#


# @lc tags=hash-table;backtracking

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
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isVaid(board, row, col, num, n):
            for i in range(n):
                if board[i][col] == num:
                    return False
            for j in range(n):
                if board[row][j] == num:
                    return False
            grid_row = (row // 3) * 3
            grid_col = (col // 3) * 3
            for i in range(0, 3):
                for j in range(0, 3):
                    if board[grid_row+i][grid_col+j] == num:
                        return False
            return True

        def backtrack(board, n):
            for i in range(n):
                for j in range(n):
                    if board[i][j] == '.':
                        for num in range(1, 10):
                            if isVaid(board, i, j, str(num), n):
                                board[i][j] = str(num)
                                if backtrack(board, n):
                                    return True
                                board[i][j] = '.'
                        return False
            return True
        n = len(board)
        backtrack(board, n)

        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('board =[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]')
    print('Exception :')
    print('[["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]')
    print('Output :')
    print(str(Solution().solveSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], [
          "4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]])))
    print()

    pass
# @lc main=end
