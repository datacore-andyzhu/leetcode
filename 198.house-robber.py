# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
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
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [-1] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        # when in transition table, either rob the previous one
        # or rob the current one plus the one before the previous one
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], (dp[i-2] + nums[i]))

        return dp[len(nums)-1]


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,2,3,1]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().rob([1, 2, 3, 1])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [2,7,9,3,1]')
    print('Exception :')
    print('12')
    print('Output :')
    print(str(Solution().rob([2, 7, 9, 3, 1])))
    print()

    pass
# @lc main=end
