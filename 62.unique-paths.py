# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#


# @lc tags=array;dynamic-programming

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
    def uniquePaths(self, m: int, n: int) -> int:
        # use DP to solve this issue
        # any path to the corder is the sum of path from left and the path from top
        # dp = [[None]*n] * m
        # # initialize number of path cross the first row
        # for i in range(n):
        #     dp[0][i] = 1
        # # initialize number of path cross the fist column
        # for i in range(m):
        #     dp[i][0] = 1
        # for i in range(1, m):
        #     for j in range(1, n):
        #         dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # return dp[m-1][n-1]

        # method 2
        # use a rolling array/list
        # first time, every number in the row has value of 1
        dp = [1] * n
        # 2nd row, start at position 1 (2nd number), add current number to the previous number,
        # you would get a increasing number, 1, 2, 3, ...
        # for 3rd row continue as it is, , but you would get 1,3, 6, 10, etc
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        return dp[n-1]

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('m = 3, n = 7')
    print('Exception :')
    print('28')
    print('Output :')
    print(str(Solution().uniquePaths(3, 7)))
    print()

    print('Example 2:')
    print('Input : ')
    print('m = 3, n = 2')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().uniquePaths(3, 2)))
    print()

    print('Example 3:')
    print('Input : ')
    print('m = 7, n = 3')
    print('Exception :')
    print('28')
    print('Output :')
    print(str(Solution().uniquePaths(7, 3)))
    print()

    print('Example 4:')
    print('Input : ')
    print('m = 3, n = 3')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().uniquePaths(3, 3)))
    print()

    pass
# @lc main=end
