# @lc app=leetcode id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
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
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        dp = [[0 for _ in range(2*k+1)] for _ in range(len(prices))]
        for j in range(1, 2*k, 2):
            dp[0][j] = -prices[0]

        for i in range(1, len(prices)):
            for j in range(0, 2*k-1, 2):
                dp[i][j+1] = max(dp[i-1][j+1], dp[i-1][j]-prices[i])
                dp[i][j+2] = max(dp[i-1][j+2], dp[i-1][j+1] + prices[i])
        return dp[len(prices)-1][2*k]
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('k = 2, prices = [2,4,1]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().maxProfit(2, [2, 4, 1])))
    print()

    print('Example 2:')
    print('Input : ')
    print('k = 2, prices = [3,2,6,5,0,3]')
    print('Exception :')
    print('7')
    print('Output :')
    print(str(Solution().maxProfit(2, [3, 2, 6, 5, 0, 3])))
    print()

    pass
# @lc main=end
