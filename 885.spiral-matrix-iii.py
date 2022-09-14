# @lc app=leetcode id=885 lang=python3
#
# [885] Spiral Matrix III
#


# @lc tags=ordered-map

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
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res = [[rStart, cStart]]
        if rows * cols == 1:
            return res

        # the walk will be in step of 1, 3, 5, ...
        for k in range(1, 2*(rows*cols), 2):
            # direction vector is the shape of (row, col, steps)
            # but in the sequence of east, south, west, north
            # east, south 1 step, then west, north need to be 2 steps
            # then east, south 3 steps, then west, north need to be 4 steps, etc
            for dr, dc, dk in [(0, 1, k), (1, 0, k), (0, -1, k+1), (-1, 0, k+1)]:
                # we need to walk each step
                for _ in range(dk):
                    rStart += dr
                    cStart += dc

                    # if the the walk is in the grid, we need to add to res
                    if 0 <= rStart < rows and 0 <= cStart < cols:
                        res.append([rStart, cStart])
                        # once we walked all the cells in the grid, we need to
                        # break, otherwise, we will walk endlessly
                        if len(res) == rows * cols:
                            return res
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('rows = 1, cols = 4, rStart = 0, cStart = 0')
    print('Exception :')
    print('[[0,0],[0,1],[0,2],[0,3]]')
    print('Output :')
    print(str(Solution().spiralMatrixIII(1, 4, 0, 0)))
    print()

    print('Example 2:')
    print('Input : ')
    print('rows = 5, cols = 6, rStart = 1, cStart = 4')
    print('Exception :')
    print('[[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]')
    print('Output :')
    print(str(Solution().spiralMatrixIII(5, 6, 1, 4)))
    print()

    pass
# @lc main=end
