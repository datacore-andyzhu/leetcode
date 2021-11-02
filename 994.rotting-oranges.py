# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
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
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        total = 0
        visited = [[False for _ in range(n)] for _ in range(m)]
        direction_vector = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = collections.deque([])
        fresh_num = 0
        # let's build up the rotten queue and count the number of fresh oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    fresh_num += 1
        while queue and fresh_num != 0:
            level_size = len(queue)
            for _ in range(level_size):
                rotten_x, rotten_y = queue.popleft()
                for dir_x, dir_y in direction_vector:
                    new_x = rotten_x + dir_x
                    new_y = rotten_y + dir_y
                    if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n or grid[new_x][new_y] != 1:
                        continue
                    grid[new_x][new_y] = 2
                    queue.append((new_x, new_y))
                    fresh_num -= 1
            total += 1
        return total if fresh_num == 0 else -1

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('grid = [[2,1,1],[1,1,0],[0,1,1]]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('grid = [[2,1,1],[0,1,1],[1,0,1]]')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]])))
    print()

    print('Example 3:')
    print('Input : ')
    print('grid = [[0,2]]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().orangesRotting([[0, 2]])))
    print()

    pass
# @lc main=end
