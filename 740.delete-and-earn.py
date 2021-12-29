# @lc app=leetcode id=740 lang=python3
#
# [740] Delete and Earn
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
    def deleteAndEarn(self, nums: List[int]) -> int:
        val = [0] * 10001

        m = 0
        for i in nums:
            m = max(m, i)
            val[i] += i

        dp = [0] * (m+1)
        dp[0] = 0
        dp[1] = val[1]

        for i in range(2, m+1):
            dp[i] = max(val[i] + dp[i-2], dp[i-1])

        return dp[m]
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [3,4,2]')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().deleteAndEarn([3,4,2])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums = [2,2,3,3,3,4]')
    print('Exception :')
    print('9')
    print('Output :')
    print(str(Solution().deleteAndEarn([2,2,3,3,3,4])))
    print()
    
    pass
# @lc main=end
