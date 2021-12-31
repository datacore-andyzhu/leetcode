# @lc app=leetcode id=918 lang=python3
#
# [918] Maximum Sum Circular Subarray
#


# @lc tags=heap

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
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def dp(nums):
            n = len(nums)
            dp = [0] * n
            dp[0] = nums[0]
            max_ans = nums[0]
            for i in range(n):
                dp[i] = max(dp[i-1] + nums[i], nums[i])
                max_ans = max(max_ans, dp[i])
            return max_ans

        S = sum(nums)
        if len(nums) == 1:
            return S
        ans1 = dp(nums)
        ans2 = S + dp([-nums[i] for i in range(1, len(nums))])
        ans3 = S + dp([-nums[i] for i in range(len(nums)-1)])

        return max(ans1, ans2, ans3)
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,-2,3,-2]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().maxSubarraySumCircular([1, -2, 3, -2])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [5,-3,5]')
    print('Exception :')
    print('10')
    print('Output :')
    print(str(Solution().maxSubarraySumCircular([5, -3, 5])))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [-3,-2,-3]')
    print('Exception :')
    print('-2')
    print('Output :')
    print(str(Solution().maxSubarraySumCircular([-3, -2, -3])))
    print()

    pass
# @lc main=end
