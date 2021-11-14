# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
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
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if target == nums[mid]:
                return mid
            # to see if after rotation, the left side is bigger than the right side or not
            if nums[start] <= nums[mid]:
                if nums[mid] > target >= nums[start]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1

        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [4,5,6,7,0,1,2], target = 0')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().search([4, 5, 6, 7, 0, 1, 2], 0)))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [4,5,6,7,0,1,2], target = 3')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().search([4, 5, 6, 7, 0, 1, 2], 3)))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [1], target = 0')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().search([1], 0)))
    print()

    pass
# @lc main=end
