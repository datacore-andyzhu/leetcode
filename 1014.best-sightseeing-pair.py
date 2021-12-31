# @lc app=leetcode id=1014 lang=python3
#
# [1014] Best Sightseeing Pair
#


# @lc tags=divide-and-conquer;heap;sort

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
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        """ Solution 1: DP no DP table"""
        # prev_max = values[0] + 0
        # ans = 0
        # for i in range(1, len(values)):
        #     ans = max(ans, prev_max+values[i]-i)
        #     prev_max = max(prev_max, values[i]+i)
        # return ans

        """ DP with DP table """
        dp = [0] * len(values)
        dp[0] = values[0] 
        ans = 0
        for j in range(1, len(values)):
            dp[j] = max(dp[j-1], values[j]+j)
            ans = max(ans, dp[j-1]+values[j]-j)
        return ans
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('values = [8,1,5,2,6]')
    print('Exception :')
    print('11')
    print('Output :')
    print(str(Solution().maxScoreSightseeingPair([8,1,5,2,6])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('values = [1,2]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().maxScoreSightseeingPair([1,2])))
    print()
    
    pass
# @lc main=end
