# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#


# @lc tags=array;greedy

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
    def canJump(self, nums: List[int]) -> bool:
        """ Solution 1: Using DP """
        # can = [False] * len(nums)
        # can[0] = True
        # for i in range(1, len(nums)):
        #     for j in range(i):
        #         if can[j] == True and nums[j] + j >= i:
        #             can[i] = True
        #             break
        # return can[len(nums)-1]
        """ Solution 2: Greedy Algorithm"""
        if not nums or len(nums) == 0:
            return False
        cover = 0
        i = 0
        while i <= cover:
            cover = max(cover, i+nums[i])
            if cover >= (len(nums) - 1):
                return True
            i += 1
        return False
        # cover = nums[0] + 0
        # for i in range(1, len(nums)):
        #     if i < cover and nums[i] + i > cover:
        #         cover = nums[i] + i
        # return True if cover >= (len(nums)-1) else False
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [2,3,1,1,4]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().canJump([2, 3, 1, 1, 4])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [3,2,1,0,4]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().canJump([3, 2, 1, 0, 4])))
    print()

    pass
# @lc main=end
