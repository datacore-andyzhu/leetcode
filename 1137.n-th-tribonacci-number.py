# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#


# @lc tags=array

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
    def tribonacci(self, n: int) -> int:
        dp = [0] * 38
        if n == 0:
            return 0
        if n == 2 or n == 1:
            return 1
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

        return dp[n]
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 4')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().tribonacci(4)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 25')
    print('Exception :')
    print('1389537')
    print('Output :')
    print(str(Solution().tribonacci(25)))
    print()

    pass
# @lc main=end
