# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#


# @lc tags=array;divide-and-conquer;dynamic-programming

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
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = [None] * len(nums)
        dp[0] = nums[0]
        max_dp = dp[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            max_dp = max(max_dp, dp[i])

        return max_dp

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [-2,1,-3,4,-1,2,1,-5,4]')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().maxSubArray([1])))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [5,4,-1,7,8]')
    print('Exception :')
    print('23')
    print('Output :')
    print(str(Solution().maxSubArray([5, 4, -1, 7, 8])))
    print()

    pass
# @lc main=end
