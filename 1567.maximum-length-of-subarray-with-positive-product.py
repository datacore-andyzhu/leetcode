# @lc app=leetcode id=1567 lang=python3
#
# [1567] Maximum Length of Subarray With Positive Product
#


# @lc tags=Unknown

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
    def getMaxLen(self, nums: List[int]) -> int:
        positives = [0] * len(nums)
        negatives = [0] * len(nums)

        if nums[0] > 0:
            positives[0] = 1
        elif nums[0] < 0:
            negatives[0] = 1
        max_length = positives[0]

        for i in range(1, len(nums)):
            if nums[i] > 0:
                positives[i] = positives[i-1] + 1

                if negatives[i-1] != 0:
                    negatives[i] = negatives[i-1] + 1
                elif negatives[i-1] == 0:
                    negatives[i] = 0
            elif nums[i] < 0:
                negatives[i] = positives[i-1] + 1

                if negatives[i-1] != 0:
                    positives[i] = negatives[i-1] + 1
                elif negatives[i-1] == 0:
                    positives[i] = 0
            else:
                positives[i] = 0
                negatives[i] = 0

            max_length = max(max_length, positives[i])
        return max_length
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,-2,-3,4]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().getMaxLen([1, -2, -3, 4])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [0,1,-2,-3,-4]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().getMaxLen([0, 1, -2, -3, -4])))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [-1,-2,-3,0,1]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().getMaxLen([-1, -2, -3, 0, 1])))
    print()

    pass
# @lc main=end
