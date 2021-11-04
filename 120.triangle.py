# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#


# @lc tags=array;dynamic-programming

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
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        for i in range(n-2, -1, -1):
            for j in range(len(triangle[i])-1, -1, -1):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])

        return triangle[0][0]


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]')
    print('Exception :')
    print('11')
    print('Output :')
    print(str(Solution().minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('triangle = [[-10]]')
    print('Exception :')
    print('-10')
    print('Output :')
    print(str(Solution().minimumTotal([[-10]])))
    print()

    pass
# @lc main=end
