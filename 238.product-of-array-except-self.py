# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#


# @lc tags=array

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
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # we will use prefix and suffix array
        prefix = [0] * len(nums)
        prefix[0] = 1
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]

        suffix = [0] * len(nums)
        suffix[len(nums)-1] = 1
        for j in range(len(nums)-2, -1, -1):
            suffix[j] = suffix[j+1] * nums[j+1]
        result = []
        for i in range(len(nums)):
            result.append(prefix[i]*suffix[i])
        return result
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,2,3,4]')
    print('Exception :')
    print('[24,12,8,6]')
    print('Output :')
    print(str(Solution().productExceptSelf([1, 2, 3, 4])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [-1,1,0,-3,3]')
    print('Exception :')
    print('[0,0,9,0,0]')
    print('Output :')
    print(str(Solution().productExceptSelf([-1, 1, 0, -3, 3])))
    print()

    pass
# @lc main=end
