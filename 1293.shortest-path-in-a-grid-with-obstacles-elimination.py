# @lc app=leetcode id=1293 lang=python3
#
# [1293] Shortest Path in a Grid with Obstacles Elimination
#


# @lc tags=Unknown

# @lc imports=start
from imports import *
import collections
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
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        direction_vector = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows = len(grid)
        cols = len(grid[0])

        target = (rows-1, cols-1)
        if k >= rows + cols - 2:
            return rows+cols-2
        # state vatable to store x,y coord and remaining
        # obstacles
        state = (0, 0, k)
        # queue store distance from origin and state
        queue = collections.deque([(0, state)])

        # visited set to store the coordinates and num of obstacles left
        visited = set()
        visited.add(state)

        while queue:
            steps, (row, col, k) = queue.popleft()
            if (row, col) == target:
                return steps

            for _x, _y in direction_vector:
                new_row = row + _x
                new_col = col + _y
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    # depend the new_row, new_col,
                    # grid[new_row][new_col] coule be 1 or 0
                    new_elimination = k - grid[new_row][new_col]
                    new_state = (new_row, new_col, new_elimination)
                    if new_elimination >= 0 and new_state not in visited:
                        visited.add(new_state)
                        queue.append((steps+1, new_state))
        return -1
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().shortestPath(
        [[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]], 1)))
    print()

    print('Example 2:')
    print('Input : ')
    print('grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().shortestPath([[0, 1, 1], [1, 1, 1], [1, 0, 0]], 1)))
    print()

    pass
# @lc main=end
