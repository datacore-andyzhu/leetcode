# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#


# @lc tags=trie

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
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # n = len(cost)

        # dp = [None] * n

        # # first step has cost, but not the last one
        # dp[0] = cost[0]
        # dp[1] = cost[1]
        # for i in range(2, n):
        #     dp[i] = min(cost[i-1], cost[i-2]) + cost[i]

        # return min(cost[n-1], cost[n-2])

        n = len(cost)
        dp = [None] * (n+1)
        dp[0] = 0
        dp[1] = 0
        # first step cost == 0 ?
        for i in range(2, n+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2] + cost[i-2])
        return dp[n]


# @lc code=end
# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('cost = [10,15,20]')
    print('Exception :')
    print('15')
    print('Output :')
    print(str(Solution().minCostClimbingStairs([10, 15, 20])))
    print()

    print('Example 2:')
    print('Input : ')
    print('cost = [1,100,1,1,1,100,1,1,100,1]')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().minCostClimbingStairs(
        [1, 100, 1, 1, 1, 100, 1, 1, 100, 1])))
    print()

    pass
# @lc main=end
