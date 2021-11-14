# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
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
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] > nums[mid+1]:
                end = mid
            else:
                start = mid + 1
        return start
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,2,3,1]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().findPeakElement([1,2,3,1])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums = [1,2,1,3,5,6,4]')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().findPeakElement([1,2,1,3,5,6,4])))
    print()
    
    pass
# @lc main=end