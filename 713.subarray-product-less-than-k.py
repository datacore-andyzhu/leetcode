# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#


# @lc tags=array;two-pointers

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
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        result = 0
        product = 1
        left = 0
        right = 0
        if min(nums) >= k:
            return 0
        while right < len(nums):
            product *= nums[right]
            while product >= k:
                product //= nums[left]
                left += 1

            result += right - left + 1
            right += 1
        return result
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [10,5,2,6], k = 100')
    print('Exception :')
    print('8')
    print('Output :')
    print(str(Solution().numSubarrayProductLessThanK([10, 5, 2, 6], 100)))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,2,3], k = 0')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().numSubarrayProductLessThanK([1, 2, 3], 0)))
    print()

    pass
# @lc main=end
