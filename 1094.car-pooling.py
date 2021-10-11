# @lc app=leetcode id=1094 lang=python3
#
# [1094] Car Pooling
#


# @lc tags=sort

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
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # use the difference array tricks
        # since from the input 0 <= fromi < toi <= 1000
        diff_trips = [0 for _ in range(1001)]
        for i in range(len(trips)):
            # add num of passengers at the start of the trip
            diff_trips[trips[i][1]] += trips[i][0]
            # need to remove same number of passengers when ttip ends
            diff_trips[trips[i][2]] -= trips[i][0]

        current_capacity = 0
        # now let's build up the actual capacuty array along the various trip
        # and see if the value over the input of capacity
        for i in range(len(diff_trips)):
            current_capacity += diff_trips[i]
            if current_capacity > capacity:
                return False
        return True


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('trips = [[2,1,5],[3,3,7]], capacity = 4')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().carPooling([[2, 1, 5], [3, 3, 7]], 4)))
    print()

    print('Example 2:')
    print('Input : ')
    print('trips = [[2,1,5],[3,3,7]], capacity = 5')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().carPooling([[2, 1, 5], [3, 3, 7]], 5)))
    print()

    print('Example 3:')
    print('Input : ')
    print('trips = [[2,1,5],[3,5,7]], capacity = 3')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().carPooling([[2, 1, 5], [3, 5, 7]], 3)))
    print()

    print('Example 4:')
    print('Input : ')
    print('trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().carPooling([[3, 2, 7], [3, 7, 9], [8, 3, 9]], 11)))
    print()

    pass
# @lc main=end
