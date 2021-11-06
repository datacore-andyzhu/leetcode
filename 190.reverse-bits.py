# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
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
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(31, -1, -1):
            if (n >> i) & 1:
                result += 1 << (31 - i)
        return result

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 00000010100101000001111010011100')
    print('Exception :')
    print('964176192 (00111001011110000010100101000000)')
    print('Output :')
    print(str(Solution().reverseBits(00000010100101000001111010011100)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 11111111111111111111111111111101')
    print('Exception :')
    print('3221225471 (10111111111111111111111111111111)')
    print('Output :')
    print(str(Solution().reverseBits(11111111111111111111111111111101)))
    print()

    pass
# @lc main=end
