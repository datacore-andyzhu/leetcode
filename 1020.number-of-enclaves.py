# @lc app=leetcode id=1020 lang=python3
#
# [1020] Number of Enclaves
#


# @lc tags=array;dynamic-programming;sliding-window

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
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(grid, row, col):
            m = len(grid)
            n = len(grid[0])

            if row < 0 or row >= m or col < 0 or col >= n:
                return
            if grid[row][col] == 0:
                return

            grid[row][col] = 0

            dfs(grid, row+1, col)
            dfs(grid, row-1, col)
            dfs(grid, row, col+1)
            dfs(grid, row, col-1)

        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            dfs(grid, i, 0)
            dfs(grid, i, n-1)

        for j in range(n):
            dfs(grid, 0, j)
            dfs(grid, m-1, j)

        cells = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cells += 1

        return cells
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().numEnclaves(
        [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().numEnclaves(
        [[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]])))
    print()

    pass
# @lc main=end
