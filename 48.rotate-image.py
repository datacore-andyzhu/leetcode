# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
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
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # use the linear algebra reverse and transpose
        def reverse(matrix):
            l = 0
            r = len(matrix) - 1
            while l < r:
                matrix[l], matrix[r] = matrix[r], matrix[l]
                l += 1
                r -= 1

        def transpose(matrix):
            for i in range(len(matrix)):
                for j in range(i):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        reverse(matrix)
        transpose(matrix)

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('matrix = [[1,2,3],[4,5,6],[7,8,9]]')
    print('Exception :')
    print('[[7,4,1],[8,5,2],[9,6,3]]')
    print('Output :')
    print(str(Solution().rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]')
    print('Exception :')
    print('[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]')
    print('Output :')
    print(str(Solution().rotate(
        [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]])))
    print()

    print('Example 3:')
    print('Input : ')
    print('matrix = [[1]]')
    print('Exception :')
    print('[[1]]')
    print('Output :')
    print(str(Solution().rotate([[1]])))
    print()

    print('Example 4:')
    print('Input : ')
    print('matrix = [[1,2],[3,4]]')
    print('Exception :')
    print('[[3,1],[4,2]]')
    print('Output :')
    print(str(Solution().rotate([[1, 2], [3, 4]])))
    print()

    pass
# @lc main=end
