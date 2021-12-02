# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
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
        def robber(nums):
            # print(nums)
            if len(nums) == 1:
                return nums[0]
            dp = [-1] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            return dp[len(nums)-1]
        if len(nums) == 1:
            return nums[0]
        option1 = robber(nums[:-1])
        option2 = robber(nums[1:])
        return max(option1, option2)
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [2,3,2]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().rob([2, 3, 2])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,2,3,1]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().rob([1, 2, 3, 1])))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [1,2,3]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().rob([1, 2, 3])))
    print()

    pass
# @lc main=end
