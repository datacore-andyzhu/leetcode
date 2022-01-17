# @lc app=leetcode id=1254 lang=python3
#
# [1254] Number of Closed Islands
#


# @lc tags=Unknown

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
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid, row, col):
            m = len(grid)
            n = len(grid[0])

            if row < 0 or row >= m or col < 0 or col >= n:
                return
            if grid[row][col] == 1:
                return
            grid[row][col] = 1
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

        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    result += 1
                    dfs(grid, i, j)
        return result
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('grid =[[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().closedIsland([[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [
          1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().closedIsland(
        [[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]])))
    print()

    print('Example 3:')
    print('Input : ')
    print('grid = [[1,1,1,1,1,1,1],[1,0,0,0,0,0,1],[1,0,1,1,1,0,1],[1,0,1,0,1,0,1],[1,0,1,1,1,0,1],[1,0,0,0,0,0,1],⁠              [1,1,1,1,1,1,1]]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().closedIsland([[1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 1], ⁠              [1, 1, 1, 1, 1, 1, 1]])))
    print()

    pass
# @lc main=end
