# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#


# @lc tags=tree

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
    def fib(self, n: int) -> int:
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1
        # a = 0
        # b = 1
        # for i in range(2, n+1):
        #     a, b = b, a + b

        # return b
        if n == 0:
            return 0
        if n == 1:
            return 1
        dp = [None] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]


# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 2')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().fib(2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 3')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().fib(3)))
    print()

    print('Example 3:')
    print('Input : ')
    print('n = 4')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().fib(4)))
    print()

    pass
# @lc main=end
