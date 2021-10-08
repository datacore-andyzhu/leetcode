# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
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
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        -use slow and fast pointer, when fast pointer points to a number that
        -is not 0, assign that value to the slow pointer 
        -then move the slow pointer, 
        -other wise do not do anything with slow pointer
        -but in both cases, we need to move the fast pointer
        -also do not forget to zero out rest of list to 0
        """
        slow = 0
        fast = 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        while slow < len(nums):
            nums[slow] = 0
            slow += 1

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [0,1,0,3,12]')
    print('Exception :')
    print('[1,3,12,0,0]')
    print('Output :')
    print(str(Solution().moveZeroes([0, 1, 0, 3, 12])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [0]')
    print('Exception :')
    print('[0]')
    print('Output :')
    print(str(Solution().moveZeroes([0])))
    print()

    pass
# @lc main=end
