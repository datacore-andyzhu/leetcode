# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#


# @lc tags=array;greedy

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
        """ SOlution 1: DP """
        dp = [[0 for _ in range(2)] for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]-prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i])
        return dp[len(prices)-1][1]

        """ SOlution 2: Greedy """
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        return res
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('prices = [7,1,5,3,6,4]')
    print('Exception :')
    print('7')
    print('Output :')
    print(str(Solution().maxProfit([7,1,5,3,6,4])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('prices = [1,2,3,4,5]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().maxProfit([1,2,3,4,5])))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('prices = [7,6,4,3,1]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().maxProfit([7,6,4,3,1])))
    print()
    
    pass
# @lc main=end
