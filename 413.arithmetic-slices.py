# @lc app=leetcode id=413 lang=python3
#
# [413] Arithmetic Slices
#


# @lc tags=math;dynamic-programming

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
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        dp = [0] * len(nums)
        ans = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp[i] = dp[i-1] + 1
            ans += dp[i]
        return ans
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,2,3,4]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().numberOfArithmeticSlices([1, 2, 3, 4])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().numberOfArithmeticSlices([1])))
    print()

    pass
# @lc main=end
