# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
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
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [float('inf')]*(amount + 1)
        dp[0] = 0
        for i in range(len(coins)):
            for j in range(coins[i], amount+1):
                dp[j] = min(dp[j], dp[j-coins[i]]+1)

        return dp[amount] if dp[amount] != float('inf') else -1
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('coins = [1,2,5], amount = 11')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().coinChange([1, 2, 5], 11)))
    print()

    print('Example 2:')
    print('Input : ')
    print('coins = [2], amount = 3')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().coinChange([2], 3)))
    print()

    print('Example 3:')
    print('Input : ')
    print('coins = [1], amount = 0')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().coinChange([1], 0)))
    print()

    print('Example 4:')
    print('Input : ')
    print('coins = [1], amount = 1')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().coinChange([1], 1)))
    print()

    print('Example 5:')
    print('Input : ')
    print('coins = [1], amount = 2')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().coinChange([1], 2)))
    print()

    pass
# @lc main=end
