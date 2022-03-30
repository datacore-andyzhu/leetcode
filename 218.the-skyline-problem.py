# @lc app=leetcode id=218 lang=python3
#
# [218] The Skyline Problem
#


# @lc tags=divide-and-conquer;heap;binary-indexed-tree;segment-tree;line-sweep

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
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        heights = []
        for building in buildings:
            heights.append((building[0], building[2]))
            heights.append((building[1], -building[2]))

        heights.sort(key=lambda x: (x[0], -x[1]))
        # print(heights)
        pq = []
        res = []
        heapq.heappush(pq, 0)
        preMax = 0
        for height in heights:
            if height[1] < 0:
                pq.remove(height[1])
                heapq.heapify(pq)
            else:
                heapq.heappush(pq, -height[1])
            currMax = -pq[0]
            if preMax != currMax:
                res.append([height[0], currMax])
                preMax = currMax
        return res
        """ Solution 2 """
        points = []
        for start, end, height in buildings:
            points.append([start, -height, end])
            points.append([end, 0, 0])
            # points.append([r, h, 0])
        points.sort()

        res = [[0, 0]]
        # height composed of height and end x coordinate
        heights = [[0, float("inf")]]
        heapq.heapify(heights)

        for start, _height, end in points:
            while start >= heights[0][1]:
                heapq.heappop(heights)

            if _height < 0:
                heapq.heappush(heights, [_height, end])

            if res[-1][1] != -heights[0][0]:
                res.append([start, -heights[0][0]])
        return res[1:]
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]')
    print('Exception :')
    print('[[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]')
    print('Output :')
    print(str(Solution().getSkyline(
        [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('buildings = [[0,2,3],[2,5,3]]')
    print('Exception :')
    print('[[0,3],[5,0]]')
    print('Output :')
    print(str(Solution().getSkyline([[0, 2, 3], [2, 5, 3]])))
    print()

    pass
# @lc main=end
