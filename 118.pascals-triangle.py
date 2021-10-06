# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
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
    def generate(self, numRows: int) -> List[List[int]]:
        pascalTriangle = []
        trow = [1]
        y = [0]
        for i in range(numRows):
            pascalTriangle.append(trow)
            trow = [l+r for l, r in zip(trow+y, y+trow)]
        return pascalTriangle

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('numRows = 5')
    print('Exception :')
    print('[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]')
    print('Output :')
    print(str(Solution().generate(5)))
    print()

    print('Example 2:')
    print('Input : ')
    print('numRows = 1')
    print('Exception :')
    print('[[1]]')
    print('Output :')
    print(str(Solution().generate(1)))
    print()

    pass
# @lc main=end
