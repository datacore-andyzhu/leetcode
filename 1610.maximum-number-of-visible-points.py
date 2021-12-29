# @lc app=leetcode id=1610 lang=python3
#
# [1610] Maximum Number of Visible Points
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
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        samePoints = 0
        degrees = []
        for p in points:
            if p == location:
                samePoints += 1
            else:
                degrees.append(atan2(p[1]-location[1], p[0]-location[0]))
        degrees.sort()
        n = len(degrees)
        degrees += [deg + 2*pi for deg in degrees]

        maxCount = 0
        right = 0
        degree = angle * pi / 180
        for i in range(n):
            while right < n*2 and degrees[right] <= degrees[i]+degree:
                right += 1
            maxCount = max(maxCount, right - i)
        return samePoints + maxCount
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('points = [[2,1],[2,2],[3,3]], angle = 90, location = [1,1]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().visiblePoints([[2, 1], [2, 2], [3, 3]], 90, [1, 1])))
    print()

    print('Example 2:')
    print('Input : ')
    print('points = [[2,1],[2,2],[3,4],[1,1]], angle = 90, location = [1,1]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().visiblePoints(
        [[2, 1], [2, 2], [3, 4], [1, 1]], 90, [1, 1])))
    print()

    print('Example 3:')
    print('Input : ')
    print('points = [[1,0],[2,1]], angle = 13, location = [1,1]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().visiblePoints([[1, 0], [2, 1]], 13, [1, 1])))
    print()

    pass
# @lc main=end
