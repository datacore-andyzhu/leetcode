# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
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
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        slow, fast = 2, 2
        while fast < n:
            if nums[fast] != nums[slow-2]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,1,1,2,2,3]')
    print('Exception :')
    print('5, nums = [1,1,2,2,3,_]')
    print('Output :')
    print(str(Solution().removeDuplicates([1, 1, 1, 2, 2, 3])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [0,0,1,1,1,1,2,3,3]')
    print('Exception :')
    print('7, nums = [0,0,1,1,2,3,3,_,_]')
    print('Output :')
    print(str(Solution().removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3])))
    print()

    pass
# @lc main=end
