# @lc app=leetcode id=986 lang=python3
#
# [986] Interval List Intersections
#


# @lc tags=math

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
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """ Solution 1 """
        # result = []
        # if len(firstList) == 0 or len(secondList) == 0:
        #     return result
        # thirdList = firstList + secondList
        # thirdList.sort(key=lambda x: (x[0], x[1]))
        # # print(thirdList)
        # base = thirdList[0]
        # for i in range(1, len(thirdList)):
        #     if thirdList[i][0] <= base[0] or thirdList[i][0] <= base[1]:
        #         base_start = max(base[0], thirdList[i][0])
        #         base_end = min(base[1], thirdList[i][1])
        #         result.append([base_start, base_end])
        #     # to select the next base, we need to make sure the base
        #     # has the widest range
        #     if thirdList[i][1] > base[1]:
        #         base = thirdList[i]
        # return result
        """ Solution 2: without actual merge the list """
        ans = []
        i = j = 0

        while i < len(firstList) and j < len(secondList):
            # Let's check if A[i] intersects B[j].
            # lo - the startpoint of the intersection
            # hi - the endpoint of the intersection
            lo = max(firstList[i][0], secondList[j][0])
            hi = min(firstList[i][1], secondList[j][1])
            if lo <= hi:
                ans.append([lo, hi])

            # Remove the interval with the smallest endpoint
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return ans
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        'firstList = [[0,2],[5,10],[13,23],[24,25]], secondList =[[1,5],[8,12],[15,24],[25,26]]')
    print('Exception :')
    print('[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]')
    print('Output :')
    print(str(Solution().intervalIntersection(
        [[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('firstList = [[1,3],[5,9]], secondList = []')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().intervalIntersection([[1, 3], [5, 9]], [])))
    print()

    print('Example 3:')
    print('Input : ')
    print('firstList = [], secondList = [[4,8],[10,12]]')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().intervalIntersection([], [[4, 8], [10, 12]])))
    print()

    print('Example 4:')
    print('Input : ')
    print('firstList = [[1,7]], secondList = [[3,10]]')
    print('Exception :')
    print('[[3,7]]')
    print('Output :')
    print(str(Solution().intervalIntersection([[1, 7]], [[3, 10]])))
    print()

    pass
# @lc main=end
