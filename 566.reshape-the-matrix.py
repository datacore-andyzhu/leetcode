# @lc app=leetcode id=566 lang=python3
#
# [566] Reshape the Matrix
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
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        m = len(mat)
        n = len(mat[0])
        result = [[0 for _ in range(c)] for _ in range(r)]
        if m*n != r*c:
            return mat
        for i in range(m*n):
            result[i//c][i % c] = mat[i//n][i % n]
        return result


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('mat = [[1,2],[3,4]], r = 1, c = 4')
    print('Exception :')
    print('[[1,2,3,4]]')
    print('Output :')
    print(str(Solution().matrixReshape([[1, 2], [3, 4]], 1, 4)))
    print()

    print('Example 2:')
    print('Input : ')
    print('mat = [[1,2],[3,4]], r = 2, c = 4')
    print('Exception :')
    print('[[1,2],[3,4]]')
    print('Output :')
    print(str(Solution().matrixReshape([[1, 2], [3, 4]], 2, 4)))
    print()

    pass
# @lc main=end
