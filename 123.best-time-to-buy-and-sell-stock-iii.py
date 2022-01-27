# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
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
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        dp = [[0 for _ in range(5)] for _ in range(n)]
        dp[0][1] = -prices[0]
        dp[0][3] = -prices[0]
        for i in range(1, n):
            dp[i][0] = dp[i-1][0]
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i])
            dp[i][3] = max(dp[i-1][3], dp[i-1][2] - prices[i])
            dp[i][4] = max(dp[i-1][4], dp[i-1][3] + prices[i])

        return dp[n-1][4]

        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('prices = [3,3,5,0,0,3,1,4]')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().maxProfit([3, 3, 5, 0, 0, 3, 1, 4])))
    print()

    print('Example 2:')
    print('Input : ')
    print('prices = [1,2,3,4,5]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().maxProfit([1, 2, 3, 4, 5])))
    print()

    print('Example 3:')
    print('Input : ')
    print('prices = [7,6,4,3,1]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().maxProfit([7, 6, 4, 3, 1])))
    print()

    pass
# @lc main=end
