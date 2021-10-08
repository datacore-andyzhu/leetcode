# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
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
    def removeElement(self, nums: List[int], val: int) -> int:

        fast = 0
        slow = 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1

            fast += 1
        # need to pay attention where the slow pointer at
        return slow


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [3,2,2,3], val = 3')
    print('Exception :')
    print('2, nums = [2,2,_,_]')
    print('Output :')
    print(str(Solution().removeElement([3, 2, 2, 3], 3)))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [0,1,2,2,3,0,4,2], val = 2')
    print('Exception :')
    print('5, nums = [0,1,4,0,3,_,_,_]')
    print('Output :')
    print(str(Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)))
    print()

    pass
# @lc main=end
