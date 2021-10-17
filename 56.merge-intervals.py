# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#


# @lc tags=array;sort

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
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # result = []

        # intervals.sort(key=lambda x: x[0])
        # interval = intervals[0]

        # for item in intervals:
        #     start = interval[0]
        #     end = interval[1]
        #     if end >= item[0]:
        #         start = min(interval[0], item[0])
        #         end = max(item[1], interval[1])
        #         interval = [start, end]
        #     else:
        #         result.append(interval)
        #         interval = item
        # result.append(interval)
        # return result
        intervals.sort(key=lambda x: x[0])
        new_intervals = []
        if len(intervals) == 1:
            return intervals
        for i in range(len(intervals)-1):
            [a, b] = intervals[i]
            [c, d] = intervals[i+1]
            if (b >= c):
                intervals[i+1] = [min(a, c), max(b, d)]
                new_intervals.append([min(a, c), max(b, d)])
            else:
                new_intervals.append([a, b])
                new_intervals.append([c, d])
        return new_intervals

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('intervals = [[1,3],[2,6],[8,10],[15,18]]')
    print('Exception :')
    print('[[1,6],[8,10],[15,18]]')
    print('Output :')
    print(str(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('intervals = [[1,4],[4,5]]')
    print('Exception :')
    print('[[1,5]]')
    print('Output :')
    print(str(Solution().merge([[1, 4], [4, 5]])))
    print()

    pass
# @lc main=end
