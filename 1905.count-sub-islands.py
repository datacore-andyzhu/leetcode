# @lc app=leetcode id=1905 lang=python3
#
# [1905] Count Sub Islands
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
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
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

        m = len(grid1)
        n = len(grid1[0])

        for i in range(m):
            for j in range(n):
                if grid1[i][j] == 0 and grid2[i][j] == 1:
                    # grid1 is not island but grid2 is island
                    # we need to clear out those islands in grid2
                    dfs(grid2, i, j)

        result = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    result += 1
                    dfs(grid2, i, j)

        return result
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]],grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().countSubIslands([[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]],[[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]],grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().countSubIslands([[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]],[[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]])))
    print()
    
    pass
# @lc main=end
