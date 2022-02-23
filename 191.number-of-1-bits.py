# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
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
    def hammingWeight(self, n: int) -> int:
        """ Soltuion 1 """
        res = 0
        while n != 0:
            # n & n-1 will get rid of last 1 bit in a number
            n = n & (n-1)
            res += 1
        return res

        """ Solution 2 """
        res = 0
        while n > 0:
            if n & 1 != 0:
                res += 1
            n = n >> 1
        return res
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 00000000000000000000000000001011')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().hammingWeight(00000000000000000000000000001011)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 00000000000000000000000010000000')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().hammingWeight(00000000000000000000000010000000)))
    print()

    print('Example 3:')
    print('Input : ')
    print('n = 11111111111111111111111111111101')
    print('Exception :')
    print('31')
    print('Output :')
    print(str(Solution().hammingWeight(11111111111111111111111111111101)))
    print()

    pass
# @lc main=end
