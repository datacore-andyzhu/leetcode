# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
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
    def increasingTriplet(self, nums: List[int]) -> bool:
        current_min = float("inf")
        # Track the smallest a, b so we would always find c (a < b < c) if it exists
        best_twin = []
        for num in nums:
            if len(best_twin) == 2 and num > best_twin[-1]:
                return True  # Found triplet
            if num <= current_min:
                current_min = num
            else:
                # current_min < num <= best_twin[-1], so we update best_twin
                best_twin = [current_min, num]

        return False

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,2,3,4,5]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().increasingTriplet([1, 2, 3, 4, 5])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [5,4,3,2,1]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().increasingTriplet([5, 4, 3, 2, 1])))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [2,1,5,0,4,6]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().increasingTriplet([2, 1, 5, 0, 4, 6])))
    print()

    pass
# @lc main=end
