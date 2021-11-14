# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
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
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        start = 0
        end = len(nums) - 1
        if nums[start] < nums[end]:
            return nums[0]
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[start]:
                start = mid + 1
            else:
                end = mid - 1
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [3,4,5,1,2]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().findMin([3, 4, 5, 1, 2])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [4,5,6,7,0,1,2]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().findMin([4, 5, 6, 7, 0, 1, 2])))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [11,13,15,17]')
    print('Exception :')
    print('11')
    print('Output :')
    print(str(Solution().findMin([11, 13, 15, 17])))
    print()

    pass
# @lc main=end
