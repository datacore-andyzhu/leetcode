# @lc app=leetcode id=1779 lang=python3
#
# [1779] Find Nearest Point That Has the Same X or Y Coordinate
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
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_dist = float('inf')
        min_idx = float('inf')
        for i, point in enumerate(points):
            if point[0] == x or point[1] == y:
                dist = abs(point[0]-x) + abs(point[1]-y)
                if dist < min_dist:
                    min_dist = dist
                    min_idx = i
        return min_idx if min_idx != float('inf') else -1
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().nearestValidPoint(
        3, 4, [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('x = 3, y = 4, points = [[3,4]]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().nearestValidPoint(3, 4, [[3, 4]])))
    print()

    print('Example 3:')
    print('Input : ')
    print('x = 3, y = 4, points = [[2,3]]')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().nearestValidPoint(3, 4, [[2, 3]])))
    print()

    pass
# @lc main=end
