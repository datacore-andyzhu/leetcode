# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#


# @lc tags=hash-table;math

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
    def isHappy(self, n: int) -> bool:
        def getNext(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum

        while n != 1 and n != 4:
            n = getNext(n)

        return n == 1
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 19')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isHappy(19)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 2')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isHappy(2)))
    print()

    pass
# @lc main=end
