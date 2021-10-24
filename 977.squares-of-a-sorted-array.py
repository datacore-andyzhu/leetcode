# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#


# @lc tags=dynamic-programming

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
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        if len(nums) == 1:
            return [nums[0]**2]
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        position = n - 1
        while left <= right:
            if nums[left]**2 < nums[right]**2:
                result[position] = nums[right]**2
                right -= 1
                position -= 1
            else:
                result[position] = nums[left]**2
                left += 1
                position -= 1
      
        return result
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [-4,-1,0,3,10]')
    print('Exception :')
    print('[0,1,9,16,100]')
    print('Output :')
    print(str(Solution().sortedSquares([-4, -1, 0, 3, 10])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [-7,-3,2,3,11]')
    print('Exception :')
    print('[4,9,9,49,121]')
    print('Output :')
    print(str(Solution().sortedSquares([-7, -3, 2, 3, 11])))
    print()

    pass
# @lc main=end
