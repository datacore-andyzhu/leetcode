# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#


# @lc tags=array;depth-first-search

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
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid, x, y, m, n):
            if x < 0 or x >= m or y < 0 or y >= n:
                return 0
            if grid[x][y] == 0:
                return 0
            grid[x][y] = 0

            return dfs(grid, x+1, y, m, n) + dfs(grid, x-1, y, m, n) + dfs(grid, x, y+1, m, n) + dfs(grid, x, y-1, m, n) + 1

        m = len(grid)
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, dfs(grid, i, j, m, n))
        return res
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('grid =[[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [
          0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('grid = [[0,0,0,0,0,0,0,0]]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().maxAreaOfIsland([[0, 0, 0, 0, 0, 0, 0, 0]])))
    print()

    pass
# @lc main=end
