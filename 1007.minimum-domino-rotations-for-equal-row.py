# @lc app=leetcode id=1007 lang=python3
#
# [1007] Minimum Domino Rotations For Equal Row
#


# @lc tags=dynamic-programming

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
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(x):
            rotationA = rotationB = 0
            for i in range(len(tops)):
                if tops[i] != x and bottoms[i] != x:
                    return -1
                elif tops[i] != x:
                    rotationA += 1
                elif bottoms[i] != x:
                    rotationB += 1
            return min(rotationA, rotationB)
        n = len(tops)
        rotation = check(tops[0])
        if rotation != -1 or tops[0] == bottoms[0]:
            return rotation
        else:
            return check(bottoms[0])

        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().minDominoRotations(
        [2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2])))
    print()

    print('Example 2:')
    print('Input : ')
    print('tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().minDominoRotations([3, 5, 1, 2, 3], [3, 6, 3, 3, 4])))
    print()

    pass
# @lc main=end
