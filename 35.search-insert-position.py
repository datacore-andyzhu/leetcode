# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#


# @lc tags=array;binary-search

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
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
        return low


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,3,5,6], target = 5')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().searchInsert([1, 3, 5, 6], 5)))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,3,5,6], target = 2')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().searchInsert([1, 3, 5, 6], 2)))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [1,3,5,6], target = 7')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().searchInsert([1, 3, 5, 6], 7)))
    print()

    print('Example 4:')
    print('Input : ')
    print('nums = [1,3,5,6], target = 0')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().searchInsert([1, 3, 5, 6], 0)))
    print()

    print('Example 5:')
    print('Input : ')
    print('nums = [1], target = 0')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().searchInsert([1], 0)))
    print()

    pass
# @lc main=end
