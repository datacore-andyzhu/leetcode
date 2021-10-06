# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#


# @lc tags=array;binary-search

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
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        # starting from the top right corner
        # if target is larger then the element, move to the next row
        # if target is small then the element, move to the left column
        j = n - 1
        i = 0
        while i < m and j >= 0:
            if target == matrix[i][j]:
                return True
            if target < matrix[i][j]:
                j -= 1
            if target > matrix[i][j]:
                i += 1
        return False


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().searchMatrix(
        [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)))
    print()

    print('Example 2:')
    print('Input : ')
    print('matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().searchMatrix(
        [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13)))
    print()

    pass
# @lc main=end
