# @lc app=leetcode id=343 lang=python3
#
# [343] Integer Break
#


# @lc tags=math;dynamic-programming

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
    def integerBreak(self, n: int) -> int:
        """ Solution 1: DP """
        # dp = [1 for _ in range(n+1)]
        # for i in range(3, n+1):
        #     for j in range(1, i):
        #         dp[i] = max(dp[i], max(j*(i-j), j*dp[i-j]))
        # return dp[n]

        """ Solution 2: Pure Math """
        if n == 2: return 1
        if n == 3: return 2
        if n == 4: return 4
        result = 1
        while n > 4:
            result *= 3
            n -= 3
        result *= n
        return result
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 2')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().integerBreak(2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 10')
    print('Exception :')
    print('36')
    print('Output :')
    print(str(Solution().integerBreak(10)))
    print()

    pass
# @lc main=end
