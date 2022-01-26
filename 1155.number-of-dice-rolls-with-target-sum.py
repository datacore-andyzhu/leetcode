# @lc app=leetcode id=1155 lang=python3
#
# [1155] Number of Dice Rolls With Target Sum
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
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10**9 + 7
        dp = [[0 for _ in range(target+1)] for _ in range(n+1)]

        dp[0][0] = 1
        for i in range(1, n+1):
            for j in range(1, target+1):
                for dice_value in range(1, k+1):
                    if j >= dice_value:
                        dp[i][j] = (dp[i][j] + dp[i-1][j-dice_value]) % mod

        return dp[n][target]
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 1, k = 6, target = 3')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().numRollsToTarget(1, 6, 3)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 2, k = 6, target = 7')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().numRollsToTarget(2, 6, 7)))
    print()

    print('Example 3:')
    print('Input : ')
    print('n = 30, k = 30, target = 500')
    print('Exception :')
    print('222616187')
    print('Output :')
    print(str(Solution().numRollsToTarget(30, 30, 500)))
    print()

    pass
# @lc main=end
