# @lc app=leetcode id=790 lang=python3
#
# [790] Domino and Tromino Tiling
#


# @lc tags=array;math

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
    def numTilings(self, n: int) -> int:
        mod = 10**9 + 7
        if n <= 2:
            return n
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5
        for i in range(4, n+1):
            dp[i] = (2*dp[i-1] + dp[i-3]) % mod
        return dp[n]
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 3')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().numTilings(3)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('n = 1')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().numTilings(1)))
    print()
    
    pass
# @lc main=end
