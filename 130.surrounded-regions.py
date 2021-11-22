# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#


# @lc tags=depth-first-search;breadth-first-search;union-find

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
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(board, row, col, m, n):
            direction_vector = [
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1)
            ]

            stack = []

            stack.append((row, col))
            while stack:
                _row, _col = stack.pop()
                if board[_row][_col] == 'O':
                    board[_row][_col] = 'E'
                for x, y in direction_vector:
                    new_row = _row + x
                    new_col = _col + y
                    if 0 <= new_row < m and 0 <= new_col < n and board[new_row][new_col] == 'O':
                        board[new_row][new_col] = 'E'
                        stack.append((new_row, new_col))
        m = len(board)
        n = len(board[0])
        # we use DFS mark the edge 'O' to something else instead 
        # of like other graph problem of mark tehe one we really wants 
        # so we do not need to flip to x later
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i == 0 or i == m-1 or j == 0 or j == n-1):
                    dfs(board, i, j, m, n)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'E':
                    board[i][j] = 'O'

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        'board =[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]')
    print('Exception :')
    print('[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]')
    print('Output :')
    print(str(Solution().solve([["X", "X", "X", "X"], [
          "X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('board = [["X"]]')
    print('Exception :')
    print('[["X"]]')
    print('Output :')
    print(str(Solution().solve([["X"]])))
    print()

    pass
# @lc main=end
