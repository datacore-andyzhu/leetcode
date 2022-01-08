# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#


# @lc tags=bit-manipulation

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
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        max_int = 0x7fffffff
        return a if a < max_int else ~(a ^ mask)
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('a = 1, b = 2')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().getSum(1, 2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('a = 2, b = 3')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().getSum(2, 3)))
    print()

    pass
# @lc main=end
