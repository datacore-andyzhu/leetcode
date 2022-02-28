# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
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
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output = []
        left, right, n = 0, 1, len(nums)

        while right < n:
            while right < n and nums[right]-nums[right-1] == 1:
                right += 1

            if left == right-1:
                output.append(str(nums[left]))
            else:
                output.append(str(nums[left]) + "->" + str(nums[right-1]))

            left = right
            right += 1

        if left < n:
            output.append(str(nums[left]))

        return output
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [0,1,2,4,5,7]')
    print('Exception :')
    print('["0->2","4->5","7"]')
    print('Output :')
    print(str(Solution().summaryRanges([0, 1, 2, 4, 5, 7])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [0,2,3,4,6,8,9]')
    print('Exception :')
    print('["0","2->4","6","8->9"]')
    print('Output :')
    print(str(Solution().summaryRanges([0, 2, 3, 4, 6, 8, 9])))
    print()

    pass
# @lc main=end
