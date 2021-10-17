# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
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
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0 for _ in range(n)] for _ in range(n)]
        left, right, up, down = 0, n-1, 0, n-1
        number = 1
        while left < right and up < down:
            for x in range(left, right):
                result[up][x] = number
                number += 1

            for y in range(up, down):
                result[y][right] = number
                number += 1

            for x in range(right, left, -1):
                result[down][x] = number
                number += 1

            for y in range(down, up, -1):
                result[y][left] = number
                number += 1

            left += 1
            right -= 1
            up += 1
            down -= 1

        # if n is an odd number, do not forget to fill
        # the middle number
        if n % 2 != 0:
            result[n//2][n//2] = number
        return result
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 3')
    print('Exception :')
    print('[[1,2,3],[8,9,4],[7,6,5]]')
    print('Output :')
    print(str(Solution().generateMatrix(3)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 1')
    print('Exception :')
    print('[[1]]')
    print('Output :')
    print(str(Solution().generateMatrix(1)))
    print()

    pass
# @lc main=end
