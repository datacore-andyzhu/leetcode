# @lc app=leetcode id=1162 lang=python3
#
# [1162] As Far from Land as Possible
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
    def maxDistance(self, grid: List[List[int]]) -> int:
        # use mutli-source BFS
        INF = float('inf')
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        n = len(grid)
        dist = [[INF for _ in range(n)] for _ in range(n)]
        queue = collections.deque()

        # set the land's position in Distance table as 0
        # and append the land's position into queue as multi-source
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    queue.append((i, j))

        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                x, y = queue.popleft()
                for i in range(4):
                    new_x = x + dx[i]
                    new_y = y + dy[i]
                    if 0 <= new_x < n and 0 <= new_y < n:
                        if dist[new_x][new_y] > dist[x][y]+1:
                            dist[new_x][new_y] = dist[x][y]+1
                            queue.append((new_x, new_y))
        # go through the distance table
        # find the max cost because when
        # we go through each land cell, the distance from
        # land to ocean is different in regards to each land cell
        ans = -1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    ans = max(ans, dist[i][j])
        return ans if ans < INF else -1
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('grid = [[1,0,1],[0,0,0],[1,0,1]]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().maxDistance([[1,0,1],[0,0,0],[1,0,1]])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('grid = [[1,0,0],[0,0,0],[0,0,0]]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().maxDistance([[1,0,0],[0,0,0],[0,0,0]])))
    print()
    
    pass
# @lc main=end
