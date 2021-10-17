# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#


# @lc tags=greedy

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
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], x[1]))
        count = 0
        base = intervals[0]
        for i in range(1, len(intervals)):
            start = base[0]
            end = base[1]
            if end <= intervals[i][0]:
                base = intervals[i]
            else:
                # if the base's end time larger then the one 
                # in the list, we need to only keep the one with end
                # time is smaller to reduce the chance of overlapping 
                # later
                if end > intervals[i][1]:
                    base = intervals[i]
                count += 1
        return count


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('intervals = [[1,2],[2,3],[3,4],[1,3]]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().eraseOverlapIntervals(
        [[1, 2], [2, 3], [3, 4], [1, 3]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('intervals = [[1,2],[1,2],[1,2]]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]])))
    print()

    print('Example 3:')
    print('Input : ')
    print('intervals = [[1,2],[2,3]]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().eraseOverlapIntervals([[1, 2], [2, 3]])))
    print()

    pass
# @lc main=end
