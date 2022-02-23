# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#


# @lc tags=dynamic-programming;bit-manipulation

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
    def countBits(self, n: int) -> List[int]:
        bits = [0]
        for i in range(1, n+1):
            bits.append(bits[i & (i-1)]+1)
        return bits
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 2')
    print('Exception :')
    print('[0,1,1]')
    print('Output :')
    print(str(Solution().countBits(2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 5')
    print('Exception :')
    print('[0,1,1,2,1,2]')
    print('Output :')
    print(str(Solution().countBits(5)))
    print()

    pass
# @lc main=end
