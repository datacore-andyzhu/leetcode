# @lc app=leetcode id=1091 lang=python3
#
# [1091] Shortest Path in Binary Matrix
#


# @lc tags=Unknown

# @lc imports=start
import collections
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
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] != 0:
            return -1
        queue = collections.deque([])
        queue.append((0, 0))
        step = 1
        direction_vector = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1)
        ]
        grid[0][0] = 1
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                _row, _col = queue.popleft()
                # grid[_row][_col] = 1
                if (_row, _col) == (n-1, n-1):
                    return step
                # grid[_row][_col] = 1
                for x, y in direction_vector:
                    new_row = _row + x
                    new_col = _col + y
                    if 0 <= new_row < n and 0 <= new_col < n and grid[new_row][new_col] == 0:
                        grid[new_row][new_col] = 1
                        queue.append((new_row, new_col))
            step += 1
            # print(step)
        return -1
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('grid = [[0,1],[1,0]]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().shortestPathBinaryMatrix([[0, 1], [1, 0]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('grid = [[0,0,0],[1,1,0],[1,1,0]]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().shortestPathBinaryMatrix(
        [[0, 0, 0], [1, 1, 0], [1, 1, 0]])))
    print()

    print('Example 3:')
    print('Input : ')
    print('grid = [[1,0,0],[1,1,0],[1,1,0]]')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().shortestPathBinaryMatrix(
        [[1, 0, 0], [1, 1, 0], [1, 1, 0]])))
    print()

    pass
# @lc main=end
