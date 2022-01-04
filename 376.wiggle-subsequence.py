# @lc app=leetcode id=376 lang=python3
#
# [376] Wiggle Subsequence
#


# @lc tags=dynamic-programming;greedy

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
    def wiggleMaxLength(self, nums: List[int]) -> int:
        """ Solution 1: Greedy algorithm """
#         if len(nums) < 2:
#             return len(nums)

#         prevDiff = nums[1] - nums[0]
#         count = 2 if prevDiff !=0 else 1

#         for i in range(2, len(nums)):
#             diff = nums[i] - nums[i-1]
#             if (diff > 0 and prevDiff <=0) or (diff < 0 and prevDiff >= 0):
#                 count += 1
#                 prevDiff = diff

#         return count
        """ Solution 2: DP """
        n = len(nums)
        if n < 2:
            return n
        dp_up = [0] * n
        dp_down = [0] * n
        dp_up[0] = dp_down[0] = 1
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                dp_up[i] = dp_down[i-1] + 1
                dp_down[i] = dp_down[i-1]
            elif nums[i] < nums[i-1]:
                dp_up[i] = dp_up[i-1]
                dp_down[i] = dp_up[i-1] + 1
            else:
                dp_up[i] = dp_up[i-1]
                dp_down[i] = dp_down[i-1]
        return max(dp_up[-1], dp_down[-1])
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,7,4,9,2,5]')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().wiggleMaxLength([1, 7, 4, 9, 2, 5])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,17,5,10,13,15,10,5,16,8]')
    print('Exception :')
    print('7')
    print('Output :')
    print(str(Solution().wiggleMaxLength(
        [1, 17, 5, 10, 13, 15, 10, 5, 16, 8])))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [1,2,3,4,5,6,7,8,9]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().wiggleMaxLength([1, 2, 3, 4, 5, 6, 7, 8, 9])))
    print()

    pass
# @lc main=end
