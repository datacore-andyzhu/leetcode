# @lc app=leetcode id=980 lang=python3
#
# [980] Unique Paths III
#


# @lc tags=dynamic-programming

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
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        sr, sc = 0, 0
        er, ec = 0, 0
        steps = 0
        self.res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    sr, sc = i, j
                if grid[i][j] == 2:
                    er, ec = i, j
                if grid[i][j] != -1:
                    steps += 1

        def dfs(r, c, steps):
            steps -= 1
            if r == er and c == ec:
                if steps == 0:
                    self.res += 1
                return
            grid[r][c] = -1
            for nr, nc in [(r-1, c), (r, c+1), (r+1, c), (r, c-1)]:
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != -1:
                    dfs(nr, nc, steps)
            grid[r][c] = 0

        dfs(sr, sc, steps)
        return self.res
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,2]])))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('grid = [[0,1],[2,0]]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().uniquePathsIII([[0,1],[2,0]])))
    print()
    
    pass
# @lc main=end
