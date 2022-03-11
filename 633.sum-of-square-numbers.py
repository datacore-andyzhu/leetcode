# @lc app=leetcode id=633 lang=python3
#
# [633] Sum of Square Numbers
#


# @lc tags=math

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
    def judgeSquareSum(self, c: int) -> bool:
        start = 0
        end = int(sqrt(c))
        while start <= end:
            curr = start**2 + end**2
            if curr < c:
                start += 1
            elif curr > c:
                end -= 1
            elif curr == c:
                return True
        return False
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('c = 5')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().judgeSquareSum(5)))
    print()

    print('Example 2:')
    print('Input : ')
    print('c = 3')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().judgeSquareSum(3)))
    print()

    pass
# @lc main=end
