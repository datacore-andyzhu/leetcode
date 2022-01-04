# @lc app=leetcode id=1289 lang=python3
#
# [1289] Minimum Falling Path Sum II
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
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        # n = len(grid)
        # first_sum, first_pos, second_sum = 0, -1, 0
        # for i in range(n):
        #     fs, fp, ss = 10**9, -1, 10**9
        #     for j in range(n):
        #         cur_sum = (first_sum if first_pos !=
        #                    j else second_sum) + grid[i][j]
        #         if cur_sum < fs:
        #             fs, fp, ss = cur_sum, j, fs
        #         elif cur_sum < ss:
        #             ss = cur_sum
        #     first_sum, first_pos, second_sum = fs, fp, ss
        # return first_sum
        n = len(grid)

        dp = [[0 for _ in range(n)] for _ in range(n)]

        for j in range(n):
            dp[0][j] = grid[0][j]

        for i in range(1, n):
            for j in range(n):
                dp[i][j] = grid[i][j] + min(dp[i-1][y]
                                            for y in range(n) if y != j)
        return min(dp[n-1])

        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('arr = [[1,2,3],[4,5,6],[7,8,9]]')
    print('Exception :')
    print('13')
    print('Output :')
    print(str(Solution().minFallingPathSum(error)))
    print()

    print('Example 2:')
    print('Input : ')
    print('grid = [[7]]')
    print('Exception :')
    print('7')
    print('Output :')
    print(str(Solution().minFallingPathSum([[7]])))
    print()

    pass
# @lc main=end
