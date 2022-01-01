# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#


# @lc tags=math;dynamic-programming;heap

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
    def nthUglyNumber(self, n: int) -> int:
        dp = [1]
        # p2, p3, p5 used to track how many time the 2, 3, 5 factor been used
        p2 = 0
        p3 = 0
        p5 = 0

        for i in range(n+1):
            t2 = dp[p2] * 2
            t3 = dp[p3] * 3
            t5 = dp[p5] * 5

            temp = min(t2, t3, t5)
            dp.append(temp)

            if temp == dp[p2] * 2:
                p2 += 1
            if temp == dp[p3] * 3:
                p3 += 1
            if temp == dp[p5] * 5:
                p5 += 1

        return dp[n-1]
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 10')
    print('Exception :')
    print('12')
    print('Output :')
    print(str(Solution().nthUglyNumber(10)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 1')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().nthUglyNumber(1)))
    print()

    pass
# @lc main=end
