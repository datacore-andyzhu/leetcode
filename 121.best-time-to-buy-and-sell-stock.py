# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
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
        # if len(prices) == 1:
        #     return 0
        # min_price = float('inf')
        # max_profit = 0
        # for price in prices:
        #     min_price = min(min_price, price)
        #     max_profit = max(max_profit, price - min_price)
        # return max_profit
        # initialize the DP table, initial the # of columns first, then # of rows
        dp = [[None] * 2] * len(prices)
        # print(dp)
        # dp[i][0] store the cash have left if we purchase stoack at
        # certain prices, but we need to keep the min cash out of poacket
        # becasue buying stock means pay out the cash, so the number is negative
        # get the cheapest price mean the max of negative number
        dp[0][0] = -prices[0]
        # dp[i][1] store if we want to keep the stock or sell the stock at that price
        # the diff is current price + previous day's negative cash value
        # first day, we did not sell any, so it is zero
        dp[0][1] = 0
        # we start the calculation from day 2
        for i in range(1, len(prices)):
            # shall we keep previous day's stock or buy at the new lower price
            dp[i][0] = max(dp[i-1][0], -prices[i])
            # shall we not sell the stock at today's price and keep yesterday's profit?
            dp[i][1] = max(dp[i-1][1], prices[i] + dp[i-1][0])
        # return the max profit
        return dp[i][1]


# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('prices = [7,1,5,3,6,4]')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().maxProfit([7, 1, 5, 3, 6, 4])))
    print()

    print('Example 2:')
    print('Input : ')
    print('prices = [7,6,4,3,1]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().maxProfit([7, 6, 4, 3, 1])))
    print()

    pass
# @lc main=end
