# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#


# @lc tags=dynamic-programming;depth-first-search

# @lc imports=start
from functools import lru_cache
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
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """ recursive with memo """
        # @lru_cache(None)
        # def recurse(curr, idx):
        #     # reached the end of array. Moment of truth.
        #     # Has the pattern yielded the target?
        #     if idx == len(nums):
        #         return 1 if curr == target else 0

        #     return recurse(curr - nums[idx], idx + 1) + recurse(curr + nums[idx], idx + 1)

        # return recurse(0, 0)
        """ DP solution with 0/1 knapsack """
        sumValue = sum(nums)
        if abs(target) > sumValue or (target+sumValue) % 2 == 1:
            return 0
        bagSize = (target + sumValue) // 2
        dp = [0] * (bagSize + 1)
        dp[0] = 1
        for i in range(len(nums)):
            for j in range(bagSize, nums[i]-1, -1):
                dp[j] += dp[j-nums[i]]
        return dp[bagSize]

        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,1,1,1,1], target = 3')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3)))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1], target = 1')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().findTargetSumWays([1], 1)))
    print()

    pass
# @lc main=end
