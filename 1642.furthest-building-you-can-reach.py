# @lc app=leetcode id=1642 lang=python3
#
# [1642] Furthest Building You Can Reach
#


# @lc tags=Unknown

# @lc imports=start
from imports import *
import heapq
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
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        buildings = []
        n = len(heights)
        bricksNeeded = 0
        for i in range(1, n):
            if heights[i] > heights[i-1]:
                heapq.heappush(buildings, (heights[i]-heights[i-1]))
                if len(buildings) > ladders:
                    bricksNeeded += heapq.heappop(buildings)

                if bricksNeeded > bricks:
                    return i - 1
        return n-1
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().furthestBuilding([4, 2, 7, 6, 9, 14, 12], 5, 1)))
    print()

    print('Example 2:')
    print('Input : ')
    print('heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2')
    print('Exception :')
    print('7')
    print('Output :')
    print(str(Solution().furthestBuilding(
        [4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2)))
    print()

    print('Example 3:')
    print('Input : ')
    print('heights = [14,3,19,3], bricks = 17, ladders = 0')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().furthestBuilding([14, 3, 19, 3], 17, 0)))
    print()

    pass
# @lc main=end
