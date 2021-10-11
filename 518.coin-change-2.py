# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change 2
#


# @lc tags=Unknown

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
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1
        for i in range(len(coins)):
            for j in range(coins[i], amount+1):
                dp[j] = dp[j] + dp[j-coins[i]]
        return dp[amount]

        
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('amount = 5, coins = [1,2,5]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().change(5,[1,2,5])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('amount = 3, coins = [2]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().change(3,[2])))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('amount = 10, coins = [10]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().change(10,[10])))
    print()
    
    pass
# @lc main=end