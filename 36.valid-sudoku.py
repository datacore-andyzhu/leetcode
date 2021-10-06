# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#


# @lc tags=hash-table

# @lc imports=start
import collections
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
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # # verify each role does not violate the rule
        # for i in range(9):
        #     counts = {}
        #     row = board[i]
        #     for j in row:
        #         if j <= '9' and j > '0':
        #             if counts.get(j, 0) == 1:
        #                 return False
        #             else:
        #                 counts[j] = 1
        # for i in range(9):
        #     counts = {}
        #     col = [sub[i] for sub in board]
        #     for j in col:
        #         if j <= '9' and j > '0':
        #             if counts.get(j, 0) == 1:
        #                 return False
        #             else:
        #                 counts[j] = 1
        # i = 0
        # j = 0
        # for i in range(0, 9, 3):
        #     for j in range(0, 9, 3):
        #         counts = {}
        #         for k in range(3):
        #             for l in range(3):
        #                 if board[i+k][j+l] != '.':
        #                     if counts.get(board[i+k][j+l], 0) == 1:
        #                         return False
        #                     else:
        #                         counts[board[i+k][j+l]] = 1

        # return True
        counts = {}
        for i in range(9):
            for j in range(9):
                number = board[i][j]
                if number != '.':
                    if (number+'-row-'+str(i)) in counts \
                        or (number+'-col-'+str(j)) in counts \
                        or (number+'-box-'+str(i//3)+'and'+str(j//3)) in counts:
                        return False
                    else:
                        counts[number+'-row-'+str(i)] = 1
                        counts[number+'-col-'+str(j)] = 1
                        counts[number+'-box-'+str(i//3)+'and'+str(j//3)] = 1

        return True
                    

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('board =[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], [
          "4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('board =[["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isValidSudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], [
          "4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]])))
    print()

    pass
# @lc main=end
