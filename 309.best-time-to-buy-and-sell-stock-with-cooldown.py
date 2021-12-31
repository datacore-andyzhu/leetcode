# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
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
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        dp = [[0 for _ in range(4)] for _ in range(n)]
        dp[0][0] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], max(dp[i-1][1] -
                           prices[i], dp[i-1][3]-prices[i]))
            dp[i][1] = max(dp[i-1][1], dp[i-1][3])
            dp[i][2] = dp[i-1][0] + prices[i]
            dp[i][3] = dp[i-1][2]

        return max(dp[n-1][3], dp[n-1][2], dp[n-1][1])
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('prices = [1,2,3,0,2]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().maxProfit([1,2,3,0,2])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('prices = [1]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().maxProfit([1])))
    print()
    
    pass
# @lc main=end
