# @lc app=leetcode id=1568 lang=python3
#
# [1568] Minimum Number of Days to Disconnect Island
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


class UnionFind:
    def __init__(self, n, size):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
        self.size = size

    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)
        if parentX != parentY:
            if self.rank[parentX] > self.rank[parentY]:
                self.parent[parentY] = parentX
            elif self.rank[parentX] < self.rank[parentY]:
                self.parent[parentX] = parentY
            else:
                self.parent[parentY] = parentX
                self.rank[parentX] += 1
            self.size -= 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)
        
class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        """ Solution 1 """
        # def dfs(grid, row, col):
        #     m = len(grid)
        #     n = len(grid[0])
        #     grid[row][col] = 2
        #     for tx, ty in [(row, col+1), (row, col-1), (row+1, col), (row-1, col)]:
        #         if 0 <= tx < m and 0 <= ty < n and grid[tx][ty] == 1:
        #             dfs(grid, tx, ty)

        # def count(grid):
        #     m = len(grid)
        #     n = len(grid[0])
        #     cnt = 0
        #     for i in range(m):
        #         for j in range(n):
        #             if grid[i][j] == 1:
        #                 cnt += 1
        #                 dfs(grid, i, j)

        #     # restore so the count can be called multiple times
        #     # when we try fill the land with water
        #     for i in range(m):
        #         for j in range(n):
        #             if grid[i][j] == 2:
        #                 grid[i][j] = 1
        #     return cnt
        # if count(grid) != 1:
        #     return 0
        # m = len(grid)
        # n = len(grid[0])
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == 1:
        #             grid[i][j] = 0
        #             if count(grid) != 1:
        #                 return 1
        #             grid[i][j] = 1
        # return 2
        
        """Solution 2: Using union find """
        """ This solution is actually much slower """

        # add UnionClass above

        def count(grid):
            m = len(grid)
            n = len(grid[0])

            ones = 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        ones += 1

            uf = UnionFind(m*n, ones)
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        for tx, ty in directions:
                            new_x = i + tx
                            new_y = j + ty
                            if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == 1:
                                uf.union(i*n+j, new_x*n+new_y)
            return uf.size

        m = len(grid)
        n = len(grid[0])

        if count(grid) != 1:
            return 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if count(grid) != 1:
                        return 1
                    grid[i][j] = 1
        return 2
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().minDays([[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('grid = [[1,1]]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().minDays([[1, 1]])))
    print()

    pass
# @lc main=end
