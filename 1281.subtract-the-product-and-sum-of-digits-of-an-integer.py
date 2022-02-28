# @lc app=leetcode id=1281 lang=python3
#
# [1281] Subtract the Product and Sum of Digits of an Integer
#


# @lc tags=Unknown

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
    def subtractProductAndSum(self, n: int) -> int:
        sumx = 0
        prodx = 1
        while n > 0:
            mod = n % 10
            sumx += mod
            prodx *= mod
            n = n // 10
        return prodx - sumx
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 234')
    print('Exception :')
    print('15')
    print('Output :')
    print(str(Solution().subtractProductAndSum(234)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 4421')
    print('Exception :')
    print('21')
    print('Output :')
    print(str(Solution().subtractProductAndSum(4421)))
    print()

    pass
# @lc main=end
