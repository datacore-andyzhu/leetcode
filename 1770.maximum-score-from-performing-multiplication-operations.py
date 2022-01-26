# @lc app=leetcode id=1770 lang=python3
#
# [1770] Maximum Score from Performing Multiplication Operations
#


# @lc tags=Unknown

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
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)
        n = len(nums)

        dp = [[0 for _ in range(m+1)] for _ in range(m+1)]

        for i in range(m-1, -1, -1):
            for left in range(i, -1, -1):
                multiplier = multipliers[i]
                right = n-1-(i-left)
                dp[i][left] = max(multiplier*nums[left]+dp[i+1]
                                  [left+1], multiplier*nums[right]+dp[i+1][left])

        return dp[0][0]
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,2,3], multipliers = [3,2,1]')
    print('Exception :')
    print('14')
    print('Output :')
    print(str(Solution().maximumScore([1, 2, 3], [3, 2, 1])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]')
    print('Exception :')
    print('102')
    print('Output :')
    print(str(Solution().maximumScore(
        [-5, -3, -3, -2, 7, 1], [-10, -5, 3, 4, 6])))
    print()

    pass
# @lc main=end
