# @lc app=leetcode id=714 lang=python3
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#


# @lc tags=array;dynamic-programming;greedy

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
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [[0 for _ in range(2)] for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]-prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i]-fee)
        return dp[len(prices)-1][1]
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('prices = [1,3,2,8,4,9], fee = 2')
    print('Exception :')
    print('8')
    print('Output :')
    print(str(Solution().maxProfit([1, 3, 2, 8, 4, 9], 2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('prices = [1,3,7,5,10,3], fee = 3')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().maxProfit([1, 3, 7, 5, 10, 3], 3)))
    print()

    pass
# @lc main=end
