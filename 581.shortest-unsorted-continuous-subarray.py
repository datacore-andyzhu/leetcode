# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
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
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        sorted_nums = sorted(nums)
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] == sorted_nums[i]:
                i += 1
            if nums[j] == sorted_nums[j]:
                j -= 1
            if nums[i] != sorted_nums[i] and nums[j] != sorted_nums[j]:
                return j - i + 1

        return 0
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [2,6,4,8,10,9,15]')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,2,3,4]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().findUnsortedSubarray([1, 2, 3, 4])))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [1]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().findUnsortedSubarray([1])))
    print()

    pass
# @lc main=end
