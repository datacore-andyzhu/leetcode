# @lc app=leetcode id=1284 lang=python3
#
# [1284] Minimum Number of Flips to Convert Binary Matrix to Zero Matrix
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
    def minFlips(self, mat: List[List[int]]) -> int:

        def flip(x, y):

            direction_vector = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]
            for _x, _y in direction_vector:
                if 0 <= x+_x < len(mat) and 0 <= y+_y < len(mat[0]):
                    mat[x+_x][y+_y] ^= 1

        def allzero():
            return sum(sum(row) for row in mat) == 0

        self.res = float('+inf')

        def helper(pos, moves):
            if allzero():
                self.res = min(self.res, moves)
                return
            if not pos:
                return
            for i in range(len(pos)):
                x, y = pos[i]
                flip(x, y)
                helper(pos[i+1:], moves+1)
                flip(x, y)  # -> backtrack

        pos = [(x, y) for x in range(len(mat)) for y in range(len(mat[0]))]
        helper(pos, 0)
        return self.res if self.res != float('+inf') else -1

        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('mat = [[0,0],[0,1]]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().minFlips([[0, 0], [0, 1]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('mat = [[0]]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().minFlips([[0]])))
    print()

    print('Example 3:')
    print('Input : ')
    print('mat = [[1,0,0],[1,0,0]]')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().minFlips([[1, 0, 0], [1, 0, 0]])))
    print()

    pass
# @lc main=end
