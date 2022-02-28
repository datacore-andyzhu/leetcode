# @lc app=leetcode id=976 lang=python3
#
# [976] Largest Perimeter Triangle
#


# @lc tags=hash-table

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
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(2, len(nums)):
            if nums[i] + nums[i-1] > nums[i-2]:
                return nums[i] + nums[i-1] + nums[i-2]
        return 0
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [2,1,2]')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().largestPerimeter([2, 1, 2])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,2,1]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().largestPerimeter([1, 2, 1])))
    print()

    pass
# @lc main=end
