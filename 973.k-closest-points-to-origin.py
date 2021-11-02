# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#


# @lc tags=string;greedy

# @lc imports=start
from imports import *
from heapq import *
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
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        myheap = [] * k
        for i in range(k):
            distance = -points[i][0]**2 - points[i][1]**2
            heappush(myheap, (distance, points[i]))
        for j in range(k, len(points)):
            distance = -points[j][0]**2 - points[j][1]**2
            # need to remember here is larger, not less
            # because of the negative number
            if distance > myheap[0][0]:
                heappop(myheap)
                heappush(myheap, (distance, points[j]))
        result = []
        while myheap:
            distance, point = heappop(myheap)
            result.append([point[0], point[1]])
        return result


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('points = [[1,3],[-2,2]], k = 1')
    print('Exception :')
    print('[[-2,2]]')
    print('Output :')
    print(str(Solution().kClosest([[1, 3], [-2, 2]], 1)))
    print()

    print('Example 2:')
    print('Input : ')
    print('points = [[3,3],[5,-1],[-2,4]], k = 2')
    print('Exception :')
    print('[[3,3],[-2,4]]')
    print('Output :')
    print(str(Solution().kClosest([[3, 3], [5, -1], [-2, 4]], 2)))
    print()

    pass
# @lc main=end
