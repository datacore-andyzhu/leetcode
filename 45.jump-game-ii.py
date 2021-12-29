# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
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
    def jump(self, nums: List[int]) -> int:
        """ Solution 1: DP """
        # minJump = [0] * len(nums)
        # minJump[0] = 0
        # for i in range(1, len(nums)):
        #     for j in range(i):
        #         if nums[j] + j >= i:
        #             minJump[i] = minJump[j] + 1
        #             break
        # return minJump[len(nums)-1]
        """ Solution 2: Greedy Algorithm"""

        end = 0
        steps = 0
        maxReach = 0
        for i in range(len(nums)-1):
            maxReach = max(maxReach, nums[i]+i)
            if i == end:
                end = maxReach
                steps += 1
        return steps
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [2,3,1,1,4]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().jump([2, 3, 1, 1, 4])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [2,3,0,1,4]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().jump([2, 3, 0, 1, 4])))
    print()

    pass
# @lc main=end
