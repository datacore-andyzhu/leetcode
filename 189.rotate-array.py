# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
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
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        def reverse(nums, left, right):
            while left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            return nums
        if k > n:
            k = k % n

        nums = reverse(nums, 0, n-1)
        nums = reverse(nums, 0, k-1)
        nums = reverse(nums, k, n-1)

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,2,3,4,5,6,7], k = 3')
    print('Exception :')
    print('[5,6,7,1,2,3,4]')
    print('Output :')
    print(str(Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3)))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [-1,-100,3,99], k = 2')
    print('Exception :')
    print('[3,99,-1,-100]')
    print('Output :')
    print(str(Solution().rotate([-1, -100, 3, 99], 2)))
    print()

    pass
# @lc main=end
