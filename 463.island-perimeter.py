# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#


# @lc tags=hash-table

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
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def dfs(grid, x, y):
            m = len(grid)
            n = len(grid[0])
            if x < 0 or x >= m or y < 0 or y >= n:
                return 1
            if grid[x][y] == 0:
                return 1
            if grid[x][y] == 2:
                return 0
            grid[x][y] = 2
            return dfs(grid, x+1, y) + dfs(grid, x-1, y) + dfs(grid, x, y+1) + dfs(grid, x, y-1)

        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return dfs(grid, i, j)

        return 0
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]')
    print('Exception :')
    print('16')
    print('Output :')
    print(str(Solution().islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('grid = [[1]]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().islandPerimeter([[1]])))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('grid = [[1,0]]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().islandPerimeter([[1,0]])))
    print()
    
    pass
# @lc main=end
