# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#


# @lc tags=tree;depth-first-search

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
    # this function returns number
    # of days a ship with capacity 'capacity'
    # to ship all the weights
    def fx(self, weights, capacity):
        # days = 1
        # sum_weight = capacity
        # for i in range(len(weights)):
        #     if weights[i] > sum_weight:
        #         days += 1
        #         sum_weight = capacity
        #     sum_weight -= weights[i]
        # return days
        # days = 1
        # sum_weight = 0
        # for i in range(len(weights)):
        #     # sum_weight += weights[i]
        #     if sum_weight + weights[i] <= capacity:
        #         sum_weight += weights[i]
        #     else:
        #         days += 1
        #         sum_weight = weights[i]

        # return days
        days = 1
        sum_weight = 0
        for i in range(len(weights)):
            sum_weight += weights[i]
            if sum_weight <= capacity:
                continue
            else:
                days += 1
                sum_weight = weights[i]

        return days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = 0
        right = 1
        for w in weights:
            left = max(left, w)
            right += w
        while left < right:
            mid = left + (right-left)//2
            if self.fx(weights, mid) == days:
                right = mid
            elif self.fx(weights, mid) < days:
                right = mid
            elif self.fx(weights, mid) > days:
                left = mid + 1
        return left

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('weights = [1,2,3,4,5,6,7,8,9,10], days = 5')
    print('Exception :')
    print('15')
    print('Output :')
    print(str(Solution().shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)))
    print()

    print('Example 2:')
    print('Input : ')
    print('weights = [3,2,2,4,1,4], days = 3')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().shipWithinDays([3, 2, 2, 4, 1, 4], 3)))
    print()

    print('Example 3:')
    print('Input : ')
    print('weights = [1,2,3,1,1], days = 4')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().shipWithinDays([1, 2, 3, 1, 1], 4)))
    print()

    pass
# @lc main=end
