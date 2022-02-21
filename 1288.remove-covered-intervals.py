# @lc app=leetcode id=1288 lang=python3
#
# [1288] Remove Covered Intervals
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
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        n = len(intervals)
        ans, rmax = n, intervals[0][1]

        for i in range(1, n):
            if intervals[i][1] <= rmax:
                ans -= 1
            else:
                rmax = max(rmax, intervals[i][1])
        return ans
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('intervals = [[1,4],[3,6],[2,8]]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().removeCoveredIntervals([[1, 4], [3, 6], [2, 8]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('intervals = [[1,4],[2,3]]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().removeCoveredIntervals([[1, 4], [2, 3]])))
    print()

    pass
# @lc main=end
