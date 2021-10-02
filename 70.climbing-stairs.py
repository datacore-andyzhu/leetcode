# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#


# @lc tags=dynamic-programming

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
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
        dp = [None] * (n+1)
        
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]




# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 2')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().climbStairs(2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 3')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().climbStairs(3)))
    print()

    pass
# @lc main=end
