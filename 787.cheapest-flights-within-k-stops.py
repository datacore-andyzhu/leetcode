# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#


# @lc tags=breadth-first-search

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
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if src == dst:
            return 0
        previous = [float('inf')] * n
        current = [float('inf')] * n
        previous[src] = 0

        for i in range(k+1):
            current[src] = 0
            for flight in flights:
                prev_flight, curr_flight, cost = flight
                if previous[prev_flight] < float('inf'):
                    current[curr_flight] = min(
                        current[curr_flight], previous[prev_flight]+cost)
            previous = current.copy()

        return current[dst] if current[dst] < float('inf') else -1
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        'n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k= 1')
    print('Exception :')
    print('200')
    print('Output :')
    print(str(Solution().findCheapestPrice(
        3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1)))
    print()

    print('Example 2:')
    print('Input : ')
    print(
        'n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k= 0')
    print('Exception :')
    print('500')
    print('Output :')
    print(str(Solution().findCheapestPrice(
        3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0)))
    print()

    pass
# @lc main=end
