# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#


# @lc tags=array;dynamic-programming

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
    def maxProduct(self, nums: List[int]) -> int:
        """ Solution 1: DP table """
        # dp_max = [1] * len(nums)
        # dp_min = [1] * len(nums)
        # dp_max[0] = nums[0]
        # dp_min[0] = nums[0]
        # max_result = nums[0]

        # for i in range(1, len(nums)):
        #     dp_max[i] = max(dp_max[i-1]*nums[i], nums[i], dp_min[i-1]*nums[i])
        #     dp_min[i] = min(dp_min[i-1]*nums[i], nums[i], dp_max[i-1]*nums[i])
        #     max_result = max(max_result, dp_max[i], dp_min[i])

        # return max_result

        """ Without the DP table """
        curMax, curMin = 1, 1
        res = nums[0]

        for n in nums:
            vals = (n, n * curMax, n * curMin)
            curMax, curMin = max(vals), min(vals)

            res = max(res, curMax)

        return res
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [2,3,-2,4]')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().maxProduct([2, 3, -2, 4])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [-2,0,-1]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().maxProduct([-2, 0, -1])))
    print()

    pass
# @lc main=end
