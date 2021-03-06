# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
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
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def binarySearch(nums, low, high, target):
            
            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1
            return -1
        return binarySearch(nums, 0, n-1, target)

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [-1,0,3,5,9,12], target = 9')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().search([-1, 0, 3, 5, 9, 12], 9)))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [-1,0,3,5,9,12], target = 2')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().search([-1, 0, 3, 5, 9, 12], 2)))
    print()

    pass
# @lc main=end
