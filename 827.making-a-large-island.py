# @lc app=leetcode id=827 lang=python3
#
# [827] Making A Large Island
#


# @lc tags=string

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
    def largestIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid, x, y, index):
            m = len(grid)
            n = len(grid[0])

            if x < 0 or x >= m or y < 0 or y >= n:
                return 0
            if grid[x][y] == 0 or grid[x][y] == index:
                return 0

            grid[x][y] = index
            return 1 + dfs(grid, x+1, y, index) + dfs(grid, x-1, y, index) \
                + dfs(grid, x, y+1, index) + dfs(grid, x, y-1, index)

        area = {}
        index = 2
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area[index] = dfs(grid, i, j, index)
                    index += 1

        ans = max(area.values() or [0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = set()
                    if i+1 < m and grid[i+1][j] > 1:
                        seen.add(grid[i+1][j])
                    if i-1 >= 0 and grid[i-1][j] > 1:
                        seen.add(grid[i-1][j])
                    if j+1 < n and grid[i][j+1] > 1:
                        seen.add(grid[i][j+1])
                    if j - 1 >= 0 and grid[i][j-1] > 1:
                        seen.add(grid[i][j-1])

                    ans = max(ans, 1+sum(area[i] for i in seen))
        return ans
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('grid = [[1,0],[0,1]]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().largestIsland([[1, 0], [0, 1]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('grid = [[1,1],[1,0]]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().largestIsland([[1, 1], [1, 0]])))
    print()

    print('Example 3:')
    print('Input : ')
    print('grid = [[1,1],[1,1]]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().largestIsland([[1, 1], [1, 1]])))
    print()

    pass
# @lc main=end
