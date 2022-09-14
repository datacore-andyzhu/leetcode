# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#


# @lc tags=array

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
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = n - 1
        top = 0
        bottom = m - 1

        res = []
        while left <= right and top <= bottom:
            for y in range(left, right+1):
                res.append(matrix[top][y])
            for x in range(top+1, bottom+1):
                res.append(matrix[x][right])
            for y in range(right-1, left-1, -1):
                if bottom > top:
                    res.append(matrix[bottom][y])
            for x in range(bottom-1, top, -1):
                if right > left:
                    res.append(matrix[x][left])
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return res
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('matrix = [[1,2,3],[4,5,6],[7,8,9]]')
    print('Exception :')
    print('[1,2,3,6,9,8,7,4,5]')
    print('Output :')
    print(str(Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]')
    print('Exception :')
    print('[1,2,3,4,8,12,11,10,9,5,6,7]')
    print('Output :')
    print(str(Solution().spiralOrder(
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])))
    print()

    pass
# @lc main=end
